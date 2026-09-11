# Publication plan

Twelve notes (71 pp) regrouped into five papers **by subject, not by sign of result**.
The master paper is Paper I and is unchanged.

| Series no. | Title | Source notes | Status |
|---|---|---|---|
| — | *KMS state uniqueness and phase transitions* (foundational) | `master_bost_connes_paper` | **done**, 23 pp |
| **I** | *Factor type and the spectrum of transitions* | `factor_type_note` + `cantor_spectrum_note` | **done**, 10 pp, revised, `papers/I-type-spectrum/` |
| **II** | *Ideal structure, boundary quotient, and index* | `ktheory_note` + `boundary_simplicity_note` + `subfactor_note` | **done**, 10 pp, `papers/II-structure/` |
| **III** | *Invariants, entropy, and the measure class* | `entropy_note` + `markov_entropy_note` + `modular_homology_note` + `dlhs_determinant_note` | **done**, 8 pp, revised, `papers/III-invariants/` |
| **IV** | *Noncommutative metric geometry* | `nc_metric_note` | **done**, 8 pp, `papers/IV-metric/` |
| **V** | *The free variant and the free critical exponent* | `free_probability_note` + `free_exponent_note` | **done**, 7 pp, `papers/V-free/` |

**One numbering scheme only.** Earlier drafts used two — series numerals in the titles and
working labels (`PaperII`, `PaperV`, …) in the bibitem keys — which clashed. Everything now
uses the series numerals: bibitem keys are `SeriesI`, `SeriesIII`, `SeriesIV`, `SeriesV`,
and the foundational paper is `Main`. The directory `papers/II-structure/` retains its name
from the old scheme but holds **Series II**; rename it when the others are written.

The original notes stay in `paper/` as the working record, including their erratum boxes.
The papers in `papers/` are rewrites, not concatenations.

---

## On negative results

They are kept, and the reason is that most of them are theorems rather than failures. Three
categories, handled differently:

| Category | Treatment | Examples |
|---|---|---|
| **Proved negative theorem** | keep, but subordinate to a positive claim | $\Psi$ is not Lipschitz; $K_0(\mathcal{B})=0$; index always infinite; the free deformation annihilates the cascade |
| **Not computed** | compress to one line in the open problems | $K_*(\partial\mathcal{A}^{\mathrm{aff}})$; the fibre of the free KMS simplex |
| **Erratum** | absorb silently into a correct statement; never publish as an erratum | the three notes flagged below |

Several positive results are meaningless without their negatives. The squeeze theorem
matters because $W_1$ is local while $\Psi$ is a tail observable. The relative-entropy
staircase matters because no dynamical entropy is available. The Cantor realization and the
impossibility of the devil's staircase are two halves of one proof — both follow from
$\widehat{G_S}$ being countable.

**Editorial rule applied in Paper IV, to be applied in V and VI:** lead with the structural
lemma, then present each negative as a corollary of it, and close with a control experiment
that confirms causality. In Paper IV the lemma is the single-isometry phenomenon
(Lemma 1.1: one isometry per prime, nested range projections), and the control is the affine
system, where restoring the additive part restores partitioning ranges and produces a
Kirchberg boundary. What would otherwise read as a list of failures reads as one structural
cause with six consequences.

## Errata status

Three notes carry erratum boxes and **must not be published in that form**:

- `ktheory_note` — Thm. 4.2 false ($\mathcal{A}_{K,S}$ is Cuntz–Pimsner, not Toeplitz).
- `modular_homology_note` — Thms. 5.1, 5.2 false (KMS states are not traces).
- `dlhs_determinant_note` — is itself the erratum.

**Series II absorbed the first; Series III has absorbed the other two.** Prop. 4.1 there states the corrected
$K_1=\ker(1-\alpha_*)$, $K_0=\operatorname{coker}(1-\alpha_*)$ directly, with
$[1]=[\mathbf{1}_{\mathfrak{p}Y_S}]$ given as the reason Pimsner's $KK$-equivalence does not
apply — a positive statement, no erratum language. In Series III, Prop. 3.1 states plainly that a KMS state at $\beta\neq0$ is not a trace and
so does not act on $K_0(\mathcal{A}_{K,S})$; Theorem 3.2 replaces the false "faithful
receptacle" with the eigenvalue equation
$\omega\circ\alpha_{\mathfrak{p}*}=N\mathfrak{p}^{-\beta}\omega$ on
$K_0(C(Y_S))$; and Prop. 4.3 states the correct domain of the de la Harpe–Skandalis
determinant. **No erratum language appears in either paper.** All three source notes are
now superseded.


