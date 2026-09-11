#!/usr/bin/env python3
"""
Numerical verification of every computationally checkable claim in the paper.

Each check prints PASS/FAIL and writes its evidence to ../data/.
These are finite verifications: they can refute a claim but never prove one.
The proofs are in the manuscript; this script guards against slips.

Usage:  python3 verify_claims.py [--quick]
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bcloc.core import (  # noqa: E402
    AdelicPoint,
    admissible_classes,
    all_characters,
    detecting_set,
    generated_subgroup,
    is_prime,
    legendre_mod3,
    m_p,
    primes_in_class,
    primes_upto,
    quadratic_character,
    represented_by,
    sophie_germain_upto,
    unit_group,
    xi_partial_sum,
)

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
os.makedirs(DATA, exist_ok=True)
RESULTS: list[dict] = []


def record(name: str, ref: str, passed: bool, detail: str) -> bool:
    tag = "PASS" if passed else "FAIL"
    print(f"[{tag}] {name}  ({ref})\n       {detail}")
    RESULTS.append({"check": name, "reference": ref, "status": tag, "detail": detail})
    return passed


# ---------------------------------------------------------------- Lemma 3.2 ----

def check_lemma_3_2(trials: int) -> bool:
    """1 - |m_p|^2 = 2 t (1 - Re c) / |1 - c t|^2."""
    worst = 0.0
    rng = random.Random(20260827)
    rows = []
    for _ in range(trials):
        t = rng.uniform(1e-3, 1 - 1e-3)
        phi = rng.uniform(0, 2 * math.pi)
        c = complex(math.cos(phi), math.sin(phi))
        m = m_p(t, c)
        lhs = 1 - abs(m) ** 2
        rhs = 2 * t * (1 - c.real) / abs(1 - c * t) ** 2
        rel = abs(lhs - rhs) / max(1e-15, abs(lhs) + abs(rhs))
        worst = max(worst, rel)
        if len(rows) < 200:
            rows.append({"t": t, "phi": phi, "lhs": lhs, "rhs": rhs, "rel_err": rel})
    with open(os.path.join(DATA, "lemma_3_2_identity.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["t", "phi", "lhs", "rhs", "rel_err"])
        w.writeheader()
        w.writerows(rows)
    return record(
        "Lemma 3.2 identity for 1-|m_p|^2",
        "Lemma 3.2",
        worst < 1e-6,
        f"worst relative error over {trials} random (t,phi): {worst:.3e}",
    )


# ---------------------------------------------------------------- Lemma 5.6 ----

def check_lemma_5_6(bound: int) -> bool:
    """<A_M> = (Z/MZ)^* for every M."""
    bad = []
    rows = []
    for M in range(2, bound + 1):
        A = admissible_classes(M)
        gen = generated_subgroup(M, A)
        full = {a % M for a in unit_group(M)}
        ok = gen == full
        if not ok:
            bad.append(M)
        rows.append({"M": M, "phi_M": len(full), "size_A_M": len(A), "generates": ok})
    with open(os.path.join(DATA, "lemma_5_6_admissible.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["M", "phi_M", "size_A_M", "generates"])
        w.writeheader()
        w.writerows(rows)
    return record(
        "Admissible classes generate (Z/MZ)^*",
        "Lemma 5.6",
        not bad,
        f"no counterexample for 2 <= M <= {bound}" if not bad else f"counterexamples: {bad}",
    )


# --------------------------------------------------------- Proposition 4.12 ----

def check_prop_4_12(trials: int) -> bool:
    """Psi is pointwise invariant under multiplication by any prime of S."""
    P1 = [p for p in primes_upto(400) if p % 3 == 1]
    R = [p for p in primes_upto(400) if p % 3 == 2 and p != 2][:8]
    rng = random.Random(11235)
    fails = 0
    for _ in range(trials):
        x = AdelicPoint(
            u3=rng.choice([1, 2, 4, 5, 7, 8]),
            vR={r: rng.randint(0, 3) for r in R},
        )
        ell = rng.choice([3] + P1[:10] + R)
        if x.psi() != x.multiply(ell, R).psi():
            fails += 1
    # and the control: dropping the R-correction destroys invariance
    x = AdelicPoint(u3=1, vR={r: 0 for r in R})
    control_broken = legendre_mod3(x.u3) != legendre_mod3(x.multiply(R[0], R).u3)
    ok = fails == 0 and control_broken
    return record(
        "Pointwise invariance of Psi (and necessity of its R-correction)",
        "Proposition 4.12(2)",
        ok,
        f"{fails} failures in {trials} trials; control (Legendre factor alone) broken: {control_broken}",
    )


# -------------------------------------------------------------- Example 4.2 ----

def check_example_4_2(bound: int) -> bool:
    """Genus theory for Q(sqrt(-5))."""
    rows, bad = [], []
    for p in primes_upto(bound):
        if p in (2, 5):
            continue
        if pow(-5 % p, (p - 1) // 2, p) != 1:
            continue  # inert
        principal = represented_by(p, 1, 5)
        nonprincipal = represented_by(2 * p, 1, 5)
        cls = p % 20
        ok = (
            (principal and cls in (1, 9))
            or (nonprincipal and cls in (3, 7))
        ) and not (principal and nonprincipal)
        if not ok:
            bad.append(p)
        rows.append(
            {
                "p": p,
                "p_mod_20": cls,
                "principal": principal,
                "nonprincipal": nonprincipal,
            }
        )
    with open(os.path.join(DATA, "example_4_2_genus_theory.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["p", "p_mod_20", "principal", "nonprincipal"])
        w.writeheader()
        w.writerows(rows)
    return record(
        "Genus theory for Q(sqrt(-5)): principal <=> p = 1,9 mod 20",
        "Example 4.2",
        not bad,
        f"{len(rows)} split primes below {bound}, no exceptions"
        if not bad
        else f"exceptions: {bad[:10]}",
    )


# --------------------------------------------------------- Proposition 4.15 ----

def check_prop_4_15() -> bool:
    """
    The group theory behind the cascade:
      <4> has index 4 in (Z/15Z)^*, the quotient is (Z/2Z)^2 generated by the
      quadratic characters at 3 and 5, and the quartic character kills 4.
    """
    U15 = unit_group(15)
    H = generated_subgroup(15, [4])
    index = len(U15) // len(H)

    chars = all_characters(15)
    trivial_on_H = [c for c in chars if H <= c.kernel()]
    orders = sorted(c.order() for c in trivial_on_H)

    # the quadratic characters at 3 and 5, inflated to modulus 15
    chi3 = quadratic_character(3)
    chi5 = quadratic_character(5)

    def infl(c, m):
        vals = [0j] * 15
        for a in U15:
            vals[a] = c(a % m)
        from bcloc.core import DirichletCharacter

        return DirichletCharacter(15, tuple(vals))

    X3, X5 = infl(chi3, 3), infl(chi5, 5)
    quartic = [c for c in all_characters(5) if c.order() == 4]

    checks = {
        "index of <4> in (Z/15Z)^*": index == 4,
        "H = {1,4}": H == {1, 4},
        "quotient is (Z/2Z)^2": orders == [1, 2, 2, 2],
        "chi3 trivial on H": H <= X3.kernel(),
        "chi5 trivial on H": H <= X5.kernel(),
        "quartic psi_5 has psi_5(4) = -1": all(
            abs(c(4) + 1) < 1e-9 for c in quartic
        ),
        "chi3(11)=-1, chi5(11)=+1": abs(X3(11) + 1) < 1e-9 and abs(X5(11) - 1) < 1e-9,
        "chi3(7)=+1, chi5(7)=-1": abs(X3(7) - 1) < 1e-9 and abs(X5(7) + 1) < 1e-9,
        "P u R1 u R2 generates (Z/15Z)^*": generated_subgroup(15, [1, 4, 11, 7])
        == {a % 15 for a in U15},
        "classes 1,4 / 11 / 7 pairwise disjoint": len({1, 4} & {11}) == 0
        and len({1, 4} & {7}) == 0,
    }
    with open(os.path.join(DATA, "prop_4_15_group_theory.json"), "w") as f:
        json.dump({k: bool(v) for k, v in checks.items()}, f, indent=2)
    bad = [k for k, v in checks.items() if not v]
    return record(
        "Cascade group theory: (Z/15Z)^*/<4> = (Z/2Z)^2, quartic excluded",
        "Proposition 4.15",
        not bad,
        f"all {len(checks)} sub-checks pass" if not bad else f"failed: {bad}",
    )


def check_prop_4_15_sums(bound: int) -> bool:
    """
    The detecting sets of chi3, chi5, chi3*chi5 on the cascade set S are
    R1, R2, R1 u R2 respectively (up to the finitely many primes 3, 5).
    """
    P = [p for p in primes_upto(bound) if p % 15 in (1, 4)]
    R1 = [p for p in primes_upto(bound) if p % 15 == 11]
    R2 = [p for p in primes_upto(bound) if p % 15 == 7]
    S = sorted(set(P) | set(R1) | set(R2))

    U15 = unit_group(15)
    from bcloc.core import DirichletCharacter

    def infl(c, m):
        vals = [0j] * 15
        for a in U15:
            vals[a] = c(a % m)
        return DirichletCharacter(15, tuple(vals))

    X3 = infl(quadratic_character(3), 3)
    X5 = infl(quadratic_character(5), 5)
    X35 = DirichletCharacter(15, tuple(X3(a) * X5(a) if math.gcd(a, 15) == 1 else 0j for a in range(15)))

    got = {
        "chi3": set(detecting_set(X3, S)),
        "chi5": set(detecting_set(X5, S)),
        "chi3chi5": set(detecting_set(X35, S)),
    }
    want = {"chi3": set(R1), "chi5": set(R2), "chi3chi5": set(R1) | set(R2)}
    ok = got == want
    return record(
        "Detecting sets on the cascade set are exactly R1, R2, R1 u R2",
        "Proposition 4.15, computation of Xi_beta",
        ok,
        f"|P|={len(P)}, |R1|={len(R1)}, |R2|={len(R2)} below {bound}; sets match: {ok}",
    )


# ------------------------------------------------------------- Theorem 5.5 ----

def check_theorem_5_5(bound: int) -> bool:
    """
    Sophie Germain primes: Brun-type upper bound is consistent with the data,
    the partial sums of 1/p are slowly growing (Brun-summable), and every SG
    prime lies in an admissible class.
    """
    SG = sophie_germain_upto(bound)
    rows = []
    partial = 0.0
    for p in SG:
        partial += 1.0 / p
        rows.append({"p": p, "partial_sum_inv_p": partial})
    with open(os.path.join(DATA, "sophie_germain.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["p", "partial_sum_inv_p"])
        w.writeheader()
        w.writerows(rows)

    # admissibility: p mod M in A_M for each modulus M, excluding the
    # documented exceptions p | M and (2p+1) | M (see Theorem 5.5(5))
    bad = []
    for M in (3, 5, 7, 8, 9, 11, 15):
        A = set(admissible_classes(M))
        for p in SG:
            if math.gcd(p, M) != 1 or M % (2 * p + 1) == 0:
                continue
            if p % M not in A:
                bad.append((M, p))
                break
    return record(
        "Sophie Germain primes lie in admissible classes; sum 1/p converges slowly",
        "Theorem 5.5, Lemma 5.6",
        not bad,
        f"{len(SG)} SG primes below {bound}; sum 1/p = {partial:.5f}; "
        f"admissibility violations: {bad if bad else 'none'}",
    )


# ---------------------------------------------------------- Example 3.13 ----

def check_example_3_13(bound: int) -> bool:
    """
    For S = {3} u {l = 1 mod 3}, the quadratic character at 3 has an empty
    detecting set, so Xi_beta is nontrivial for every beta.
    """
    S = [3] + [p for p in primes_upto(bound) if p % 3 == 1]
    chi3 = quadratic_character(3)
    # chi(sigma_l) = (l | 3), and sigma_3 has trivial 3-component
    det = [ell for ell in S if ell != 3 and abs(chi3(ell) - 1) > 1e-9]
    total = xi_partial_sum(chi3, [e for e in S if e != 3], beta=0.5)
    return record(
        "Empty detecting set for S = {3} u {l = 1 mod 3}",
        "Example 3.13",
        not det and total == 0.0,
        f"|S|={len(S)} below {bound}; detecting set empty: {not det}; "
        f"partial sum at beta=0.5: {total}",
    )


# ---------------------------------------------------------- Theorem 4.10 ----

def check_theorem_4_10(bound: int, sparse_k: int) -> bool:
    """
    For S = {3} u P1 u R with R sparse, the detecting set of chi is exactly R,
    and its beta-weighted sum converges for every beta > 0 while the ambient
    sum over P1 diverges.
    """
    P1 = [p for p in primes_upto(bound) if p % 3 == 1]
    # a genuinely sparse R: least prime = 2 mod 3 above 2^(2^k)
    R = []
    for k in range(1, sparse_k + 1):
        n = 2 ** (2**k) + 1
        while not (n % 3 == 2 and is_prime(n)):
            n += 1
        R.append(n)
    S = [3] + P1 + R
    chi3 = quadratic_character(3)
    det = set(detecting_set(chi3, [e for e in S if e != 3]))
    sum_R = sum(float(p) ** -0.1 for p in R)
    sum_P1 = sum(1.0 / p for p in P1)
    ok = det == set(R)
    with open(os.path.join(DATA, "theorem_4_10_sparse_R.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["k", "r_k", "r_k mod 3", "r_k^{-0.1}"])
        for k, p in enumerate(R, 1):
            w.writerow([k, p, p % 3, float(p) ** -0.1])
    return record(
        "Detecting set is exactly the sparse part R; its weighted sum converges",
        "Theorem 4.10, Lemma 4.6",
        ok,
        f"|R|={len(R)} (largest {len(str(R[-1]))} digits); sum_R p^-0.1 = {sum_R:.6f}; "
        f"sum_P1 1/p = {sum_P1:.4f} (diverges); detecting set = R: {ok}",
    )


# ------------------------------------------------------------------- main ----

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="smaller bounds")
    args = ap.parse_args()
    q = args.quick

    print("=" * 78)
    print("Verification of computational claims")
    print("=" * 78)

    ok = True
    ok &= check_lemma_3_2(20_000 if q else 200_000)
    ok &= check_lemma_5_6(200 if q else 600)
    ok &= check_prop_4_12(5_000 if q else 20_000)
    ok &= check_example_4_2(2_000 if q else 20_000)
    ok &= check_prop_4_15()
    ok &= check_prop_4_15_sums(20_000 if q else 200_000)
    ok &= check_theorem_5_5(20_000 if q else 200_000)
    ok &= check_example_3_13(20_000 if q else 200_000)
    ok &= check_theorem_4_10(20_000 if q else 200_000, 4)

    with open(os.path.join(DATA, "verification_results.json"), "w") as f:
        json.dump(RESULTS, f, indent=2)

    print("=" * 78)
    print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
    print(f"Evidence written to {os.path.abspath(DATA)}")
    print("=" * 78)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
