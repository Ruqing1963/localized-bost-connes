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

**Paper II — reviewed line by line; three theorems were false as stated and are replaced,
two proofs were invalid and are replaced, plus smaller repairs. Awaiting DOI.**

1. *Theorem 2.4 ("the ideal lattice is completely determined") was false.* It claimed every
   ideal is $C^*(\mathcal G_S|_V)$ for an open invariant $V$, that the diagonal detects ideals,
   and that all ideals are gauge-invariant. Topological principality gives this only on the
   essentially principal part: the boundary orbit has isotropy $I_S^0$ of infinite rank and
   $\partial\mathcal A\cong M_h(C(\widehat{I_S^0}))$ has a torus of primitive ideals, invisible
   to the diagonal and moved by the gauge flow — the paper's own Prop. 2.5 ($C(\mathbb T)$
   quotient for one prime) already exhibits them. New Theorem 2.5: (1) topological
   principality for all $K,S$; (2) ideals containing the boundary ideal $\leftrightarrow$
   closed subsets of $\widehat{I_S^0}$, not detected by $C(Y_S)$, not gauge-invariant in
   general; (3) if the action off the boundary is free (finite $\mathcal O^\times_{K,+}$),
   ideals of the boundary ideal $\leftrightarrow$ open invariant subsets (Renault 1991);
   (4) $\operatorname{Prim}$ as a disjoint union.
2. *Abstract overclaimed trivial isotropy off the boundary for all $K$*; Prop. 2.2 proves it
   only for finite $\mathcal O^\times_{K,+}$ and Remark 2.3 rightly leaves the general case
   (a Leopoldt-type closure question) open. Abstract corrected; "$S\setminus T$ infinite" in
   Prop. 2.2 weakened to $T\ne S$ (one prime suffices), with the discreteness of
   $K^\times_{S,+}$ proved rather than asserted.
3. *Theorem 5.2 (infinite index), proof invalid:* "finite index $\Rightarrow$ finite-dimensional
   relative commutant" fails when the small algebra is not a factor (e.g. $N\subseteq N\otimes M_2$).
   New proof at the symmetric state: the valuation projections $e_k=\mathbf 1_{\{v_\mathfrak p=k\}}$
   are moved onto one another by partial isometries $W$ built from "shift $v_\mathfrak p$, keep
   $g$", which commute with $M_{S_1}$ on the GNS space; then $F(e_k)\ge\lambda e_k$ forces a
   projection of $M_{S_1}$ dominating $e_k$ to be $1$, whence $\varphi(F(e_k))\ge\lambda$ for all
   $k$, contradicting $\sum_kF(e_k)=1$. This gives $\operatorname{Ind}(F)=\infty$ for *every*
   expectation, at the symmetric state. For non-symmetric extremal states the fibre measure
   moves with $v_\mathfrak p$ and the question is left open (Remark 5.4). Prop. 5.6
   (continuum of intermediate algebras) restricted accordingly, with the recovery of the
   partition now proved via $W$.
4. *Theorem 5.7 (Galois correspondence with the subgroup lattice) was false, and Theorem 5.8
   (standard invariant $\mathrm{Vec}_{\widehat{\Xi_\beta}}$) was meaningless.* The inclusion
   $M_{\mathrm{sym}}^G\subseteq M_{\mathrm{sym}}$ is $D\otimes1\subseteq D\otimes\ell^\infty(G)$ for the
   factor $D=M_{\varepsilon_0}$: a permutation of summands, not an outer action on a factor.
   By Ge–Kadison splitting its intermediate algebras are indexed by the *partitions* of $G$
   (Bell number many), the subgroup lattice embedding properly for $|G|\ge3$; index $|G|$ and
   relative commutant $\mathbb C^{|G|}$ stand. Theorem 5.8 replaced by Remark 5.9 saying
   exactly this; the assessment's question about the tower of fusion categories removed.
5. *Section 4 ($K$-theory).* The "Koszul formula" $K_1=\ker(1-\alpha_*)$, $K_0=\operatorname{coker}(1-\alpha_*)$
   for finite $S$ and the claim "$K_0$ free of infinite rank, $K_1=0$, independently of $K$ and
   $S$" were unproved; for $|S|\ge2$ the generators move the $G_S$-coordinate by $\sigma_\mathfrak p$,
   so the action is not a product and the strata contribute nontrivial Koszul homology. Now:
   Prop. 4.2 proves, for one prime and every $K$, $K_1=0$ and $K_0\cong C(G_S,\mathbb Z)/\mathbb Z\oplus\mathbb Z$
   (free; of finite rank when $G_S$ is finite, which happens for a split prime in a real
   quadratic field with open unit closure); Prop. 4.3 states the collapsing Kasparov spectral
   sequence for finite $S$ and identifies the image of $K^0(Y_S)$ with the coinvariants; the
   general computation is declared not done.