---

## Paper IV, referee round 1

| Point | Disposition |
|---|---|
| Series numbering unclear | Added a roadmap paragraph in §1 fixing the correspondence between the roman numerals and the five papers. |
| Prop. 2.2 proof: spell out the $\mathfrak{p}'$-component argument | **This surfaced a real gap.** The proof as written used the $\mathbb{Q}$-normalization of $\sigma_\mathfrak{a}$; over a general $K$ the ideal need not be principal and $\sigma_\mathfrak{a}$ is defined only modulo $U_S$. Proposition 2.2 now states the correct general formula $\mathrm{Iso}=\mathrm{div}(\overline{K^\times_{S,+}}\cap\mathbb{I}_T)$, proves triviality unconditionally when $\mathcal{O}^\times_{K,+}$ is finite, and Remark 2.3 records that the general case needs a Leopoldt-type condition we do not decide. **Theorem 2.4 was rewritten to not depend on it**: the strata are nowhere dense whatever their isotropy. |
| Cite Pimsner/Katsura theorem numbers | Papers cited; the specific numbers proposed ("Pimsner Thm. 4.8", "Katsura Thm. 5.5") are **not** asserted, since they are unverified. Logged in `BIBLIOGRAPHY_CHECK.md`. |
| Thm. 5.2: show the $e_k$ are nonzero | Added: $\varphi_2(e_k)=(1-N\mathfrak{p}^{-\beta})N\mathfrak{p}^{-k\beta}>0$ for every $k$, so the family is infinite in the GNS representation. |
| Contrast $[1]$ in the two systems | Added Remark 6.6: the multiplicative $K_0$ is torsion-free and stores $h^+_S$ by divisibility; the affine one is killed by $\gcd(N\mathfrak{p}-1)$. The nested projections are here an *advantage*. The $\mathcal{O}_n$ comparison is included; no claim is made about the ambient affine $K$-groups. |
| Physical reading of index $=$ entropy | Added, but deliberately deflated: both sides are $\log$(number of phases). The identity's content is that the two bookkeepings agree with no correction from the type III structure. |
| "Non-gauge-invariant ideals remain open" | **Misreading.** Theorem 2.4 proves there are none; the question is resolved, not open, and does not appear in §7. |


## Forward references to unwritten papers

Series II originally carried five self-citations, four of them to papers that do not exist,
and two of those were **load-bearing in statements**: the central decomposition of
$M_{\mathrm{sym}}$ and the value of the relative entropy. That is not acceptable — a
referee cannot check a citation to an unwritten paper, and a theorem may not rest on one.

Rule adopted for the whole series: **a paper may signpost its companions but may not depend
on them.** In Series II both dependencies were removed by proving the results in place —
Lemma 5.5 (central decomposition, three lines from [Main, Thm. 3.6]) and Lemma 5.7
(relative entropy $=\log|G|$, purely central, from the direct-sum formula). Both are now
results of Series II rather than imports, which also makes Corollary 5.8
($\log$ index $=$ relative entropy) a self-contained statement.

All `bibitem`s for unwritten papers were deleted; the roadmap in §1 lists the companions by
numeral with the note that they are in preparation and that nothing depends on them. The
only self-citation remaining is [Main], which exists.

When Series I, III, IV, V are written, forward references may be upgraded to real citations
— but the proofs must stay independent, so that each paper is readable alone.


## Progress

| Series | Pages | Self-citations | Errata absorbed | Compile |
|---|---|---|---|---|
| — (foundational) | 23 | 2 (companion notes) | — | clean |
| II | 10 | 1 (`Main`) | K-theory | clean, 0 overfull |
| III | 7 | 2 (`Main`, `SeriesII`) | modular homology, dlHS | clean, 0 overfull |
| I, IV, V | — | — | — | not written |

Series III may cite Series II because Series II now exists; the citations are to
Lemma 5.5 (central decomposition), Corollary 5.8 (index staircase), Proposition 4.1
($K_0=\operatorname{coker}$), Lemma 1.1 (single isometry) and Theorem 3.1 (boundary). Each
is a real result of a real paper. **Series III still does not depend on any unwritten
paper**; the one forward reference, to Paper I for the extended obstruction group, is a
signpost in the open-problems section only.


## Series III, referee round 1

