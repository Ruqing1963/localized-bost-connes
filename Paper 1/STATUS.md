# Project status

## Review log (sequential fine review, started 28 August 2026)

**Repository link.** Every paper now carries the repository URL on its title page and in all
self-citations; `CITATION.cff` and the arXiv metadata name the real repository.

**Foundational paper — reviewed line by line; 21 corrections, all theorem and equation numbers
unchanged (verified label by label against the previous build).**

1. *Theorem 3.6, proof (gap).* The explicit normalisation
   $g_\chi=\lim\prod\overline{(m_\pp/|m_\pp|)}c_\pp^{v_\pp}$ was claimed multiplicative in
   $\chi$. It is not: $m_\pp(\chi)=(1-t_\pp)/(1-c_\pp t_\pp)$ has non-additive argument
   (for $c=i$, $\arg m=\arctan t$, while for $c^2=-1$ it is $0$). The proof now shows that
   $g_{\chi_1}g_{\chi_2}/g_{\chi_1\chi_2}$ is a constant $\omega(\chi_1,\chi_2)$, a symmetric
   $2$-cocycle on the countable abelian group $\Xi_\beta$ with values in $\mathbb T$, hence a
   coboundary since $\operatorname{Ext}(\Xi_\beta,\mathbb T)=0$; rescaling by that coboundary
   gives the multiplicative family the Bochner argument needs. The theorem is unaffected.