6. *Foundational paper, Prop. 2.7 — an error found here, recorded in `docs/ERRATA.md`.*
   The projection $Y_{S'}\to Y_S$ is canonical iff $\mathrm{Cl}^+_{S'}=\mathrm{Cl}^+_S$
   ($\mathrm{Cl}^+_S$ is a subgroup, not a quotient, of $\mathrm{Cl}^+_{S'}$); the direct-limit
   statement survives along the tail of a chain, the uses in the paper are over $\mathbb Q$.
   Paper II, Remark 5.1, states the qualification and assumes $\mathrm{Cl}^+_{S_2}=\mathrm{Cl}^+_{S_1}$.
7. *Section 6.* The action of $J_S$ on $\widehat{\mathcal O}_S$ needs a choice of uniformizers
   (canonical over $\mathbb Q$), now said; the fixed-point argument ("at most one solution")
   was wrong for the ideal action (fixed sets are $\{x_\mathfrak p=0,\ \mathfrak p\in\operatorname{supp}\mathfrak a\}$
   when $b=0$), replaced; "unital copy of $\mathcal O_n$ gives pure infiniteness" is not a
   proof (properly infinite $\ne$ purely infinite), replaced by local contractivity and
   Anantharaman-Delaroche; $\mathcal A^{\mathrm{aff}}$ is its own boundary quotient, now said.
8. *Lemma 1.1(3)* ("no isometries with orthogonal ranges summing to 1") was proved only for
   the generators; now proved for all isometries via the tracial boundary quotient.
9. *Bibliography.* Eleven of the sixteen entries were never cited; all are now cited where
   used, Renault 2008 replaced by Renault 1991 (ideal structure), and Anantharaman-Delaroche,
   Brown–Clark–Farthing–Sims, Ge–Kadison, Kasparov added (20 entries, all cited).
10. *Renumbering.* Old $\to$ new: Thm 2.4 $\to$ Thm 2.5 (new Remark 2.6, Prop 2.5 $\to$ 2.7);
   Prop 4.1 $\to$ Prop 4.2 (Lemma 4.2 $\to$ 4.1, new Prop 4.3, Ex 4.3 $\to$ 4.4, Rem 4.4 $\to$ 4.5);
   Section 5 shifted by one (new Remark 5.1): Prop 5.1 $\to$ 5.2, Thm 5.2 $\to$ 5.3, Rem 5.3 $\to$ 5.5,
   Prop 5.4 $\to$ 5.6, Lem 5.5 $\to$ 5.7, Thm 5.6 $\to$ 5.8, Thm 5.7 (standard invariant) $\to$
   Rem 5.9, Lem 5.8 $\to$ 5.10, Cor 5.9 $\to$ 5.11; new Prop 6.5 (Cuntz relation forces
   $\beta=1$; Papers V and XIII already cite "Prop 6.5" for exactly this), Example $\to$ 6.6,
   Remark $\to$ 6.7. Other papers' citations renumbered mechanically. **Content changes to
   watch when those papers are reviewed:** III cites the one-prime $K_0$ formula (now Prop 4.2)
   for general $S$; IX, XVIII, XX cite "K-theory carries no arithmetic" (now Rem 4.5, proved
   for one prime only); XIII and XIV cite the Cartan/ideal theorem (now Thm 2.5, whose ideal
   claims changed; the Cartan statement stands).

**Paper III — reviewed line by line; one lemma corrected, one proposition replaced,
several proofs made self-contained. Cites only the foundational paper and Paper I.**

1. *Lemma 2.1(4) and "$E(\Phi)=\Lambda^\perp$" removed.* The equivalence "$\psi$ trivial on
   the essential values $\Leftrightarrow$ $\psi\circ\Phi$ a coboundary" needs the cocycle to
   be regular (the same gap that invalidated Paper I's old type criterion); only the
   inclusion $E(\Phi)\subseteq\Lambda^\perp$ is proved, which is all Theorem 2.3 uses. New
   Remark 2.2 says when the converse holds (compact targets) and why it is open for the
   $G_S\times\mathbb R$-valued cocycle, with a pointer to Paper I, Prop. 2.2/Rem. 2.3.
2. *Prop. 6.4 ("all KMS states have the same free energy, by the variational principle")
   replaced.* No free-energy functional is defined for these systems; the variational
   characterization is a theorem for lattice systems, not for arbitrary $C^*$-dynamical
   systems. New Prop. 6.4 ("no preferred phase"): $G_S$ permutes the extremal $\mathrm{KMS}_\beta$
   states transitively and commutes with the dynamics, so nothing attached to the system
   prefers one; Remark 6.5 notes that in the Gibbs regime the extremal states literally share
   the partition function. Abstract sentence changed accordingly.
3. *Cor. 3.3* no longer relies on the (now one-prime) formula $K_0=\operatorname{coker}(1-\alpha_*)$
   of Paper II: $\iota_*[\mathbf 1_U]=\iota_*[\mathbf 1_{\mathfrak pU}]$ in $K_0(\mathcal A)$ directly
   (partial isometry $\mu_\mathfrak p\mathbf 1_U$), so any functional factoring through $K_0$ is
   $\alpha_*$-invariant. Remark 4.2's "$K_1=0$ for one prime" proved inline.
4. *Thm 4.1(3)* restated precisely (the dual weight vanishes on every projection in its
   domain; the earlier "pairing on $K_0$ of the Pedersen ideal" is not needed) with a clean
   proof (unitary equivalence of homotopic projections plus the trace property).
5. *Thm 5.4 (topological entropy)* used a metric $d(x,y)$ with "$x-y$" on $Y_S$, which is not a
   group for general $K$, and identified $\alpha_\mathfrak a$ with a map of $Y_S$; now stated for
   $T_\mathfrak a$ (which induces $\mathcal L_\mathfrak a$ on $C(Y_S)$) via the $1$-Lipschitz lift to
   $\widehat{\mathcal O}_S\times G_S$, and on the boundary via inner automorphisms (Brown).
   Prop. 5.1's counterexample now uses $E=Y_S\setminus\mathfrak aY_S$ (a clopen set of positive
   measure for *every* KMS state; a general nonempty clopen set can be null for a
   non-symmetric extremal state). Thm 5.2's proof now derives $\nu(Y_S)=1$ before
   concentrating on the boundary. Remark 5.7's "$\log\mathrm N\mathfrak p$ are $\mathbb Q$-linearly
   independent" is false when two primes share a norm; restricted to $K=\mathbb Q$ with the
   general statement given.
6. *Prop. 4.6* for infinite $S$ needs the Milnor sequence; said.
7. *Citations.* All ten citations of Paper II replaced by self-contained arguments or
   numeral signposts; Paper I cited by DOI (series paragraph, Remark 2.2, assessment);
   $[\mathrm{Main},\ \mathrm{Lem.}\ 2.9]\to2.10$; four of the twelve bibliography entries were
   never cited (CS, FM, ST, Voiculescu), now cited where they belong; Brown 1999 added.
   13 entries, all cited. Numbering: new Remark 2.2 shifts Section 2 (old Thm 2.2 $\to$ 2.3,
   Cor 2.3 $\to$ 2.4, Rem 2.4 $\to$ 2.5); Sections 3--6 unchanged. Other papers' citations
   renumbered mechanically; VI and VII cite "the scalar dictionary [III, Lem. 2.1]" — its
   item (4) (duality with the essential values) no longer exists, so their uses must be
   checked; XIV cites a nonexistent "[III, Lem. 1.1]" for the gauge action.

**Paper IV — reviewed line by line; the crossed-product framing was unsupported, the
numerical table was wrong, two definitions needed repair. Cites only the foundational
paper and Paper I.**

1. *Proposition 2.2 ("reduction to the base") and the claim that $D_{\mathrm{base}}$ commutes
   with the isometries were false.* The isometry $\mu_\mathfrak p$ shifts the level $k$ of
   $v_\mathfrak p$, so commutation would force $w_{\ell,k}=w_{\ell,k+1}$, incompatible with the
   summability that Theorem 3.2 needs; and the proof of 2.2 assumed the gauge unitaries
   (multiplication by $z^v$) commute with $D$, which they do not. Consequently the paper's
   "Connes spectral distance between the two KMS states" is really the Connes--Rieffel
   distance of the *base* algebra $C(X)$ between their measures. Reframed throughout
   (abstract, new Remark 2.2 defining $W_1$ on the base, Lemma 2.5, Theorem 5.3, assessment);
   a spectral triple on the crossed product is declared open. The mathematics of
   Sections 3--6 is unaffected, since it always worked on $C(X)$.
2. *Definition 2.3 (moves).* "$(g_i)$ generating a dense subgroup" is not enough for the
   equicontinuity in Lemma 3.1/Theorem 3.2 (a single generator of $\mathbb Z_p$ gives a word
   metric not inducing the topology); replaced by generators adapted to a basis of open
   subgroups $U_k$ with $U_1=\ker\chi_3$, and $g_0$ fixed as $-1$ at $3$ so that $\theta_0$ is
   an involution. Lemma 3.1 and the Arzelà--Ascoli step rewritten accordingly.
3. *Theorem 6.2 (continuity at $\beta_c$)* silently used $\sum_{\ell\in R}\ell^{-\beta_c}=\infty$;
   without it $\Psi$ exists at $\beta_c$, the squeeze gives $W_1(\beta_c)>0$ and the diameter
   *jumps*. Hypothesis added (holds for the cascade sets), the alternative recorded in the
   statement; $\ell\ge3$ corrected to $\ell\ge2$ ($2\in R$ is possible).
4. *Remark 6.4 (numerics) was wrong.* The five tabulated values (0.667, 0.691, 0.824, 0.935,
   0.979) lie *below* the value $(w_0^{-2}+w_r^{-2})^{-1/2}$ of the explicitly feasible
   alternating profile (0.707 for $w_r=1$, 0.981 for $w_r=5$), so they cannot be maxima of a
   convex program. Recomputed (`code/verify_series.py`, section "Paper IV"): the alternating
   profile is the optimizer for $t=0.5,0.9$, independently of $t$; for $t=0.1$, $w_r=1$ the
   optimum is 0.838. Table replaced; the Muckenhoupt "numerical verification" replaced by the
   exact computation $B_n=t(1-t^n)/(1-t)^2\uparrow t/(1-t)^2$.
5. *Theorem 4.2* overclaimed "the Lipschitz domain of any Dirac operator making $C(X)$ a
   CQMS"; now: for the operators of Definition 2.4, plus the trivial general fact that
   $\Psi_N\notin C(X)$. Remark 3.3's example made explicit ($f_n=\sum_{k<n}w_{\ell,k}\mathbf 1_{v_\ell>k}$).
   Prop. 2.1's "modular Dirac operator on $\ell^2(J_S)$" phrased inside a representation.
6. *Citations.* Papers II and III cited five times, all replaced by numerals; Paper I cited by
   DOI; $[\mathrm{Main},\ \mathrm{Lem.}\ 2.9]\to2.10$; none of the seven other references was
   cited anywhere — Connes, Christensen--Ivan, Rieffel, Miclo, Muckenhoupt now cited where
   used. 9 entries, all cited. Numbering unchanged (Prop 2.2 became Remark 2.2 with the same
   number). Other papers cite "[IV, Def. 2.5]" (no such item; the Dirac operator is Def. 2.4)
   and "[IV, Thm. 6.2]" (now with the divergence hypothesis) — to be checked when reviewed.

**Paper V — reviewed line by line; the defining object was inconsistent and is replaced,
the KMS structure is now completely determined, numerics recomputed. Cites only the
foundational paper and Paper I.**

1. *Definition 1.1 defined the zero algebra.* Keeping $C(Y_S)$ with $\mu_\mathfrak pf\mu_\mathfrak p^*=\alpha_\mathfrak p(f)$
   and imposing $\mu_\mathfrak p^*\mu_\mathfrak q=0$ is contradictory: $e_\mathfrak pe_\mathfrak q=0$ makes the
   image of $\mathbf 1_{\mathfrak{pq}Y_S}=\alpha_\mathfrak p(\mathbf 1_{\mathfrak qY_S})$ vanish, hence
   $\mathbf 1_{\mathfrak qY_S}=\mu_\mathfrak p^*\alpha_\mathfrak p(\mathbf 1_{\mathfrak qY_S})\mu_\mathfrak p=0$, hence
   $\mu_\mathfrak q=0$, hence $1=0$. So the "Fock--Gibbs state" of the paper was not a state on
   the algebra it named (no representation of $C(Y_S)$ on $\ell^2(\mathbb F_S^+)$ is compatible
   with the relations). This is now Proposition 1.1 (Incompatibility), and it sharpens the
   paper's thesis: the free deformation cannot carry the coefficient algebra, hence neither
   $G_S$ nor $\Xi_\beta$. The free system is redefined (Def. 1.2) as the Toeplitz--Cuntz
   algebra $\mathcal T_S$ of $\mathbb F_S^+$ with the norm dynamics, on which everything the
   paper computes (Sections 2--5, all in the Fock--Gibbs state) is unchanged.
2. *KMS structure completed.* Old Thm 1.3(2) only exhibited the Fock--Gibbs state; old
   Prop. 1.5 ("the simplex fibres over $\operatorname{Prob}(G_S/\Xi_\beta^\perp)$") was about
   the zero algebra. New Thm 1.4: a $\mathrm{KMS}_\beta$ state satisfies
   $\varphi(\mu_w\mu_v^*)=\delta_{wv}\mathrm Nw^{-\beta}$ (KMS with the entire $\mu_w$ plus gauge
   invariance), so there is at most one at every $\beta$; none below $\beta_c^{\mathrm{free}}$,
   the Fock--Gibbs state for $L_S<1$, a weak-$*$ limit at $\beta_c^{\mathrm{free}}$. The open
   question about "the permutation part of the fixed-point algebra" is gone; the assessment
   now asks whether some coefficient algebra adapted to the word tree can survive.
3. *Numerics* (`code/verify_series.py`, section "Paper V"): all prime-zeta roots of
   Remarks 4.4 and 5.3 confirmed to six decimals; the $p>10^8$ value is the tail integral
   alone (said). Sophie Germain and twin rows depended on the tail model: with the stated
   tail $2C_2/\log x$ ($=0.0785$, not the $0.083$ quoted) the values are $1.535$/$1.2114$ and
   $1.059$/$1.0089$ (paper: $1.536$/$1.211313$, $1.063$/$1.009747$); corrected, precision
   stated, Brun's constant cross-check added.
4. *Theorem 4.2's realization of $\lambda_S=\lambda$* used a greedy selection inside a set
   whose tail sums are too small to reach the target; replaced by deleting an initial
   segment and adjoining a greedy $O(\log x)$-sparse set of large primes.
5. Corollary 3.2's proof made explicit; Theorem 2.1's density argument now decomposes the
   Fock space over words not beginning with $\mathfrak p$; the three standard references (Nica--Speicher,
   Voiculescu, VDN) were never cited and now are; Bratteli--Robinson and Cuntz 1977 added.
   Papers II, III cited seven times, all replaced by numerals; Paper I by DOI. 7 entries,
   all cited. Numbering: Section 1 shifted (Def 1.1 $\to$ 1.2, Prop 1.2 $\to$ 1.3, Thm 1.3 $\to$
   1.4, Rem 1.4 $\to$ 1.5, Prop 1.5 removed); Sections 2--5 unchanged. The five citations
   "[V, Thm 1.2]" in VII, IX, X renumbered to 1.4.

**Paper VI — reviewed line by line; the "matrix Kakutani" theorem was ill-posed, one
corollary misstated, the $GL_2$ section used a non-unitary representation. Cites only the
foundational paper and Paper I.**

1. *Theorem 2.3 ("matrix Kakutani") was ill-posed.* It spoke of "the $U(n)$-valued cocycle
   on the tail relation with $c(v+e_\mathfrak p,v)=\rho(\mathrm{Frob}_\mathfrak p)$"; the tail relation
   is generated by commuting shifts, so the cocycle identity along the two paths to
   $v+e_\mathfrak p+e_\mathfrak q$ forces $\rho(\mathrm{Frob}_\mathfrak p)\rho(\mathrm{Frob}_\mathfrak q)=\rho(\mathrm{Frob}_\mathfrak q)\rho(\mathrm{Frob}_\mathfrak p)$:
   no such cocycle exists for non-commuting Frobenius classes, and "(2) $\Rightarrow$ (1)"
   was false (convergence of $\Xi_\beta$ does not imply commutation). The proof also applied
   the scalar dictionary to matrix coefficients $\langle\rho(g)\xi,\eta\rangle$, which are not
   unimodular. Rewritten: (1) the cocycle exists iff the classes commute; (2) then it is a
   coboundary iff $\Xi_\beta(\rho,S)<\infty$, by simultaneous diagonalization and the
   foundational paper's Props. 3.3/3.4 for each eigencharacter. New Remark 2.4 says that
   without commutation the Dirichlet series is the primary object; the rest of the paper
   (Tannakian closure, $L$-function dictionary) uses only the series. Abstract, item (i) of
   the introduction and the assessment table corrected accordingly.
2. *Standing conventions were wrong twice.* "$G$ a quotient of $\mathrm{Gal}(\bar K/K)$
   unramified outside $S$" is the wrong condition (Frobenius at $\mathfrak p\in S$ needs
   unramified *at* $\mathfrak p$); now: unramified outside a finite set, Frobenius defined for
   all but finitely many $\mathfrak p\in S$, or more generally any compact group with a family
   of classes (needed for §5). And "$\zeta_{K,S}(\beta)=\sum\mathrm N\mathfrak p^{-\beta}$" clashed
   with the foundational paper's product and with Theorem 4.1's own $\log\zeta_{K,S}$; fixed.
3. *Corollary 4.3* asserted "$\Xi_1(\rho,P_K)<\infty\iff L(1,\rho)\ne0,\infty$", but the
   $2n\log\zeta_K$ term diverges regardless, and the "$\beta<1$ via the zero-free region"
   clause was unnecessary (monotonicity in $\beta$). Restated: $\Xi_\beta(\rho,P_K)=\infty$
   for all $\beta\le1$ and nontrivial irreducible $\rho$, given $L(1,\rho)\ne0,\infty$.
4. *§5* used "the representation attached to a non-CM elliptic curve" as if it were a
   unitary representation of a profinite group and invoked Serre's open image for the
   "residual symmetry"; the $\ell$-adic representation is not unitary. Now formulated for
   the Sato--Tate group $SU(2)$ with the Satake classes, to which §§2--4 apply verbatim; the
   residual quotient is $SU(2)$ itself. "$\Xi_\beta\sim4\zeta_{K,S}$" in the abstract corrected
   to $4\sum\mathrm N\mathfrak p^{-\beta}$.
5. *Citations.* Paper III cited twice (the removed duality item of its Lemma 2.1, and the
   "pattern"), both replaced; Paper I by DOI. Of the six references, *none* was cited
   (Connes--Marcolli, Deligne--Serre, Jacquet--Shalika, Serre, Taylor); four now cited where
   used, Deligne--Serre dropped. 6 entries, all cited. Numbering: new Remark 2.4 shifts
   Lemma 2.4 $\to$ 2.5, Remark 2.5 $\to$ 2.6; Sections 3--6 unchanged. Paper VII cites
   "[VI, Thm 2.3]" (the matrix Kakutani, now conditional on commuting classes) — to be
   checked when VII is reviewed; its other citations of VI (Lem 2.2, Thm 3.2, 4.1, 5.3,
   Rem 5.4) keep their numbers.

**Paper VII — reviewed line by line; the model lacked a topology and used the wrong
algebra, one proposition was false, "Route B" was misconceived. Cites only the foundational
paper and Paper I.**

1. *Definition 1.1* put $\Omega_S=V\times G$ with $V=\mathbb Z_{\ge0}^S$ (no topology named)
   and took $\mathcal A_{G,S}=C_0(\widetilde\Omega_S)\rtimes I_S$, the non-unital dilated
   algebra, on which no KMS *state* exists (a finite measure scaling under the whole group
   $I_S$ has mass $0$ or $\infty$). Now $\Omega_S=\overline{\mathbb N}^S\times G$, compact, and
   $\mathcal A_{G,S}=C(\Omega_S)\rtimes J_S$, the unital full corner, exactly as in the
   foundational paper; Prop. 2.1 then goes through verbatim.
2. *Proposition 3.3(1) ("$\Xi_\beta(\rho,S)=\infty\Rightarrow F_\rho\equiv0$") was false.*
   Only the eigencomponents of $\rho|_A$ with divergent series vanish; the others survive.
   Counterexample inside the paper's own $S_3$ example with $\mathrm{Frob}=(12)$: the constant
   family $\frac12(\delta_e+\delta_{(12)})$ is equivariant with $F_\rho\ne0$ while
   $\Xi_\beta(\rho,S)=\infty$. The martingale "$\prod U_\mathfrak p^{-v_\mathfrak p}\langle U_\mathfrak p^{-1}\rangle^{v_\mathfrak p}$"
   of part (2) was garbled. Replaced by Prop. 3.4 (all solutions of the matrix cohomological
   equation, via simultaneous diagonalization and the foundational paper's Props. 3.3/3.4):
   a unitary solution exists iff $\Xi_\beta(\rho,S)<\infty$ iff $\rho|_{E_\beta}=1$; a nonzero
   solution iff $\rho^{E_\beta}\ne0$. New Remark 3.5: $\operatorname{rank}F_\rho F_\rho^*=\dim\rho^{E_\beta}$
   for extremal families, the multiplicity function of $\mathrm{Ind}_{E_\beta}^G\mathbf 1$ ---
   a refinement of the Frobenius series that sees the simplex (though not $E_\beta$ up to
   conjugacy in general). Theorem 5.1's proof now cites this instead of "essential values".
3. *Theorem 4.2's proof* appealed to "ergodic components indexed by the annihilator of the
   coboundary characters" (the regularity question again); now argued by the foundational
   paper's Fourier method coset by coset, which for compact abelian targets needs no
   regularity. Statement unchanged and correct.
4. *Section 6 ("Route B: the matrix corner") was wrong.* "$p_\rho\in C(G)$ the central
   projection cutting down to the $\rho$-isotypic part of $L^2(G)$" confuses $C(G)$ with the
   group algebra, and the claim that the corner's KMS states are $\operatorname{Prob}(E_\beta\backslash G)$
   pushed forward was unsupported. Replaced by Prop. 6.1: KMS states are tracial on the
   fixed-point algebra, hence of the form $\varphi_0\otimes\frac1n\mathrm{Tr}$ on
   $B\otimes M_n$, and the inner twist $\mathrm{Ad}\,\rho(\mathrm{Frob}_\mathfrak p)$ is invisible:
   $\mathrm{KMS}_\beta$ of the twisted system equals that of the untwisted one. Route B adds
   nothing, for a simpler reason than claimed.
5. *Citations.* Papers III, V, VI cited eleven times (including the removed duality item of
   III and the now-conditional matrix Kakutani of VI), all replaced by numerals or by direct
   arguments; Paper I by DOI. Feldman--Moore, Renault, Schmidt were never cited, now are.
   6 entries, all cited. Numbering: Prop 3.3 $\to$ 3.4 (new Remark 3.5), otherwise unchanged;
   other papers cite only Def. 1.1 and Rem. 1.3, unaffected.

**Paper VIII — reviewed line by line; the class-group analogue was wrong, one "proposition"
was false as stated, the sign convention was inverted, and the main topological example was
weaker than claimed. Two new results added. Cites only the foundational paper and Paper I.**

1. *The class-group entry of the dictionary was wrong.* Theorem 1.4 and Theorem 4.1 identified
   $\mathrm{Cl}^+_S$ with the *quotient* $H_1(M)/\langle[K_i]\rangle$, and the "term-by-term"
   exact sequence had a zero map where a surjection was claimed ($[\mu_i]\mapsto0$,
   $[\lambda_i]\mapsto[K_i]$ kills everything in that quotient). In the foundational paper
   $\mathrm{Cl}^+_S$ is the *subgroup* of $\mathrm{Cl}^+_K$ generated by the primes of $S$
   (Prop. 2.5). Corrected: $\mathrm{Cl}_{\mathcal L}=\langle[K_i]\rangle\le H_1(M;\mathbb Z)$, with the
   exact sequence $1\to(\oplus\hat{\mathbb Z}\mu_i)/(\ker\iota_*\cap\oplus\hat{\mathbb Z}\mu_i)\to
   \iota_*(\mathbb I_\partial)\to\mathrm{Cl}_{\mathcal L}\to1$ proved via Dehn filling
   ($H_1(M)=H_1(X)/\langle\mu_i\rangle$). Theorem 4.1 now has two parts: (1) characters trivial
   on $\mathrm{Cl}_{\mathcal L}$ (the quotient $H_1(M)/\mathrm{Cl}_{\mathcal L}$, which $G_{\mathcal L}$
   sees but $G_S$ never does) break the symmetry at every $\beta$ — a purely topological
   obstruction with no arithmetic counterpart; (2) the true analogue of the foundational
   Prop. 4.1: knot classes lying, up to a summable set, in a proper subgroup of
   $\mathrm{Cl}_{\mathcal L}$. Corollary 4.2, Example 4.3 and the dictionary table rewritten.
2. *"Lemma 1.1" was a convention with a heuristic "proof".* Now Definition 1.1 (the local
   dictionary entry, after Mazur, Kapranov–Smirnov, Reznikov, Morishita), with the reasons
   given as explanation and the coarsening (tame group vs. $\pi_1(T)$) stated.
3. *Proposition 5.2* claimed "by Jørgensen–Thurston the number of hyperbolic 3-manifolds of
   volume $\le V$ grows like $V^{cV}$" — false in dimension 3 (Dehn filling gives infinitely
   many below a fixed volume; the growth estimate is BGLM, dimension $\ge4$). The conclusion
   ($\beta_c=\infty$ for the full family) is true for a stronger reason: the twist knots have
   volumes increasing to the Whitehead volume. Rewritten with a proof; new Remark 5.3.
4. *Theorem 3.3 (parallel copies)* concluded "the transition sits at the convergence exponent"
   without saying that characters with $f\Sigma_F\in\mathbb Z$ are never detected, so that the
   KMS state of this family is never unique. Stated. Then two new results: Lemma 3.4 (every
   symmetric integer matrix is the linking matrix of a countable tame link in $S^3$, by
   band-summing meridian circles) and Theorem 3.5 (the link with
   $\mathrm{Lk}(K_i,K_j)=\mathrm{bit}_{\min(i,j)}(\max(i,j))$ and norm $(i+1)^\gamma$ has a unique
   KMS state for $\beta\le1/\gamma$ and simplex $\mathrm{Prob}(\prod\hat{\mathbb Z})$ above: the
   Bost–Connes phase diagram realized by linking alone; every nontrivial character detected
   with lower density $\ge\frac12$). Proposition 5.4 (was 5.3) restated correctly and now
   realizes both open and closed broken phases with prescribed norms; Remark 5.5 keeps the
   geometric-norm gap honest.
5. *Sign convention.* Prop. 6.2 had $\sigma_p=(p^{-1})_{\ell\ne p}$; the foundational paper's
   $\sigma_p=\theta_p=(p)_{\ell\ne p}$ (Lemma 2.10(1), $\sigma_{\mathfrak a}=r(s_{\mathfrak a})^{-1}$).
   Fixed, with $\chi(\sigma_p)=\chi_{\ell_0}(p)=\chi(\mathrm{Frob}_p)^{-1}$ (Lemma 3.8); abstract
   and table corrected.
6. *Definition 2.4* wrote $G_{\mathcal L}=\varprojlim=H_1(X;\hat{\mathbb Z})$ (not true for infinite
   links) and $Y_{\mathcal L}=\hat{\mathbb Z}^{\mathcal L}\times_{U_{\mathcal L}}G_{\mathcal L}$ (undefined);
   now the inverse limit and $Y_{\mathcal L}=\overline{\mathbb N}^{\mathcal L}\times G_{\mathcal L}$ with
   the corner algebra, as in the foundational paper. Prop. 2.5 (was 2.6) claimed "all results
   of Main and Papers I–IV apply verbatim"; restricted to what does (the classification and
   sequence-only results), with the density caveat (a character trivial on all
   $\sigma_{K_i}$ breaks the symmetry at every $\beta$; density is a condition on the linking
   matrix, Chebotarev in arithmetic). Citations: Thm 5.5 $\to$ Thm 5.2, Prop 2.6 $\to$ 2.5,
   Prop 4.2 $\to$ 4.1 of the foundational paper.
