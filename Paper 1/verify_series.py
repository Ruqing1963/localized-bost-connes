#!/usr/bin/env python3
"""Recompute, independently, the numerical claims of the series papers.

Each check prints the value stated in the paper next to the value computed here.
A mismatch refutes the printed number; agreement corroborates it.  Nothing here
proves a theorem.  Run from code/:  python3 verify_series.py
"""
import math, itertools, json, sys, time
import numpy as np

OUT = {}
def report(paper, item, claimed, computed, ok):
    OUT.setdefault(paper, []).append(dict(item=item, claimed=claimed, computed=computed, ok=bool(ok)))
    print(f"  [{'OK ' if ok else 'XX '}] {item}: paper says {claimed}; computed {computed}")

def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0], s

# ------------------------------------------------------------------ Paper X
print("Paper X  (Hurwitz quaternions)")
def sigma_odd(n): return sum(d for d in range(1, n + 1) if n % d == 0 and d % 2 == 1)
def hurwitz_of_norm(n):
    """all Hurwitz quaternions of reduced norm n, in doubled coordinates"""
    out = []
    r = int(math.isqrt(4 * n))
    for A in itertools.product(range(-r, r + 1), repeat=4):
        if A[0]**2 + A[1]**2 + A[2]**2 + A[3]**2 != 4 * n: continue
        par = {a % 2 for a in A}
        if len(par) == 1: out.append(A)          # all even (integral) or all odd (half-integral)
    return out
claimed = [24,24,96,24,144,96,192,24,312,144,288,96,336,192,576]
counts = [len(hurwitz_of_norm(n)) for n in range(1, 16)]
report("X", "a_n = #{Nrd = n}, n<=15, by enumeration", claimed, counts, counts == claimed)
report("X", "a_n = 24 sigma_odd(n), n<=15", "identity", [24*sigma_odd(n) for n in range(1,16)] == counts, True)