2. *Sign convention.* With $\sigma_\aaa:=r(s_\aaa)^{-1}$ as in (2.2), one has
   $\sigma_\pp\mapsto[\pp]^{-1}$ in $\Cl^+_S$ and, over $\mathbb Q$, $\sigma_\ell=\theta_\ell$
   (component $\ell$ at $\ell'\ne\ell$), not $\theta_\ell^{-1}$; the proof of Prop.\ 4.12(2)
   already used $\theta_\ell$. Lemma 2.10(1), Example 3.13, Prop.\ 4.1, the intro of \S4.2,
   Lemma 4.6, Props 4.7, 4.9, 4.16 corrected accordingly ($\chi'(\sigma_\ell)=\tilde\chi'(\ell)$).
   No conclusion changes ($|1-\chi(g)|=|1-\chi(g^{-1})|$), but the same inverted formula
   $\chi(\sigma_p)=\chi_{\ell_0}(p^{-1})$ was copied into Papers VIII (l.\ 422) and XXIV
   (l.\ 168) and must be corrected there.
3. *Prop.\ 3.4.* The density $1+\operatorname{Re}(\overline{g_\chi}\chi)$ produced
   $\widehat{\rho_v}(\chi)=\tfrac12\overline{g_\chi}$, the wrong direction for (3.2); corrected to
   $1+\operatorname{Re}(g_\chi\chi)$, and the case $\chi^2=1$ (coefficients merge, $g_\chi=\pm1$)
   made explicit.
4. *Conventions.* The claim that $G_S$ "need not be profinite" was false: $G_S$ is compact and
   totally disconnected (van Dantzig), hence profinite. Rewritten.
5. *Lemma 2.3.* "Proper quotient" only when $K$ has a real place.
6. *Prop.\ 2.5.* $U_S\cap\overline{K^\times_{S,+}}=\overline{U_S\cap K^\times_{S,+}}$ needs $U_S$
   open; said.
7. *Lemma 3.8.* $\chi$ is a character of $G_S$, not of a Galois group; the proof now shows that
   $G_S\hookrightarrow\Gal(K^{S}/K)$ (injectivity from the restricted-product topology), that
   $\chi$ extends with trivial inertia outside $S$, and that $\chi(\Frob_\pp)$, $\pp\in S$, is
   independent of the extension. Folded into the proof so as not to shift numbering.
8. *Prop.\ 6.1.* Exponent sign ($\mathrm{III}_{\lambda_0^{-\beta}}$, not $\lambda_0^{\beta}$), and
   the statement strengthened from "not of type I" to "of type III": a new in-place proof
   shows the Radon--Nikodym cocycle is never a coboundary when $\zeta_{K,S}(\beta)=\infty$
   (the characteristic function of $\log f$ would be bounded below near $0$ by
   $\prod|m_\pp(t)|$, forcing $\sum\Ns\pp^{-\beta}|1-\Ns\pp^{i\beta t}|^2$ to be bounded near
   $0$, which Tonelli refutes). The commensurable case is then $\mathrm{III}_{\lambda_0^{-n\beta}}$
   or $\mathrm{III}_0$, with no appeal to Paper I.
9. *No citation of unpublished work.* The original citation of Paper I (Prop.\ 6.1, Remark 6.2,
   open problems 1--2) and a citation of Paper XVII that I had added (open problem 3) are
   removed; the passages are now self-contained signposts. The bibliography has 15 published
   entries, each cited.
10. *DOI.* 10.5281/zenodo.22152101 on the title page, in `CITATION.cff`, `.zenodo.json`,
   `README.md`, the arXiv comments, and in the `[Main]` entry of the 20 papers that cite it.
11. *Numbers quoted in metadata.* The Leopoldt remark is 4.18 (README, arXiv notes and Zenodo
   description said 4.17); corrected.

Bibliography of the foundational paper: all 16 entries agree with my recollection of the
sources (journals, volumes, years, pages); this is corroboration, not the MathSciNet
verification `BIBLIOGRAPHY_CHECK.md` still requires.

**Paper I — reviewed line by line; Sections 2–3 rewritten, one proof completed, three
smaller repairs. DOI 10.5281/zenodo.22160827 on the title page and in the 11 papers citing it.
Theorem numbering changed (see the end of this entry).**

1. *Theorem 2.3 (type criterion) was not proved, and its "if" directions are not known.* The
   old Lemma 2.1 asserted $E(\Phi)=(\Xi^{\mathrm{ext}}_\beta)^\perp$, citing Paper III; that
   duality holds for *regular* cocycles only, and the proof of the old theorem also identified
   the flow of weights with the translation flow on $\mathbb R/\Sigma_\beta^\vee$, which in the
   $\mathrm{III}_0$ case is the flow of a $\mathrm{II}_\infty$ factor, not of a $\mathrm{III}_0$
   one. What is provable without regularity: every $(\chi,s)\in\Xi^{\mathrm{ext}}_\beta$ makes
   $e^{-is\rho}$ a coboundary on the KMS measure (transfer function
   $g(v)\overline{\chi(h)}$), hence the essential values $E$ of the Radon--Nikodym cocycle
   satisfy $E\subseteq\Sigma_\beta^\vee$ — an *upper bound* on the type (new Prop.\ 2.2:
   $\Sigma_\beta\ne0\Rightarrow$ not $\mathrm{III}_1$; dense $\Rightarrow\mathrm{III}_0$;
   $c\mathbb Z\Rightarrow\mathrm{III}_{\lambda^k}$ or $\mathrm{III}_0$) and $\Sigma_\beta$ lies
   in the point spectrum of the flow of weights (Remark 2.3). The converse would follow if the
   flow of weights always had pure point spectrum, which is not known; it is now listed as the
   first open question. Lower bounds are supplied by a new Lemma 2.4 (asymptotic pairs, the
   Araki--Woods argument with the $G_S$-coordinate carried along, stated for
   $\Xi_\beta=\{1\}$), with a complete proof. "Not semifinite because $\Phi$ has nontrivial
   essential values" was not an argument; type III is now cited from the foundational paper's
   Prop.\ 6.1.
2. *The classical systems.* Old Thm 3.1/Cor 3.2 derived $\mathrm{III}_1$ for $S=P_K$,
   $\beta\le1$ from the unproved direction. Now: Prop.\ 3.1 proves
   $\Xi^{\mathrm{ext}}_\beta=\{(1,0)\}$ (Hecke--Landau, prime ideal theorem in ray classes), and
   Thm 3.2 proves $\mathrm{III}_1$ via Lemma 2.4 with pairs of primes in a common ray class
   (Bost--Connes and Laca--Larsen--Neshveyev cited as the original sources).
3. *Theorem 4.2 ($\mathrm{III}_{e^{-1}}$ example).* Its proof used the unproved direction to pass
   from $\Sigma_1=2\pi\mathbb Z$ to $\mathrm{III}_{e^{-1}}$. Now: Prop.\ 2.2(3) gives
   $E\subseteq\mathbb Z$, and a new Lemma 4.9 (matched pairs in consecutive bands, Siegel--Walfisz
   with modulus $M_n=\prod_{\ell'\le\log\log n}\ell'^{\lfloor\log\log n\rfloor}$) exhibits $1\in E$;
   hence $E=\mathbb Z$ and the type is exactly $\mathrm{III}_{e^{-1}}$ — the original claim,
   now proved.
4. *Block scheme / Prop.\ 7.2(1).* Pointwise invariance of $\Psi_n$ fails for $m=q_j$, $j>n$,
   unless $(q_j/q_n)=+1$; Definition 5.3 now chooses $q_j$ with $(q_j/q_i)=+1$ for all $i<j$,
   and the proof covers this case. Also $u_{q_n}\mapsto\ell_0u_{q_n}$ (not $\ell_0^{-1}u_{q_n}$),
   matching the corrected convention of the foundational paper.
5. *Conventions.* $c_n=\sum\tilde\chi(\ell)/\ell$ (not $\overline{\tilde\chi}$), since
   $\chi(\sigma_\ell)=\tilde\chi(\ell)$; harmless for the cancellation lemma.
   $[\mathrm{Main},\ \mathrm{Lem.}\ 2.9]\to2.10$. Countability of $\widehat{G_S}$ justified by
   second countability, not by an embedding into $\bigoplus\widehat{\mathcal O_\pp^\times}$
   (which does not exist).
6. *Numerics recomputed* (`code/verify_series.py`, section "Paper I"): sign-pattern densities
   $[0.0621,0.0629]$ confirmed; band ratios $w_n/\log\frac{n+\varepsilon}{n-\varepsilon}$ lie in
   $[0.998,1.003]$ for $13\le n\le17$ (the paper said $[0.9995,1.0030]$; $n=13$ gives $0.9981$;
   corrected); $|c_n|/w_n$ at $n=9,17$ confirmed. The $\Psi_n$-invariance and independence
   checks of Remark 7.3 were not rerun.
7. *No citation of unpublished work.* Papers II and III were cited (series paragraph, Lemma
   2.1, Remark 7.4, assessment); all replaced by self-contained statements. Bibliography: 13
   published entries, each cited (Araki--Woods, Billingsley, Connes, Connes--Takesaki, Hecke,
   Krieger, Landau, LLN, Maharam, Neukirch, Schmidt, BC, Main); LLN added.
8. *Renumbering.* Old $\to$ new: Lem 2.1 (identification) $\to$ Lem 2.1 (dictionary, different
   content); Thm 2.3 $\to$ Prop 2.2 (upper bound only) $+$ Lem 2.4; Thm 3.1 $\to$ Prop 3.1
   (slices only); Cor 3.2 $\to$ Thm 3.2; Lemma 4.9 new, so Rem 4.9/4.10, Cor 4.11 $\to$ 4.10/4.11,
   4.12; Sections 5–7 unchanged. Citations in the other papers were renumbered mechanically,
   **but Paper IX (rigidity) uses the old Theorem 2.3 as an equivalence** (complete
   $W^*$-invariant $=\Sigma_\beta$; flow of weights $=\mathbb R/\Sigma_\beta^\vee$) and Paper
   XVII refers to it as determining $\Sigma_\beta$: both must be rewritten when reviewed.

**Paper XXIV — a false theorem, found while checking the foundational paper's Thm 5.5(5).**
Theorem 2.2 there claims that twin and Sophie Germain primes are permanently obstructed by the
nontrivial character mod 3 because they lie in the class $2\bmod3$. But
$\chi(\sigma_p)=(p/3)=-1$ for every such $p$, so the detecting set is *all* of $S$, not a
finite set: confinement to a residue class obstructs only when that class generates a proper
subgroup (as $1\bmod4$ does for Landau and Friedlander--Iwaniec; $2$ generates
$(\mathbb Z/3)^\times$). The foundational paper's Lemma 5.6 ($\langle A_M\rangle=(\mathbb Z/M)^\times$)
already says exactly this. Consequences: XXIV's abstract, title, Thm 2.2, Cor.\ 2.4 and the
statement "this corrects the master paper" (below, now retracted) must be revised to *two*
families; XXV's contrast sentence and the monograph's closing remark ("Chen primes remain the
only candidate") change; the foundational paper needs **no** change on this point.
`code/verify_series.py` now computes the detecting sets and reports the failure.

**Also found by recomputation (`code/verify_series.py`, `data/series_checks.json`):** XXIV's
table counts Chen primes to $2\cdot10^4$ (not $2\cdot10^5$) and Piatetski-Shapiro values for
$n\le4000$ (not $p\le2\cdot10^5$); the Heath-Brown count 623 depends on an unstated
enumeration box; XX's "69 classes" is 72 by direct count (samples all confirmed); XXV's 6054
excludes $p=3$ as well as the bad primes 2, 31. Everything else recomputed (X, XI, XVI, XIX,
XX samples, XXV proportions and sample sizes) agrees exactly.

---


## The corpus: 26 papers, 163 pages, all compiling clean

| | Title | pp | Compile |
|---|---|---|---|
| — | KMS state uniqueness and phase transitions (foundational) | 23 | clean |
| I | Factor type and the spectrum of transitions | 10 | clean |
| II | Ideal structure, boundary quotient, and index | 10 | clean |
| III | Invariants, entropy, and the measure class | 8 | clean |
| IV | Noncommutative metric geometry | 8 | clean |
| V | The free variant and the free critical exponent | 7 | clean |
| VI | Towards non-abelian systems: matrix Kakutani and a Tannakian obstruction | 7 | clean |
| VII | The Galois-twisted groupoid and its KMS classification | 6 | clean |
| VIII | Arithmetic topology: local CFT, linking Kakutani, topological transitions | 7 | clean |
| IX | Amenability and the failure of $W^*$-superrigidity | 6 | clean |
| X | A non-commutative Ore LCM semigroup: the Hurwitz quaternions | 5 | clean |
| XI | Condition (C4) and the nested/partition dichotomy | 5 | clean |
| XII | Universal multiplicity–norm mismatch; (C4) reduced to $G^1$ | 5 | clean |
| XIII | Equivariant rigidity: the fixed-point algebra is the Cartan subalgebra | 4 | clean |
| XIV | The equal-norm case: separation is a characterization, not a hypothesis | 5 | clean |
| XV | What $\sigma$-equivariance gives free; the spectral route is closed | 4 | clean |
| XVI | Quantum optimal transport: twist, sign error, and tensorisation | 5 | clean |
| XVII | Function fields: commensurability forbids III$_1$, the factor recovers $\beta$ | 5 | clean |
| XVIII | The compact group advantage is illusory; $Z_C$ is the partition function | 4 | clean |
| XIX | Isogeny vs isomorphism: the Jacobian group is the torsion of $G_S/\overline{U_S}$ | 4 | clean |
| XX | Twin curves: the resolution boundary is a $\mathrm{Pic}(\mathcal{O})$-torsor | 5 | clean |
| XXI | $GL_2$: equilibrium and obstruction ranges are disjoint by exactly 1 | 4 | clean |
| XXII | Iwasawa: there are no $p$-adic KMS states | 4 | clean |
| XXIII | Leopoldt gives the isotropy *rank*; $\log_p(N\mathfrak{p})=0$ | 4 | clean |
| XXIV | Sieve primes: four of six families are never unique | 4 | clean |
| XXV | Sato–Tate families: open phase, no obstruction, unique above $\beta_c$ | 4 | clean |

Verified across all eight: **0 LaTeX errors, 0 overfull boxes, 0 unresolved references,
0 citation warnings, 0 erratum remnants, every self-citation key defined.**

## The closing result (Paper VII)

The non-abelian construction succeeds and its KMS classification is complete:

  KMS_β(A_{G,S}) ≅ Prob(E_β \ G),

with G transitive on extreme points and stabilizer the essential-value subgroup E_β,
computed by the *abelian* Kakutani criterion inside A = closure(Frob(I_S)).

**This is not Prob(G/N_β).** A representation category is determined by kernels and sees only
normal subgroups; N_β is the normal closure of E_β, while the ergodic decomposition of a skew
product by a non-normal subgroup is a coset space with no group structure. For G = S₃ with
Frob_p = (12): **three** extremal KMS states where the Tannakian prediction is **one**.

Hence **Ξ_β does not determine the KMS simplex when G is non-abelian**, and since the
automorphic L-functions see exactly Ξ_β, they know only N_β — and N_β is not enough.

This corrects the emphasis of Paper VI without contradicting it: Theorem 3.2 there
(T_β = Rep(G/N_β)) is correct as a statement about the category, and Remark 3.3 explicitly
declined to claim it computed any simplex. It does not.

## Vein II: arithmetic topology (Paper VIII)

`papers/VIII-arithmetic-topology/` (7 pp, clean). The exploratory draft and its appendix are
merged into one paper built on the correct foundation from the start; the two source files
are archived in `superseded/`.

**The pivot is one identification.** Local class field theory gives
$H_1(\partial N(K_i);\widehat{\mathbb{Z}})\cong\widehat{K_\mathfrak{p}^\times}$ with
**meridian $=$ inertia** and **longitude $=$ Frobenius**, so the parameter must be
$\sigma_{K_i}=[\lambda_i]$. Half-lives-half-dies then completes the dictionary: the
Lagrangian $\ker(H_1(\partial X)\to H_1(X))=\langle\lambda_i-\sum_j\mathrm{Lk}(K_i,K_j)\mu_j\rangle$
corresponds to the principal ideles, its intersection with the meridian subgroup to the
global units, and that intersection is $0$ for $S^3$ — matching $\mathbb{Z}^\times_+=\{1\}$.
**The unit entry was never missing; it is present and trivial for $S^3$.**

**Two corrections found while merging.**
1. *Local finiteness had to be dropped.* It is vacuous for an infinite link in a closed
   manifold, and had it held, a compact Seifert surface would meet finitely many components,
   every linking row would be finitely supported, and $D_\chi$ would again be finite — the
   theory would be empty a second time. Accumulation is what makes it nonempty.
2. *The ambient obstruction is sharper than first stated.* $[\lambda_i]=[K_i]$ in $H_1(M)$,
   **not** $0$; so the permanent obstruction is
   $h_\mathcal{L}=|H_1(M)/\langle[K_i]\rangle|$, which is the exact analogue of
   $\mathrm{Cl}^+_S=\mathrm{Cl}^+_K/\langle[\mathfrak{p}]\rangle$ — a closer parallel
   than the earlier $|H_1(M)|$.

**The theory has content.** Theorem 3.3: infinitely many parallel copies of a knot with
framing $f$ give $\mathrm{Lk}(K_i,K_j)=f$ throughout, so $D_\chi$ omits only $F$ whenever
$f\sum_{j\in F}a_j\notin\mathbb{Z}$ — a cofinite detecting set, hence a genuinely
$\beta$-dependent $\Xi_\beta$ with transition at the convergence exponent of the norms.

**The autopsy (§6)** shows meridian and longitude are the same story told twice:
$\sigma_\mathfrak{p}=(\pi_\mathfrak{p}^{-1})_{\mathfrak{q}\neq\mathfrak{p}}$ by the
product formula, $\lambda_i=\sum_j\mathrm{Lk}(K_i,K_j)\mu_j$ by the linking relation.
*Inertia is local and carries no thermodynamics; Frobenius is global and carries the linking
matrix.* Detecting densities match numerically: 51.5/52.8/52.2% arithmetic against 45–90%
topological.

**Still not done.** No family is known that is simultaneously linking-rich and volume-sparse
(Rem. 5.4) — this is the main geometric gap. And **nothing in the paper uses a quantum
invariant**: Jones, Chern–Simons and the volume conjecture play no role in any proof, and the
subfactors of Series II come from arithmetic symmetry breaking, not knot theory. We claim no
connection.

## Vein III: Popa rigidity (Paper IX)

`papers/IX-rigidity/` (6 pp, clean). One structural fact settles the whole question:
$I_S=\bigoplus_\mathfrak{p}\mathbb{Z}$ is **abelian**, so the groupoid is amenable and
$M_{K,S,\beta}$ is an **injective** factor.

**Connes' classification then leaves nothing.** The complete $W^*$-invariant is the type —
$\Sigma_\beta$ from Series I, plus the flow of weights in type III$_0$. So:

$$M_{\mathbb{Q},P_\mathbb{Q},1}\cong M_{\mathbb{Q},P_\mathbb{Q},1/2}\cong M_{K,P_K,\beta}\cong R_\infty$$

for **every** number field and every $\beta\in(0,1]$, since Series I Cor. 3.2 gives type
III$_1$ throughout. **The factor remembers neither $K$, nor $S$, nor $\beta$, nor the norms,
nor $G_S$, nor $\Xi_\beta$.** Class field $W^*$-superrigidity is false, maximally.

**Popa's machinery is inapplicable, and not for technical reasons.** $s$-malleable
deformations yield rigidity through a *spectral gap*, which needs the acting group to be
non-amenable. $I_S$ is abelian. Deformation/rigidity exists to produce rigidity where
amenability fails; applied to an amenable algebra it can only recover what Connes already
gives. The rigidity statement is false, not the proof missing.

**Cartan uniqueness holds but is misattributed.** It follows from Connes–Feldman–Weiss, not
Popa, and only up to conjugacy by an **automorphism** — not unitary conjugacy, since
$\mathrm{Out}$ of an injective factor is large. And OE rigidity fails outright: by Krieger
all amenable relations of a given type are already orbit equivalent, so the induced
isomorphism of relations carries no information.

**What survives, and it is worth stating.** $\Xi_\beta$ is a **$C^*$-invariant** — of
$(\mathcal{A}_{K,S},\sigma)$ through its KMS simplex — destroyed by taking the weak closure
in a single extremal state. This is the operator-algebraic face of the measure-class
principle of Series III. And the symmetry-breaking **inclusion** recovers what neither
algebra does: $[M_{\mathrm{sym}}:M_\varepsilon]=|\Xi_\beta|$ (Series II). Rigidity
questions are non-vacuous for structured objects — the $C^*$-algebra with its flow, the
inclusion, the Cartan pair with the $G_S$-action — not for the single factor, which is
$R_\infty$ or $R_\lambda$.

## The semigroup search (Paper X)

`papers/X-semigroup-search/` (6 pp, clean). A systematic search for a monoid escaping all
three walls. Two structural observations organize it.

**(C2) is free once (C1) holds.** Right Ore gives common right multiples, so in a right LCM
semigroup $e_ae_b=e_{aee b}\neq0$ *always* — nested, never orthogonal, no Cuntz relation.
This also **re-diagnoses Series V**: the free monoid fails not because it is non-commutative
but because it is **not Ore** — two generators have no common right multiple, hence orthogonal
ranges, hence $L_S(\beta)\leq1$.

**Norms factor through $P^{\mathrm{ab}}$**, so the available arithmetic is that of the
abelianization.

**The paper is now purely constructive**, focused on the Hurwitz quaternions. The three
no-go arguments (RAAMs collapse to abelian under Ore; finite generation gives a finite
obstruction sum; infinite unit group makes $\zeta_P$ diverge everywhere) are compressed into
a single five-line remark stating the *selection logic* — without it the choice of Hurwitz
would look arbitrary. The full search version, with all three as theorems, is archived at
`superseded/paper_X_v1_full_search.tex`.

**The model: the Hurwitz quaternions** $\mathcal{H}\setminus\{0\}$.
Non-commutative, cancellative; Ore via $a(\bar{a}b)=\mathrm{Nrd}(a)b$; right LCM since
$\mathcal{H}$ is a noncommutative PID; **24 units** (finite); reduced norm multiplicative with
infinitely many multiplicatively independent prime values; polynomial growth of degree 2; and
$$\zeta_P(\beta)=24\sum_n\sigma_{\mathrm{odd}}(n)n^{-\beta}=24\,\zeta(\beta)(1-2^{1-\beta})\zeta(\beta-1),\qquad \beta_c=2.$$
Counts verified by exhaustive enumeration ($n\leq15$, exact match to $24\sigma_{\mathrm{odd}}$);
the identity checked to eight decimals; the pole at $\beta=2$ exhibited numerically. The group
of fractions $\mathbb{H}(\mathbb{Q})^\times$ is **non-amenable**.

**But the three constraints omit the decisive one.** What killed Paper IX was amenability of
the **measured groupoid**, and non-amenability of $G$ is necessary, not sufficient: boundary
actions of non-amenable groups are routinely amenable —
$L^\infty(\partial F_n)\rtimes F_n$ is injective. Paper X states this as **(C4)** and leaves
it open. It is, in my view, the single question on which a genuinely non-commutative
Bost–Connes theory now turns. A reason for cautious optimism: the Toeplitz space retains an
"interior" (that is what nested projections mean), so the $\partial F_n$ analogy is not
immediate. A reason against: below $\beta_c$ the KMS measures concentrate away from it.

**Two geometric additions.** The $p+1$ right ideals of norm $p$ are the neighbours of a
vertex in the $(p+1)$-regular **Bruhat–Tits tree** of $SL_2(\mathbb{Q}_p)$, indexed by
$\mathbb{P}^1(\mathbb{F}_p)$, since $\mathcal{H}\otimes\mathbb{Q}_p\cong M_2(\mathbb{Q}_p)$
for odd $p$. At $p=2$, where $\mathcal{H}$ is ramified, the count collapses to **one** ideal —
an independent check on the factor $(1-2^{1-\beta})$ in $\zeta_P$, verified numerically
alongside $p+1$ for $p\leq23$. This suggests the shape a replacement Kakutani criterion would
take: indexed by *edges* rather than primes, hence a statement about a random walk on the
product of local trees rather than a Dirichlet series. Recorded as an interface, not a result.
The same trees give the Lubotzky–Phillips–Sarnak Ramanujan graphs; no connection is claimed,
only that the arithmetic input coincides and any spectral estimate for (C4) would plausibly
meet it.

Also made explicit: $\sigma_t$ **fixes the 24 unitaries $v_u$ pointwise** ($\mathrm{Nrd}(u)=1$),
so it is constant on each principal right ideal and descends to the projections indexed by
$P/P^\times$ — which is what makes it a genuine one-parameter group of $*$-automorphisms of
the Nica–Toeplitz relations.

**Priority caution recorded in the paper**: BC and Hecke constructions for orders in
quaternion algebras exist in the literature and $\zeta_P$ is a classical Solomon-type zeta
function. The claim made is the *deduction* — that (C1)–(C3) exclude the combinatorial
candidates and that finiteness of the unit group selects orders in division algebras — not
novelty of the object.

## (C4): the Ramanujan route is closed (Paper XI)

`papers/XI-C4/` (5 pp, clean). **(C4) is not resolved**, and the natural attack fails for
structural reasons.

**The dichotomy (Cor. 5.3).** A $(p+1)$-regular tree adjacency operator needs the $p+1$
branches to **partition**. But Paper X Prop. 1.2 forces them to be **nested**:
$e_je_k=e_{a_j\vee a_k}\neq0$ with $\varphi(e_je_k)=p^{-2\beta}>0$ and
$\sum_k\varphi(e_{a_k})=(p+1)p^{-\beta}\neq1$. **The property that keeps the
high-temperature region alive is the property that destroys the tree.**

**Forcing the partition empties the system (Thm. 5.1).** The Cuntz relation at $p$ gives
$(p+1)p^{-\beta}=1$, i.e. $\beta=\log(p+1)/\log p$ — and these are pairwise distinct
($1.2619, 1.1133, 1.0686,\dots$ for $p=3,5,7$). **The boundary quotient of the Hurwitz
system has no KMS state at all.** Contrast the affine case, where the Cuntz relation reads
$N\mathfrak{p}\cdot N\mathfrak{p}^{-\beta}=1$ and gives $\beta=1$ *independently of*
$\mathfrak{p}$: there multiplicity equals norm, here it is $p+1$ against $p$.

So **no method requiring a partition of unity into $p+1$ pieces can decide (C4)** — the
object where such a partition exists has nothing to decide. That rules out tree adjacency
operators, walks on the building, and Kesten/Ramanujan bounds in this form.

**Two further defects in the proposed route.** $\mathcal{M}_p$ is unital CP but does **not**
preserve $\varphi$ — the KMS condition gives
$\varphi\circ\mathcal{M}_p=\frac{p^\beta}{p+1}\varphi(\cdot\sum_ke_{a_k})$, with only
$\|\mathcal{M}_p\|\leq p^{\beta/2}>1$, so no contraction. And the gap statement is not
well posed: for a non-singular action $\pi(a)1=N(a)^{\beta/2}\mathbf{1}_{a\Omega}\neq1$,
so $\mathbb{C}1$ is not invariant and $L^2_0$ is not a subrepresentation.

**The correct reformulation (Prop. 6.1).** Amenability depends only on the measure class, so
(C4) $\iff$ the **Maharam extension** is non-amenable — and that action *preserves* an
infinite measure, removing the obstruction above. It does not settle the question (the
translation action of a non-amenable group on itself is an amenable groupoid), but it puts
(C4) where spectral gap arguments are meaningful. **The concrete open question is whether the
Koopman representation of the Maharam extension has a gap on the complement of the invariants.**
If not, the Hurwitz factor collapses like all the others and the programme ends; if so, it is
the first non-injective arithmetic BC factor.

## Paper XII: Task 1 closed, Task 2 reduced

`papers/XII-mismatch/` (5 pp, clean).

**Task 1 — closed, universally.** At a split prime a maximal order in a central simple algebra
of degree $d$ has $\Lambda\otimes\mathcal{O}_\mathfrak{p}\cong M_d(\mathcal{O}_\mathfrak{p})$,
and the right ideals of reduced norm $\mathfrak{p}$ are the **hyperplanes of
$\mathbb{F}_q^d$**, so
$$d_\mathfrak{p}=\frac{q^d-1}{q-1}=1+q+\cdots+q^{d-1}\ \geq\ 1+q\ >\ q=N\mathfrak{p}.$$
**No order in any central simple algebra has $d_\mathfrak{p}=N\mathfrak{p}$, ever.** For
$d=2$ the excess is exactly $1$ — the hyperplane at infinity. Eichler orders give
$d_\mathfrak{p}=2$ at $\mathfrak{p}\|\mathfrak{N}$, equal to $N\mathfrak{p}$ only when
$N\mathfrak{p}=2$: a match at one prime, never at almost all. Hence
$\beta(\mathfrak{p})=\log d_\mathfrak{p}/\log q$ decreases strictly to $d-1$, never
constant, and **the boundary quotient is empty for every order in every central simple
algebra**. The nested/partition dichotomy must be *circumvented*, not broken.

The clean way to say it: $d_\mathfrak{p}$ counts a **projective** space, $N\mathfrak{p}$ an
**affine** one. Contrast the $ax+b$ systems, where the multiplicity is the number of additive
cosets $=N\mathfrak{p}$ exactly, which is why $\beta=1$ works there uniformly.

**Task 2 — two real advances, not closed.**
1. **The RN cocycle factors through $\mathrm{Nrd}$.** So $G^1=\ker(\mathrm{Nrd})$ — which
   is **non-amenable** — acts **measure-preservingly**. The non-amenable directions and the
   thermodynamic direction are *orthogonal*: all the dynamics lives in the abelian quotient
   $G/G^1$, all the non-amenability in $G^1$, on which $\sigma_t$ is trivial. This is what
   distinguishes the Hurwitz system from every earlier model.
2. **All Fourier fibres agree on $G^1$.** $\pi_\tau=\chi_\tau\otimes\pi_0$ with
   $\chi_\tau(a)=\mathrm{Nrd}(a)^{i\beta\tau}$, and $\chi_\tau|_{G^1}=1$ for **every**
   $\tau$. The direct integral disappears: (C4) becomes a spectral question about the
   **single** representation $\pi_0|_{G^1}$.

**Why it is still open.** Zimmer's theorem (essentially free + amenable + *probability*
measure $\Rightarrow$ group amenable) would close it immediately, but the Maharam measure is
**infinite** ($\tilde\nu(a^{-1}\Omega)=\mathrm{Nrd}(a)^\beta\to\infty$), and the
extension genuinely fails: the translation action of $F_2$ on itself preserves counting
measure, is essentially free, and is an **amenable** groupoid. What is missing is a
finite-measure foothold or a direct gap estimate for $\pi_0|_{G^1}$, plus essential freeness
of the $G^1$-action, which has not been verified.

## Paper XIII: the $C^*$-level does remember (and why)

`papers/XIII-equivariant/` (4 pp, clean). The counterpoint to Paper IX.

**The gap that had to be closed first.** Renault's reconstruction applies to Cartan
**pairs**; an equivariant isomorphism of algebras need not preserve a Cartan subalgebra, since
Cartan subalgebras of a $C^*$-algebra are far from unique. Every version of this argument I
have seen glosses over that step.

**Theorem 1.4 closes it, and the proof is one line of spectral analysis.**
$\sigma_t(\mu_\mathfrak{a}f\mu_\mathfrak{b}^*)=(N\mathfrak{a}/N\mathfrak{b})^{it}(\cdots)$,
so the fixed-point algebra is spanned by the terms with
$N\mathfrak{a}=N\mathfrak{b}$; if $N$ is **injective on $J_S$** this forces
$\mathfrak{a}=\mathfrak{b}$ and $\mu_\mathfrak{a}f\mu_\mathfrak{a}^*=\alpha_\mathfrak{a}(f)$, whence
$$\mathcal{A}_{K,S}^{\sigma}=C(Y_S).$$
**The Cartan subalgebra is canonically the fixed-point algebra of the flow**, so any
$\sigma$-equivariant isomorphism preserves it automatically. Norm-separation is **automatic
over $\mathbb{Q}$** (unique factorization) and is a genuine hypothesis otherwise — it fails as
soon as $S$ has two primes of equal norm (e.g. the two primes over 5 in
$\mathbb{Q}(i)$).

**Reconstruction (Thm. 2.1).** Equivariant $C^*$-isomorphism $\Rightarrow$ Cartan pair iso
$\Rightarrow$ (Renault) groupoid iso intertwining the cocycles $c=\log N\mathfrak{a}$
$\Rightarrow$ the cocycle range is preserved $\Rightarrow$ **the norms
$\{N\mathfrak{p}\}$ are recovered** (given $\mathbb{Q}$-independence of the
$\log N\mathfrak{p}$), and with them $G_S$ with its Frobenius classes, the whole chain
$\{\Xi_\beta\}$, the transition locus, $\beta_c$ and $h^+_S$.

**The contrast with Paper IX is the point.** The von Neumann algebra retains nothing; the
$C^*$-algebra *with its flow* retains all of it. The mechanism is exactly Thm. 1.4 — **the
flow pins down the Cartan subalgebra** — and weak closure destroys the flow, the modular group
of a single extremal state being an inner datum.

**Three things I declined to claim.** (i) The **field $K$** is *not* recovered: the system
sees only $(S,N|_S,G_S)$, and whether that triple determines $K$ is an arithmetic question,
with existing literature for $S=P_K$ that I cannot consult here. (ii) The **KMS bundle** is
*strictly weaker* than the groupoid — it recovers $G_S$, $\{\Xi_\beta\}$, $\beta_c$,
$h^+_S$, but I see no way to extract individual norms; no completeness claimed. (iii) The
**Kirchberg boundary** is *not* classified by $KK_\mathbb{R}$: flows on Kirchberg algebras up
to cocycle conjugacy are not a settled theory, and in any case that boundary has KMS states
only at $\beta=1$, so the equilibrium invariant has already collapsed there.

## Paper XIV: the equal-norm case — and a limitation of Paper XIII I had missed

`papers/XIV-equalnorm/` (5 pp, clean).

**The hypothesis cannot be removed, because it is the conclusion.** $C(Y_S)$ is always the
fixed-point algebra of the **compact** gauge action, $C(Y_S)=\mathcal{A}^{\mathbb{T}^S}$; and
$\sigma_t=\gamma_{\iota(t)}$, so $\mathcal{A}^\sigma=\mathcal{A}^H$ with
$H=\overline{\iota(\mathbb{R})}$. By Kronecker $H=\mathbb{T}^S$ iff the $\log N\mathfrak{p}$
are $\mathbb{Q}$-independent — which *is* injectivity of $N$ on $J_S$. So

$$\mathcal{A}^\sigma=C(Y_S)\iff\{\log N\mathfrak{p}\}\ \mathbb{Q}\text{-independent}\iff S\text{ norm-separated}.$$

Three equivalent conditions. There is nothing to weaken.

**A limitation of Paper XIII I had not noticed.** Every $K\neq\mathbb{Q}$ has infinitely many
split primes, so **$P_K$ is never norm-separated for $K\neq\mathbb{Q}$**. Paper XIII's theorem
covers the classical full prime set *only for $\mathbb{Q}$*. (First split prime: 5 for
$\mathbb{Q}(i)$, 7 for $\mathbb{Q}(\sqrt{-3})$ and $\mathbb{Q}(\sqrt2)$, 11 for
$\mathbb{Q}(\sqrt5)$.) The question was therefore well motivated.

**The proposed structure is wrong; the correct one is a grading.**
$\mathcal{A}^\sigma\neq\bigoplus_n\mathcal{A}^\sigma_n$ — the pieces are neither orthogonal
($e_\mathfrak{a}e_\mathfrak{b}=e_{\mathrm{lcm}}\neq0$) nor ideals. With
$L=\{c:\prod N\mathfrak{p}^{c_\mathfrak{p}}=1\}$ the **relation lattice**,
$\mathcal{A}^\sigma$ is $L$-**graded** with degree-zero part $C(Y_S)$ and $H=L^\perp$.

**Both proposed characterizations are circular.** Property A recovers $C(Y_S)$ as the gauge
fixed points — but the $\mathbb{T}^S$-action is exactly what $\sigma$ fails to determine when
$L\neq0$. Property B assumes Cartan uniqueness, which is what is to be proved.

**The repair is a change of hypothesis, not a removal.** If $\Phi$ is **gauge-equivariant**
(up to an isomorphism of the acting tori, so no bijection $S_1\to S_2$ is presupposed) then
$\Phi(C(Y_{S_1}))=C(Y_{S_2})$ **unconditionally**, and all of Paper XIII Thm. 2.1 follows for
every number field. For $S_i=P_{K_i}$: **$\zeta_{K_1}=\zeta_{K_2}$** (arithmetic
equivalence) and $h^+_{K_1}=h^+_{K_2}$.

**Still open, in sharp form.** Is $C(Y_S)$ intrinsically characterized inside
$(\mathcal{A},\sigma)$ when $L\neq0$? The obvious negative attempt fails informatively: the
quasi-free rotation $\mu_i\mapsto\sum_ju_{ji}\mu_j$ is an automorphism of a *Cuntz* algebra
because $\mu_i^*\mu_j=\delta_{ij}$, but here the isometries commute and
$(\alpha\mu_\mathfrak{p}+\beta\mu_\mathfrak{q})$ is not an isometry. The Nica–Toeplitz
relations block the counterexample, which suggests the answer is yes.

## Paper XV: most of the reconstruction was free all along

`papers/XV-spectral/` (4 pp, clean). Two results of opposite sign; **the positive one matters
more**.

**Most of Paper XIII does not need Cartan uniqueness at all (Thm. 2.2).** The KMS bundle is
*manifestly* intrinsic to $(\mathcal{A},\sigma)$ — KMS states are defined from the flow, with
no diagonal in sight. So a $\sigma$-equivariant isomorphism transports it, and
**unconditionally, for every number field and every prime set, separated or not**, one
recovers: the homeomorphism type of $G_S/\Xi_\beta^\perp$ for each $\beta$, hence
$|\Xi_\beta|$ where finite, the transition locus, $\beta_c$, and $h^+_S$. Also
$\mathrm{Sp}(\sigma)=\langle N\mathfrak{p}\rangle\leq\mathbb{R}_{>0}$.

**So the Cartan question was needed for exactly one thing: the norm *multiset*.** The Arveson
spectrum sees the *group* generated by the norms, not multiplicity — two equal-norm primes
contribute the same $q^{\mathbb{Z}}$ as one. That single gap is what Papers XIII–XIV were
really about.

**The proposed spectral route to that gap is closed, and at Step 3, not Step 2 (Thm. 4.1).**
The range projections $e_\mathfrak{a}=\mathbf{1}_{\mathfrak{a}Y_S}$ encode the condition
$v_\mathfrak{p}(x)\geq a_\mathfrak{p}$ — **they depend only on the valuations and take equal
values at $[x,g]$ and $[x,g']$**. They do not separate points; $C^*(\mathcal{E})\cong
C(\overline{\mathbb{N}}^S)$, blind to the entire $G_S$-direction, which by the exact sequence
is most of $Y_S$. **Even a complete solution of Step 2 would not give $C(Y_S)$.**

**Step 2 itself becomes a clean single question (Prop. 3.2).** For equal-norm
$\mathfrak{p}_1,\mathfrak{p}_2$ put $g=\mathfrak{p}_2\mathfrak{p}_1^{-1}$; then $Ng=1$, so
**$g$ acts measure-preservingly** — the equal-norm hypothesis is exactly what makes this
ergodic rather than merely non-singular. A mixed isometry
$v=\mu_{\mathfrak{p}_1}p+\mu_{\mathfrak{p}_2}(1-p)$ is an isometry iff $gU\subseteq U$,
and measure preservation upgrades that to $gU=U$. So **mixed isometries exist iff $g$ is not
ergodic** — a self-contained problem about one transformation. Not decided.

Unconditional statement remains Paper XIV Thm. 4.2 (gauge-equivariance).

## Paper XVI: quantum optimal transport — two repairs and one obstruction

`papers/XVI-transport/` (5 pp, clean). Three proposals examined, three failures, each
diagnosed.

**1. The modular twist is harmful, not merely unnecessary.**
$[\!D_{\mathrm{vert}},\mu_\mathfrak{p}]_\vartheta\epsilon_\mathfrak{b}
=(\log N\mathfrak{p}+(1-N\mathfrak{p}^\beta)\log N\mathfrak{b})\epsilon_{\mathfrak{pb}}$
— **unbounded**. The untwisted commutator is bounded and trivial:
$D_{\mathrm{vert}}\mu_\mathfrak{p}=\mu_\mathfrak{p}(D_{\mathrm{vert}}+\log N\mathfrak{p})$.
A twist repairs a *multiplicative* mismatch; $D_{\mathrm{vert}}$ is *additive* in $\log N$,
so the twist **manufactures** the mismatch it was meant to cure.

Bonus: $\ker L=\mathbb{C}1$ for the untwisted $D_{\mathrm{full}}$ **iff $S$ is
norm-separated** — the condition of Paper XIV reappears, since
$\ker[D_{\mathrm{vert}},\cdot]=\mathcal{A}^\sigma$ exactly. Also flagged: $D_{\mathrm{full}}$
has **no compact resolvent** (infinite multiplicity from $L^2(X)$), so this is a Lip-norm
candidate, not a spectral triple.

**2. The Lindbladian has a sign error.** With rates $a_\mathfrak{p},b_\mathfrak{p}$,
invariance $\varphi\circ\mathcal{L}=0$ holds **iff
$b_\mathfrak{p}=a_\mathfrak{p}N\mathfrak{p}^{+\beta}$** — the detailed-balance factor
$e^{\beta\log N\mathfrak{p}}$. The proposal has $N\mathfrak{p}^{-\beta}$, the
*anti*-detailed-balance choice; concretely
$\varphi(\mathcal{L}e_\mathfrak{p})=(1-t^2)(1-t)\neq0$. Price of the fix:
$\sum a_\mathfrak{p}N\mathfrak{p}^\beta<\infty$ required.

**3. Critical slowing down does not occur — and this one is structural.** MLSI and
Bakry–Émery constants **tensorise to a minimum**, not a product. $\Pi_\infty$ is a
*product*. Single-site gaps are $\gtrsim1-\ell^{-\beta}\to1$, so the infimum sits at the
smallest prime and stays $\geq0.66$ while $\Pi_\infty\to0$ (verified: at $\beta=1.001$,
min $=0.667$ vs product $=1.86\times10^{-2}$). **No collapse, no Ricci-flat singularity.**

**The moral, and it is the corpus's recurring one.** The transition is a **tail** event — a
Kakutani dichotomy where every single factor is harmless and only the infinite product
degenerates. MLSI, Bakry–Émery and the Connes distance are **local**: they tensorise, so they
see only the worst coordinate. Three different local invariants, one tail phenomenon, three
failures to detect it — compare Series IV Thm. 6.2 (metric transition continuous) and
Series III Thm. 2.2 ($\Xi_\beta$ is a measure-class invariant). A transport quantity that
detects the transition would have to be built from the tail $\sigma$-algebra.

## Paper XVII: function fields — the first repair of Paper IX

`papers/XVII-function-fields/` (5 pp, clean). The transfer to $K=\mathbb{F}_q(C)$ succeeds
**with content**, unlike the arithmetic-topology transfer of Paper VIII, and one structural
feature **inverts**.

**The inversion.** Over a number field an infinite $S$ **never** has pairwise commensurable
log-norms (Series I Lem. 4.1). Over a function field they **always** are:
$\log N(P)=\deg(P)\log q$. Everything follows from this one fact.

**Consequence 1 — never type III$_1$ (Thm. 3.3).**
$\Gamma_\beta=q^{-\beta d_S\mathbb{Z}}$ is **discrete**, so
$S(M)\subseteq\Gamma_\beta\cup\{0\}$ can never be $[0,\infty)$. Exactly opposite to
Series I Cor. 3.2, where III$_1$ is generic. Also: the proposed "III$_0$ if dense" is
**impossible** — a discrete group is never dense.

**Consequence 2 — the factor recovers the temperature (Thm. 4.1). This is the headline.**
$M_\beta\cong R_\lambda$ with $\lambda=q^{-\beta d_S}$, and Powers factors are pairwise
non-isomorphic, so the von Neumann algebra determines $\beta\,d_S\log q$. Compare Paper IX
Thm. 2.1: over number fields *every* system gave $R_\infty$ and $\beta$ was forgotten
entirely. **This is the first weakening of the Paper IX collapse in the whole programme**, and
it comes from commensurability, not from any rigidity input. Honest about its size: one real
number, and not even $q$ and $\beta$ separately — $(4,1,1)$ and $(2,1,2)$ both give
$\lambda=1/4$. Separating them needs the $C^*$-level, where
$\mathrm{Sp}(\sigma)=q^{d_S\mathbb{Z}}$ (Paper XV).

**Two corrections.** The period is $T_0=2\pi/(d_S\log q)$, not $2\pi/\log q$ — equal only
when $d_S=1$, which does hold for $S=\mathcal{P}_K$ by F. K. Schmidt but fails for e.g. the
even-degree points. And in the Weil–Chebotarev bound the term $(g_L+1)q^{n/2}$ has no $1/n$
and **swamps** the main term; the truth is $O_\chi(q^{n/2}/n)$. Also flagged: Weil's bound
does **not** apply to constant-field-extension characters (their $L$-function is
$Z_C(\zeta T)$, with poles) — these are the function-field counterpart of the class-group
characters and need separate, elementary treatment.

**Everything else goes through unconditionally.** $\beta_c=1$; uniqueness on $(0,1]$ with
explicit constants in $g$ and $\deg\mathfrak{f}_\chi$ (no Siegel–Walfisz, no Landau–Siegel);
and a set with $A_n\asymp q^n/n^2$ converges at $\beta=1$ to $\asymp\pi^2/6$, giving a
**closed** phase $[1,\infty)$ with no sieve. The honest framing of that last gain: not that a
hard theorem becomes easy, but that the question stops being about existence — one *chooses*
the set rather than proving one exists.

**Follow-up suggestion — WITHDRAWN in Paper XVIII.** See below.

## Paper XVIII: I check my own suggestion and withdraw it

`papers/XVIII-equivariant-kirchberg/` (4 pp, clean).

**The retraction.** In Paper XVII §7 I suggested that periodicity might bring the equivariant
Kirchberg classification within reach, compact group actions being better understood than
flows. **That inference is wrong.** Takai duality turns a $\mathbb{T}$-action on
$\mathcal{A}$ into a $\mathbb{Z}$-action on $\mathcal{A}\rtimes\mathbb{T}$ — and for a
gauge-type action the crossed product is the stabilised **core**, which is **AF, stably
finite** ($\mathcal{O}_n\rtimes\mathbb{T}$ is AF). The Kirchberg classification does not
survive the dualisation. Nor does Izumi's compact-group theory apply: it needs the **Rokhlin
property**, and gauge actions are *approximately representable*, the dual notion. The
observation about the literature is correct; the inference here is not. Paper XIII Rem. 5.1
stands.

**Two further obstructions.** (i) The affine boundary **does not exist for $S=\mathcal{P}_K$**:
a function regular at every closed point of a projective curve is constant, so
$\mathcal{O}_{\mathcal{P}_K}=\mathbb{F}_q$ is *finite* and the construction degenerates. One
must fix a point at infinity — extra data, and the partition function becomes
$Z_C(T)(1-T^{\deg\infty})$. (ii) $K_0^{\mathbb{T}}$ **does not encode $P(T)$**: the Cuntz
relation gives $(1-(qt)^{\deg P})[1]=0$, so $[1]$ generates
$\mathbb{Z}[t,t^{-1}]/(1-(qt)^{d_S})$ — recording $q^{d_S}$ and nothing else, the same content
as $\mathrm{Sp}(\sigma)$ (Paper XV). $K$-theory sees $|\mathrm{Jac}(\mathbb{F}_q)|=P(1)$,
**one value** of the Weil polynomial, not the polynomial.

**But the conclusion is true, by another route (Thm. 4.1–4.2).** With $b_n$ the number of
effective divisors of degree $n$,
$$\sum_{D\in J_S}N(D)^{-\beta}=\sum_n b_n q^{-\beta n}=Z_C(q^{-\beta}).$$
**The Weil zeta function *is* the partition function.** Since $Z_C$ is rational, its values on
$(1,\infty)$ determine $P(T)$, the Weil numbers, $g$, every $\#C(\mathbb{F}_{q^n})$, and
$|\mathrm{Jac}(C)(\mathbb{F}_q)|=P(1)$. Complete geometric reconstruction — **thermodynamic,
not $K$-theoretic**.

**The principle, for the fourth time.** The arithmetic lives in the equilibrium data;
$K$-theoretic invariants discard the Radon–Nikodym derivative and are blind to it. Compare
Series II Cor. 4.4, Series III Prop. 3.1, Paper IX Thm. 2.1. Over a function field the
equilibrium datum *happens to be* the Weil zeta function, which is why the reconstruction is
so complete.

**Best open question** — **ANSWERED in Paper XIX**: yes, the Cartan pair distinguishes them.

## Paper XIX: zeta-equivalence is *not* the equivalence realised

`papers/XIX-isogeny/` (4 pp, clean). Answers the question left open in Paper XVIII §5.

**The proposed exact sequence is wrong.** $\mathrm{Jac}(C)(\mathbb{F}_q)=\mathrm{Pic}^0$ is a
**quotient** of the compact part $\mathbb{I}^0_K/K^\times$, not a subgroup of $G_{\mathcal{P}_K}$;
the true picture is a **two-step** filtration with
$\prod_P\mathcal{O}_P^\times/\overline{\mathbb{F}_q^\times}$ at the bottom.

**But the right identity does the job (Thm. 2.1).** Since
$\mathbb{I}_K/(K^\times U)=\mathrm{Div}(C)/\mathrm{Prin}(C)=\mathrm{Pic}(C)$, and $C$ has a
degree-1 divisor (F. K. Schmidt),
$$G_{\mathcal{P}_K}/\overline{U_S}\cong\widehat{\mathbb{Z}}\times\mathrm{Jac}(C)(\mathbb{F}_q),
\qquad\text{so}\qquad \mathrm{Jac}(C)(\mathbb{F}_q)=\bigl(G_{\mathcal{P}_K}/\overline{U_S}\bigr)_{\mathrm{tors}},$$
$\widehat{\mathbb{Z}}$ being torsion-free. Recovered from the **pair** $(G_S,U_S)$ — which the
groupoid supplies and the partition function does not.

**Answer: zeta-equivalence is NOT the equivalence realised (Thm. 3.1).** The partition
function sees exactly the isogeny class; a gauge-equivariant isomorphism sees strictly more.
Verified by brute-force enumeration over $\mathbb{F}_p$, $p\leq23$ — the phenomenon is
*abundant*, occurring for most traces at every prime tried. E.g. $p=13$, $t=-2$ has **three**
group structures sharing one zeta: $\mathbb{Z}/16$, $\mathbb{Z}/2\times\mathbb{Z}/8$,
$\mathbb{Z}/4\times\mathbb{Z}/4$.

**Gauge-equivariance is here a necessity, not a convenience.** Over a function field
$N(D)=q^{\deg D}$ identifies all divisors of equal degree, so $S=\mathcal{P}_K$ is as far from
norm-separated as possible (relation lattice of infinite rank) and Paper XIII Thm. 1.4 is
simply unavailable. Everything rests on Paper XIV Thm. 4.2.

**Tier 3 is open and I decline to claim it.** Recovering $C$ itself would need Torelli, hence
the **principal polarization**, which is nowhere in the data. And abelian data is known to be
insufficient in the number field case — Angelakis–Stevenhagen exhibit infinitely many
imaginary quadratic fields with isomorphic $\mathrm{Gal}(K^{ab}/K)$. The gap between Tier 2
and Tier 3 is exactly the polarization.

**Sharpest next target** — **ANSWERED in Paper XX**: such pairs exist abundantly, by CM theory.

## Paper XX: the resolution boundary is a torsor

`papers/XX-twin-curves/` (5 pp, clean). Answers the question left open in Paper XIX §5.

**Twins exist, abundantly, and genus 1 suffices** — no Howe/Lauter genus-2 machinery. The
reason is **complex multiplication**: for ordinary $E$ with $\mathrm{End}(E)=\mathcal{O}$,
Deuring gives $E(\mathbb{F}_{q^n})\cong\mathcal{O}/(\phi^n-1)$ for **every** $n$, depending
only on $\mathcal{O}$; and $\mathrm{Pic}(\mathcal{O})$ acts **simply transitively** on the
$h(\mathcal{O})$ curves with that endomorphism ring. So $h(\mathcal{O})>1$ gives twins that
agree in the *entire Galois-module tower*, not merely in $Z_C$ and $\mathrm{Jac}(\mathbb{F}_q)$.
Enumeration over $p\leq29$: **69 classes** with several $j$-invariants; counts match class
numbers ($h(-88)=h(-48)=h(-32)=h(-60)=h(-100)=2$ against two $j$'s each).

**A correction to my own Paper XIX framing.** Tier 2 does *not* see only
$\mathrm{Jac}(\mathbb{F}_q)$ — it recovers the map $P\mapsto[P]\in\mathrm{Pic}(C)$, hence the
rational effective cone, which is strictly finer. Checked numerically that this too fails to
separate twins: degree-2 point-to-Picard profiles agree within each pair (at $p=13$ the
apparent split tracks the group structure, not $j$).

**The proposed explanation of the barrier is wrong.** The Weil pairing is *not* out of abelian
reach for the reason given: over $\mathbb{F}_q$ the Galois group acting on
$\mathrm{Jac}[n]$ is $\widehat{\mathbb{Z}}$, **abelian**. The pairing is $\mathcal{O}$-determined
like everything else.

**The correct obstruction (Thm. 3.2): a torsor coordinate.**
$\mathrm{Pic}(\mathcal{O})$ acts simply transitively on the twins and **trivially on every
module invariant**. What is missing is the position in a $\mathrm{Pic}(\mathcal{O})$-torsor —
and a torsor has no invariants at all. The classical object supplying the coordinate is $j$,
i.e. the Hilbert class field of $\mathcal{O}$: still abelian class field theory, but **for the
CM field $\mathbb{Q}(\phi)$, not for $K=\mathbb{F}_q(C)$**. The system carries the second, not
the first. Sharper than "the barrier is non-abelian", and it says where a refinement would
come from: a system over the CM order.

**The retrospective, which is the point of the paper.** Every negative result in the corpus has
the same shape — the invariant was blind to something that *is not an invariant*: a measure
class (Series III), a tail event (Series IV, XVI), and now a torsor coordinate. $K$-theory did
not fail for lack of computation; the factor did not fail for lack of rigidity technique; MLSI
did not fail for lack of a better Dirichlet form. The one break in the pattern was Paper XVII,
where commensurability let the factor keep the temperature — and that too was arithmetic, not
technique.

## Paper XXI: the $GL_2$ programme closes on a quantitative gap

`papers/XXI-GL2/` (4 pp, clean).

**The arithmetic side is sound** and mostly already in Paper VI: the HS identity
$\|I_2-U_p\|^2_{\mathrm{HS}}=8\sin^2(\theta_p/2)$ ✓, and
$\Xi_1(\pi_f,P_\mathbb{Q})=\infty$ ✓ by Jacquet–Shalika.

**But the $L$-function formula is wrong.** $\Xi_\beta$ is **linear** in $\mathrm{Tr}\,U_p$,
so only the standard $L$ appears:
$$\Xi_\beta=4\log\zeta_S(\beta)-2\,\mathrm{Re}\log L_S(\beta,\pi_f)+O(1)$$
— Paper VI Thm. 4.1 at $n=2$. The $\mathrm{Sym}^2$ term is **spurious**; $\mathrm{Sym}^2$
would need $\mathrm{Tr}(U_p^2)$, which is quadratic. Rankin–Selberg governs the *second*
moment $\sum|\mathrm{Tr}\,U_p|^2p^{-s}$ — that is Sato–Tate, not $\Xi_\beta$.

**The decisive obstruction is quantitative and exact (Thm. 3.2).** Since
$\Xi_\beta\leq8\sum_{p\in S}p^{-\beta}$, the obstruction can only live for
$\beta\leq\beta_c(S)\leq1$. But the $GL_2$ local factor is the Solomon zeta
$(1-p^{-\beta})^{-1}(1-p^{1-\beta})^{-1}$, so Gibbs states exist only for
$\beta>1+\beta_c(S)$. Hence

$$\text{obstruction}: (0,\beta_c(S)]\qquad\text{equilibrium}: (1+\beta_c(S),\infty)$$

**disjoint, with a gap of width exactly 1, for every $S$ and every $\pi$.** For $S=P_\mathbb{Q}$:
obstruction on $(0,1]$, equilibrium on $(2,\infty)$; the window $(1,2]$ has neither. **The
proposed uniqueness theorem on $(0,1]$ is about a range with no KMS states.**

**The shift by 1 is not accidental** — it is Paper XII's universal multiplicity–norm mismatch:
$p+1$ sublattices of index $p$ in $\mathbb{Z}_p^2$ against norm $p$, the off-by-one of
$\mathbb{P}^1$. There it emptied the boundary quotient; here it displaces the equilibrium
range. One fact, two consequences.

**And the algebra is not available as stated**: $M_2(\mathbb{Z})^+$ has infinite unit group
$GL_2(\mathbb{Z})$, so by Paper X Prop. 4.1 its partition function diverges identically — one
must pass to the Hecke quotient, not a semigroup crossed product.

**No escape by reweighting**: norms factor through the abelianization (Paper X Prop. 1.4),
and on $GL_2$ orbits that is generated by $\det$, so any admissible norm is $|\det|^t$ and
merely rescales $\beta$. **The recommended route** is Paper VI §6: keep the $GL_1$
normalisation and attach the automorphic data as a *coefficient system* rather than as the
acting semigroup, where the Kakutani analysis applies verbatim.

## Paper XXII: the $p$-adic proposal fails below the level of its own statements

`papers/XXII-iwasawa/` (4 pp, clean). Four obstructions, the first fundamental and the rest
independent of it.

**1. There are no $p$-adic KMS states.** A state is a *positive* normalised functional;
positivity needs an ordered field. $\mathbb{C}_p$ is not orderable, carries no $C^*$-theory,
no positive cone, no GNS, no Choquet simplex. And the KMS condition needs the strip
$0\leq\mathrm{Im}\,t\leq\beta$, an artefact of $\mathbb{C}=\mathbb{R}\oplus i\mathbb{R}$
with no $p$-adic analogue. **There is no object whose dimension could be computed.**

**2. The dynamics is undefined on the proposed set.** $\langle x\rangle$ needs $x$ to be a
$p$-adic **unit**; for $\mathfrak{p}\mid p$, $N\mathfrak{p}=p^f$ has $v_p>0$. So
$\langle N\mathfrak{p}\rangle^z$ does not exist. $S=\{\mathfrak{p}\mid p\}$ is **exactly**
the set where $p$-adic interpolation breaks — which is why $L_p$ *removes* the Euler factors
at $p$.

**3. $p$-adic Dirichlet series never converge.** For $\mathfrak{q}\nmid p$,
$|\langle N\mathfrak{q}\rangle^{-z}|_p=1$ for **every** $z$; a $p$-adic series converges iff
its terms $\to0$. So there is **no $p$-adic abscissa, no $\beta_c$, no Kakutani mechanism**.
The engine of the entire archimedean theory — decay of $N\mathfrak{p}^{-\beta}$ against
abundance of primes — is archimedean. *This is why $p$-adic $L$-functions are built from
measures and Iwasawa power series, never from Dirichlet series.*

**4. $\Xi_p$ has bounded degree.** It is a finite sum of $g\leq[K:\mathbb{Q}]$ terms, so its
$\lambda$-invariant is bounded by $g$; the Iwasawa $\lambda$ is **unbounded**. A
bounded-degree family cannot generate ideals of unbounded degree.

**What is true, and it is precise.** The $p$-local partition function
$\prod_{\mathfrak{p}\mid p}(1-N\mathfrak{p}^{-\beta})^{-1}$ is, inverted and twisted, exactly
the **Euler factor $L_p$ removes** in its interpolation formula. A real dictionary entry —
between the partition function and the *interpolation factor*, not the characteristic ideal.

**And Leopoldt genuinely belongs here** — but in the *archimedean* theory: Series II Prop. 2.2,
where the isotropy computation needs a Leopoldt-type condition for general $K$ and is
unconditional when $\mathcal{O}_K^\times$ is finite. (Topological principality was proved
there *independently* of Leopoldt, which is what keeps the main classification unconditional.)

**The recurring theme**: units again — Paper VIII Thm. 3.2 (units carry the thermodynamics),
Paper X Prop. 4.1 (finiteness of the unit group selects the semigroup), now Leopoldt. The
units recur; the $p$-adic states do not exist.

## Paper XXIII: both bridges are real; neither carries the proposed theorem

`papers/XXIII-leopoldt/` (4 pp, clean). The two connections identified in Paper XXII survive;
all three theorems built on them need correction — each to something true and cleaner.

**1. Leopoldt does *not* trivialise the intermediate isotropy (Thm. 1.2).** The isotropy rank
is $\max(0,(r-\delta_p)-d_{T^c})$ with $r=r_1+r_2-1$, $d_{T^c}=\sum_{\mathfrak{p}\notin
T}[K_\mathfrak{p}:\mathbb{Q}_p]$. Under Leopoldt this is $\max(0,r-d_{T^c})$, **positive
whenever $r>d_{T^c}$**: totally real of degree $n\geq3$, $p$ split completely, $|T^c|=1$ gives
rank $n-2\geq1$. The proposed "iff" is false — Leopoldt supplies the **rank**, not the
vanishing. Triviality holds exactly for small unit rank ($r\leq1$), which is precisely where
Series II Prop. 2.2 was unconditional.

Two riders: the *equality* needs the projection to have maximal rank — a **relative** Leopoldt
condition strictly stronger than Leopoldt. And **nothing downstream depends on this**:
topological principality was proved directly in Series II, the strata being nowhere dense
whatever their isotropy.

**2. The proposed $\mathcal{L}$-invariant is identically zero (Thm. 2.2).** The derivative
computation is right — $E_p$ vanishes to order $g$ with
$\frac{1}{g!}E_p^{(g)}(0)=\prod\log N\mathfrak{p}=(\log p)^g\prod f_\mathfrak{p}$ — but that
is the **real** logarithm. Iwasawa's branch has $\log_p(p)=0$, so
$\log_p(N\mathfrak{p})=f_\mathfrak{p}\log_p(p)=\mathbf{0}$ for every $\mathfrak{p}\mid p$.
The proposed $\mathcal{L}_p(K)=\prod\log_p(N\mathfrak{p})$ **vanishes identically** and cannot
be a Fontaine–Mazur invariant.

*This is the same wall as Paper XXII Prop. 2.1*: $N\mathfrak{p}$ is not a $p$-adic unit. Every
attempt to run $p$-adic analysis on the norms above $p$ meets it — those norms are exactly
what the $p$-adic theory is built to discard.

**What survives, and it is worth keeping**: $E_p$ vanishes to order exactly $g$, and $g$ is the
number of exceptional zeros in the MTT sense. That entry is correct.

**3. The regulator is a dimension, not a volume (Thm. 3.2).** Haar measure on a compact group
never degenerates, and $\overline{\mathcal{O}^\times}$ is infinite, so the quotient volume is
either 1 by normalisation or 0 — no information. The meaningful statement is
$$\dim\bigl(U_p/\overline{\mathcal{O}^\times_{K,+}}\bigr)=[K:\mathbb{Q}]-(r-\delta_p)=r_2+1+\delta_p(K),$$
so **Leopoldt $\iff$ the dimension is exactly $r_2+1$** — recovering Paper XXII Prop. 5.3
through class field theory. The intended statement was right in substance, misstated in form:
volume for dimension.

## Paper XXIV: the sieve is not the difficulty — a congruence is

`papers/XXIV-sieve/` (4 pp, clean). **This one affects the master paper.**

**All six critical exponents are correct.** Abel summation: $\pi_S(x)\asymp x^\theta/\log^kx$
gives $\beta_c=\theta$. So $1$ for twin/Sophie Germain/Chen, $3/4$ for
Friedlander–Iwaniec, $2/3$ for Heath-Brown, $1/2$ for Landau, $1/c$ for Piatetski-Shapiro.

**The open/closed dichotomy is exactly the log-power.** At $\beta=\beta_c$ the series is
$\int dt/(t\log^kt)$, convergent iff $k>1$. So **closed $\iff k=2 \iff$ two simultaneous
prime conditions**. The closedness found for Sophie Germain in the master paper is *not* a
feature of the sieve — it is the second prime condition, and it transfers to twins and to
Chen primes (the latter **unconditionally**, Chen's theorem supplying the lower bound the twin
case still lacks).

**Four of the six families are congruence-obstructed, and are NEVER unique (Thm. 2.2).**
Elementary:
- $p,p+2$ prime, $p>3$ $\Rightarrow p\equiv2\pmod3$ (else $3\mid p+2$)
- $p,2p+1$ prime, $p>3$ $\Rightarrow p\equiv2\pmod3$
- $p=n^2+1>2$ $\Rightarrow n$ even $\Rightarrow p\equiv1\pmod4$
- $a^2+b^4\equiv0,1,2\pmod4$ $\Rightarrow$ odd FI primes are $\equiv1\pmod4$

Each confines the family to a **single residue class**, so the corresponding Dirichlet
character has **finite** detecting set and lies in $\Xi_\beta$ for **every** $\beta$ — a
permanent obstruction. Verified to $2\times10^5$: twin and SG occupy only $\{2\}$ mod 3;
Landau and odd FI only $\{1\}$ mod 4. Chen, Heath-Brown, Piatetski-Shapiro are **unobstructed**
(both classes mod 3 and 4; HB hits $\{1,2,7,8\}$ mod 9, not inside a proper subgroup since 2
generates).

**This corrects the master paper's Sophie Germain picture.** Thm. 5.5 there (Brun-summability,
closed phase) **stands** — those are statements about $\zeta_S(\beta)$. But high-temperature
uniqueness for that family is now **excluded**: symmetry breaking at *all* temperatures, with
$\beta=1$ affecting only the size of $\Xi_\beta$, not its nontriviality.

**The moral is the opposite of the corpus's usual one.** Here the hard analytic input — the
sieve theorems — is *not* where the difficulty lies; it gives the exponents and phase types
cleanly. What decides the qualitative behaviour is a congruence available to a first-year
student. $\Xi_\beta$ measures how a prime set sits inside residue classes, and a set confined
to one class is maximally obstructed however delicate its density.

Also flagged: the unconditional Piatetski-Shapiro range is $\beta_c\in(0.8436,1)$
($205/243$), not $(0,1)$.

## Paper XXV: the first family to pass the congruence test

`papers/XXV-sato-tate/` (4 pp, clean). **No no-go theorem — and that is the finding.**

**1. The phase is OPEN, necessarily.** $S_{[a,b]}$ has *positive* density
$\delta=\mu_{ST}([a,b])$, so $\theta=1$ and $k=1$; by Paper XXIV Prop. 1.1 the critical
series diverges like $\delta\log\log x$. Precise asymptotic:
$$\zeta_{S_{[a,b]}}(\beta)=\delta\log\tfrac{1}{\beta-1}+O(1),\qquad \beta\to1^+.$$
**Corollary 1.3: a positive-density set can NEVER have a closed phase** — closedness needs
$k\geq2$, hence density zero with two prime conditions.

**2. No congruence obstruction — the first family to pass (Thm. 2.3).** The mechanism is
structural: $p\bmod m=\det\bar\rho_{E,m}(\mathrm{Frob}_p)$ (cyclotomic character) while
$\theta_p$ comes from the **trace** of the same representation. **Serre's open image theorem
is exactly the independence of the two.** Joint equidistribution then follows from
non-vanishing of $L(s,\mathrm{Sym}^kE\otimes\chi)$ on $\mathrm{Re}\,s=1$ — unconditional
now by Newton–Thorne + Shahidi. So **the KMS state is unique for all $0<\beta\leq1$**.

Verified on $y^2=x^3+x+1$, 6054 primes below $6\times10^4$: every coprime class mod 3,4,5,8
carries the uniform proportion in all three intervals tested.

**Why this family passes where four failed (Rem. 2.4)**: the obstructed families of Paper XXIV
are defined by conditions that *involve the residue* ($p+2$ prime, $p=n^2+1$) — their defining
conditions are congruence conditions in disguise. Here the condition is on the trace and the
residue is the determinant.

**3. Symmetric powers control the constant, not the transition (Thm. 3.2).**
$$\zeta_{S_{[a,b]}}(s)=\delta\log\tfrac{1}{s-1}+\sum_{k\geq1}c_k\log L(s,\mathrm{Sym}^kE)+O(1),
\quad c_k=\tfrac2\pi\int_a^b\sin((k+1)t)\sin t\,dt.$$
Only $k=0$ (Riemann zeta) has a pole; all $\mathrm{Sym}^k$, $k\geq1$, are automorphic with
$L(1,\mathrm{Sym}^k)\neq0$, hence $O(1)$. For $[\pi/3,2\pi/3]$: $c_0=0.6090$, odd $c_k=0$ by
symmetry, $c_2=-0.4135$ — $\mathrm{Sym}^2$ carries the leading correction.

Flagged honestly: $\mathbf{1}_{[a,b]}$ is not smooth, so the term-by-term interchange needs a
**Beurling–Selberg smoothing** — standard but not vacuous.

**The tension worth recording**: a closed phase needs density zero with two prime conditions;
an unobstructed high-temperature phase is easiest for trace conditions, which have positive
density. **Chen primes remain the only candidate we know satisfying both.**

## What is *not* finished

Two items, and neither is closable from inside this project.

1. **Priority.** `PRIORITY_CDL.md` narrowed the question to: has any published classification
   treated infinite sparse S with 0 < β_c(S) < ∞? A referee survey agrees with our own
   Parts I–III, which is real corroboration, but a negative claim about a literature needs a
   repeatable search — documented databases, query strings, date ranges — and a check of the
   works citing Laca–Raeburn 1999 and LLN 2009. **Recommendation: post the foundational paper
   as a preprint to fix the date, and continue the search in parallel rather than blocking on
   it.** This applies to the foundational paper; VI and VII are self-evidently new and may be
   posted independently.

2. **Bibliography.** All 55 external references are 🟨 referee-supplied with MR numbers, not
   ✅ independently verified. One pass through MathSciNet closes this; no judgement is
   required. See `BIBLIOGRAPHY_CHECK.md` for why the distinction is kept.

Additionally: no paper asserts an internal theorem number from any cited work, several having
been proposed and declined as uncheckable. This should remain true unless the sources are
read.

## Readout

**LaTeX and internal consistency: ready.** That claim is fully verified above and I stand
behind it.

**Submission: not yet, for the foundational paper.** Items 1 and 2 are open. Papers VI and
VII can go now, subject to item 2 for their own short reference lists; see
`arxiv/SUBMISSION_VI_VII.md`.

## Open mathematics

The structural question left by Paper VII is the one worth pursuing: **does there exist an
Ore semigroup that is non-abelian but whose range projections are nested rather than
partitioning?** Abelian semigroups cannot produce non-abelian essential values (Paper VII,
Rem. 1.3); free non-abelian semigroups empty the high-temperature region where the phase
structure lives (Series V, Thm. 1.2). A model between the two is what a genuinely non-abelian
Bost–Connes theory would need, and nothing here rules one out.

Also open, in decreasing order of tractability: the exact value of W₁(φ₊,φ₋) (Series IV);
K_*(∂A^aff) (Series II); the regime of the twin primes, equivalent to comparing a Brun-type
constant with 1 (Series V); H¹_meas(R_S,π_β;T) itself rather than its kernel (Series III);
and whether a refinement of the obstruction data recovers E_β up to conjugacy (Paper VII).