| Point | Disposition |
|---|---|
| Reframe the abstract's "withdrawn and replaced" | Adopted. These notes were never circulated, so a first publication should state the mathematics, not the drafting history. The two propositions remain as results (Prop. 3.1, Prop. 4.3); the correction record stays in this file and in the erratum boxes of the superseded notes. |
| Make the Connes–Thom chain explicit | **This surfaced an overclaim.** Theorem 4.1(1) asserted $K_0(\mathcal{B})=0$, which needs $K_1(\mathcal{A})=\ker(1-\alpha_*)=0$ — verified only for $\lvert S\rvert=1$. For $\lvert S\rvert\geq2$, $K_1(\mathcal{A})$ is the *odd* Koszul homology and is not determined. **The theorem was restated and the proof replaced by a stronger, unconditional one**: from $\hat\varphi\circ\hat\sigma_s=e^{-s}\hat\varphi$ and $\hat\sigma_*=\mathrm{id}$ (homotopy) one gets $\hat\varphi_*[p]=e^{-s}\hat\varphi_*[p]$ for all $s$, hence $0$ — regardless of the group. Remark 4.2 records that connectedness of $\mathbb{R}$, not the vanishing of a $K$-group, is what kills the pairing. |
| Cite CNT / Ohya–Petz for compact-group entropy | Works cited; the proposed numbers ("CMP 1987 Cor. 4.3", "Ohya–Petz Thm. 14.12") **not** asserted, being unverified. |
| Cite Araki / Ohya–Petz for direct-sum relative entropy | Same: works cited, the proposed "Prop. 5.23" not asserted. The formula is displayed with its conventions and its one-line justification. |
| Sharpen the assessment with the Radon–Nikodym point | Adopted, and made concrete: the eigenvalue equation *is* $d(\nu\circ\alpha_\mathfrak{p})/d\nu=N\mathfrak{p}^{-\beta}$, the cohomology is taken modulo the RN cocycle, and the relative entropy is $\int\log(d\omega/d\psi)d\omega$. The negative entries are the constructions that discard the derivative. |
| "Copy-paste remnant: 'the present paper (II)'" | **Misreading.** Series III's roadmap reads "`[SeriesII]` treats ideals, boundary and index", pointing backwards; the phrase quoted is from Series II. No remnant exists. |


## Series III, referee round 2

Three of the four reported symptoms were `pdftotext` extraction artifacts, not source
errors — the source reads `$(\hat\varphi,\hat\delta)$`, `summand-$\varepsilon$`, and
`---` respectively. Verified by grep before touching anything. Two genuine improvements were
extracted from them nonetheless:

| Point | Disposition |
|---|---|
| "(6,8)" in Remark 4.4 | Artifact. Source is `$(\hat\varphi,\hat\delta)$`; hatted Greek does not survive text extraction. No change. |
| "$\mu_\delta$ should be $\mu_\varepsilon$" | The subscript was correct — $\delta$ ranged over $G$, so $\mu_\delta=\lvert G\rvert^{-1}$ *for every* $\delta$ is the intended statement, and $\mu_\varepsilon$ alone would be weaker. **But the report exposed a real collision**: $\delta$ was carrying four roles (Kronecker delta, summation index, generator $\hat\delta$ of the dual flow, modulus $\delta(\epsilon)$). The proof of Thm. 6.1 was rewritten with the index renamed to $\eta$ and the Kronecker delta eliminated; $\delta$ now has two non-adjacent roles. |
| "summand- term" | Artifact (`summand-$\varepsilon$`). Fixed incidentally by the rewrite. |
| Em-dash reads as a minus sign | Source already had `---`, but the point about visual ambiguity next to $e^{-s}$ is fair. Clause parenthesized. |
| Say which paper this is | Adopted: "The present paper is III in the series." Both II and III carry roadmap paragraphs, so a reader should know at once which is in hand. |

**Method note.** When a reported error comes from extracted text, check the source before
editing — three of these would have been "fixed" into errors. The one substantive finding
(the $\delta$ overload) was invisible in the PDF and only appeared on inspecting the source.


## Series I

Written as a merge, not a concatenation: 17 pp of notes into 10 pp, organized around the
observation that the two notes answer the **two coordinate directions of one object**. The
extended obstruction group $\Xi^{\mathrm{ext}}_\beta\leq\widehat{G_S}\times\mathbb{R}$
has the phase classification as its $s=0$ slice and the factor type as its $s\neq0$ slices;
at $S=P_K$, $\beta=1$ both reduce to non-vanishing of Hecke $L$-functions on
$\mathrm{Re}=1$.