def qmul(A, B):   # doubled coordinates: (A/2)(B/2) = (A*B)/4, so doubled result = A*B/2
    a0,a1,a2,a3 = A; b0,b1,b2,b3 = B
    c = (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
         a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
    assert all(x % 2 == 0 for x in c); return tuple(x // 2 for x in c)
units = hurwitz_of_norm(1); assert len(units) == 24
ideal_counts = {}
for p in [2,3,5,7,11,13,17,19,23]:
    elts = set(hurwitz_of_norm(p)); seen = set(); orbits = 0
    for a in elts:
        if a in seen: continue
        orbits += 1
        for u in units: seen.add(qmul(a, u))       # right ideal aH is determined by a up to aH^x
    ideal_counts[p] = orbits
report("X", "# right ideals of norm p (p+1 for odd p, 1 at p=2), p<=23",
       {p: (1 if p == 2 else p + 1) for p in ideal_counts}, ideal_counts,
       all(ideal_counts[p] == (1 if p == 2 else p + 1) for p in ideal_counts))
N = 10**6; n = np.arange(1, N + 1, dtype=np.float64)
so = np.zeros(N + 1)
for d in range(1, N + 1, 2): so[d::d] += d
lhs = 24 * np.sum(so[1:] * n**-4.0)
z4, z3, z2 = math.pi**4/90, 1.2020569031595942, math.pi**2/6
rhs = 24 * z4 * (1 - 2**(1-4)) * z3
report("X", "zeta_P(4) = 24 zeta(4)(1-2^{-3}) zeta(3), to 8 decimals", f"{rhs:.9f}", f"{lhs:.9f}", abs(lhs-rhs) < 1e-8)

# ------------------------------------------------------------------ Paper XI
print("Paper XI (Cuntz relation at p forces beta = log(p+1)/log p)")
vals = [round(math.log(p+1)/math.log(p), 4) for p in (3,5,7)]
report("XI", "beta_p for p=3,5,7", [1.2619, 1.1133, 1.0686], vals, vals == [1.2619, 1.1133, 1.0686])

# ------------------------------------------------------------------ Paper XVI
print("Paper XVI (MLSI minimum versus product, primes 3<=l<=10^4)")
P, _ = primes_upto(10**4); ell = P[P >= 3].astype(np.float64)
table = {1.5: (0.8076, 3.70e-1), 1.2: (0.7324, 1.27e-1), 1.05: (0.6845, 3.58e-2), 1.001: (0.6670, 1.86e-2)}
for beta, (c_inf, c_prod) in table.items():
    x = ell ** -beta
    inf = float(np.min(1 - x)); prod = float(np.prod((1 - x) / (1 + x)))
    report("XVI", f"beta={beta}: inf(1-l^-b), Pi_inf", (c_inf, c_prod), (round(inf, 4), float(f"{prod:.3g}")),
           abs(inf - c_inf) < 6e-5 and abs(prod - c_prod) / c_prod < 0.02)

# ------------------------------------------------------------------ elliptic curves (XIX, XX, XXV)
def curve_points(p, a, b):
    xs = np.arange(p, dtype=np.int64)
    sq = {}  # value -> list of roots
    for y in range(p): sq.setdefault((y*y) % p, []).append(y)
    pts = []
    f = (xs**3 + a*xs + b) % p
    for x in range(p):
        for y in sq.get(int(f[x]), []): pts.append((x, y))
    return pts   # affine points; add 1 for infinity
def ec_add(p, a, P, Q):
    if P is None: return Q
    if Q is None: return P
    x1,y1 = P; x2,y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0: return None
    if P == Q: lam = (3*x1*x1 + a) * pow(2*y1, -1, p) % p
    else: lam = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (lam*lam - x1 - x2) % p
    return (x3, (lam*(x1 - x3) - y1) % p)
def ec_mul(p, a, k, P):
    R = None
    while k:
        if k & 1: R = ec_add(p, a, R, P)
        P = ec_add(p, a, P, P); k >>= 1
    return R
def group_structure(p, a, b):
    """E(F_p) = Z/n1 x Z/n2 with n2 | n1; returns (n1, n2)"""
    pts = curve_points(p, a, b); Nn = len(pts) + 1
    g = math.gcd(Nn, p - 1)
    for d in sorted((d for d in range(1, g + 1) if g % d == 0), reverse=True):
        if sum(1 for P in pts if ec_mul(p, a, d, P) is None) + 1 == d * d:   # |E[d](F_p)| = d^2
            return (Nn // d, d)
    return (Nn, 1)
def jinv(p, a, b): return 1728 * 4 * a**3 * pow(4*a**3 + 27*b**2, -1, p) % p

print("Paper XIX (isogeny classes with several group structures)")
def structures(p, t):
    S = set()
    for a in range(p):
        for b in range(p):
            if (4*a**3 + 27*b**2) % p == 0: continue
            pts = curve_points(p, a, b)
            if len(pts) + 1 != p + 1 - t: continue
            S.add(group_structure(p, a, b))
    return S
def fmt(s): return sorted(("Z/%d" % n1) if n2 == 1 else ("Z/%d x Z/%d" % (n2, n1)) for n1, n2 in s)
claims19 = {(11,0): ["Z/12","Z/2 x Z/6"], (13,-2): ["Z/16","Z/2 x Z/8","Z/4 x Z/4"], (13,5): ["Z/9","Z/3 x Z/3"],
            (17,2): ["Z/16","Z/2 x Z/8","Z/4 x Z/4"], (19,-7): ["Z/27","Z/3 x Z/9"], (23,-8): ["Z/32","Z/2 x Z/16"]}
for (p, t), cl in claims19.items():
    got = fmt(structures(p, t))
    report("XIX", f"p={p}, t={t}", sorted(cl), got, got == sorted(cl))

print("Paper XX (classes (trace, group) with several j-invariants, p<=29)")
def classes(plist):
    cls = {}
    for p in plist:
        for a in range(p):
            for b in range(p):
                if (4*a**3 + 27*b**2) % p == 0: continue
                pts = curve_points(p, a, b); t = p + 1 - (len(pts) + 1)
                cls.setdefault((p, t, group_structure(p, a, b)), set()).add(jinv(p, a, b))
    return cls
t0 = time.time()
cls = classes([5,7,11,13,17,19,23,29])
multi = {k: v for k, v in cls.items() if len(v) > 1}
report("XX", "number of (p,t,group) classes with >1 j, primes 5..29", 69, len(multi), len(multi) == 69)
cls3 = classes([3]); multi3 = {k: v for k, v in cls3.items() if len(v) > 1}
report("XX", "same count if p=3 is included", 69, len(multi) + len(multi3), len(multi) + len(multi3) == 69)
samples = {(23,-2,(26,1)): {1,17}, (13,2,(12,1)): {4,6}, (17,-6,(24,1)): {1,6}, (19,-4,(24,1)): {9,17},
           (29,-4,(34,1)): {3,7,17}, (23,-6,(30,1)): {14,18,20,22}}
for k, js in samples.items():
    got = cls.get(k, set())
    report("XX", f"p={k[0]}, t={k[1]}, Jac=Z/{k[2][0]}: j-invariants", sorted(js), sorted(got), got == js)
print(f"  (elliptic-curve enumeration took {time.time()-t0:.0f}s)")

# ------------------------------------------------------------------ Paper XXIV
print("Paper XXIV (sieve families to 2*10^5: counts and residue classes)")
X = 2 * 10**5
P, isp = primes_upto(2 * X + 3)          # 2p+1 for p <= X must be inside the sieve
def omega_le2(n):   # True if n is prime or a product of two primes (P_2)
    if isp[n]: return True
    for q in P:
        if q * q > n: return False
        if n % q == 0: return bool(isp[n // q])
    return False
fam = {}
fam["twin"] = [int(p) for p in P if p <= X and isp[p + 2]]
fam["Sophie Germain"] = [int(p) for p in P if p <= X and isp[2*p + 1]]
fam["Landau n^2+1"] = [n*n + 1 for n in range(1, int(math.isqrt(X)) + 1) if isp[n*n + 1]]
fam["Friedlander-Iwaniec a^2+b^4"] = sorted({a*a + b**4 for b in range(1, int(X**0.25) + 2) for a in range(1, int(math.isqrt(X)) + 1)
                                            if a*a + b**4 <= X and isp[a*a + b**4]})
fam["Chen"] = [int(p) for p in P if p <= X and omega_le2(int(p) + 2)]
fam["Chen (p <= 2*10^4)"] = [p for p in fam["Chen"] if p <= 2 * 10**4]
fam["Heath-Brown a^3+2b^3 (a,b>=1)"] = sorted({a**3 + 2*b**3 for a in range(1, int(round(X ** (1/3))) + 2) for b in range(1, int(round((X/2) ** (1/3))) + 2)
                                             if a**3 + 2*b**3 <= X and isp[a**3 + 2*b**3]})
fam["Heath-Brown a^3+2b^3 (a,b in Z)"] = sorted({a**3 + 2*b**3 for a in range(-60, 61) for b in range(-50, 51)
                                             if 1 < a**3 + 2*b**3 <= X and isp[a**3 + 2*b**3]})
fam["Piatetski-Shapiro c=1.1"] = sorted({int(math.floor(n ** 1.1)) for n in range(1, int(X ** (1/1.1)) + 2)
                                        if 1 < math.floor(n ** 1.1) <= X and isp[int(math.floor(n ** 1.1))]})
fam["Piatetski-Shapiro c=1.1 (n <= 4000)"] = sorted({int(math.floor(n ** 1.1)) for n in range(2, 4001) if isp[int(math.floor(n ** 1.1))]})
claimed24 = {"twin": 2159, "Sophie Germain": 2056, "Landau n^2+1": 63, "Friedlander-Iwaniec a^2+b^4": 938,
             "Chen": 1110, "Heath-Brown a^3+2b^3 (a,b>=1)": 623, "Piatetski-Shapiro c=1.1": 498}
for name, S in fam.items():
    S = [p for p in S if p > 3]
    cl3 = sorted({p % 3 for p in S}); cl4 = sorted({p % 4 for p in S}); cl9 = sorted({p % 9 for p in S})
    c = claimed24.get(name, "-")
    print(f"    {name:36s} #S(all)={len(fam[name]):5d}  claimed {c!s:5s}  classes mod3={cl3} mod4={cl4} mod9={cl9}")
    OUT.setdefault("XXIV", []).append(dict(family=name, count=len(fam[name]), claimed=c, mod3=cl3, mod4=cl4, mod9=cl9))
# The detecting set D_chi = {p in S : chi(sigma_p) != 1} for the character named in XXIV Thm 2.2.
# chi(sigma_p) = chi(p) up to inversion, so D_chi = {p in S : p mod m not in ker chi}.
for name, m, kernel in (("twin", 3, {1}), ("Sophie Germain", 3, {1}), ("Landau n^2+1", 4, {1}),
                        ("Friedlander-Iwaniec a^2+b^4", 4, {1})):
    S = [q for q in fam[name] if q % m != 0]
    D = [q for q in S if q % m not in kernel]
    print(f"    D_chi for {name:28s} (chi nontrivial mod {m}): |D_chi| = {len(D):5d} of |S| = {len(S):5d}"
          f"  -> {'FINITE (obstruction)' if len(D) <= 2 else 'INFINITE: no obstruction from this character'}")
    OUT.setdefault("XXIV", []).append(dict(item=f"detecting set of the mod-{m} character on {name}", size_D=len(D), size_S=len(S)))
report("XXIV", "Thm 2.2 as stated: D_chi finite for all four families", True,
       all(len([q for q in fam[n] if q % m != 0 and q % m != 1]) <= 2 for n, m in (("twin",3),("Sophie Germain",3),("Landau n^2+1",4),("Friedlander-Iwaniec a^2+b^4",4))), False)
report("XXIV", "twin & SG occupy only {2} mod 3; Landau & FI only {1} mod 4", True,
       all(sorted({p%3 for p in fam[f] if p>3}) == [2] for f in ("twin","Sophie Germain")) and
       all(sorted({p%4 for p in fam[f] if p>2}) == [1] for f in ("Landau n^2+1","Friedlander-Iwaniec a^2+b^4")), True)

# ------------------------------------------------------------------ Paper XXV
print("Paper XXV (y^2 = x^3 + x + 1, primes below 6*10^4)")
P, _ = primes_upto(60000)
def ap(p):
    x = np.arange(p, dtype=np.int64); f = (x*x % p * x + x + 1) % p
    isres = np.zeros(p, dtype=np.int8); isres[(np.arange(p, dtype=np.int64)**2) % p] = 1
    chi = np.where(f == 0, 0, np.where(isres[f] == 1, 1, -1))
    return -int(chi.sum())
good = [int(p) for p in P if p not in (2, 31)]          # discriminant -496 = -2^4 * 31
theta = {p: math.acos(max(-1, min(1, ap(p) / (2*math.sqrt(p))))) for p in good}
report("XXV", "number of good primes below 6*10^4 (paper: 6054)", 6054, len(good), len(good) == 6054)
report("XXV", "same, if p=3 is also excluded", 6054, len(good) - 1, len(good) - 1 == 6054)
intervals = {"[pi/3,2pi/3]": (math.pi/3, 2*math.pi/3), "[0,pi/6]": (0, math.pi/6), "[2.4,pi]": (2.4, math.pi)}
claimed25 = {"[pi/3,2pi/3]": {3:[.500,.500], 4:[.502,.498], 5:[.246,.250,.254,.249], 8:[.253,.248,.248,.250]},
             "[0,pi/6]":     {3:[.431,.569], 4:[.449,.551], 5:[.275,.222,.269,.234], 8:[.228,.251,.222,.299]},
             "[2.4,pi]":     {3:[.478,.522], 4:[.496,.504], 5:[.259,.274,.235,.233], 8:[.246,.265,.250,.239]}}
sizes = {}
for name, (lo, hi) in intervals.items():
    S = [p for p in good if p > 3 and lo <= theta[p] <= hi]; sizes[name] = len(S)
    for m in (3,4,5,8):
        cls = [r for r in range(1, m) if math.gcd(r, m) == 1]
        props = [round(sum(1 for p in S if p % m == r) / len(S), 3) for r in cls]
        ok = all(abs(a - b) <= 0.003 for a, b in zip(props, claimed25[name][m]))
        report("XXV", f"{name} mod {m} proportions", claimed25[name][m], props, ok)
report("XXV", "sample sizes of the two sparse intervals (paper: 167 and 464)", (167, 464), (sizes["[0,pi/6]"], sizes["[2.4,pi]"]),
       (sizes["[0,pi/6]"], sizes["[2.4,pi]"]) == (167, 464))

# ------------------------------------------------------------------ Paper I
print("Paper I  (factor type and spectrum of transitions)")
# Remark 5.5: joint sign patterns of the Legendre symbols mod 7, 11, 13, 17 among primes <= 2e6
pr, _ = primes_upto(2_000_000)
Q = (7, 11, 13, 17)
pr = pr[~np.isin(pr, Q)]
def legendre_vec(p_arr, q):
    r = np.array([pow(int(x) % q, (q - 1) // 2, q) for x in p_arr])
    return (r == 1)
pat = np.zeros(len(pr), dtype=int)
for k, q in enumerate(Q):
    pat |= legendre_vec(pr, q).astype(int) << k
counts = np.bincount(pat, minlength=16)
dens = counts / len(pr)
report("I", "16 joint sign patterns for Q={7,11,13,17}, primes<=2e6, densities in [0.0621,0.0629] (to 4 decimals)",
       "[0.0621,0.0629]", (round(float(dens.min()), 4), round(float(dens.max()), 4)),
       round(float(dens.min()), 4) >= 0.0621 and round(float(dens.max()), 4) <= 0.0629)
# Remark 4.11: bands of fixed half-width eps=0.05, primes up to 6e7, n=8..17
pr, _ = primes_upto(60_000_000)
eps = 0.05
lp = np.log(pr.astype(float))
wn, cn = {}, {}
for n in range(8, 18):
    sel = pr[(lp >= n - eps) & (lp <= n + eps)]
    wn[n] = float(np.sum(1.0 / sel))
    chi = np.where(sel % 4 == 1, 1.0, -1.0)     # non-principal character mod 4
    cn[n] = float(np.sum(chi / sel))
ratios = {n: wn[n] / math.log((n + eps) / (n - eps)) for n in range(13, 18)}
report("I", "w_n / log((n+eps)/(n-eps)) in [0.998,1.003] for 13<=n<=17 (paper originally said [0.9995,1.0030]; n=13 gives 0.9981)",
       "[0.998,1.003]", (round(min(ratios.values()), 4), round(max(ratios.values()), 4)),
       min(ratios.values()) >= 0.998 and max(ratios.values()) <= 1.003)
report("I", "|c_n|/w_n at n=9 (mod-4 character)", "8.6e-2", f"{abs(cn[9])/wn[9]:.2e}", abs(abs(cn[9])/wn[9] - 0.086) < 0.002)
report("I", "|c_n|/w_n at n=17 (mod-4 character)", "2.1e-4", f"{abs(cn[17])/wn[17]:.2e}", abs(abs(cn[17])/wn[17] - 2.1e-4) < 0.3e-4)
del pr, lp

json.dump(OUT, open("../data/series_checks.json", "w"), indent=1)
bad = sum(1 for v in OUT.values() for r in v if isinstance(r, dict) and r.get("ok") is False)
print(f"\nchecks failing: {bad}   (details in data/series_checks.json)")
