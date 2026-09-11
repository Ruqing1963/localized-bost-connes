# Bibliography verification

## Status legend

- ✅ **verified** — checked against the source or a bibliographic database *by this project*
- 🟨 **referee-supplied** — full metadata provided by a referee who states it was checked
  against MathSciNet / zbMATH; **not independently verified here**, since this environment
  has no network access
- ⬜ **unchecked** — no verification of any kind

The distinction between ✅ and 🟨 is not pedantry. A referee's report is evidence, and good
evidence, but recording it as our own verification would launder an unchecked claim into the
repository. If the referee mistyped a volume number, the error would then be untraceable.
Before submission each 🟨 entry should be confirmed once at the source, which is a quick
mechanical task for anyone with database access.

## Referee round (2026)

A referee supplied volume, issue, year, page range and author spellings for **47 entries**,
stating these were collated from MathSciNet / zbMATH and the original journals. Where the
referee's data differed from ours in level of detail — issue numbers, the `1975/76` volume
designation for Araki's RIMS paper, page counts for monographs — the fuller form has been
adopted in this file. No **conflicts** were found between the referee's data and the
existing entries; the differences were all additions.

These 47 are now marked 🟨. They cover the bulk of the load-bearing citations, including
every entry previously flagged as a risk: Pimsner, Katsura, Green, Takesaki, Kosaki, Longo,
Watatani, Izumi–Longo–Popa, Renault, Exel, Laca, Neshveyev (2002 and 2013),
Cuntz–Deninger–Laca, Cuntz–Li, Araki, Connes–Narnhofer–Thirring, Voiculescu.

### Second referee round: the remaining seven, with MR numbers

The seven entries left open were supplied in a second round, now **with MathSciNet review
numbers**, which makes each a single-lookup confirmation rather than a judgement call:

| Entry | MR | Correction to what we had |
|---|---|---|
| Ha–Paugam, *BCM systems for Shimura varieties. I*, IMRP **2005**, no. 5, 237–286 | MR2211153 | subtitle "I. Definitions and properties" added |
| Hardy–Littlewood, *Partitio numerorum III*, Acta Math. **44** (1923), 1–70 | MR1555183 | year 1923 confirmed |
| Halberstam–Richert, *Sieve Methods*, LMS Monographs 4, Academic Press, 1974, xiv+364 | MR0424730 | series and page count added |
| Bratteli–Robinson, *OA and QSM 2*, **2nd ed.**, Springer, **1997**, xiv+517 | MR1441540 | **year was missing; 2nd ed. is 1997** |
| Furstenberg, *Strict ergodicity and transformations of the torus*, Amer. J. Math. **83** (1961), 573–601 | MR0133429 | year 1961 confirmed |
| Araki–Woods, *A classification of factors*, Publ. RIMS Ser. A **4** (1968/69), 51–130 | MR0244773 | `1968/69` volume designation |
| Billingsley, *Convergence of Probability Measures*, **2nd ed.**, Wiley, 1999, x+277 | MR1700749 | page count added |

All 55 entries are now 🟨. None is ✅, for the reason given above; but with MR numbers in
hand, promoting the whole file to ✅ is one afternoon's work for anyone with database access,
and no judgement is required.

### Gap closed

**Pimsner–Voiculescu (1980)**, J. Operator Theory **4** (1980), no. 1, 93–118, is now cited
in Series II. Example 4.3 previously used the coinvariant sequence for a crossed product by
$\mathbb{Z}$ without naming its source; the proof now opens by invoking Laca's dilation
theorem and the Pimsner–Voiculescu six-term sequence explicitly.

## Theorem numbers: still asserted nowhere

Independently of the metadata above, this project has consistently **declined to assert
internal theorem numbers** it could not check — "Pimsner Thm. 4.8", "Katsura Thm. 5.5",
"CNT Cor. 4.3", "Ohya–Petz Thm. 14.12", "Ohya–Petz Prop. 5.23" were all proposed by referees
and all omitted. The papers cite works and sections only. Correct volume metadata does not
license a theorem number; those must be read.

## Beyond bibliographic accuracy

**The priority question is of a different logical type, and its status is different.**
`PRIORITY_CDL.md` narrowed it to: *has any published classification treated infinite sparse
$S$ with $0<\beta_c(S)<\infty$?*

A referee has now reported a survey of the 1995–2026 literature and answers no, with the
following partition of the known results:

| Work | Coverage | $\beta_c$ |
|---|---|---|
| Bost–Connes 1995; Laca–Raeburn 1999; Neshveyev 2002 | $K=\mathbb{Q}$, $S=P_\mathbb{Q}$ | 1 |
| Ha–Paugam 2005; Laca–Larsen–Neshveyev 2009 | general $K$, $S=P_K$ | 1 |
| Laca–Neshveyev 2004; Laca–Raeburn 2010 | finite $S$, so $J_S\cong\mathbb{N}^k$ | 0 |
| Cuntz–Li 2010; Cuntz–Deninger–Laca 2013 | affine $ax+b$; additive cosets force $\beta=1$ | 1 |

This is **consistent with Parts I–III of `PRIORITY_CDL.md`**, which reached the same
conclusion for the two cases we examined ourselves — the finite-$S$ computation
($\Xi_\beta=\widehat{G_S}$ for all $\beta>0$, so no transition) and the $ax+b$ rigidity —
by direct calculation rather than by survey. Agreement between an independent survey and our
own computations raises confidence appreciably.

It does not settle the question, and the reason is logical rather than procedural. A
metadata check is a **positive** claim about one specific object, confirmable in one lookup.
"No one has published this" is a **negative** claim about an entire literature; a search that
finds nothing is weaker evidence than a search that finds something, and neither we nor the
referee can exhibit the search. Two things would make it decisive: a documented search
strategy (databases, query strings, date ranges, MSC classes) that a reader could repeat, and
a check of works citing Laca–Raeburn 1999 and LLN 2009, which is where a sparse-$S$ treatment
would most plausibly appear.

Practical recommendation: post the foundational paper as a preprint, which fixes the date for
$\Xi_\beta$, and continue the search in parallel. That is the standard way to hold priority
while a negative claim is being checked, and it does not require the claim to be settled
first.