Duplication removed: the coboundary/essential-values dictionary, which appeared in both the
factor-type note and the modular-homology note, is now stated once in Series III
(Lemma 2.1) for a general abelian target and **cited** here for the target
$G_S\times\mathbb{R}$. That is the only technical import, and Series III exists.

Self-citations: 3, all to written papers (`Main`, `SeriesII`, `SeriesIII`). No forward
dependence on Series IV or V.

The four numerical checks carried over from the notes are recorded as remarks with their
parameters and outcomes: band weights and Siegel–Walfisz cancellation (Rem. 4.9), the 16
joint sign-pattern densities and detecting sets (Rem. 5.7), pointwise invariance of $\Psi_n$
and the 15-subset independence test (Rem. 7.3).

## Progress

| Series | Pages | Self-citations | Compile |
|---|---|---|---|
| — (foundational) | 23 | 2 | clean |
| I | 10 | 3 | clean, 0 overfull |
| II | 10 | 1 | clean, 0 overfull |
| III | 8 | 2 | clean, 0 overfull |
| IV, V | — | — | not written |

Remaining: **IV** (noncommutative metric geometry) needs only a light edit of
`nc_metric_note`; **V** (the free variant) merges `free_probability_note` and
`free_exponent_note`.


## Series I, referee round 1

| Point | Disposition |
|---|---|
| Add placeholder `bibitem`s for Papers IV and V | **Declined**, and this is a policy point rather than a preference. Two rounds ago Series II was found to carry four citations to unwritten papers, two of them load-bearing, and the rule adopted was: *a paper may signpost its companions but may not depend on them*, with all such `bibitem`s deleted. Reinstating them in Series I would either make the series internally inconsistent, or force us to put back into Series II exactly what was removed from it. A `bibitem` to a nonexistent paper cannot be checked by a referee. The roadmap in §1 names Papers IV and V without citing them; they get real entries when they exist. |
| Make $\mathcal{L}(S)\cap(0,1)=\overline{J(S)\cap(0,1)}$ explicit in Cor. 6.2 | Adopted. The proof now derives the identification of the non-local-constancy locus with the closure of the jump set, and points at Rem. 6.7. |
| Display the error absorption in Lemma 4.4 | Adopted **with a correction**. The suggested display was $\log\log\log x=o(\log\log x)$; the comparison must be with $W(x)\asymp4\sqrt{\log\log x}$, so the statement needed is $\log\log\log x=o(\sqrt{\log\log x})$. The weaker form is true but does **not** complete the argument. Equation (4.3) now displays the correct comparison and says explicitly why it is with the square root. |
| Supply the lower limit in the Lemma 5.4(2) integral | Adopted, with all three regimes spelled out: constant $z_n^{\beta_n-\beta}$ from the lower limit, convergence for $\beta>\beta_n$, $\beta_n\log(x/z_n)$ at the endpoint, power divergence below. |
| Assessment table | No change requested or made. |


## The series is complete

| Series | Title | Pages | Self-cites | Overfull | Unresolved | Errata |
|---|---|---|---|---|---|---|
| — | KMS state uniqueness and phase transitions | 23 | 2 | 0 | 0 | 0 |
| I | Factor type and the spectrum of transitions | 10 | 3 | 0 | 0 | 0 |
| II | Ideal structure, boundary quotient, and index | 10 | 1 | 0 | 0 | 0 |
| III | Invariants, entropy, and the measure class | 8 | 2 | 0 | 0 | 0 |
| IV | Noncommutative metric geometry | 8 | 4 | 0 | 0 | 0 |
| V | The free variant and the free critical exponent | 7 | 4 | 0 | 0 | 0 |

**66 pages of papers from 71 pages of notes and a 23-page foundational manuscript.** Every
self-citation now points at a paper that exists; the rule "signpost but do not depend" was
kept throughout, and Series IV and V, written last, were able to cite I–III legitimately.
All three errata are absorbed as positive statements and no paper contains the word
"erratum".

### The organizing idea of each paper

- **I**: the extended obstruction group $\Xi^{\mathrm{ext}}_\beta\leq\widehat{G_S}\times\mathbb{R}$
  has the phase classification as its $s=0$ slice and the factor type as its $s\neq0$
  slices.
- **II**: the single-isometry lemma — one isometry per prime, nested range projections —
  with the affine system as a control experiment confirming causality.
- **III**: $\Xi_\beta$ is an invariant of a *measure class*; every construction that
  discards the Radon–Nikodym derivative is blind to it.