7. *Citations.* Papers II, III, IV, VII cited (VII's Def. 1.1 as the model) — replaced by
   numerals; Paper I by DOI; none of the six external references was cited, all six now are.
   Numbering: new Lemma 3.4, Theorem 3.5, Remark 3.6; old Remarks 3.4/3.5 $\to$ 3.7/3.8; new
   Remark 5.3, Prop 5.3 $\to$ 5.4, Remark 5.4 $\to$ 5.5. Papers XVII and XXII cite "[VIII,
   Thm 3.2]" (unchanged number) and "[VIII]" — to be checked when reviewed.

**Paper IX — reviewed line by line; it used Paper I's withdrawn "type criterion" as a
theorem, and misstated the finite-index inclusion. Cites only the foundational paper and
Paper I.**

1. *The "complete $W^*$-invariant $=\Sigma_\beta$" claim (abstract, Theorem 1.2, table) rested
   on the equivalence $\Sigma_\beta=\{0\}\iff\mathrm{III}_1$, which Paper I no longer asserts
   (its Prop. 2.2 is only an upper bound, $\Sigma_\beta\subseteq T(M)$, Remark 2.3). Restated:
   the complete invariant is the flow of weights (Connes, Krieger, Haagerup); $\Sigma_\beta$
   bounds it and determines it when the spectrum is pure point, which is open in general;
   the two cases decided in Paper I ($S=P_K$, $\beta\le1$: $R_\infty$; the band set:
   $R_{e^{-1}}$) are what the paper actually uses, so the main theorem (no reconstruction:
   $M_{K,P_K,\beta}\cong R_\infty$) stands unchanged. New Remark 1.3 on what the factor can
   still remember ($S(M)\subseteq\overline{\Gamma_\beta}\cup\{0\}$, foundational Prop. 6.1).
   Example 2.2's "same factor as any system with $\Sigma_\beta=2\pi\mathbb Z$" corrected
   (that only excludes $\mathrm{III}_1$). Lemma 1.1's type-III reference moved from Paper I
   to the foundational Prop. 6.1.
