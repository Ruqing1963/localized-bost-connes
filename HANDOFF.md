# Handoff: localized Bost–Connes series

Written 31 August 2026, at the point where Papers I–XIII, XXVII, XXVIII and the two Q47 papers
have been reviewed or written, and the sequential review is about to resume at **Paper XIV**.
Read this first, then `docs/STATUS.md` (the long-form log, one entry per paper reviewed).

---

## 1. What this repository is

A foundational paper plus a series of companion papers on *localized* Bost–Connes systems: the
Bost–Connes construction with the set of all primes replaced by an arbitrary set `S`. The
foundational result is that the KMS_β simplex is `Prob(G_S / Ξ_β^⊥)`, where `Ξ_β` is an
obstruction group defined by convergence of `Σ_p N(p)^{-β} |1 - χ(σ_p)|²`. Everything else in the
series computes, obstructs, or generalizes that.

```
paper/master_bost_connes_paper.tex   the foundational paper (24 pp)
papers/<numeral>-<slug>/             the companions, one directory each
docs/STATUS.md                       review log — the single most important file
docs/ERRATA.md                       errors found in the *published* foundational paper
docs/ZENODO_*.txt|md                 deposit metadata
code/, data/, figures/               verification scripts and their output
monograph/                           assembly script (not yet cleaned)
superseded/                          older drafts, ignore
```

Build everything with `bash build_all.sh` (three pdflatex passes per paper, prints a table of
errors / warnings / overfull / underfull / pages). **The whole corpus currently compiles at
0 errors, 0 warnings, 0 overfull boxes.** Keep it that way; it is the cheapest regression test
there is.

---

## 2. Publication state — read before touching any DOI

| item | DOI | state |
|---|---|---|
| foundational paper | 10.5281/zenodo.22152101 | **published, v1** |
| Paper I | 10.5281/zenodo.22160827 | DOI reserved, draft saved, **not published** |
| Paper II | 10.5281/zenodo.22177726 | DOI reserved, draft saved, **not published** |
| Q47 Bateman–Horn (empirical) | 10.5281/zenodo.20753750 | published |
| everything else | — | not deposited |

**The trap.** Every companion now cites the *reviewed* numbering of the foundational paper, which
differs from the published v1 in places. So: publish the foundational paper v2 (built from
`docs/ERRATA.md`) **before** releasing any companion, and then update the DOI in every companion
to the v2 version DOI, or switch to the Zenodo concept DOI.

Author block used throughout:

```latex
\author{Ruqing Chen}
\address{GUT Geoservice Inc., Montreal, Canada}
\email{ruqing@hotmail.com}
```

The two most recent papers (XXVIII and the Q47 spacing paper) carry it **commented out** for
double-blind submission; uncomment to attribute.

---

## 3. Working conventions (these were decided, not defaults)

1. **Citation policy.** A paper may cite by DOI only what is published: the foundational paper,
   Paper I, and the Q47 empirical paper. Every reference to an unpublished companion is a numeral
   signpost in prose — "Paper V of the series shows…" — with **no bibitem**. When a companion's
   result is actually needed, re-prove it in place rather than cite it.
2. **Every bibliography entry must be cited.** Several papers arrived with entries never cited in
   the text; that is now checked mechanically on every pass.
3. **Honesty over polish.** Where a result is conditional, weaker than its original statement, or
   only consistent rather than proved, the text says so. Several papers had theorems that were
   false as stated; they were rewritten, not quietly softened. See `docs/STATUS.md` for what was
   wrong in each.
4. **Numbering.** Renumbering inside a paper is recorded in its STATUS entry together with a list
   of which other papers cite the changed items. Do not renumber without doing that.
5. **Language.** Papers in English; correspondence with the author in Chinese.
6. **No network access** in the working environment: nothing can be pushed or fetched.

---

## 4. Sequential review: where it stands

Reviewed and corrected, in order: **foundational paper, I, II, III, IV, V, VI, VII, VIII, IX, X,
XI, XII, XIII**. Written from scratch on request: **XXVII** (non-abelian groupoids), **XXVIII**
((C4) settled), and two unnumbered **Q47** papers.

**Next: Paper XIV** (`papers/XIV-equalnorm/`), then XV–XXV in order.

### Known problems waiting in the unreviewed papers

These were found while reviewing *other* papers and must be fixed when their own turn comes:

- **Dangling citations of items that do not exist.** `[IX, Rem 3.4]` (cited in XI, XII);
  `[X, Prop 4.1]` (in XXI twice, XXII once) and `[X, Thm 3.1]` (in XXII) — both actually refer to
  the content of Paper X's Remark 1.5.
- **`[XIII, Thm 2.1]`** is now Theorem 2.5 and its content is weaker (see §5 below); five papers
  cite it.
- **Inverted sign convention** `χ(σ_p) = χ_{ℓ0}(p^{-1})` copied from the foundational paper's old
  text into **XXIV around line 168** (Paper VIII's copy is already fixed).
- **Paper XXIV, Theorem 2.2 is false**: twin and Sophie Germain primes are *not* obstructed; only
  Landau and Friedlander–Iwaniec are. Paper XXV's contrast sentences depend on it.
- **Paper XX** claims "69 classes" where the computation gives 72; **Paper XXV** claims "6054
  primes" where the check disagrees. Both flagged by `code/verify_series.py`.
- **Papers XVII and XXII** cite `[VIII, Thm 3.2]` (number unchanged, content fine) and `[VIII]`
  generally — re-check against the rewritten Paper VIII.
- **Paper IX's** and **Paper X's** closing open problems are now answered by **Paper XXVIII**;
  their open-problem sections should point there.

### Renumbering maps you will need

Items that moved during review, with the papers that cite them:

- **Paper I**: old Thm 2.3 → Prop 2.2 + Lem 2.4; Thm 3.1 → Prop 3.1; Cor 3.2 → Thm 3.2;
  Rem 4.9/4.10/Cor 4.11 → 4.10/4.11/4.12. The **old "type criterion" (Σ_β = {0} ⟺ III₁) was
  withdrawn** — it is only an upper bound now. IX and XVII used it as if true; IX is fixed, XVII
  is not.
- **Paper II**: Thm 2.4 → 2.5; Prop 4.1 → 4.2; Ex 4.3 → 4.4; Cor 4.4 → Rem 4.5; Lem 5.5 → 5.7;
  Thm 5.6 → 5.8; Cor 5.8/5.9 → 5.11. Content to re-check in III, IX, XIII, XIV, XVIII, XX.
- **Paper III**: Thm 2.2 → 2.3; Cor 2.3 → 2.4; Rem 2.4 → 2.5. Lemma 2.1(4) and "E(Φ)=Λ^⊥" were
  **removed**; VI and VII cited the removed item (both fixed). XIV cites a nonexistent
  "[III, Lem 1.1]".
- **Paper IV**: other papers cite "[IV, Def 2.5]", which does not exist.
- **Paper V**: Def 1.1 → 1.2; Prop 1.2 → 1.3; Thm 1.3 → 1.4; Rem 1.4 → 1.5; Prop 1.5 removed.
- **Paper VII**: Prop 3.3 → 3.4, new Rem 3.5.
- **Paper VIII**: new Lem 3.4, Thm 3.5, Rem 3.6; old Rem 3.4/3.5 → 3.7/3.8; new Rem 5.3;
  Prop 5.3 → 5.4; Rem 5.4 → 5.5.
- **Paper XIII**: new Lem 2.1, Def 2.2, Prop 2.3, Rem 2.4; Thm 2.1 → **2.5**; Rem 2.2 → 2.6.

---

## 5. Results that changed, and that later papers must respect

Short list of the substantive corrections; the full account is in `docs/STATUS.md`.

- **Foundational paper.** Thm 3.6's proof had a gap (the normalisation is not multiplicative;
  fixed with a symmetric 2-cocycle argument). Sign conventions fixed throughout. Prop 6.1
  strengthened to "M is of type III". **One error survives into the published v1 and is recorded
  in `docs/ERRATA.md`:** Prop 2.7's projection `Y_{S'} → Y_S` is canonical only when
  `Cl⁺_{S'} = Cl⁺_S`, because `Cl⁺_S` is a **subgroup** of `Cl⁺_K`, not a quotient.
- **Paper I.** The type criterion is now only an upper bound: `Σ_β ⊆ T(M)`. Two cases are decided
  (S = P_K with β ≤ 1 gives III₁; a band construction gives III_{e^{-1}}).
- **Paper II.** "The ideal lattice is completely determined" was false; replaced by a statement
  using topological principality and Renault's Cartan theorem. The Galois-correspondence and
  fusion-category claims were removed. Infinite index proved for *every* expectation.
- **Paper VI.** The "matrix Kakutani theorem" was ill-posed: a cocycle with constant non-commuting
  increments cannot exist on a relation generated by commuting shifts. Now: the cocycle exists iff
  the Frobenius classes commute; then it is a coboundary iff `Ξ_β(ρ,S) < ∞`.
- **Paper VII.** "Ξ_β = ∞ ⟹ F_ρ ≡ 0" was false (counterexample inside the paper's own S₃
  example). The matrix Fourier transform vanishes iff `ρ^{E_β} = 0`. "Route B" was wrong and is
  now a theorem that inner twists are invisible to KMS states.
- **Paper VIII.** The class-group entry of the arithmetic-topology dictionary was inverted:
  `Cl⁺_S` is the **subgroup** generated by the primes of S, matching `⟨[K_i]⟩ ≤ H₁(M)`, not the
  quotient. Two new results added (every symmetric matrix is a linking matrix; a link realizing
  the full Bost–Connes phase diagram).
- **Paper IX.** The complete W*-invariant is the **flow of weights**, not `Σ_β` (which only bounds
  it). The finite-index inclusion is `M_sym^G ⊂ M_sym`, not `M_ε ⊂ M_sym`.
- **Papers XI and XII.** Both "no boundary KMS state" theorems were proved for an object that is
  the **zero algebra**. Paper XII's Theorem 4.2 had its reduction backwards: by Kuhn's theorem the
  right criterion is `π₀|_{G¹} ⊀ λ_{G¹}` (non-temperedness), not the absence of almost invariant
  vectors — a spectral gap would not have sufficed.
- **Paper XIII.** The reconstruction theorem overclaimed: a groupoid isomorphism gives
  homeomorphisms of the valuation fibres, and a homeomorphism of compact groups carries no group
  structure. `G_S` with its Frobenius classes is recovered only when the symmetry actions are
  intertwined (automatic over Q for Dirichlet-dense S). `h⁺_S` is **not** recovered.
- **Paper XXVIII (new).** Condition (C4) of Paper X is **false**: every element of an arithmetic
  Ore monoid is a unit at almost every place, so the orbit relation is an increasing union of
  smooth relations, hence hyperfinite. The Hurwitz factor is injective. The Ramanujan bound
  `2√p` is *attained* by the Hecke operator, but it is the **tempered** bound, so attaining it
  certifies temperedness — the signature of amenability, not an obstruction to it. This closes the
  whole search of Paper X.

---

## 6. Remaining work, in order

1. **Sequential review of Papers XIV–XXV**, one at a time, fixing the items listed in §4.
2. **Foundational paper v2** from `docs/ERRATA.md`; publish; update DOIs everywhere.
3. **README.md** rewrite for the series (currently describes an earlier state).
4. **Monograph** (`monograph/assemble.py`) cleanup, and revision of its open problem 10.
5. **Zenodo deposits** in order: foundational v2, then I, II, then the rest.
6. Decide whether the two Q47 papers stay unnumbered (current decision: yes) and whether the
   numeral **XXVI stays unused** (current decision: yes — the spacing-statistics paper was
   drafted as XXVI and removed from the series because it contains no KMS content).

---

## 7. Verification scripts

- `code/verify_series.py` — recomputes the numerics of Papers I, IV, V, X, XI, XVI, XIX, XX, XXIV,
  XXV; writes `data/series_checks.json`. Known disagreements are listed in §4.
- `papers/Q47-degree46-family/verify_q47_paper.py` — finite checks of the Q47 paper (all pass).
- `papers/Q47-spacing-statistics/q47_*.py` — the spacing-statistics pipeline. Needs the raw prime
  data, which is **not** in this repository; it lives with the empirical paper
  (DOI 10.5281/zenodo.20753750).

---

## 8. How to resume in one line

> Continue the sequential review of the localized Bost–Connes series at **Paper XIV**
> (`papers/XIV-equalnorm/`), following `HANDOFF.md` and `docs/STATUS.md`: check the mathematics
> line by line, convert citations of unpublished companions to numeral signposts, make every
> bibliography entry cited, fix the known problems listed for that paper, keep the build at
> 0/0/0, and append a STATUS entry recording every change and every renumbering.