- **IV**: three invariants jump at each threshold and the metric one does not, because the
  order parameter cannot be Lipschitz for a Dirac operator metrizing the weak-* topology.
- **V**: the free deformation is incompatible with the phase structure — it removes exactly
  the high-temperature region where $\Xi_\beta$ lives.

### Still open across the series

Bibliography metadata is now in much better shape: a referee supplied full details for 47 of
the 55 external entries, with no conflicts against what we had. These are marked
**referee-supplied**, not **verified**, in `BIBLIOGRAPHY_CHECK.md` — the distinction matters,
because recording someone else's check as our own would make any error untraceable. Seven
entries remain unchecked, and one gap was exposed: Series II, Ex. 4.3 uses
Pimsner–Voiculescu without citing it. The priority
question narrowed in `PRIORITY_CDL.md` — whether any published classification has treated
infinite sparse $S$ with $0<\beta_c(S)<\infty$ — is also unresolved and should be settled
before submission.


## Correction found during the referee round

The foundational paper was still citing the two **superseded notes** (`FactorType`, `Cantor`)
rather than Series I, which replaced them. This was introduced when Series I was written and
the master paper was not revisited. Both citations now point at
`\bibitem{SeriesI}`; the master paper has one self-citation and still compiles clean at
23 pp.

**Lesson for the remaining work:** when a note is superseded by a paper, every citation of
that note across the whole corpus must be re-pointed in the same commit. A grep for
`companion note` across all six papers is now part of the pre-submission checklist.


## Pre-submission checklist

1. ~~Series II, Ex. 4.3 cites the coinvariant sequence without naming Pimsner–Voiculescu.~~
   **Done** — `\bibitem{PV}` added and the proof now invokes Laca's dilation theorem and the
   PV six-term sequence explicitly.
2. All 55 references are 🟨 referee-supplied with MR numbers. Promote to ✅ by one pass
   through MathSciNet. **Mechanical, no judgement required.**
3. Theorem numbers inside cited works remain unasserted throughout. Any that are wanted must
   be read at the source.
4. The priority question is **not closed**. A referee survey agrees with our own Parts I–III,
   which is real corroboration, but a negative claim about a literature needs a repeatable
   search. Recommendation: post the foundational paper as a preprint to fix the date, and
   continue the search in parallel rather than blocking on it.


## Phase II: the non-abelian question

`papers/VI-nonabelian/` (7 pp, clean) examines whether the $GL_1$ theory extends to
non-abelian Galois image. It is **not** numbered in the Series I–V sequence, because it does
not complete a construction — it determines what the answer would have to be and identifies
what is missing.

**Transfers unchanged.** The Kakutani dichotomy is representation-theoretic, not
character-theoretic: with $\|I_n-U\|_{\mathrm{HS}}^2=2(n-\mathrm{Re}\,\mathrm{Tr}\,U)$
the whole analysis goes through for $U(n)$-valued cocycles. The Chebotarev criterion
transfers for **finite image** (Artin) representations, with detecting set
$D_\rho=\{\mathfrak{p}:\rho(\mathrm{Frob}_\mathfrak{p})\neq I\}$.

**Does not transfer.** The classification $\mathrm{Prob}(G_S/\Xi_\beta^\perp)$ uses
Pontryagin duality twice. For non-abelian $G$ the irreducibles form a based set with a fusion
rule, not a group; $\Xi_\beta$ cannot be a subgroup of it and $\Xi_\beta^\perp$ is
undefined.

**The replacement.** $\mathcal{T}_\beta=\{\rho:\Xi_\beta(\rho,S)<\infty\}$ is closed
under $\oplus$, subobjects, $\otimes$ and duals — verified both algebraically and
numerically — hence Tannakian, hence $\mathcal{T}_\beta=\mathrm{Rep}(G/N_\beta)$. **The
obstruction generalizes as a quotient of the group, not a subgroup of its dual**; in the
abelian case $N_\beta=\Xi_\beta^\perp$.

**Two corrections to the proposed formulation.**
1. The Euler identity is $\Xi_\beta=2n\log\zeta_{K,S}(\beta)-2\,\mathrm{Re}\log L_S(\beta,\rho)+O(1)$.
   The proposed $\log\zeta_{K,S}(n\beta)-\mathrm{Re}\log L_S$ is wrong twice: the zeta
   factor is at $\beta$, not $n\beta$ — $n$ enters as the coefficient $2n$ from
   $\mathrm{Tr}\,I_n=n$, not as a dilation — and both terms carry a factor 2.