2. *Theorem 5.3* described the inclusion as $M_\varepsilon\subset M_{\rm sym}$ (one summand
   in a direct sum, not unital); Paper II's object is the fixed-point algebra
   $M_{\rm sym}^G\subset M_{\rm sym}$, identified with a summand embedded diagonally, minimal
   index $|G|=|\Xi_\beta|$. Restated with the argument reproduced (the "$|A_\beta|\log2$"
   formula, specific to Paper II's staircase, replaced by $\log|\Xi_\beta|$).
3. *Theorem 4.1's proof* ("by CFW any two amenable relations of the same type are OE") now
   gives the actual chain: Feldman–Moore (Cartan $\to$ relation $+$ 2-cocycle), CFW (amenable
   $\Rightarrow$ hyperfinite, cocycle trivial), Krieger (same flow $\Rightarrow$ OE); Houdayer–Vaes
   cited for the contrast with unitary conjugacy. Popa cited in Prop. 3.1.
4. *Citations.* Papers II, III, V, VII cited (Thm 5.8, Cor 5.11, Lem 5.7, Rem 4.5 of II; Cor 2.4
   of III; Thm 1.4 of V; Rem 1.3 of VII), all replaced by numerals; Paper XXVII's answer to
   the "non-abelian enlargement" question added (still amenable, nothing changes). None of the
   seven external references was cited; all seven now are. Numbering: new Remark 1.3; all
   other numbers unchanged. Other papers cite [IX, Lem 1.1], [IX, Thm 2.1], [IX, Thm 5.1]
   (unchanged) and "[IX, Rem 3.4]" twice — **no such item exists** (Section 3 has Prop 3.1
   and Remark 3.2); to be fixed in X–XX when reviewed.

**Paper X — reviewed line by line; mathematically sound, two small repairs. Cites only the
foundational paper and Paper I.**

1. "Group of right fractions $G=P^{-1}P$" for a right Ore monoid ($aP\cap bP\ne\emptyset$)
   is the wrong side; corrected to $G=PP^{-1}$, with the Ore condition displayed in (C1) and
   Nica / Laca–Raeburn cited for right LCM semigroups and their Toeplitz algebras.
2. *Proposition 2.4* (non-amenability of $\mathbb H(\mathbb Q)^\times$) had a one-line
   justification ("rational rotations generate free groups"); now proved via the
   Lubotzky–Phillips–Sarnak free group generated by $1+2i,1+2j,1+2k$ (norm-5 quaternions),
   with the identification $G=\mathbb H(\mathbb Q)^\times$ made explicit.
3. Remark 3.1 cited "[IX, Thm 2.1]" (the no-reconstruction theorem for the classical
   systems) for the collapse of an injective factor; the relevant statement is Connes'
   classification (Paper IX, Thm 1.2); rephrased. (C4)'s "equivalently not injective" now
   attributed to Anantharaman-Delaroche–Renault. The third closing question updated with
   Paper XXVII (non-abelian symmetry breaking via a cocycle; what $P$ must add is
   canonicity).
4. *Citations.* Papers II, V, VII, IX cited, all replaced by numerals; none of the five
   external references was cited, all now are, plus ADR and LPS added. Numbering unchanged.
   Other papers cite "[X, Prop 4.1]" (three times) and "[X, Thm 3.1]" — **neither exists**
   (Section 3 has Rem 3.1, Def 3.2, Rem 3.3; Section 4 is the assessment; both refer to the content of Remark 1.5 — finitely generated or infinite unit group excluded); [X, Prop 1.2],
   [X, Prop 1.4], [X, Prop 2.4], [X, Rem 2.5], [X, §3] are correct. To be fixed in XXI and XXII.

**Paper XI — reviewed line by line; the "boundary quotient" theorem was proved for a
nonexistent object, one proof was loose, one reformulation lacked its argument. Cites only
the foundational paper.**

1. *Theorem 5.1 ("the boundary quotient has no KMS state")* applied a KMS state to the
   relation $\sum_ke_{a_k}=1$ and found $(p+1)p^{-\beta}=1$ inconsistent across primes. But the
   quotient is the **zero algebra**: $p=a_j\bar a_j$ lies in every maximal right ideal of
   norm $p$, so $e_p\le e_{a_j}$ for all $j$, orthogonality of two $e_{a_j}$ kills $e_p$, and
   $1=v_p^*v_p=v_p^*e_pv_p=0$ — in *any* unital algebra of isometries with $v_av_b=v_{ab}$, no
   Nica covariance needed. Restated and proved that way; the numerical mismatch survives as
   Remark 5.2 ("partition in mean"). Corollary 5.3 and the assessment adjusted ("the object
   is zero").
2. *Proposition 2.1's proof* asserted "$a_j\vee a_k$ has reduced norm $p^2$" without argument;
   now shown that $a_j\mathcal H\cap a_k\mathcal H=p\mathcal H$ (two distinct maximal right ideals
   containing $p\mathcal H$, index count $p^4$), so $e_{a_j}e_{a_k}=e_p$.
3. *Proposition 3.1's proof* ("$0\le\sum e_k\le(p+1)1$ so $\varphi\circ\mathcal M_p\le p^\beta\varphi$")
   does not follow for a non-tracial state; replaced by $\varphi(xe_a)=\varphi(e_axe_a)\le\varphi(x)$
   ($e_a$ is $\sigma$-fixed) and the Kadison–Schwarz step for the $L^2$ bound.
4. *Proposition 6.1 (Maharam reformulation)* claimed (C4) $\iff$ Maharam extension
   non-amenable "because amenability depends only on the measure class" — that gives only
   one direction. Proved via Takesaki duality: $M$ injective iff the continuous core
   $M\rtimes_\sigma\mathbb R$ (the von Neumann algebra of the Maharam extension) is injective.
   Takesaki's book added to the bibliography.
5. *Citations.* Papers II, III, V, IX, X cited twenty times (including the nonexistent
   "[IX, Rem 3.4]"), all replaced by numerals or reproduced arguments; the six external
   references were never cited, now are. Numbering unchanged.
6. *Post-review touch (from the Paper XII review):* Prop. 6.1's Maharam extension had
   $s+\beta\log\mathrm{Nrd}(a)$ paired with $e^{-s}ds$, which is not invariant; changed to
   $e^{s}ds$ on the dilation $\widetilde\Omega$ with the invariance check written out. Nothing
   else in XI changed.

**Paper XII — reviewed line by line; the second main reduction was wrong in direction, the
boundary theorem was again proved for a zero object, and the local count omitted the
partially split case. Cites no series paper by key (foundational paper not needed).**

1. *Theorem 4.2's reduction "(C4) $\Leftarrow$ $\pi_0|_{G^1}$ has no almost invariant vectors"
   was false.* By Kuhn's theorem an amenable action has a Koopman representation weakly
   contained in the regular one, so a non-amenable $G^1$ acting amenably has *no* almost
   invariant vectors — the paper's own $F_2$ example (Remark 5.1) refutes its Theorem 4.2.
   Corrected: (C4) $\Leftarrow$ $\pi_0|_{G^1}\not\prec\lambda_{G^1}$ (non-temperedness), proved
   via restriction of amenability to subgroups and Kuhn; new Remark 4.3 records that a
   spectral gap is necessary but not sufficient. Abstract, Remark 4.4 (was 4.3), Remark 5.2's
   route (ii), the table and the closing paragraph adjusted.
2. *Theorem 2.1 ("no boundary KMS state")* — same defect as Paper XI's: the quotient is the
   zero algebra. Proved in general: by Cayley–Hamilton for the reduced characteristic
   polynomial, $\mathrm{Nrd}(a)\in a\Lambda$, so the central uniformizer $\pi$ of a principal
   prime lies in every right ideal of reduced norm $\mathfrak p$, $e_\pi\le e_{a_j}$, and
   orthogonality forces $1=0$. The numerical argument survives as Remark 2.2 ("partition in
   mean"). Hypothesis "all right ideals principal" (as (C1) requires) made explicit, since
   otherwise $d_{\mathfrak p}$ as defined is not the local count.
3. *Lemma 1.1* treated only split and totally ramified primes; for $d\ge3$ there are primes of
   intermediate local index $e$, $\Lambda\otimes\mathcal O_{\mathfrak p}\cong M_{d/e}(\mathcal O_{D_e})$.
   Now $d_{\mathfrak p}=(q^d-1)/(q^e-1)$ in general (hyperplanes of $\mathbb F_{q^e}^{d/e}$),
   with the row-module argument written out; Theorem 1.2 holds at every prime.
4. *Maharam extension* had the wrong sign ($s+\beta\log\mathrm{Nrd}(a)$ with $e^{-s}ds$ is not
   invariant); now $e^{s}ds$, with the invariance check, and the Koopman factor
   $\mathrm{Nrd}(a)^{\beta/2}$ derived consistently. The same sign fixed in Paper XI,
   Prop. 6.1. $G=P^{-1}P\to PP^{-1}$. Non-amenability of $G^1=\mathbb H(\mathbb Q)^1$ proved
   (index-two subgroup of the LPS free group, scaled to norm one) instead of asserted.
5. *Citations.* Papers II, IX, X, XI cited (including the nonexistent "[IX, Rem 3.4]"), all
   replaced by numerals; the five external references were never cited, now are, plus Kuhn
   added. Numbering: new Remark 4.3, old Remark 4.3 $\to$ 4.4; else unchanged.

**Paper XIII — reviewed line by line; the main theorem (the fixed-point algebra is the
Cartan subalgebra) is correct, but the reconstruction theorem overclaimed in two steps and
the two arithmetic hypotheses were the same condition. Cites only the foundational paper
and Paper I.**

1. *Theorem 2.1(3)* deduced the norms from "the unique minimal generating set up to sign" of
   the cocycle range — a free abelian group of rank $\ge2$ has no such thing ($\{\log2,\log3\}$
   and $\{\log2,\log6\}$ generate the same subgroup). Replaced by Lemma 2.1: the full
   bisections on which the cocycle is constant are exactly the semigroup elements $B_{\mathfrak a}$,
   so a cocycle-preserving groupoid isomorphism induces a norm-preserving monoid
   isomorphism $J_{S_1}\to J_{S_2}$ — under norm-separation alone.
2. *Theorem 2.1(4)–(5)* claimed the group $G_S$ with its Frobenius elements, the chain
   $\{\Xi_\beta\}$ and $h^+_S$ are recovered; the groupoid isomorphism only gives
   homeomorphisms of the valuation fibres, and a homeomorphism of compact groups carries no
   group structure. Now: (4) fibres matched, $G_S$ as a compact space; (5) the KMS simplices,
   hence the spaces $G_S/\Xi_\beta^\perp$, $|\Xi_\beta|$, transition locus and $\beta_c$ are
   invariants of the dynamical system; (6) *if* the symmetry actions are intertwined by an
   isomorphism $\iota$, then $\iota(\sigma_{\mathfrak p})\equiv\sigma_{\pi(\mathfrak p)}$ modulo
   inertia (the continuity argument in the true $Y_S$ gives exactly "modulo $r(\mathcal O_{\mathfrak p}^\times)$",
   which is also all that is canonical) and $\hat\iota$ transports $\{\Xi_\beta\}$. New
   Proposition 2.3: over $\mathbb Q$, for $S$ Dirichlet-dense at each of its members, the
   automorphisms of the groupoid fixing every $B_{\mathfrak a}$ are exactly the translations
   by $G_S$ (product-structure argument), so the intertwining is automatic there; Remark 2.4
   explains why the same argument does not settle fields with infinite unit group (the
   inertia images are not independent in $G_S$) and that the compact model of Papers
   VII/XXVII is not $Y_S$ at those points. $h^+_S$ is not recovered by any argument in the
   paper (Remark 3.2); the abstract, Prop. 4.2 (which also claimed $h^+_S$ "through the
   $\beta$-independent part of $\Xi_\beta$", meaningless) and the table corrected.
3. *Lemma 1.2 / Remark 2.2:* "norm-separated" (injectivity of $\mathrm N$ on $J_S$) and
   "$\log\mathrm N\mathfrak p$ $\mathbb Q$-independent" were treated as two conditions; they are
   equivalent, and equivalent to "$S$ contains at most one prime above each rational prime".
   Lemma 1.2 restated with that characterization; Example 1.3's "if such existed" case
   replaced by real examples. Theorem 1.4's spectral-subspace step now justified (the flow is
   the restriction of a compact-group action, $\Gamma_\beta$ torsion free).
4. *Citations.* Papers II, III, IX cited eight times, replaced by numerals or by the argument
   (topological principality: isotropy trivial on the dense set of finite valuations). Renault,
   Li, Matsumoto–Matui, Kirchberg–Phillips, Szabó were never cited, now are. Numbering: new
   Lemma 2.1, Definition 2.2, Proposition 2.3, Remark 2.4; Theorem 2.1 $\to$ 2.5; Remark 2.2
   $\to$ 2.6. Other papers cite [XIII, Thm 1.4], [XIII, Rem 5.1] (unchanged) and [XIII, Thm 2.1] — the latter is now
   Theorem 2.5, with weaker content; to be checked in XIV–XVIII.

**Q47 paper (unnumbered; `papers/Q47-degree46-family/Q47_localized_bost_connes.tex`,
12 pp, 0/0/0) — the localized system of the prime family $Q_{47}(n)=n^{47}-(n-1)^{47}$;
reviewed and revised on 30 August 2026, author information added. Cites the
foundational paper and Paper I by DOI, nothing unpublished.**

*Mathematics checked and found correct:* Prop 3.1 (irreducibility, roots $\zeta/(\zeta-1)$,
$\omega(\ell)=46$ iff $\ell\equiv1$ (47), separability, $\gcd(Q,Q')=1$); Prop 3.2 ($Q_q\equiv1$
mod $\kappa(q)=\mathrm{den}(B_{q-1})$, $\kappa(47)=282$; the table for $q=53,59,61$ and
$\varphi(56786730)=10368000$); Lemma 3.7 and Theorem 4.1 (Selberg upper bound
$\beta_c\le1/46$, Bateman–Horn lower bound, $(A/46)\log\log X$ at the critical point, open
phase); Lemmas 5.1–5.2 (Weil bound with $45\sqrt\ell$, Hensel step), Prop 5.3, Theorem 5.4
($\Xi_\beta=\{1\}$ for $\beta\le1/46$ under Bateman–Horn with congruence conditions);
Theorem 6.1 (congruence invisibility); Theorem 7.3 and the numerics of Remark 7.4
($\approx4\times10^{-7}$ tail).

*Corrections made.* (1) Prop 3.1(2): Eisenstein was applied to "$Q_q(x+1)=\sum\binom{q}{k+1}x^k$",
which is the wrong identity ($Q_q(x+1)$ has leading coefficient $q$); now applied to the
reciprocal polynomial, which is the displayed one. (2) Prop 3.2 asserted only one direction
of "$Q_q$ constant mod $\ell$ iff $(\ell-1)\mid(q-1)$", while Theorem 6.1(1) used it as an
equivalence; the converse is now proved (a nonzero polynomial of degree $r-1\le\ell-2$
cannot vanish at $\ell-2$ points unless $r=\ell-1$, which is checked directly). Theorem
6.1(1)'s "by inspection for the finitely many smaller $\ell$" removed; the statement is
restricted to what is proved. (3) Lemma 5.1's threshold "$\ell\ge8200$ suffices" corrected to
$\ell\ge8283$ (root of $\ell/2-45\sqrt\ell-46$ at $8282.98$), and in Remark 6.3. (4) Theorem 7.3's count
"each $n$ contributes $k$ primes" now notes the lower-order overlaps of consecutive
$n$. (5) Open problem (4) stated the foundational Prop 6.1 backwards ("ratio set containing
the group generated by $p^{-\beta}$"); it is an upper bound $S(M)\subseteq\overline{\Gamma_\beta}\cup\{0\}$,
now stated correctly with Paper I's criteria cited. (6) All citations of the foundational
paper converted from the old numbering to the current one: Thm 3.1$\to$3.6, Thm 3.10$\to$3.9,
Lem 3.9$\to$3.8, Rem 5.4$\to$5.3, Rem 5.5$\to$5.4, Thm 5.7$\to$5.5, Rem 5.9$\to$5.7,
Prop 6.10$\to$Prop 5.8/Rem 5.9, Prop 7.1$\to$6.1, "Def 2.1 and Rem 2.3"$\to$Def 2.1, 2.6; the
bibliography's "reader should verify the numbers" parenthetical replaced by a statement
that the numbers refer to the current version. Ha–Paugam and Laca–Larsen–Neshveyev were
in the bibliography but never cited; now cited in §2. (7) Author, email, repository
footnote, pdftitle/pdfauthor added; hyperref bookmarks disabled (math in section titles).

*Provenance.* No separate repository: the paper lives here, its checks are
`papers/Q47-degree46-family/verify_q47_paper.py` (all pass, output `q47_checks.json`), and
the empirical data belong to the Q47 Bateman–Horn record (DOI 10.5281/zenodo.20753750).

*DOI registry (30 August 2026).* Foundational paper 10.5281/zenodo.22152101 (published, v1);
Paper I 10.5281/zenodo.22160827 (DOI reserved, draft saved, not published); Paper II
10.5281/zenodo.22177726 (DOI reserved, draft saved, not published, DOI inserted in its
footnote). Later papers cite Paper I by DOI and Paper II by numeral only.

*Note on the foundational paper's numbering.* This paper, like all companions, now cites
the numbering of the reviewed (v2) foundational paper, not of the published v1 at the same
DOI; v2 must be published, and the DOI in every companion updated to the v2 version DOI (or
the Zenodo concept DOI used), before any companion is released.

**Paper XXVII — new (29 August 2026), written on request as the diagnostic follow-up to
Paper VI's Remark 6.1 and Paper VII's assessment. Cites only the foundational paper and
Paper I; Papers VI, VII by numeral.** `papers/XXVII-nonabelian-groupoids/` (10 pp, 0/0/0).

*Content.* (1) Route B (noncommutative coefficient algebra $\mathcal B\rtimes J_S$): no-go.
KMS states are tracial on $\mathcal B$, so the simplex is the simplex of scaling traces
$T_\beta(\mathcal B,\alpha)$ (bijectively when $\log\mathrm N\mathfrak p$ are $\mathbb Q$-independent,
e.g. $K=\mathbb Q$, by Kronecker); inner twists are invisible; $C(Y_S)\otimes M_n$ with any inner
twist gives the abelian simplex; for non-commuting lifts the twisted endomorphisms do not
even commute. (2) Route A, isotropy reading: no-go via Neshveyev's theorem — isotropy $N$
contributes $\mathrm{Irr}(N)$ (dual data) with the trivial character a symmetry-fixed
extreme point; a $G$-transitive action on extreme KMS states forces $\mu$-a.e. trivial
isotropy. (3) Route A, skew-product reading: the ordered Frobenius cocycle
$c(y,x)=P_n(y)P_n(x)^{-1}$, $P_n(x)=u_1^{x_1}\cdots u_n^{x_n}$ (primes by norm, lifts $u_i$ of
the classes), with increments $P_{j-1}u_jP_{j-1}^{-1}$ — well defined for non-commuting
lifts, circumventing Paper VI's obstruction. Topological model: $X_i=\overline{\{(k,u_i^k)\}}\subset\overline{\mathbb N}\times G$,
$\mathcal G_c=I_S\ltimes(\widetilde X\times G)$, étale, amenable, principal on a conull set,
$\mathcal A_c=C(X\times G)\rtimes J_S$. Theorem 4.2: $\mathrm{KMS}_\beta(\mathcal A_c)\cong\mathrm{Prob}(H\backslash G)$,
$H$ the Mackey range of $c$ (Zimmer), $G$ transitive on extreme points. Theorem 4.3
(non-abelian Kakutani): $\rho\circ c$ coboundary $\iff\Xi_\beta(\rho,S)<\infty$, for every
lift — proof by the matrix martingale $Z_n=P_nM_n^{-1}$, $m_i=(1-t_i)(I-t_iU_i)^{-1}$,
$m_i^{-*}m_i^{-1}=I+t_i(I-U_i)^*(I-U_i)/(1-t_i)^2$, determinant argument for necessity.
Corollary 4.4: $N_\beta=\langle\langle H\rangle\rangle$; $\mathrm{Prob}(G/N_\beta)$ iff $H$ normal.
Theorem 4.5 (mixing criterion): $\|m_{n+1}\cdots m_m\|\to0$ for all nontrivial $\rho$ forces
$H=G$. Theorem 4.6 (lift-dependence, $S_3$, transposition class at every prime): constant
lift $(12)$ gives 3 KMS states, alternating lift $(12),(13)$ gives 1. Corollary 4.7: no
canonical model; the lift-independent content is exactly $N_\beta$. Proposition 4.9: rigid
$N_\beta$ (no proper subgroup with the same normal closure) gives $\mathrm{Prob}(G/N_\beta)$
for every lift; Example 4.10 ($N_\beta=A_3$, two states) realizes a nontrivial $G/N_\beta$.

*Consequences for other papers.* The verdict sharpens Paper VII's closing questions
(its "intermediate structure" question is answered: the structure is a non-abelian
cocycle, not a non-abelian semigroup) and Paper VI's Remark 6.1 (both routes settled).
Neither paper is changed; when VII is next touched, its assessment should point here.
XXVI does not exist; the numbering was chosen by the author.

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


## The corpus: 27 papers (XXVI not yet written), all compiling clean

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
| XXVII | Non-abelian BC groupoids: two no-go theorems, the ordered Frobenius cocycle, a non-abelian Kakutani theorem, lift-dependence | 10 | clean |

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