2. Sato–Tate **forbids** symmetry breaking rather than producing it:
   $\int 4(1-\cos\theta)\,d\mu_{ST}=4$ exactly, so $\Xi_\beta\sim4\zeta_S(\beta)$
   diverges whenever the partition function does. Exotic phases require *deliberately
   anomalous* sets, and Theorem 5.3 constructs one (blocks with $\theta_p\leq2^{-j}$),
   conditional on Sato–Tate as an equidistribution input.

**Not done.** No $GL_n$ algebra is constructed. $M_n(J_S)$ is not a semigroup with the
needed cancellation, and the Connes–Marcolli $GL_2$ system is a different object — its
symmetry is $GL_2(\mathbb{A}_f)$ acting on lattices, its arithmetic that of modular
functions, with no Galois group acting through Frobenius classes. §6 states the gap and two
possible routes. **Until an algebra exists, "non-abelian symmetry breaking" is premature:
there is an obstruction group with nothing yet to obstruct.**


## Phase II, second step: the construction succeeds, the prediction does not

`papers/VII-galois-groupoid/` (6 pp, clean) executes Route A. **The construction works and
the KMS classification is complete**, so the question left open in Paper VI §6 is answered.
The answer is not the expected one.

**Theorem 4.2.**
$\mathrm{KMS}_\beta(\mathcal{A}_{G,S})\cong\mathrm{Prob}(E_\beta\backslash G)$, with
$G$ acting transitively on extreme points and stabilizer $E_\beta=\Xi_\beta(A)^\perp$,
computed by the **abelian** Kakutani criterion inside $A=\overline{\mathrm{Frob}(I_S)}$.

**This is not $\mathrm{Prob}(G/N_\beta)$.** A representation category sees only *normal*
subgroups, being determined by kernels; the ergodic decomposition of a skew product by a
non-normal subgroup is a coset space with no group structure. Concretely (Example 5.2):
$G=S_3$, $\mathrm{Frob}_\mathfrak{p}=(12)$ for all $\mathfrak{p}$ gives
$E_\beta=\{e,(12)\}$, so $|E_\beta\backslash G|=3$ — a 2-simplex, spontaneous symmetry
breaking with three phases — while $\mathcal{T}_\beta=\{\mathbf{1}\}$, $N_\beta=S_3$,
and $\mathrm{Prob}(G/N_\beta)$ is a **point**. Three against one.

**Corollary 5.4: $\Xi_\beta$ does not determine the KMS simplex when $G$ is non-abelian.**
The obstruction data know only $N_\beta$ = the normal closure of $E_\beta$. Since the
$L$-functions of Paper VI §4 see exactly the obstruction data, any programme reading a
non-abelian phase structure off automorphic $L$-functions must confront this: **the
$L$-functions know $N_\beta$, and $N_\beta$ is not enough.**

This *corrects the emphasis* of Paper VI Theorem 3.2. That theorem is correct as stated —
$\mathcal{T}_\beta=\mathrm{Rep}(G/N_\beta)$ — and Remark 3.3 there explicitly declined to
claim it computed any simplex. It does not.

**Two further corrections.** The matrix zero-one law "$F_\rho F_\rho^*=c_\rho I$" is
**false**: the cocycle equation *conjugates* $F_\rho F_\rho^*$, so ergodicity forces only
its spectrum to be a.e. constant. Counterexample computed: $G=S_3$, 2-dim irrep,
$\lambda=\frac12(\delta_e+\delta_{(12)})$ gives a rank-one projection, eigenvalues
$\{0,1\}$. And the cohomological equation carries $\rho(\mathrm{Frob}_\mathfrak{p})^{-1}$,
not $\rho(\mathrm{Frob}_\mathfrak{p})$.

**Route B is not independent** (Prop. 6.1): the matrix crossed product is what one sees on a
single Peter–Weyl block of Route A, and cannot repair the discrepancy, since conjugation by
$\rho(\mathrm{Frob}_\mathfrak{p})$ only ever sees $\rho(E_\beta)$ up to conjugacy.

**The deepest limitation** (Remark 1.3): $I_S$ is abelian and $a\mapsto\mathrm{Frob}_a$ is a
homomorphism, so its image is *always* abelian. Every cocycle computation happens inside $A$;
$G$ contributes only the homogeneous space. **No construction with an abelian acting
semigroup can be genuinely non-abelian.** A non-abelian semigroup costs the high-temperature
region (Series V, Thm. 1.2). Whether an Ore semigroup that is non-abelian but has nested
rather than partitioning range projections exists is the open structural question.
