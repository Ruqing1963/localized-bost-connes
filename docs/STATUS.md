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

**Paper XXVIII — new (31 August 2026): condition (C4) settled, in the negative.**
`papers/XXVIII-spectral-gap/` (6 pp, 0/0/0). Anonymised front matter (author block commented out).

*What was asked.* Build the Hecke/Laplacian operator on the Bruhat–Tits tree that Paper XI's
transfer operator failed to be, use the Ramanujan bound $2\sqrt p$ to produce a spectral gap for
the Koopman representation, and conclude that the Hurwitz factor is non-injective.

*What is true.* The operator exists and behaves perfectly: $T_p=\sum_{k}\pi(a_k)$ over the $p+1$
Hurwitz quaternions of reduced norm $p$, unitary-valued on the Maharam extension, hence no nested
projections and no Cuntz obstruction. Its spectrum on $L^2_0$ is exactly $[-2\sqrt p,2\sqrt p]$ and
the Ramanujan bound is *attained*. But that settles nothing, for two independent reasons, and the
paper proves both.

1. *The Ramanujan bound is the tempered bound.* $2\sqrt p$ is the norm of the same operator in the
   regular representation of the free group of rank $(p+1)/2$ (Kesten). Attaining it certifies that
   the Koopman representation is tempered, and by Kuhn's theorem (Paper XII) temperedness is what
   an *amenable* action has. The gap between $2\sqrt p$ and $p+1$ is Kesten's gap and measures
   non-amenability of the **group**, not of the **action**. To prove (C4) spectrally one would need
   spectrum *outside* the Ramanujan band — the failure of the property the Hurwitz order supplies.
2. *(C4) is false outright.* Every $a\in\mathbb H(\mathbb Q)^\times$ is a unit of
   $\mathcal H\otimes\mathbb Z_q$ at almost every $q$ (Lemma 1.2), so for each finite $F$ the
   subgroup $G_F=\mathbb H(\mathbb Z[1/F])^\times$ is discrete in $\prod_{p\in F}\mathbb H(\mathbb Q_p)^\times$
   (definiteness: $SU(2)$ compact at $\infty$) and acts **freely and properly** on a conull set.
   Hence $\mathcal R_F$ is smooth and $\pi\restriction G_F\cong\infty\cdot\lambda_{G_F}$; and
   $\mathcal R_G=\bigcup_F\mathcal R_F$ is hyperfinite (Dye/CFW). The groupoid is amenable, the
   factor injective, and it collapses to $R_\infty$/$R_\lambda$/Krieger/type I like every abelian
   system before it. No spectral input is used.

*Scope.* Theorem 5.1 generalizes: for any order in a finite-dimensional $\mathbb Q$-algebra with
$A\otimes\mathbb R$ a product of division algebras, the same argument applies. **Conditions
(C1)–(C3) of Paper X are incompatible with (C4)** — the search for a non-injective arithmetic
Bost–Connes factor cannot succeed by enlarging the index monoid, because finiteness of the support
of the norm means the group never acts at more than finitely many places at once. Paper XII's $F_2$
counterexample is identified as the actual mechanism, not an analogy.

*Consequences for other papers.* Paper X's (C4) is no longer open; Paper XI's Prop. 6.1 (Maharam)
and Paper XII's Thm 4.2 (Kuhn reduction) are used and remain correct, but their closing questions
are now answered. Paper IX's closing question ("is there a non-amenable enlargement?") is answered
in the negative. When X, XI, XII and IX are next touched, their open-problem sections should point
here.

**Q47 spacing-statistics paper (unnumbered; 31 August 2026).**
`papers/Q47-spacing-statistics/Q47_spacing_statistics.tex` (8 pp, 0/0/0, three figures).
Anonymised front matter for a double-blind submission; the author block is present but commented
out.

*Not part of the numbered series.* It was drafted as "Paper XXVI" and renumbered out on review:
it contains no operator algebra, no KMS states, no obstruction group. The quantities it measures
($C_1$, $g_2$, $\Sigma^2$, $P(s)$) do not enter the Bost–Connes theory at all — $\beta_c$ and
$\Xi_\beta$ depend on the convergence exponent of the detecting sets, not on the Bateman–Horn
constant and not on correlations between primes. The only link is an analogy in §7 between the
statistical inertness of $p\equiv1\ (282)$ and the invisibility of the same congruence to the
symmetry group in the Q47 paper (its Thm 6.1); the text now labels it an analogy and says the two
mechanisms differ. It is an unnumbered companion of the Q47 paper, as that paper is itself
unnumbered.

*Data.* 17 blocks of width $10^8$ covering $3\times10^8\le n<2\times10^9$ with no gap,
$15\,419\,587$ primes of 392–410 digits, from the Bateman–Horn computation (DOI
10.5281/zenodo.20753750). Integrity checked by the largest-gap statistic ($\approx\log N$ mean
gaps); one lost sub-range $n\in(1399874854,1399880001)$ found at 46.7 mean gaps (Poisson
probability $10^{-13}$) and excised, leaving two contiguous segments.

*Results.* (1) Bateman–Horn constant measured: $C_1(Q_{47})=8.6874\pm0.0018$ (the Q47 paper only
assumes $0<C_1<\infty$). (2) No level repulsion: $P(s<0.05)$ exceeds the GUE value by 332×, and
matches the lattice null (local geometric law, forced by $n\in\mathbb Z$) to $+0.36\%$; lattice
null RMSE $2.00\times10^{-3}$, $R^2=0.99991$, against $R^2=0.018$ for GUE. (3) No spectral
rigidity: $\Sigma^2(L)/L=0.9867$ flat over five decades up to $L=1.5\times10^5$; GUE wrong by
$8.3\times10^4$ there; fit $\Sigma^2/L=a+b\log L/L$ gives $a=0.9832$, $b=0.0117$ against the GUE
requirement $a=0$, $b=\pi^{-2}$. (4) The mesoscopic structure is exactly Hardy–Littlewood: only
$\ell\equiv1\ (47)$ constrain the index (46 of $\ell$ classes forbidden), giving the parameter-free
$R(d)=\prod(1+c_\ell(d)/(\ell-92))$, fitting the measured $g_2$ over $d\le600$ at
$\chi^2/\mathrm{dof}=1.047$ (599 dof), $R^2=0.982$, against 56.02 for a structureless correlation.
(5) Congruence audit: $n$ unconstrained below 283; modulo 283, 659, 941, 1129, 1223 exactly 46
classes are empty and the empty sets coincide with the root sets of $Q_{47}$.

*Honesty notes carried in the text.* The lattice null still has $\chi^2/\mathrm{dof}=11.0$ — that
residual is the Hardy–Littlewood correlation, which makes consecutive spacings dependent. The
closure $\Sigma^2/L=1+2\rho\sum(g_2-1)$ gives 0.9918 against the measured 0.9867; the 0.5\%
difference is within the normalisation systematics of $C_1$ and is recorded as consistency, not a
precision test. GUE is stated to be the wrong null from the start (Gallagher's theorem) and is
reported only because it is the ensemble against which rigidity would be measured.

*References.* Eight entries, all cited. The foundational paper was dropped: it had a single
motivational citation, and citing a KMS paper would have reasserted the link the paper does not
have. The Q47 paper is kept (provenance of the family, its congruence, and the §7 analogy) and the
empirical paper is kept (the data). Lemma 5.1's root count, previously quoted from the Q47 paper,
is now proved in place, so the paper is self-contained as mathematics.

*Provenance.* Analysis scripts and summary JSON in the same folder, duplicated from
`papers/Q47-degree46-family/gue/` where the diagnostic report `REPORT.md` also lives. Raw prime
data not redistributed. The numeral XXVI remains unused in the series.

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

**Paper XIV — reviewed line by line (4 September 2026); the equivalence theorem and the
grading are correct, but the gauge-equivariant reconstruction was stated against the
withdrawn [XIII, Thm 2.1] and its proof had a genuine gap; one example was wrong; citations
brought to policy. No renumbering: every item keeps its number (Lem 1.1 – Rem 4.4).**
`papers/XIV-equalnorm/` (6 pp, 0/0/0/0; was 5 pp).

1. *Theorem 4.2 (gauge-equivariant reconstruction): statement and proof rewritten.* The
   statement promised "all conclusions of [XIII, Thm 2.1]" — the withdrawn overclaim —
   including an isomorphism $G_{S_1}\cong G_{S_2}$ intertwining Frobenius classes and
   $h^+_{S_1}=h^+_{S_2}$. Worse, the proof asserted that XIII's "only use of norm-separation
   was" the Cartan-preservation step; XIII's own Remark 2.6 says norm-separation enters
   *twice*, in Thm 1.4 **and** in Lemma 2.1, whose bisection argument needs the value of the
   scaling cocycle to determine the group element — exactly norm-separation, and exactly
   what fails in the equal-norm case this paper is about (a full bisection can mix the two
   primes over 5 while keeping $c\equiv\log5$). Repair: gauge-equivariance intertwines not
   only the scaling cocycle $c$ but the integer-valued gauge cocycle $\tilde c(\mathfrak a
   \mathfrak b^{-1},y)=\mathfrak a\mathfrak b^{-1}$ (pointwise comparison gives
   $z^{\tilde c_1(\gamma)}=\theta(z)^{\tilde c_2(\theta_*\gamma)}$, i.e.
   $\tilde c_1=\hat\theta\circ\tilde c_2\circ\theta_*$), and Lemma 2.1's argument run with
   $\tilde c$ needs no separation, since the value of $\tilde c$ *is* the group element.
   The theorem now delivers exactly the current [XIII, Thm 2.5]: norm-preserving bijection;
   valuation fibres and $G_S$ as a compact space; KMS simplices, $|\Xi_\beta|$, transition
   loci, $\beta_c$; and — still conditionally on intertwined symmetry actions, as there —
   Frobenius classes modulo inertia and the chain $\{\Xi_\beta\}$. Renault's theorem is now
   applied with topological principality re-proved in place (reproducing [II, Thm 2.5(1)]).
   New byproduct, stated as part (2): $\delta_{\mathfrak p}=\hat\theta(\delta_{\pi(\mathfrak p)})$,
   so the torus isomorphism $\theta$ is *a posteriori* induced by the produced bijection $\pi$.
2. *$h^+$ dropped.* Abstract, Cor 4.3 and the assessment table claimed $h^+_{K_1}=h^+_{K_2}$;
   by [XIII, Rem 3.2] $h^+_S$ is recovered by no argument there, and nothing in XIV adds one.
   Corollary retitled "Dedekind zeta"; $\zeta_{K_1}=\zeta_{K_2}$ (arithmetic equivalence)
   kept — it is just the norm multiset.
3. *Definition 4.1.* "$\theta$ being induced by a bijection of the coordinate circles" was
   false as an a-priori claim: $\operatorname{Aut}(\mathbb T^S)$ is dual to
   $\operatorname{Aut}(\mathbb Z^{(S)})$, most of whose elements permute no coordinates
   (e.g. the matrix $[[2,1],[-1,0]]$ preserves the log-norm functional of the two primes
   over 5). Rewritten: no bijection presupposed, none encoded in $\theta$; Theorem 4.2
   produces one and shows $\theta$ was induced by it after all.
4. *Example 2.3 was wrong.* The degree-$k$ piece was "spanned by
   $\mu_{\mathfrak p}^m f\mu_{\bar{\mathfrak p}}^{(m+k)\,*}$-type elements" — those have
   gauge degree $m\delta_{\mathfrak p}-(m+k)\delta_{\bar{\mathfrak p}}\notin L$, and for
   $k\ne0$ are not even $\sigma$-invariant. Corrected to
   $\mu_{\mathfrak p}^{m+k}\mu_{\bar{\mathfrak p}}^{n}f(\mu_{\mathfrak p}^{m}\mu_{\bar{\mathfrak p}}^{n+k})^*$,
   e.g. $\mu_{\mathfrak p}^{k}f\mu_{\bar{\mathfrak p}}^{k\,*}$, displayed to cure an
   overfull line.
5. *Remark 3.3.* The cross terms of $(\alpha\mu_{\mathfrak p}+\beta\mu_{\mathfrak q})^*(\alpha\mu_{\mathfrak p}+\beta\mu_{\mathfrak q})$
   had the conjugates on the wrong coefficients ($\bar\alpha\beta$ goes with
   $\mu_{\mathfrak q}\mu_{\mathfrak p}^*$); fixed, and $|\alpha|^2+|\beta|^2=1$,
   $\alpha\beta\ne0$ made explicit.
6. *Gauge action constructed in place.* §1 opened with "Recall from [III, Lem 1.1]" — an
   item that does not exist in Paper III (flagged in the handoff). Replaced by an in-place
   construction: the $I_S$-valued cocycle $\tilde c$, composed with characters, gives the
   strongly continuous gauge action of $\mathbb T^S=\widehat{I_S}$, and
   $\sigma_t=\gamma_{\iota(t)}$ since $c=\langle\tilde c,\log\mathrm N\rangle$ (Paper III
   signposted by numeral for its use of that identity). The same $\tilde c$ is then what the
   repaired Theorem 4.2 runs on.
7. *Citations brought to policy.* Bibitems `SeriesII`, `SeriesIII`, `PaperXIII` removed
   (unpublished companions); all references to Papers II, III, XIII converted to numeral
   signposts, with [XIII, Thm 2.1] → Theorem 2.5 throughout, per XIII's renumbering. The
   signpost "[II, Thm 2.5]" (Cartan/topological principality) verified against the reviewed
   Paper II — the number is current. Renault, Neukirch and the foundational paper were in the
   bibliography but never cited; now cited (Renault at Rem 3.2 and in Thm 4.2's proof;
   Neukirch Ch. VII §13 for Chebotarev in Prop 1.5, now stated via the Galois closure and
   complete splitting; [Main, Thm 3.6] and the notation paragraph). Bibliography: three
   entries, each cited, all published.
8. *Abstract, assessment table and closing* aligned with 1–3: table rows added for
   "θ induced by a bijection: a posteriori", "Frobenius, $\{\Xi_\beta\}$: if symmetries
   intertwined", "$h^+$: not claimed"; the closing "everything holds" softened to "the exact
   strength of Paper XIII's Theorem 2.5". Preamble: `\cG`, `\cO` added, `\raggedbottom`
   (as in XXVIII) to remove a page-break underfull.

*Consequences for other papers.* All item numbers unchanged, so [XIV, Thm 1.3] (cited in
XVI), [XIV, Def 1.2] (XIX), [XIV, Rem 3.3] (XV) and [XIV, Thm 4.2] (XV, XIX, XX) still
exist. But Thm 4.2's Frobenius conclusion is now explicitly conditional on intertwined
symmetry actions: **Paper XX** (l. 159, "the Frobenius classes recovered by [XIV, Thm 4.2]")
must be re-checked at its turn — the recovery needs the intertwining, automatic only over
$\mathbb Q$ for Dirichlet-dense $S$ ([XIII, Prop 2.3]). XV's and XIX's uses (the open
question of Rem 3.3; Cartan transport and the gauge-equivariant hypothesis) look compatible
with the revised content; confirm at their turns.

**Paper XV — reviewed line by line (4 September 2026); the two structural negative results
(the spectrum is blind to multiplicity; the range projections are blind to $G_S$) are
correct, but the paper resurrected the withdrawn $h^+$ claim, its ergodicity "reduction" of
Step 2 was false in both directions — Step 2 is in fact settled negatively by a two-line
example — and "Arveson spectrum" named the wrong object; citations brought to policy. No
renumbering: every item keeps its number (Prop 1.1 – Rem 4.4).**
`papers/XV-spectral/` (5 pp, 0/0/0/0; was 4 pp).

1. *Theorem 2.2(5) deleted ($h^+$).* It claimed $h^+_{S_1}=h^+_{S_2}$ unconditionally,
   "this being the $\beta$-independent part of $|\Xi_\beta|$", citing a "permanent
   obstruction" in [Main, §4.1]. No such statement exists there, and §4.1's own example
   ($K=\mathbb Q(\sqrt{-5})$) shows the opposite structure: whether a class-group character
   lies in $\Xi_\beta$ is a summability condition on $S$
   ($\sum_{[\pp]\notin\ker\psi}\Ns\pp^{-\beta}<\infty$, [Main, Prop 4.1]), not a
   $\beta$-independent quantity — for $S=P_K$ and $\beta\le1$ the class-group characters are
   *not* in $\Xi_\beta$, so $\bigcap_\beta\Xi_\beta$ is trivial there while $h^+_K$ can be
   anything. This is the same "β-independent part" argument the XIII review had already
   removed as meaningless (XIII entry, item 2; XIII Rem 3.2: $h^+_S$ recovered by no
   argument). Abstract was already silent on $h^+$; theorem, its proof, Rem 2.3, the table
   and the closing prose now are too.
2. *Section 3 was wrong: Step 2 is false, not "reduced to ergodicity".* Prop 3.2 claimed
   "mixed isometries with $p\ne0,1$ exist $\iff$ $g=\pp_2\pp_1^{-1}$ is not ergodic on
   $(\widetilde Y_S,\nu_\beta)$". Both implications fail. Forward: the cross term is
   supported on $U^c\cap g(U\cap\pp_1Y_S)$ — the old proof dropped the domain restriction
   $U\cap\pp_1Y_S$ of the partial homeomorphism — so for $p=e_{\pp_1}$
   ($U=Y_S\setminus\pp_1Y_S$) the condition is vacuous:
   $\mu_{\pp_1}^*(1-e_{\pp_1})=0$ and $v=\mu_{\pp_1}e_{\pp_1}+\mu_{\pp_2}(1-e_{\pp_1})$ is a
   pure-frequency isometry mixing the two primes, invariant set nowhere in sight. Backward:
   non-ergodicity gives measurable invariant sets, and the criterion needs clopen ones.
   Rewritten: Prop 3.2 states the corrected criterion
   $v^*v=1\iff g(U\cap\pp_1Y_S)\subseteq U$ *and* the unconditional example; so
   "every pure-frequency isometry is diagonal" (Step 2 of the proposed route) is **false**,
   with no ergodic input. Rem 3.3 records the withdrawn equivalence, keeps what survives
   (single-element ergodicity of $g$, with $\Ns g=1$ hence measure-preserving, remains open
   and of independent interest, [Main, Lem 3.1] for the full group), and decouples it from
   the existence question. Section title, abstract, table ("mixed isometries $\iff$
   non-ergodic: false, both ways") and the closing "Two questions" adjusted; §4's
   Cor 4.2 now reads "even if every pure-frequency isometry were diagonal — and it is not".
   The paper's architecture survives: it had located the decisive failure at Step 3
   (Thm 4.1, range projections blind to $G_S$ — checked, correct), and that verdict is
   unchanged; the spectral route is now closed twice over.
3. *"Arveson spectrum" renamed.* $\{\lambda:\cA(\lambda)\ne0\}$ is the point spectrum
   (eigenvalue group), not the Arveson spectrum, which is the closed support of the spectral
   subspaces — the closure of $\langle\Ns\pp\rangle$, hence all of $\R_{>0}$ as soon as two
   $\log\Ns\pp$ have irrational ratio, and then nearly information-free. Prop 1.1 retitled
   "The point spectrum", notation $\Sp_p(\sigma)$ throughout, a sentence recording the
   distinction added, and the "only if" of $\cA(\lambda)\ne0\Rightarrow\lambda\in
   \langle\Ns\pp\rangle$ — previously asserted — proved via Bohr--Fourier coefficients of
   the almost periodic function $t\mapsto\varphi(\sigma_t x)$.
4. *Thm 2.2 slightly strengthened where it was free:* part (2) now notes that at any
   $\beta>\beta_c$ one has $\Xi_\beta=\widehat{G_S}$ ([Main, Thm 3.6]:
   $\zeta_{K,S}(\beta)<\infty$), so the compact space $G_S$ itself is matched — this
   replaces, correctly, what Rem 2.3's old "$G_S$ up to the relevant homeomorphisms" was
   gesturing at. The $\beta_c$/transition-locus clause now runs exactly as in
   [XIII, Thm 2.5(5)], with the note that that argument uses only KMS transport.
5. *Rem 2.3 (the gap) made honest against the current XIII:* not obtained here are the
   norm-preserving bijection *and* XIII 2.5's conditional part (6) (Frobenius classes,
   $\{\Xi_\beta\}$ as subgroups); $h^+$ is a conclusion in neither paper. The "only gap is
   the multiset" headline stands for the unconditional part.
6. *Verified correct:* Prop 2.1 (KMS bundle intrinsic); Lemma 3.1 (Nica relation,
   $\pp_1\vee\pp_2=\pp_1\pp_2$); Thm 4.1 ($e_\aaa$ depends only on valuations since the
   $G_S$-coordinate of $\aaa Y_S$ is unconstrained; $C^*(\cE)\cong C(\overline{\mathbb
   N}^{\,S})$ by Stone--Weierstrass; properness from [Main, (2.1)] — number verified);
   Cor 4.2; Rems 4.3, 4.4 (the exact sequence and the open question, the latter pointing at
   [XIV, Rem 3.3], number verified current).
7. *Citations to policy.* Bibitems `SeriesII` (never cited), `PaperXIII`, `PaperXIV`
   removed; [XIII, Thm 2.1] → Theorem 2.5 by numeral throughout (per XIII's renumbering),
   [XIV, Thm 4.2] and [XIV, Rem 3.3] → numerals (numbers verified against the reviewed XIV).
   Arveson, Nica, Renault were in the bibliography but never cited; now cited (Arveson at
   the spectral subspaces, Nica at the covariance relation, Renault at Cor 4.2 where the
   reconstruction it feeds is named). [Main, Thm 3.6], [Main, Lem 3.1], [Main, (2.1)]
   verified against the current build. Bibliography: four entries, each cited, all
   published. A notation-and-policy sentence added at the head of §1.

*Consequences for other papers.* All item numbers unchanged. **XVII** (l. 240) and
**XVIII** (ll. 70, 167) cite [XV, Prop 1.1] as "the Arveson spectrum" — the number and the
mathematical content (the eigenvalue subgroup $\langle\Ns\pp\rangle$ is an invariant) are
unchanged, but the name should become "point spectrum" at their turns. Nothing downstream
cites XV's §3, so the Step-2 reversal (open → false) propagates nowhere. XV's own use of
[XIV, Thm 4.2] as "the strongest unconditional statement" is compatible with the revised
XIV.

**Paper XVI — reviewed line by line (4 September 2026); the three negative verdicts (twist
harmful; sign error in the proposed rates; no critical slowing down) all stand, but the
tensorisation theorem's own lower bound was unsupported and contradicted its weight
constraint, the "no compact resolvent" claim rested on an invalid one-line argument, and
the generator was not written in GKLS form; one dangling reference; citations brought to
policy. No renumbering: every item keeps its number (Prop 1.1 – Rem 4.4).**
`papers/XVI-transport/` (6 pp, 0/0/0/0; was 5 pp).

1. *Theorem 4.1 rewritten.* It asserted $\alpha_\pp\gtrsim1-t_\pp$ "by the standard
   comparison of MLSI with the spectral gap for birth--death chains" --- no such comparison
   exists in that direction, and single-site MLSI positivity for this M/M/1-type chain is
   not resolved here --- and its display $\alpha\gtrsim\inf_\pp a_\pp\,(1-\Ns\pp_0^{-\beta})>0$
   is false for the norm-summable weights its own Remark 3.3 requires
   ($\inf a_\pp=0$). Now "Tensorisation to an infimum": (i) the spectral gap is exactly
   $\inf_\pp a_\pp\,\mathrm{gap}(\cL_\pp/a_\pp)$ with
   $\mathrm{gap}\ge(1-t)^2/4t\ge(1-t)^2/4$ by [IV, Lem 6.1] (number and sharp constant
   $C(t)=4t/(1-t)^2$ verified exact; its Dirichlet form $\mathbb E_{\mu_t}|\Delta h|^2$ is
   that of the normalized corrected chain with rates $(1,t^{-1})$); (ii) MLSI
   $=\inf_\pp a_\pp\alpha_0(t_\pp)$ by entropy subadditivity + Dirichlet additivity, with
   single-site tests for $\le$; (iii) explicit weight dichotomy --- rates bounded below:
   gap $\ge\inf a_\pp(1-3^{-\beta})^2/4>0$ near $\beta_c$; norm-summable rates: the infima
   vanish for every $\beta$, $\beta$-independently, for the weight reason alone. Either
   way no constant has the product shape $\Pi_\infty$; the headline conclusion (no critical
   slowing down) is unchanged and now stands on two legs. Cor 4.2/abstract/table wording
   aligned ("infimum, not product"; single-site defect $\ge0.66$, unit-rate gap
   $\ge(1-3^{-\beta})^2/4\ge0.11$).
2. *Remark 2.2's non-compact-resolvent "proof" was invalid.* "The eigenvalue $\log\Ns\aaa$
   of $\Dv$ occurs with the infinite multiplicity of $L^2(X)$" ignores that $\Db$ acts on
   that factor: $\Df^2=\Db^2\otimes1+1\otimes\Dv^2$, and over $\Q$ the norms are distinct
   and tend to $\infty$, so $\Df$ has compact resolvent iff $\Db$ does --- a property of
   Paper IV's weights that IV neither establishes nor refutes (its own assessment leaves the
   spectral triple on the crossed product open). Rewritten as an honest reduction
   ("Spectral triple: not established"), Rieffel cited for the CQMS notion actually at
   issue; abstract and table adjusted from "false" to "not established".
3. *Proposition 3.1's generator was not a $*$-map:* the second Lindblad term "$-e_\pp x$"
   is now the GKLS-symmetrised $-\tfrac12(e_\pp x+xe_\pp)$ (agreeing with $e_\pp f$ on the
   abelian part, so \eqref{eq:inv}-type computation unchanged); the KMS scaling relations
   are re-derived in place from $\varphi(xy)=\varphi(y\sigma_{i\beta}(x))$,
   $\sigma_{i\beta}(\mu_\pp)=\Ns\pp^{-\beta}\mu_\pp$, with [III, Prop 5.1] verified exact
   (both displayed relations match verbatim) and kept as a numeral signpost; and the
   "only if" of the detailed-balance ratio, previously argued for a single failing prime,
   is proved via independence ($\nu(e_\pp e_\qq)=t_\pp t_\qq$): test $f=1$ and $f=e_\qq$,
   subtract, $A_\qq(1-t_\qq)=0$.
4. *Corollary 3.2:* the cross-prime terms cancel for the proposed rates
   ($A_\qq t_\qq+B_\qq=0$), which the displayed single-prime computation silently assumed;
   the clause is now explicit. All numerics recomputed and exact: the four values of
   $(1-t^2)(1-t)$; Remark 1.4's twisted-commutator table (eight values); and Cor 4.2's
   table, $\Pi_\infty$ over $3\le\ell\le10^4$ = 3.702e-1/1.270e-1/3.578e-2/1.857e-2 and
   $1-3^{-\beta}$ = 0.8076/0.7324/0.6845/0.6670 at $\beta=1.5/1.2/1.05/1.001$.
5. *Dangling reference:* "[IV, Def.~2.5]" for the horizontal operator --- in the reviewed
   IV, 2.5 is the commutator-formula Lemma; the operator is **Definition 2.4**. Fixed, and
   the representation made explicit: $\mu_\aaa$ acts on $\ell^2(J_S)$ alone and $f$ acts on
   the summand $\bb$ as $f\circ m_\bb$, so $[\Db,\mu_\aaa]=0$ --- no conflict with IV's
   remark that its weights are incompatible with bounded isometry commutators, which
   concerns a different representation; Prop 2.1's kernel proof now runs through the
   $\bb=(1)$ summand and [IV, Lem 3.1] (verified: $\{f:L(f)=0\}=\C1$ on $C(X)$).
6. *Citations to policy.* Bibitems `SeriesIII`, `SeriesIV`, `PaperXIV` removed (numerals
   throughout); `JungeLi` (a preprint, never cited) dropped; `Main` was in the bibliography
   but never cited --- now cited in the new notation-and-policy sentence at the head of
   §1; `CM`, `Rieffel`, `CarlenMaas`, `Cipriani` were in the bibliography but never cited
   --- now cited at the twist remark, the CQMS remark, quantum detailed balance, and
   KMS-symmetry respectively. [I, Prop 7.2] kept as \cite (Paper I citable by DOI;
   existence and tail-content verified). A provenance clause added to Rem 1.3: the twisted
   triple refuted in §1 is the candidate proposed in Paper IV's closing assessment.
   Bibliography: six entries, each cited.
7. *Verified correct:* Prop 1.1 (twisted commutator, coefficient
   $\log\Ns\pp+(1-\Ns\pp^\beta)\log\Ns\bb$, unbounded) and all eight numerical values of
   Rem 1.4; Prop 1.2; Prop 2.1's equivalence with norm-separation ([XIV, Thm 1.3] verified
   current); the KMS relations and the corrected ratio $b_\pp=a_\pp\Ns\pp^{+\beta}$;
   [IV, Lem 5.1] (Kakutani), [IV, Thm 6.2] (continuous vanishing), [III, Thm 2.3]
   (measure-class invariance) all verified by number and content and converted to numerals.

*Consequences for other papers.* All item numbers unchanged. **XX** (l. 272) cites
[XVI, Thm 4.1] as "the quantum transport inequalities did not fail for lack of a better
Dirichlet form" --- number unchanged, and the rewritten theorem still supports the gloss
(tensorising constants are blind to the tail event); confirm at XX's turn. Nothing else
cites XVI.

**Paper XVII — reviewed line by line (4 September 2026); the headline results (periodic
flow, never $\mathrm{III}_1$, the factor recovers $\beta d_S\log q$, unconditional
uniqueness on $(0,1]$, sieve-free closed phase) all stand, but the symmetry group as
defined was not compact, the uniqueness theorem rested on a class group defined backwards
relative to [Main], the Weil--Chebotarev bound had a wrong uniform constant and dropped the
mixed characters, and one numerical value was a truncation off by one term; citations
brought to policy. No renumbering (Prop 1.1 – Rem 6.3).**
`papers/XVII-function-fields/` (6 pp, 0/0/0/0; was 5 pp).

1. *The symmetry group needed a compactification convention.* For $S=\cP_K$ the degree map
   gives $\mathbb I_S/\overline{K^\times_S}$ a quotient $\Z$ ($K^\times$ is discrete and
   closed in the ideles of a function field), so the group as written is not compact,
   whereas [Main]'s framework requires a compact $G_S$. A convention paragraph now fixes
   $G_S$ as the profinite completion in the degree direction (the standard choice for
   function-field Bost--Connes systems); $\widehat{G_S}$ is then torsion, and the
   constant-field characters are exactly $\zeta^{\deg}$ with $\zeta$ a root of unity ---
   which is what Rem 5.3 was already tacitly assuming, and what makes the character
   dichotomy of Thm 5.4 exhaustive.
2. *Theorem 5.4 rewritten.* It defined $\Cl_S:=\Cl(C)/\langle[P]:P\in\cP_K\rangle$ --- a
   quotient, trivially $0$ since every divisor is a sum of points --- and concluded
   "$h_S=1$, no permanent obstruction [Main, §4.1]". Main's $\Cl^+_S$ is the \emph{subgroup
   generated} by the classes of $S$ (for $S=P_K$ the full class group), and its characters
   are the obstruction candidates; the quotient being zero says nothing. The theorem now
   states the correct fact with the correct mechanism: for every nontrivial
   $\chi\in\widehat{G_S}$ the detecting series diverges on $(0,1]$ --- via
   $\sum_{\deg P=n}|1-\chi(\Frob_P)|^2=2a_n-2\operatorname{Re}\sum\chi(\Frob_P)\ge a_n$ for
   $n$ large when $\chi$ is nontrivial on the geometric part (Prop 5.1), and via Rem 5.3
   for constant-field $\chi$ --- so $\Xi_\beta=\{1\}$, with the added statement that the
   $\operatorname{Pic}(C)$-characters (the analogue of Main §4.1's class-group characters)
   have detecting sets of \emph{positive density}: the permanent unramified obstruction has
   no analogue at $S=\cP_K$. Applicability of [Main, Thm 3.9] (number verified: the
   Chebotarev-criterion theorem) noted: its Kakutani--martingale proof uses only the product
   structure. Abstract and dictionary row adjusted accordingly.
3. *Proposition 5.1 corrected twice.* (i) Its constant: the claim
   $|\sum_{\deg P=n}\chi(\Frob_P)|\le B_\chi q^{n/2}/n+2q^{n/2}/n$ for all $n\ge1$ fails
   for small $n$ and large genus (the lower-degree terms are bounded by
   $\#C(\F_{q^m})\le q^m{+}1{+}2gq^{m/2}$, not $q^m$); the uniform constant is now
   $(4g+4)q^{n/2}/n$, with the honest two-line estimate replacing the "Möbius inversion at
   a cost of $O(q^{n/2})$" gesture. (ii) Its hypothesis: "extension geometric" excluded the
   \emph{mixed} characters $z^{\deg}\chi_0$ (both parts nontrivial), which also fell outside
   Rem 5.3 --- a gap in the case analysis. Now the hypothesis is "does not factor through
   the constant-field tower", with $L(T,\chi)=L(zT,\chi_0)$, same degree and $|\alpha_j|=
   q^{1/2}$, so the two cases of Thm 5.4 are exhaustive over the torsion dual. Rem 5.2's
   critique of the proposed bound ($+(g_L+1)q^{n/2}$ with no $1/n$) unchanged and correct.
4. *Numerics.* Rem 6.2's value at $\beta=0.95$ was $2.939$ = the sum over $n\le199$; for
   the stated range $n\le200$ it is $2.964$ --- corrected. Everything else recomputed and
   exact: all six values of Rem 2.3 (including the $q$-independent $H_{40}=4.28$ at
   $\beta=1$), $1.640/1.493$ in Rem 6.2, and the five Powers parameters of Rem 4.2
   ($0.7071/0.5/0.25/0.0625/0.0370$), plus the ambiguity example $(4,1,1)\sim(2,1,2)$.
5. *Verified correct:* Prop 1.1 (period $2\pi/(d_S\log q)$; F.~K. Schmidt for $d_S=1$ at
   $S=\cP_K$, halving for even-degree sets); Prop 2.1/Cor 2.2 (Weil zeta, $\beta_c=1$);
   Lem 3.1 ($\Gamma_\beta=q^{-\beta d_S\Z}$ discrete); Thm 3.3 (never $\mathrm{III}_1$;
   [Main, Prop 6.1] as the $S(M)$ upper bound, list of cases exhausts Connes'
   classification); Thm 4.1 conditional as stated, with the amenability argument of
   [IX, Lem 1.1] verified (abelian acting group; transfers verbatim) and restated in
   place; Thm 6.1/Rem 6.3 (sieve-free closed phase via [Main, Thm 5.5], number verified).
   [I, Lem 4.1] ("never pairwise commensurable", statement matches verbatim),
   [I, Thm 3.2], [I, Prop 2.2], [I, Thm 4.2], [I, Thm 5.1] all verified by number and
   content ([Prop 2.2] is the \emph{bound} via the extended group; the closing question now
   cites [I, Thm 4.2] for the exact determination, which is what "determining
   $\Sigma_\beta$ exactly" referred to). [XIII, Rem 5.1] verified (Flows on Kirchberg
   algebras). [XV, Prop 1.1] rename executed: "Arveson spectrum" → point spectrum
   $\Sp_p(\sigma)$, per XV's revision.
6. *Citations to policy.* Bibitems `PaperVIII`, `PaperIX`, `PaperXIII`, `PaperXV` removed
   (numerals throughout, facts restated); Rosen, Stichtenoth, Weil were in the bibliography
   but never cited --- now cited (F.~K. Schmidt; the conductor--degree formula; the
   Riemann hypothesis for curves). Bibliography: five entries, each cited; [Main] and
   [SeriesI] by DOI.

*Consequences for other papers.* All item numbers unchanged. **XVIII** cites [XVII, §7]
(the withdrawn suggestion --- fine), [XVII, Cor 2.2] and [XVII, Prop 1.1] (numbers and
content unchanged; its "$\Sp(\sigma)$" wording to become $\Sp_p$ at its turn, together with
its two [XV, Prop 1.1] citations already flagged). **XX** (l. 275) cites [XVII, Thm 4.1]
--- unchanged, still conditional as before, gloss compatible. **XXIV** (l. 166) cites
"[XVII, Prop.~6.2]", which does not exist --- XVII's 6.2 is the numerical-check Remark;
this dangling reference joins XXIV's revision queue. **XIX** carries a `PaperXVII` bibitem
that its text never cites; to be handled at XIX's turn.

**Paper XVIII — reviewed line by line (4 September 2026); the withdrawal (no compact-group
advantage), the degeneration argument, the cyclic-module computation and the
thermodynamic reconstruction are all correct — the reconstruction's numerics are exact to
the last digit — but the paper misquoted Paper II's affine system (additive part $\cO_S$
instead of $\cO_K$, the very choice II's Remark 6.1 rejects), cited II's class-number
$K$-theory under the wrong number, left its two Takai/Rokhlin propositions resting on bare
assertion, and used the withdrawn "Arveson spectrum" name; citations brought to policy. No
renumbering (Prop 1.1 – Rem 4.4).**
`papers/XVIII-equivariant-kirchberg/` (5 pp, 0/0/0/0; page count unchanged; `\raggedbottom`
added per XIV/XXVIII precedent).

1. *Proposition 1.1 restated on the correct definition.* It quoted the affine system as
   "$C(\widehat{\cO_S})\rtimes(\cO_S\rtimes J_S)$ of [II, §6]" — but II's §6 defines
   $\cA^{\mathrm{aff}}=C(\widehat{\cO_S})\rtimes(\cO_K\rtimes J_S)$, and its Remark 6.1
   explicitly rejects the $S$-integers for exactly the pole reason. The degeneration
   conclusion survives and becomes cleaner: the function-field counterpart of $\cO_K$
   (everywhere-integral elements) at $S=\cP_K$ is $H^0(C,\cO_C)=\F_q$, finite, so no
   infinite additive group acts densely. Corollary 1.2 now also says *why* one omitted
   place suffices: $A=\cO_{\cP_K\setminus\{\infty\}}$ is dense in $\widehat{\cO_S}$ by
   strong approximation, whose hypothesis (one place omitted) is precisely the choice of
   $\infty$. Abstract aligned.
2. *Proposition 2.1's stable finiteness proved rather than asserted.* The old proof was
   "$\cA\rtimes\T$ is the stabilized fixed-point algebra ... already $\cO_n\rtimes\T$ is
   AF". Now: the gauge action is saturated, so $\cA\rtimes\T$ is stably isomorphic to the
   core $F$; on $F$ the state $\lambda\circ E$ (Haar composed with the canonical
   expectation) is a faithful trace, traciality reducing to the self-similarity
   $\lambda(\pi_DU+b)=\Ns(D)^{-1}\lambda(U)$ of Haar measure against the $\Ns(D)$ cosets;
   a unital algebra with a faithful trace is stably finite. Takai and Gabe--Szab\'o now
   carry their citations (both bibitems existed but were never cited).
3. *Proposition 2.2 made attributable:* the approximate-representability statement is
   Izumi's, for the restrictions of gauge actions to finite cyclic subgroups; \cite{Izumi}
   (previously uncited) now cited twice, and the claim scoped accordingly.
4. *Remark 3.3's citation corrected:* it cited "[II, Thm 3.1]" for "$K_0$ involves the
   class group" — II's Theorem 3.1 is now "The tight quotient is abelian-by-finite"; the
   class-number statement is **Theorem 3.3** ("The class of the unit records $h^+_S$").
   Reference and gloss fixed; the function-field counterpart
   ($|\Pic^0(C)(\F_q)|=P(1)$) unchanged and correct ($h=P(1)$).
5. *Proposition 3.1's B\'ezout step justified:* $x=qt$ is not a unit of $\Z[t,t^{-1}]$, but
   it becomes one modulo each relation $1-x^{\deg P}$, which is what lets the exponents
   combine to $\gcd$; one clause added. The relation $(1-(qt)^{\deg P})[1]=0$ from the
   $q^{\deg P}$ weighted Cuntz--Li cosets verified; the module
   $\Z[t,t^{-1}]/(1-(qt)^{d_S})$ records exactly $q^{d_S}$ — Cor 3.2's scope (the cyclic
   submodule of $[1]$) is stated correctly.
6. *Verified correct, with all numerics exact:* Thm 4.1 ($Z_C(q^{-\beta})$ as partition
   function; $J_{\cP_K}=\mathrm{Div}_+$; graded Fock dimension); Thm 4.2 (rational $Z_C$
   from its values, $P(T)$, $g$, all point counts, $|\Jac|=P(1)$); Example 4.3 — all
   fifteen $b_n$, all twelve point counts and the three Jacobian orders recomputed from
   $P(T)=1-aT+qT^2$ and exact ($b_n=c_n-ac_{n-1}+qc_{n-2}$, $c_n=(q^{n+1}-1)/(q-1)$;
   Hasse bounds satisfied, all three $(q,a)$ ordinary hence realizable); the affine
   partition function $Z_C(T)(1-T^{\deg\infty})$; and the third closing question's premise
   (same zeta, non-isomorphic Jacobians exist) — true by Tate isogeny + known examples.
7. *Citations to policy.* "Arveson spectrum" → point spectrum $\Sp_p(\sigma)$ at both
   flagged sites (abstract and Cor 3.2), with [XV, Prop 1.1] as numeral; Thm 4.2's proof
   now sources $q$ correctly ([XV, Prop 1.1] via [XVII, Rem 4.3]; $d_S=1$ by Schmidt via
   [XVII, Prop 1.1] — the old text hung both on XVII Prop 1.1 alone). Bibitems `SeriesII`,
   `SeriesIII`, `PaperIX`, `PaperXIII`, `PaperXV`, `PaperXVII` removed (numerals; numbers
   verified: [III, Cor 2.4] "Where the $\beta$-dependence sits", [III, Prop 3.1] "KMS
   states do not act on $K_0$", [II, Rem 4.5] "$K$-theory carries no arithmetic",
   [IX, Thm 2.1], [XIII, Rem 5.1], [XVII, Cor 2.2/§7]); `Rosen`, `Takai`, `GabeSzabo`,
   `Izumi` were in the bibliography but never cited — now cited; `Main` added and cited in
   the new framework sentence at the head of §1. Bibliography: five entries, each cited.

*Consequences for other papers.* All item numbers unchanged. **XIX** cites
[XVIII, Thm 4.1] twice (numbers and content unchanged), [XVIII, §5] (the third question,
still there verbatim), and `PaperXVIII` bare — all compatible; its own citation-policy
conversion happens at its turn, where its uncited `PaperXVII` bibitem is also queued.

**Paper XIX — reviewed line by line (4 September 2026); the filtration, the torsion
identity and the two-tier picture are correct and the elliptic-curve table is exact to the
last entry, but the disambiguation theorem's proof had a real gap — "induces an isomorphism
of the pairs $(G,U)$" does not follow, since an equivariant homeomorphism of Cantor spaces
carries no group structure — and its gauge hypothesis conflated the circle with the full
gauge torus; both repaired via the deep stratum (the Picard torsor of the title, which the
old proof never used); citations brought to policy. No renumbering (Prop 1.1 – Rem 4.3).**
`papers/XIX-isogeny/` (5 pp, 0/0/0/0; was 4 pp with 1 baseline underfull, now cleared;
`\raggedbottom` added per precedent).

1. *Theorem 3.1(2) rewritten.* (i) Hypothesis: the displayed non-isomorphism was of
   $(\cA,\T,\sigma)$ "as gauge-equivariant systems" with $\T$ the circle — but
   circle-equivariance is the same as $\sigma$-equivariance and does not feed
   [XIV, Thm 4.2], which needs the \emph{full} gauge action (dual of the grading group);
   the statement now says so, referencing [XIV, Def 4.1] (number verified), with the circle
   of Paper XVIII and $\sigma$ as its quotients. (ii) Proof: the old argument jumped from a
   $\theta$-equivariant homeomorphism $Y_1\cong Y_2$ to "an isomorphism of the pairs
   $(G,U)$" — unavailable: as spaces everything in sight is a Cantor set (and $|\Jac|$ is
   already matched by the zeta function, so a space-level invariant sees nothing). The
   repaired proof goes through the canonical \emph{deep stratum}
   $Y_\infty=\bigcap_D DY_S=\{[x,g]:x=0\}\cong G_{\cP_K}/\overline{U_S}$ — the Picard
   torsor — on which $J_S$ acts by the translations $\sigma_D$, running through the
   effective classes, dense in $\widehat{\Pic(C)}$; the closure of the translation monoid
   in $\mathrm{Homeo}(Y_\infty)$ is a compact group acting simply transitively (a closed
   subsemigroup of a compact group is a subgroup) and is the compactified Picard group with
   its topology and group structure; $h$ intertwines the monoids, hence the closures, hence
   gives a topological group isomorphism, and torsion subgroups give the Jacobians. A note
   records that the verbatim transfer of [XIV, Thm 4.2] to function fields is legitimate
   (its revised proof uses only the \'etale groupoid and the freeness of the grading
   monoid). Tier 2 of Thm 4.1, Cor 2.2's gloss and the closing prose aligned (the system
   canonically supplies the quotient group $G/\overline{U}$ with structure, which is what
   Thm 2.1 needs — not the pair as such).
2. *Remark 3.2 sharpened:* [XIV, Def 1.2] (relation lattice; number verified as `def:L`),
   [XIII, Thm 1.4] ("The Cartan subalgebra is the fixed-point algebra"; number verified),
   both as numerals; added the scope sentence that circle-equivariance alone is
   $\sigma$-equivariance and does not suffice for the route used.
3. *Example 3.3 verified by full enumeration:* all six rows recomputed over $\F_p$ by brute
   force (all $y^2=x^3+ax+b$, group structure via maximal point order) — the listed
   structures occur and no others, for every row; admissibility ($m\mid\gcd(N,p-1)$, Hasse
   bounds) checked. Prop 1.1 (two-step filtration; $K^\times\cap U_S=\F_q^\times$ = the
   constants; $\Idl^0_K/K^\times$ compact), Rem 1.2 (Jacobian is a quotient of the compact
   part, not a subgroup — the proposed sequence is indeed wrong), Thm 2.1
   ($G/\overline{U_S}\cong\widehat{\Pic(C)}\cong\hZ\times\Jac(\F_q)$; Schmidt splitting;
   torsion of $\hZ\times F$ is $F$) all verified correct. Rem 4.2's
   Onabe/Angelakis--Stevenhagen claim verified and now cited \cite{AS}.
4. *Coherence with the revised XVII:* §1 now states the framework sentence, including
   XVII's §1 profinite-completion convention for $G_{\cP_K}$ — which Prop 1.1's proof
   ("image after profinite completion is $\hZ$") was already tacitly using.
5. *Citations to policy.* Abstract's "[XIII, Thm 2.1]" → Theorem 2.5 (XIII's renumbering);
   bibitems `PaperXIII`, `PaperXIV`, `PaperXVII` (previously uncited — flagged at XVII's
   turn), `PaperXVIII` removed, numerals throughout ([XVIII, Thm 4.1/§5] verified current);
   `AS`, `Howe`, `Rosen`, `Tate` were all in the bibliography but never cited — now cited
   (Angelakis--Stevenhagen at Rem 4.2; Howe at Rem 4.3's polarization gap; Rosen at
   Schmidt; Tate twice, at Ex 3.3 and Tier 1); `Main` added and cited in the framework
   sentence. Bibliography: five entries, each cited.

*Consequences for other papers.* All item numbers unchanged. **XX** cites [XIX, Thm 2.1]
(unchanged) and [XIX, Thm 4.1] (number unchanged; content compatible), but its l. 68 gloss
"Tier 2 recovers the pair $(G_S,U_S)$" should become "recovers the compactified Picard
group with its translation structure" at XX's turn — the revised Tier 2 no longer claims
the pair as such. Nothing else cites XIX.

**Paper XX — reviewed line by line (4 September 2026); the CM twin construction, the torsor
diagnosis and the master statement all stand, every numeric verified (with two corrections:
the enumeration range and one garbled bibitem), and the paper's key empirical claim — that
the point-to-Picard profiles agree across twins — is upgraded from a numerical check to a
theorem; the three flags accumulated against this paper (XIV's conditional Frobenius, XVI's
rewritten Thm 4.1, XIX's revised Tier 2) are all resolved. No renumbering
(Thm 1.1 – Thm 4.1).**
`papers/XX-twin-curves/` (5 pp, 0/0/0/0; `\raggedbottom` added per precedent).

1. *Flag 1 resolved — the [XIV, Thm 4.2] Frobenius citation removed.* Rem 2.2 derived the
   map $P\mapsto[P]$ from "the Frobenius classes recovered by [XIV, Thm 4.2]" — but in the
   revised XIV that Frobenius clause is the \emph{conditional} part (6), and XX's use must
   not rest on it. It now rests on the unconditional mechanism of the revised XIX: the
   deep-stratum translation structure ($P$ acts on the Picard torsor by $\sigma_P$,
   degree-labelled), recovered in [XIX, Thm 3.1]'s proof. XIV is no longer cited anywhere
   in XX. Flags 2 and 3 also cleared: the [XVI, Thm 4.1] gloss ("did not fail for lack of a
   better Dirichlet form") is compatible with the rewritten XVI theorem and kept as a
   numeral; all Tier-2 glosses ("recovers the pair $(G_S,U_S)$") updated to the revised
   XIX formulation (compactified Picard group with translation structure), in the abstract,
   Rem 2.2 and Thm 4.1.
2. *Theorem 2.1 strengthened — the profile agreement is now proved.* The old Tier-2 clause
   gave only the module tower, and Rem 2.2 admitted the point-to-Picard map "is what would
   have to be checked", with Rem 2.3 checking degree $\le2$ numerically. In fact it is a
   theorem: under Lenstra's identification, the class of a degree-$n$ point
   $\{Q,\dots,\phi^{n-1}Q\}$ is $\nu_n\cdot Q$ with $\nu_n=(\phi^n-1)/(\phi-1)$, and
   $E(\F_q)=\ker(\phi-1)=\nu_n\cdot\cO/(\phi^n-1)$, so the degree-$n$ multiset of point
   classes is the $\nu_n$-image of the exact-degree-$n$ elements — a formula in
   $(\cO,\phi)$ alone. Thm 2.1(2) now ends with this clause, the proof carries the
   argument, and Rem 2.3 is reframed as numerical confirmation, additionally covering two
   supersingular classes outside the ordinary hypothesis (now said explicitly — the old
   "twins of Example 1.3" misdescribed the $(11,0)$ and $(17,0)$ rows, which are
   supersingular and not in that table).
3. *Numerics verified by full enumeration, one correction.* All six rows of Ex 1.3's table
   exact ($j$-sets $\{1,17\},\{4,6\},\{1,6\},\{9,17\},\{3,7,17\},\{14,18,20,22\}$;
   discriminants $t^2-4p=-88,-48,-32,-60,-100,-56$; class numbers
   $h(-88){=}h(-48){=}h(-32){=}h(-60){=}h(-100){=}2$ with the $-100$ row's "two orders"
   reading ($h(-4){=}1$ maximal order giving the third $j$) consistent; the blank cell
   filled with $h(-56)=4$ against four $j$'s). The headline count: the paper's $69$ is the
   count for $11\le p\le29$ — over "all $p\le29$" it is $72$ ($p=7$ contributes $3$) — so
   the stated range is corrected to $11\le p\le29$, under which $69$ is exact. All eight
   degree-two profiles of Rem 2.3 recomputed in $\F_{p^2}$ and exact:
   $(6^6,5^6)$ twice, $(9^9,8^9)$ twice, $(8^6,7^6)$ for $j=4,6$ and $(8^9,6^3)$ for
   $j=0,11$, the split tracking the group structure as claimed.
4. *Statement hygiene.* Thm 1.1(2): "$\bar\F_q$-isomorphism classes" → $\F_q$-isomorphism
   classes, equivalently $j$-invariants (the quadratic twist has trace $-t\ne t$ for
   ordinary $E$ — over $\bar\F_q$ the classes are the $j$'s anyway, but the torsor
   statement is the $\F_q$-one). Proof attributions fixed: the module isomorphism (1) is
   Lenstra's theorem (bibitem added, cited), not "Deuring in the form given by Waterhouse";
   Waterhouse cited for the kernel-ideal torsor (2), Deuring for the theory. Rem 3.1
   (the Weil-pairing explanation is wrong since $\Gal(\bar\F_q/\F_q)$ is abelian) and
   Thm 3.2 (torsor + trivial action on module invariants; $j$ injective) verified correct.
5. *Citations to policy.* Bibitems `SeriesII`, `PaperIX`, `PaperX`, `PaperXIV`,
   `PaperXVI`, `PaperXVII`, `PaperXVIII`, `PaperXIX` removed (numerals throughout;
   [II, Rem 4.5], [IX, Thm 2.1], [XVI, Thm 4.1], [XVII, Thm 4.1], [XVIII, Thm 4.1],
   [XIX, Thm 2.1/3.1/4.1] all verified current). The `Howe` bibitem had a second author's
   title spliced in ("Constructing distinguished representations of simple Lie groups" —
   not Howe's paper); corrected to the single genuine reference. `Deuring`, `Howe`,
   `Lauter`, `Waterhouse` were in the bibliography but never cited — now cited; `Lenstra`
   and `Main` added and cited (framework sentence at the head of §1). Bibliography: six
   entries, each cited.

*Consequences for other papers.* All item numbers unchanged. Nothing cites XX. This closes
the function-field arc XVII–XX with all cross-references verified against the reviewed
versions.

**Paper XXI — reviewed line by line (4 September 2026); the headline gap theorem, the
$L$-dictionary correction and both structural remarks stand, and every numeric is exact,
but the Solomon-zeta proposition's proof computed the wrong count (double cosets instead of
sublattices — the erroneous count would even have erased the shift the paper is about), one
companion reference was dangling, the unit group was misidentified, and the boundary case
of the range theorem was overstated; citations brought to policy. No renumbering
(Prop 1.1 – Rem 4.2).**
`papers/XXI-GL2/` (5 pp, 0/0/0/0; `\raggedbottom` added per precedent).

1. *Proposition 1.2's proof corrected — a material error.* It derived the local factor by
   "summing $p^{-\beta(a+b)}$ over elementary divisors $0\le a\le b$", i.e. over
   $GL_2(\Z_p)$-*double* cosets; that sum is $((1-x)(1-x^2))^{-1}$, not the displayed
   $((1-x)(1-px))^{-1}$, and its abscissa would be $\beta_c(S)$ — no shift, contradicting
   the paper's own main theorem. The correct count is one term per *left* coset,
   equivalently per sublattice of $\Z_p^2$, as in the Connes–Marcolli Hecke picture
   (now cited): $\sigma(p^n)=1+p+\cdots+p^n$ sublattices of index $p^n$, and
   $\sum_n\sigma(p^n)p^{-\beta n}=((1-p^{-\beta})(1-p^{1-\beta}))^{-1}$, verified in closed
   form. This also aligns the proof with Rem 3.5's "$p+1$ sublattices of index $p$", which
   was already the correct picture.
2. *Dangling companion reference:* "[X, Prop. 4.1]" (twice: abstract and Prop 1.1's proof)
   — Paper X has no 4.1; the unit-group exclusion ("a norm is $1$ on units, so an infinite
   unit group makes $\zeta_P$ diverge identically") is X's **Remark 1.5**, verified
   verbatim. Both occurrences now point there.
3. *Unit group corrected:* $P^\times$ for $P=M_2(\Z)\cap GL_2^+(\Q)$ is $SL_2(\Z)$, not
   $GL_2(\Z)$ (a unit has positive integral determinant on both sides, hence $\det=1$);
   the one-line argument is now in the statement. Infinitude, and the conclusion, are
   unchanged. (Paper X's own prose has the same $GL_n(\Z)$ slip in passing; harmless there
   — only infinitude is used — and X's turn is past.)
4. *Theorem 3.2(2)'s "if and only if" refined at the boundary:* at $\beta=1+\beta_c(S)$
   the partition function is finite exactly when the critical series
   $\sum p^{-\beta_c}$ converges (e.g. Brun-summable $S$), which the old strict
   "iff $\beta>1+\beta_c$" missed; the consequent display now reads
   $(0,\beta_c]\cap[1+\beta_c,\infty)=\emptyset$ with the width-one open interval
   $(\beta_c,1+\beta_c)$ in neither region — the gap statement is unchanged and, for
   $S=P_\Q$ (critical series divergent), so are the endpoints $(0,1]$ vs $(2,\infty)$.
5. *Verified correct, all numerics exact:* Lem 2.1 (HS identity, both forms; [VI, Lem 2.2]
   "Trace form" verified); Thm 2.2 ($\Xi_\beta=4\log\zeta_S-2\Re\log L_S+O(1)$,
   prime-power tails at $\beta>1/2$; [VI, Thm 4.1] "Euler dictionary" verified,
   $2n\log\zeta-2\Re\log L$ at $n=2$); Rem 2.3 (the $\Sym^2$ term is quadratic in
   $\Tr U_p$, hence spurious; Rankin–Selberg = second moment); Cor 2.4 (Jacquet–Shalika,
   now cited); Thm 4.1's block construction ($8\sin^2(\theta/2)\le2\theta^2$; blocks with
   $\sum p^{-1}\in[1,2]$ exist since the Sato–Tate set has divergent prime-harmonic sum;
   [VI, Thm 5.3] verified); Rem 4.2 ([VI, Rem 5.4] verified; $\beta_c(S_\Delta)=1$);
   Rem 3.4's six numerics recomputed exactly ($\sum_{p\le10^6}p^{-\beta}=4.79/2.89/1.99$;
   $\zeta(\beta)\zeta(\beta-1)=8.33/1.98/1.30$); §5's two escape routes ([X, Prop 1.4]
   "Norms factor through the abelianization" and [VI, §6] "The algebra is not constructed"
   both verified by number and title).
6. *Citations to policy.* Bibitems `PaperVI`, `PaperX`, `PaperXII` removed (numerals
   throughout; [XII, Thm 1.2] "Universal multiplicity–norm mismatch" verified); `CM`,
   `Deligne`, `BLGHT`, `JS`, `Solomon` were all in the bibliography but never cited — now
   cited (Hecke quotient and sublattice sum; unitarity; Sato–Tate for $\Delta$;
   non-vanishing at $\Re s=1$; the Solomon zeta); `Main` added and cited in the new
   framework sentence at the head of §1. Bibliography: six entries, each cited.

*Consequences for other papers.* All item numbers unchanged. **XXII**, **XXIII**, **XXIV**
and **XXV** carry `PaperXXI` citations, to be verified at their turns; note for XXIV that
its dangling "[XXI, Prop. 6.2]" (already queued) cannot simply be renumbered — XXI has no
§6 — and must be re-targeted, most plausibly to [XXI, Prop 1.2] or [XXI, Thm 3.2].

**Paper XXII — reviewed line by line (4 September 2026); the four obstructions (no
positivity, dynamics undefined at $p$, no $p$-adic abscissa, no characteristic-ideal
identity) all stand, but the fourth rested on a false quantitative lemma — "a sum of $g$
binomials has bounded $\lambda$" fails by cancellation — and is now proved by two robust
arguments instead; two companion references were dangling or mis-numbered, one companion
gloss inverted the cited paper's conclusion, and the ordering argument over $\Q_p$ was
garbled; citations brought to policy. No renumbering (Prop 1.1 – Rem 5.4).**
`papers/XXII-iwasawa/` (5 pp, 0/0/0/0; `\raggedbottom` added per precedent).

1. *Proposition 4.1 rewritten — its argument was false.* It claimed each summand of
   $\Xi_p=\sum_1^g(1-\chi_iu_i^z)$ has "$\lambda$-invariant bounded in terms of $g$ alone",
   hence bounded degree against the unbounded $\lambda_p(K)$. But $\lambda$ is not
   controlled under sums: already
   $(1+T)^{c'}-(1+T)^c=(1+T)^c((1+T)^{c'-c}-1)$ has $\lambda=p^{v_p(c'-c)}$, unbounded ---
   two binomials suffice. The conclusion (no identity $(\Xi_p)=\chr_\Lambda(X)$) is
   correct and now proved robustly: (i) for $K=\Q$ and $\chi(p)\ne1$ of order prime to $p$
   the element is a \emph{unit} of $\Lambda\otimes\Z_p[\chi]$ (its value has absolute value
   $1$ on the open disc), generating the unit ideal, while the characteristic ideal is
   proper whenever $\lambda_\chi+\mu_\chi>0$; (ii) the element depends only on the
   decomposition data of $p$ and the $\chi(\Frob_{\pp_i})$ --- finitely many $p$-adic
   parameters --- which cannot determine the Iwasawa module of the tower. The false
   quantitative claim is recorded and refuted in the proposition itself. \cite{MazurWiles}
   now cited for the main conjecture. Table row updated ("wrong dependence").
2. *Dangling/mis-numbered companion references.* "[X, Thm 3.1]" (Rem 5.2) and
   "[X, Prop 4.1]" (§6 prose) --- Paper X has neither; both facts (finite generation ⟹
   finite obstruction sum ⟹ $\Xi_\beta$ constant; infinite unit group ⟹ $\zeta_P\equiv
   \infty$) live in X's **Remark 1.5**, verified verbatim (the same dangling
   "[X, Prop 4.1]" pattern as in XXI). "[VIII, Thm 3.2]" — that is the Gauss linking
   matrix formula; worse, the gloss "the units were identified as the carrier of the
   thermodynamics" \emph{inverts} VIII's conclusion: VIII's Theorem 6.1 shows the inertia
   model, built on the meridian direction matched to the global units, has \emph{no}
   thermodynamics (moral in its Remark 6.3: inertia local and inert, Frobenius global).
   The §6 sentence now states VIII's actual result, with correct numerals — the "units
   recur" point survives in the corrected form. "[XXI, §6]" — XXI has no §6; the
   coefficient-system suggestion is XXI's §5 closing prose, itself pointing at
   [VI, §6]; re-targeted accordingly.
3. *Leopoldt citations completed:* the Leopoldt-type clause is [II, Rem 2.3] ("The general
   case, and why it does not matter here": "We do not decide it. Nothing below depends on
   it"), not [II, Prop 2.2] alone; Prop 5.3, Rem 5.4, abstract and table now cite
   Proposition 2.2 \emph{and} Remark 2.3, and Rem 5.4's independence claim is anchored at
   [II, Thm 2.5] (Topological principality) — all numbers verified against the reviewed
   II. Rank formula $r_2+1+\delta_p$ cited to \cite{Washington}.
4. *Smaller repairs.* Prop 1.1's ordering argument fixed: $\Cp$ is algebraically closed so
   $-1=i^2$ is a square; and already $\Q_p$ is non-orderable with level $1,2,4$ (the old
   "$-1$ is a sum of squares in $\Q_p$ for $p\equiv1$ (4) and in $\Q_p(\sqrt u)$
   otherwise" was both incomplete and beside the point — no field extension is needed).
   Thm 3.1's quantifier fixed ($u^z$ is defined on $\Z_p$ and on the disc
   $|z|_p<p^{(p-2)/(p-1)}$, not "for every $z\in\Cp$"), and the weighted series retyped
   $p$-adically ($w_\qq$ with $|w_\qq|_p=1$, e.g.\ $1-\chi(\Frob_\qq)$ of order prime to
   $p$ — the old "$|1-\chi(\Frob_\qq)|^2$" mixed archimedean absolute values into a
   $p$-adic series). Rem 4.2 enriched with the genuine residue theorem (Colmez at $s=1$,
   which sees $R_p(K)$, not $\mu$) — \cite{Colmez} thereby cited.
5. *Verified correct:* Cor 1.2, Rem 1.3 (Gibbs $\leftrightarrow$ measure, equilibrium
   characterization lost); Prop 2.1 ($\Ns\pp=p^f\notin\Z_p^\times$); Rem 2.2's
   interpolation formula (Euler factors at $p$ removed — standard, now cited
   \cite{Washington}); Thm 3.1's core (all terms of absolute value $1$; non-archimedean
   convergence criterion); Cor 3.2 (with Paper IV as numeral); Prop 5.1 (partition
   function = interpolation factor — exact); Rem 5.2's logic (finite $S$: $\beta_c=0$,
   $\Xi_\beta$ full for all $\beta$); Prop 5.3's rank formula.
6. *Citations to policy.* Bibitems `SeriesII`, `SeriesIII`, `SeriesIV`, `PaperVIII`,
   `PaperX`, `PaperXXI` removed (numerals throughout); `Colmez`, `FW`, `Iwasawa`,
   `MazurWiles`, `Washington` were all in the bibliography but never cited — now cited;
   [Main] and [SeriesI] kept by DOI (both cited). A policy sentence added at the head of
   §1. Bibliography: seven entries, each cited.

*Consequences for other papers.* All item numbers unchanged. **XXIII** cites
[XXII, Prop 2.1] and [XXII, Prop 5.3] — both numbers and contents unchanged — plus
`PaperXXII` bare; to be converted at its turn.

**Paper XXIII — reviewed line by line (5 September 2026); §§2–3 (the vanishing
$\cL$-invariant, the dimension-not-volume correction) are sound, but §1 computed the wrong
group: the object it called "the isotropy" is the divisor-zero \emph{kernel}, which maps to
the identity ideal — the actual isotropy of [II, Prop 2.2] is the divisor image, now
identified exactly, and the corrected result is \emph{stronger}: intermediate isotropy is
nontrivial already for real quadratic fields, unconditionally; the numerical table was
wrong in its headline column; citations brought to policy. No renumbering
(Prop 1.1 – Cor 3.4).**
`papers/XXIII-leopoldt/` (5 pp, 0/0/0/0; `\raggedbottom` and the missing `\Idl` macro
added).

1. *§1 rewritten around the correct object.* [II, Prop 2.2] (verified verbatim) gives
   $\Iso(y)=\mathrm{div}(\overline{K^\times_{S,+}}\cap\Idl_T)$ — the \emph{divisor image}.
   The paper instead analyzed $\overline{\cO^\times_{K,+}}\cap\prod_{T}\cO_\pp^\times$,
   which is the \emph{kernel} of the divisor map on that intersection and contributes only
   the identity ideal. The new Theorem 1.2 identifies the isotropy exactly:
   $\Iso(Y_T)\cong\ker(\varphi:L_T\to U_{T^c}/\pi_{T^c}(\overline{\cO^\times_{K,+}}))$,
   with $L_T$ the rank-$|T|$ lattice of $T$-supported principal divisors (totally positive
   generators), $\varphi(a)=\alpha_a|_{T^c}$; both inclusions are proved, the key point
   being that $\pi_{T^c}(\overline{\cO^\times_{K,+}})$ is compact hence closed.
   Consequences: (i) finite unit group ⟹ trivial isotropy (recovering II's unconditional
   case via $K\hookrightarrow K_{\pp'}$); (ii) $r\ge1$ and $d_{T^c}=1$ ⟹ the image of
   $\pi_{T^c}$ is \emph{open} (a single coordinate of an infinite-order unit has nonzero
   logarithm, and a nonzero $\Z_p$-multiple of it is open), the quotient finite, and
   $\Iso(Y_T)$ of \emph{full rank} $|T|$ — so already real quadratic, $p$ split, gives
   infinite intermediate isotropy, unconditionally, and totally real degree $n$ gives rank
   $n-1$ (the old conditional "$n-2$ under Leopoldt + maximal rank" is superseded). The
   proposed equivalence "Leopoldt $\iff$ trivial isotropy" is thus false for a sharper
   reason: triviality tracks finiteness of the unit group, and Leopoldt enters only as the
   budget $\rank\pi_{T^c}\le r-\delta_p$.
2. *Proposition 1.1 kept as the honest kernel/projection-rank computation* (its
   rank-nullity argument was correct as far as it went), retitled, with the automatic
   $\rank\pi_{T^c}\ge1$ observation added and an explicit warning that the kernel is not
   the isotropy. Rem 1.3's table redone with both columns (kernel rank vs the true
   $\rank\Iso=|T|$): the old "real quadratic: rank 0" row was wrong for the isotropy.
   Rem 1.5 reframed: for $d_{T^c}\ge2$ finiteness of the quotient needs \emph{open} image
   (relative nondegeneracy), automatic for $d_{T^c}=1$; a positive Leopoldt defect can
   only lower the projection rank. Rem 1.4's principality independence re-anchored at
   [II, Thm 2.5]. Abstract and assessment table/closing question aligned.
3. *§2 verified with small fixes:* Prop 2.1's order-$g$ vanishing and leading coefficient
   $(\log p)^g\prod f_\pp$ exact (numerics $2.5903$, $4.1689$ recomputed ✓); Thm 2.2's
   vanishing of $\prod\log_p\Ns\pp$ correct (Iwasawa branch), but "those being nonzero by
   definition" softened to the true state (nonzero in the proved cases — split
   multiplicative $\log_p q_E\ne0$ — conjecturally always), with \cite{MTT,GreenbergSteven}
   now cited; Rem 2.4's exceptional-zero dictionary kept with \cite{MTT}.
4. *§3 verified:* Prop 3.1 (volume vacuous on compact groups) and Thm 3.2
   ($\dim=r_2+1+\delta_p$, as $p$-adic analytic groups; the arithmetic
   $r_1+2r_2-(r_1+r_2-1)$ checks) correct; Ex 3.3's six cases check; Cor 3.4's agreement
   with [XXII, Prop 5.3] (number and content unchanged by XXII's review) verified.
5. *Citations to policy.* Bibitems `SeriesII` and `PaperXXII` removed (numerals
   throughout); `Brumer`, `GreenbergSteven`, `MTT`, `Washington` were all in the
   bibliography but never cited — now cited (Baker–Brumer for abelian Leopoldt; the
   $\cL$-invariant literature; the closed-unit rank); `Main` cited in the new framework
   sentence. Bibliography: five entries, each cited.

*Consequences for other papers.* All item numbers unchanged, but **Theorem 1.2's content
changed materially** (exact identification and unconditional nontriviality, superseding the
conditional rank formula): nothing downstream cites XXIII, so nothing propagates.

**Paper XXIV — reviewed line by line (5 September 2026); the long-queued revision executed:
the false four-family obstruction theorem is now the correct two-family theorem with an
explicit anti-obstruction clause, the title/abstract/corollary/moral all follow, the
consequence-for-[Main] remark is reversed from "excluded" to "confirmed", two dangling
companion references are re-sourced to [Main], and three of the seven numerical rows are
corrected (one had the wrong range, one the wrong representation domain, one
irreproducible); citations brought to policy. No renumbering (Prop 1.1 – Rem 3.2).**
`papers/XXIV-sieve/` (5 pp, 0/0/0/0; was 4 pp with 1 baseline underfull, now cleared;
`\raggedbottom` added).

1. *Theorem 2.2 rewritten — the diagnosed false theorem.* The old statement claimed a
   finite detecting set, hence permanent obstruction and never-uniqueness, for FOUR
   families (twin, SG, Landau, FI), arguing "all but finitely many elements of $S$ lie in
   a single residue class" — the fallacy being that confinement obstructs only when the
   occupied class lies in the character's \emph{kernel}. Corrected two-part theorem:
   (1) Landau and Friedlander–Iwaniec occupy the class $1\bmod4$ — the kernel of
   $\chi_4$ — so $D_{\chi_4}$ is finite and the KMS state is never unique
   ([Main, Thm 3.9], [Main, §4.1]); (2) twin and Sophie Germain occupy $2\bmod3$ with
   $\chi_3(2)=-1$, so the detecting set is \emph{cofinite} — full-strength detection —
   and by [Main, Lem 5.6] (admissible classes generate $(\Z/M)^\times$ for every $M$;
   statement verified verbatim) no Dirichlet character obstructs these families at all.
   The Frobenius convention is sourced to [Main, (1.1)] ($|1-\chi(\sigma_p)|=
   |1-\chi(p)|$), replacing the two dangling references "[XVII, Prop 6.2]" and
   "[XXI, Prop 6.2]" (neither exists; both long-flagged).
2. *Everything downstream of the theorem follows:* title ("two families that are never
   unique"), abstract (kernel-condition framing; the "applies to [Main] itself ...
   uniqueness now excluded" paragraph replaced by consistency with [Main, Thm 5.5(5)] +
   Lem 5.6); Cor 2.4 (equidistribution is sufficient but not necessary — twin/SG are
   maximally non-equidistributed yet unobstructed; kernel confinement decides); Rem 2.5
   reversed (SG: no obstruction anywhere, uniqueness in the divergent range conditional
   on [Main, Thm 5.5(2)], full breaking on the closed phase); assessment table (two new
   rows), moral (confinement to the class $1$ vs to a generating class), and the closing
   questions (question 1 is now largely answered by the correction itself: twin/SG/Chen
   all closed-phase and unobstructed; the sharp remaining case is Chen, unconditional via
   Chen's theorem; question 2 re-pointed at Landau).
3. *Lemma 2.1 verified correct and kept unchanged* — all four congruences are true; the
   error was never in the congruences but in their reading.
4. *Numerics recomputed by full enumeration to $2\cdot10^5$.* Verified exact with stated
   conventions: twin 2159 ($p>3$), SG 2056 ($p>3$), Landau 63 (odd), FI 938; all class
   occupancies ($\{2\}$ of $\{1,2\}$; $\{1\}$ of $\{1,3\}$; HB's $\{1,2,7,8\}\bmod9$
   exact, and its generation argument correct). Three corrections: Chen 1110 was the
   count to $2\cdot10^4$ (wrong range) — at $2\cdot10^5$, $p>3$, it is 7523;
   Heath-Brown 623 is not the positive-range count (the range of \cite{HB}) — that is
   289 (623 is close to a $\Z\times\Z$ box count, 632 in our box); Piatetski-Shapiro 498
   is irreproducible — the distinct primes $\lfloor n^{1.1}\rfloor\le2\cdot10^5$ number
   6040. Conventions now stated in the remark. Qualitative claims (both classes occupied
   for Chen/HB/PS) unchanged and verified.
5. *Verified correct:* Prop 1.1 (Abel summation, the $k>1$ criterion, the three-case
   asymptotics at $\beta=\theta$); Thm 1.2's table (all seven $(\theta,k,\beta_c)$ rows;
   proof now carries the five external citations — Brun \cite{HR}, Chen \cite{Chen},
   \cite{FI}, \cite{HB}, Rivat–Sargos \cite{RS} — all previously uncited bibitems);
   Rem 1.3 (dichotomy = second prime condition; [Main, Thm 5.5] verified); Thm 3.1 and
   Rem 3.2 (the unconditional PS interval $(0.8436,1)$; $205/243=0.8436$ ✓).
6. *Citations to policy.* Bibitems `PaperXVII`, `PaperXXI` removed (nothing from either
   paper is used once the convention is sourced to [Main]); the five external bibitems
   were all uncited and are now cited; [Main] by DOI throughout; a no-companion policy
   sentence added at the head of §1. Bibliography: six entries, each cited.

*Consequences for other papers.* All item numbers unchanged, but **Thm 2.2's content is
reversed for twin/SG**. **XXV** cites [XXIV, Prop 1.1] (×3) and [XXIV, Rem 1.3] — numbers
and contents unchanged — but its l. 66 glosses "[XXIV, Thm 2.2], where twin, Sophie
Germain, Landau and [FI are obstructed]": the gloss must become "Landau and
Friedlander–Iwaniec" at XXV's turn. The long-standing XXIV queue (false theorem; two
dangling Prop 6.2 references; two-family revision) is now cleared.

**Paper XXV — reviewed line by line (5 September 2026); all three verdicts (open phase,
no congruence obstruction with uniqueness on $(0,1]$, symmetric powers control only the
constant) stand, and every numeric — the four exact densities, the three empirical
densities, all thirty-six class proportions, the seven Chebyshev coefficients — is exact;
the repairs are the honest error analysis behind the $\zeta_S$ asymptotic, the flagged
update of the [XXIV, Thm 2.2] glosses to the revised two-family version, one off-by-one
prime count, and the $k$-dependence caveat in the interchange remark; citations brought to
policy. No renumbering (Prop 1.1 – Ex 3.4).**
`papers/XXV-sato-tate/` (5 pp, 0/0/0/0; `\raggedbottom` added).

1. *Theorem 1.2's "+O(1)" was stronger than plain Sato–Tate delivers.* From
   $\pi_S=(\delta+o(1))\pi$ alone, partial summation gives only
   $\zeta_S(\beta)=(\delta+o(1))\log\frac1{\beta-1}$ — the error
   $\int x^{-\beta-1}E(x)dx$ with $E=o(x/\log x)$ is $o(\log\frac1{\beta-1})$, not $O(1)$.
   Statement and abstract now carry the two-tier form: the $o(1)$ version
   unconditionally, sharpening to $O(1)$ under any effective Sato–Tate error term
   $E\ll x/\log^{1+\varepsilon}x$ (then $\int x^{-2}|E|<\infty$); the proof carries the
   one-line integration by parts. Nothing downstream used the $O(1)$: uniqueness needs
   only divergence.
2. *Flag cleared — the [XXIV, Thm 2.2] glosses updated to the revised theorem.* The
   abstract's "twin, Sophie Germain, Landau and Friedlander–Iwaniec ... never unique"
   now reads Theorem 2.2(1) (Landau/FI, kernel class) with the twin/SG part (2)
   (generating class, unobstructed) stated as the complementary mechanism; Thm 2.3's
   "in the sense of", Rem 2.4's contrast sentence, Rem 2.5's "obstructed families"
   scoping, and §4's two paragraphs (including "Chen the one candidate" → twin/SG/Chen
   per the revised 2.2(2), Chen unconditional) all aligned. [XXIV, Prop 1.1] (×3) and
   [XXIV, Rem 1.3] verified unchanged and converted to numerals.
3. *Numerics verified by full recomputation on $y^2=x^3+x+1$* ($\Delta=-2^4\cdot31$): the
   exact densities $0.6090/0.0288/0.0775/0.5$ (closed forms check), the empirical
   densities $0.6206/0.0276/0.0766$, the interval sample sizes $167$ and $464$, and all
   thirty-six entries of Rem 2.4's class-proportion table exact to the printed digits.
   One correction: the good-prime count is $6055$ ($\pi(6\cdot10^4)=6057$ minus the bad
   primes $2,31$), not $6054$ — fixed at all three occurrences. Ex 3.4's seven Chebyshev
   coefficients recomputed in closed form and exact (odd ones vanish by symmetry;
   $c_2=-3\sqrt3/4\pi$ etc.).
4. *Remark 3.3 extended:* beyond the non-uniform convergence of the Chebyshev series, the
   individual $O(1)$'s in the expansion are $k$-dependent (prime-power tails
   $\le(k+1)$; $\log L(s,\Sym^kE)$ near $s=1$ grows through the analytic conductor), so
   the series over $k$ converges only through the Beurling–Selberg bracketing; Thm 3.2's
   statement now says the $k$-series is summed by truncation as in that remark.
5. *Verified correct:* Prop 1.1 (the $\mu_{\ST}$ formula); Cor 1.3 (positive density ⟹
   open, [XXIV, Rem 1.3]); Lem 2.1 (det = cyclotomic); Thm 2.2's proof route (open
   image, $U_k\otimes\chi$ characters, Newton–Thorne automorphy, Jacquet–Shalika +
   Shahidi nonvanishing, Wiener–Ikehara); Thm 2.3 (detecting sets of density
   $\delta(1-|\ker|/\varphi(m))>0$, divergence for $\beta\le1$, [Main, Thm 3.9]; full
   breaking above); Prop 3.1's coefficient formulas; Thm 3.2's per-term $O(1)$'s.
6. *Citations to policy.* Bibitems `PaperVI` ([VI, Thm 5.3] verified, numeral) and
   `PaperXXIV` removed; `BLGHT`, `NT`, `Serre`, `Shahidi` were all in the bibliography
   but never cited — now cited — and `JS` added and cited (the proof invoked
   Jacquet–Shalika by name with no entry); [Main] by DOI; policy sentence at the head of
   §1. Bibliography: six entries, each cited.

*Consequences for other papers.* All item numbers unchanged; nothing cites XXV. The
XXIV-related flag raised at XXIV's review is cleared.

**Paper XXVII — reviewed line by line (5 September 2026); the two no-go theorems, the
ordered-cocycle construction, the non-abelian Kakutani theorem, the mixing criterion, the
$S_3$ lift-dependence theorem and the $A_3$ example are all correct — every identity and
estimate was checked, most by direct computation — with exactly one repair: Theorem 4.2's
proof asserted "the ergodic equivariant families are Haar on the fibres" without excluding
other conformal measures within a component; the missing within-component uniqueness
argument is supplied. Citations were already at policy. No renumbering
(Thm 2.1 – Ex 4.10). The renumbering question (XXVII→XXVI) was raised and declined: the
numeral XXVI is retired by the recorded review decision (STATUS ll.713/757/793/1636 — the
Q47 spacing paper was drafted as XXVI and renumbered out), and XXVII is cited by name in
IX (l.394), X (l.360) and XXVIII (l.390).**
`papers/XXVII-nonabelian-groupoids/` (10 pp, 0/0/0/0; page count unchanged).

1. *The one repair — Theorem 4.2's within-component uniqueness.* Multiple mutually
   singular conformal measures for the same cocycle on the same relation is exactly what
   KMS multiplicity \emph{is}, so component-ergodicity alone does not force an equivariant
   family to be Haar on its fibre. Supplied: for nontrivial $\sigma\in\Irr(H)$ the Fourier
   coefficient $B(x)=(\int\sigma^*d\rho'_x)^*$ satisfies $B(y)=\sigma(c')B(x)$, so
   $\Phi(x,h)=\Tr(\sigma(h)^*B(x))$ is skew-product-invariant, hence constant $=0$ (since
   $\int_H\sigma=0$), and Fourier inversion gives $\rho'_x=m_H$. Conclusion of the theorem
   unchanged.
2. *Verified by direct computation:* the expansion
   $m_i^{-*}m_i^{-1}=I+t_i(I-U_i)^*(I-U_i)/(1-t_i)^2$ (both sides equal
   $(I+t^2I-t(U+U^*))/(1-t)^2$); the martingale structure
   ($\E[Z_{n+1}|\cF_{\le n}]=Z_n$; $\E\|Z_n\|^2_{\HS}=\|M_n^{-1}\|^2_{\HS}$ by unitarity of
   $P_n$; the bound $d\exp(\sum t_i\|I-U_i\|^2_{\HS}/(1-t_{\max})^2)$ via
   $\|\cdot\|_{\op}\le\|\cdot\|_{\HS}$); the deterministic increasing $|\det Z_n|$ giving
   invertibility of the limit; $F^*F$ constant by ergodicity and $W=FQ^{-1}$; the
   necessity argument ($C_n=M_{(n,m]}C_m$, $|\det M_{(n,m]}^{-1}|\to\infty$ when
   $\Xi_\beta=\infty$, forcing $\det C_n=0$ against $|\det F|=1$); Theorem 4.6's $S_3$
   estimates exactly ($m_i=Q_i+\lambda_iQ_i^\perp$ with $\lambda_i=(1-t_i)/(1+t_i)$ for a
   reflection; the $60^\circ$ two-case analysis; per-pair contraction
   $1-\min(t_{2k-1},t_{2k})/32$; $\sum_kt_{2k}\ge\frac12\sum_{i\ge2}t_i=\infty$ by
   monotonicity); Example 4.10 ($\|I-\rho((123))\|^2_{\HS}=3+3=6$; $N_\beta=A_3$ rigid;
   Chebotarev density $\frac13$). Also verified: Route B's dilation-trace KMS computation
   and the Kronecker step in Thm 2.1(3); the Neshveyev parametrization use and all three
   parts of Thm 3.1; the cocycle identities (independence of $n$; increments
   $P_{j-1}u_jP_{j-1}^{-1}$); Lemma 4.1's concentration and marginal arguments; Cor 4.4's
   factor-of-ergodic and Peter–Weyl steps; Thm 4.5's Fourier argument.
3. *Citations already at policy:* all seven bibitems cited (Laca, Feldman–Moore,
   Neshveyev, Renault, Zimmer by name-and-number in the text; \cite{Main} and
   \cite{SeriesI} by DOI); Papers VI and VII by numeral with the policy sentence in §1
   ("we recall from them only what is needed and prove everything used" — accurate: every
   companion fact is re-proved in place). [Main, Prop 2.8 = prop:kmsmeasures,
   Lem 2.10, Lem 3.1, Thm 3.6] and [SeriesI, §5] verified by number and content.

*Consequences for other papers.* No item numbers changed; the downstream prose citations
(IX l.394, X l.360, XXVIII l.390 — "non-abelian symmetry breaking to a normal subgroup")
gloss conclusions that are unchanged, and remain compatible.

**Paper XXVIII — reviewed line by line (5 September 2026); the no-go theorem, its proof
route (finite support → local properness → hyperfiniteness) and the Kuhn-orientation
diagnosis all stand, and the gap table is exact, but the spectral theorem was stated for
the wrong operator ($T_p$ is normal, not self-adjoint — its spectrum is a disc, not the
interval), the LPS free-rank claim lacked its $p\equiv1\ (4)$ hypothesis, the null-locus
step and the backtracking count were gestures, and the general theorem's "automatic
discreteness" clause was false as stated (real quadratic counterexample — the Leopoldt
object of XXII–XXIII); also the author block had been commented out by a stray double-blind
template. No renumbering (Hyp 1.1 – Rem 6.3).**
`papers/XXVIII-spectral-gap/` (7 pp, 0/0/0/0; was 6 pp).

1. *Theorem 1.4 restated for the self-adjoint Hecke operator.* $T_p^*=\varepsilon_p^{-1}T_p$
   (Lem 2.2(1)), so $T_p$ is normal but not self-adjoint; decomposing over the characters
   of the central $\langle p\rangle$, each fibre is a phase times a tree adjacency, so
   $\mathrm{sp}(T_p\restriction L^2_0)$ is the closed \emph{disc} of radius $2\sqrt p$,
   while the interval $[-2\sqrt p,2\sqrt p]$ is the spectrum of
   $\varepsilon_p^{-1/2}T_p$. Statement, abstract display and verdict-table row now say
   so; $\|T_p\|=2\sqrt p$ and everything built on norms (Cor 4.1, Thm 4.2) unaffected.
   The proof now carries the fibre/gauge reduction (phase twists on a tree are
   gauge-trivial) and the LPS attribution is scoped: free of rank $(p+1)/2$ for
   $p\equiv1\ (\mathrm{mod}\ 4)$ \cite{LPS}, a free product of cyclic groups in general,
   simply transitive either way — Kesten's tree spectrum applies in every case.
2. *Two proof gestures made rigorous.* (i) The null-locus step ("proper closed subvariety
   hence null") now runs through the scaling: the zero-norm locus at $p$ is covered, for
   every $n$, by the $\sigma(p^n)$ right ideals of norm $p^n$, each an honest translate by
   Lemma 1.2 (norm-$p^n$ elements are units elsewhere), so its measure is at most
   $\sigma(p^n)p^{-n\beta}\to0$ for $\beta>1$ — in particular throughout Paper X's Gibbs
   range $\beta>2$. (ii) Lem 2.2(2)'s backtracking count: "$\varepsilon_p$ up to a unit"
   sharpened — with the self-conjugate choice of (1), $a_ja_k\in p\cH$ forces
   $a_k=\bar a_j$ exactly and the contribution is exactly $\varepsilon_p$; the vertex
   identification in (3) now carries the homothety caveat (the central
   $\langle p\rangle$ is trivialized on vertices, which is where self-adjointness lives).
3. *Theorem 6.1's "automatic" clause corrected — it was false.* "Automatic when
   $A\otimes\R$ is a product of division algebras" fails already for a real quadratic
   field: the closure of $\langle\varepsilon\rangle$ in $\Z_p^\times$ is not discrete —
   precisely the Leopoldt object of Papers XXII–XXIII. The clause now reads: automatic
   when the orders have finite unit groups (definite quaternion algebras over $\Q$);
   otherwise the discreteness hypothesis must be checked. Corollary 6.2's headline
   ("(C1)–(C3) incompatible with (C4) for every order in every algebra") is \emph{saved}
   by the bridge the old proof skipped: (C3) forces $P^\times$ finite ([X, Rem 1.5] — the
   same remark that repaired XXI and XXII), hence the archimedean norm-one group compact,
   hence discreteness — so the corollary stands with a complete proof.
4. *Verified correct:* Lem 1.2 (finite support); Thm 1.3's discreteness (norm argument +
   definite norm-one lattice), properness (translation by a discrete subgroup;
   one-factor properness), smoothness and the multiple-of-regular Koopman identification;
   Cor 3.1; Cor 4.1's six-column gap table exact ($2\sqrt p$ and $1-2\sqrt p/(p+1)$ to all
   printed digits); Thm 4.2's equivalences and their orientation (Kuhn: temperedness is
   necessary for amenability, so attaining Ramanujan certifies the wrong thing for (C4));
   the no-go proof (increasing union of smooth relations, Dye/CFW hyperfiniteness,
   FM/ADR amenability–injectivity); Rem 5.2's $F_2$ mechanism identification; Rem 6.3
   ([II] and [XXVII] exclusions — both compatible with the reviewed versions). All eleven
   bibitems cited; [Main] by DOI; Papers IX–XII by numeral with the re-proving sentence
   (accurate). Author block restored (the double-blind comment was a template artifact
   from the Q47 spacing paper; XXVIII is a numbered series paper).

*Consequences for other papers.* All item numbers unchanged; the conclusions cited by X
(its §3 status remark) and by the research-target adjudications are unchanged. **This
closes the sequential line-by-line review of the entire corpus: the foundational paper,
Papers I–XXV, XXVII, XXVIII (XXVI retired), and the two Q47 papers all now carry review
entries, and the full-corpus build is 0 errors / 0 warnings / 0 overfull, with the only
remaining underfulls the three legacy page-break underfulls in I, IV and XII, reviewed
before the `\raggedbottom` convention.**

---

**Monograph synchronization pass (5 September 2026).** The draft in `monograph/` had been
assembled on 28 August from pre-review sources; twelve of its twenty-six chapters carried
superseded mathematics (including the four-family XXIV and the $GL_2(\Z)$/dangling-reference
XXI) and it lacked XXVII and XXVIII. Actions, all verified by rebuild:

1. `assemble.py`: XXVII added to "Towards non-abelian systems", XXVIII to "Non-commutative
   semigroups and $GL_2$"; MERGE gained `Neshveyev → Nesh13`, removing an exact duplicate
   bibliography entry (VII's and XXVII's copies of Neshveyev 2013). Reassembled: 28
   chapters, 128 merged entries, 229 pp, 0 errors; stale pre-review chapter files purged.
2. Paper-source repairs found by the external review of the reassembled draft and verified
   here: XXIV's §2 heading still read "Four families are congruence-obstructed" and its
   abstract's first paragraph still said "wrong for four of the six families" — both
   leftovers of the September revision (the theorem, tables and all classifications were
   already correct; the reviewer's further claim that the body classifies twin/SG as
   obstructed was checked and is false). Heading now "Congruence confinement versus
   obstruction"; abstract says "wrong for two of the six families". XXIV recompiled
   0/0/0/0.
3. Papers X and XI: the forward pointer directed by XXVIII's entry ("when X, XI ... are
   next touched") added — one sentence at the end of each abstract recording that (C4) is
   settled, in the negative, in Paper XXVIII. Both recompiled 0/0/0/0; full-corpus
   regression clean.
4. Monograph frontmatter: preface's "end on an open condition (C4)" replaced by the no-go
   statement with a chapter reference; reading guide's paper count corrected (I–XXV, XXVII,
   XXVIII; XXVI retired); the two settled open-problem items annotated inline as settled by
   Chapter XXVIII (with the genuine residual question recorded), supplementing the
   editorial note; title-page affiliation address updated to Rivière-Beaudette, Québec at
   the author's instruction (paper folders and zenodo.txt files still read Montreal,
   pending the author's decision).

Remaining monograph editorial queue (not blocking): de-modularization of chapter openings
(repeated notation and "The series" paragraphs → standing notation; prose "Paper N" →
"Chapter \ref"), preface/acknowledgements rewrite, hyperref cosmetics, and the 17/21
book-level over/underfulls.

**Monograph de-modularization pass (5 September 2026).** Implemented in `assemble.py`
(paper sources untouched — they keep "Paper N" for standalone publication): (1) prose
"Paper N" / "Papers A, B and C" / "Papers A--B" converted to chapter references, with
heading-safe short titles (running heads cannot carry `\ref`), duplicate-ref and
"of the series" cleanups; residual "Paper N" occurrences are exactly the 27
`\chapterorigin` provenance notes, by design. (2) The standalone-paper policy sentences
("unpublished companions", "cited by DOI", the `\emph{The series.}` paragraphs) are
dropped at assembly. (3) The dependencies table is now built from the assembled chapters'
`\ref{ch:N}` graph, not only `\cite{PaperN}` keys, so prose-cited prerequisites appear
(e.g. Chapter XXVIII: Main, II, XXVII, IX, X, XI, XII). (4) Reading-guide's
"not harmonised" list updated. A second external patch proposing to overwrite Chapter
XXIV's §2 by hand was declined: the chapter was verified already correct, the patch would
have deleted the cited and proved statements and overclaimed unconditional uniqueness for
twin/SG, and `chapters/` is generated output. Book: 226 pp, 0 errors, 0 undefined
references. Still open (author's voice, not fabricated here): preface rewrite and
acknowledgements; open-problems thematic regrouping; book-level over/underfull cosmetics.

**Preface and acknowledgements installed (5 September 2026), text by the author.** Four
factual alignments made at installation, each checked against the body: (i) "the
hyperfinite factors R_infty or R_lambda" completed to the injective list (R_infty,
R_lambda, or a Krieger factor — Chapters IX/XXVIII); (ii) the garbled "deep space
non-amenability is strictly incompatible with the thermal framework" replaced by the
correct orientation "the non-amenability so abundant in the group is strictly denied to
the action" (Chapter XXVIII's Kuhn point); (iii) Part 6's description now notes its
opening arithmetic-topology chapter (VIII) before the function-field chapters; (iv)
Part 4 described as "equivariant rigidity and reconstruction" (it contains XIII–XVI, not
rigidity alone). The Chen sentence was left as written — "occupy generating classes"
correctly covers the multi-class case — and, deliberately, the preface claims only
"escape unobstructed" for twin/SG/Chen, not unconditional uniqueness, which keeps it
inside what is proved. CJK originals of the two teachers' names are preserved in a source
comment (pdflatex here has no CJK fonts; enable CJKutf8 to typeset them). All draft
placeholders removed; book compiles 227 pp, 0 errors, 0 undefined references.

**Paper XXIX — new (5 September 2026): the W_1 open problem advanced.**
`papers/XXIX-wasserstein/` (4 pp, 0/0/0/0). The numeral XXIX (next free; XXVI remains
retired — reuse was proposed and declined again, this time for new content, since the
retirement is codified in three places and XXIX is also chronologically honest). Content:
(1) Theorem 2.1, the finite-dimensional reduction, with the sharp sandwich
$\Pi_{(N,\infty)}W_1^{(N)}\le W_1\le\Pi_{(N,\infty)}W_1^{(N)}+2\rho_N$ — note this
corrects the version circulated in review (which had a spurious $-2\rho_N$ on the lower
side and omitted the $\Pi$ factor on the upper): the truncation optimizer contributes
$\Pi\cdot W^{(N)}$ exactly by independence, and the upper split uses Jensen for
$L(E_Nf)\le L(f)$ plus a martingale-difference variance bound with the explicit constant
$\rho_N^2=2\sum_{j>N}w_j^2t_j/(1-t_j)^2$ (geometric variances, no abstract $C_0$).
(2) Theorem 3.1, the quadratic chaos lower bound
$\Pi_\infty(w_0^2+4\sum_jw_j^2t_j^2/(1-t_j)^2)^{1/2}$ under the interior condition
$w_0^2\ge2\sum_jw_j^2t_j/(1-t_j)$, with the boundary case recorded as a remark; strictly
sharper than the squeeze at every finite beta, collapsing onto it as beta to infinity.
(3) Proposition 4.1 (optimizers odd and asymptotically finite-level) and Conjecture 4.2
(the odd Walsh-chaos hierarchy exhausts $W_1$), with the two genuinely remaining questions
stated (matching upper bound; parity measurability). Squeeze re-proved in place; three
bibitems, each cited; [Main] by DOI, Paper IV by numeral. Monograph: added to Part 2 after
Chapter IV (book now 29 chapters, 231 pp, 0 errors, 0 undefined; `conjecture` environment
added to the book preamble); the $W_1$ open-problem item annotated "[Partially settled]"
with the three remaining sub-questions; guide and dedicatory counts updated to twenty-nine.
zenodo.txt written.

**Conjecture 4.2 numerically tested (5 September 2026) — degree-1 does not saturate, and
the conjecture itself is expected false.** Scripts and outputs in `code/conj42/`
(scipy SLSQP; the feasible set is convex and the objective linear, so KKT = global; all
certified violations at machine precision except the two flagged grid runs at ~1e-5,
orders below the observed effects). Toy model $w_0=1$, $w_j=(j+1)^{-1}$, $t_j=p_j^{-1}$.
Findings: (1) the exact $2^N$ parity SOCP — the limit of the odd Walsh-chaos hierarchy,
truncation-free since forward steps flip parity — beats Theorem 3.1's closed form by
+26% ($N=2$) and +39% ($N=3$); at $N=1$ it reproduces the closed form to $10^{-16}$
(pipeline cross-validation). (2) Matched-truncation control: full-grid optimum exceeds the
parity optimum by a stable, $M$-independent $2$--$4\times10^{-3}$ at $N\ge2$, while the
same gap vanishes to $10^{-15}$ at $N=1$ with matched boundary parity — the $N\ge2$ gap
is bulk, so the optimal profile is *not* parity-measurable and the hierarchy converges
strictly below $W_1^{(N)}$. Paper XXIX gains Remark 4.3 recording both findings and
re-orienting Conjecture 4.2 (parity value = certified computable lower bound, not the
answer); question (c) is numerically answered in the negative. XXIX recompiled 0/0/0/0
(4 pp); book reassembled (231 pp, 0 errors).

**Paper XXX — new (5 September 2026): the affine-boundary K-theory open problem advanced.**
`papers/XXX-affine-ktheory/` (3 pp, 0/0/0/0; four bibitems, each cited; [Main] by DOI,
Paper II by numeral with facts restated). Content: (0) the repair — Paper II §6's affine
monoid is well defined over O_K only for global uniformizers; computation done at a
principal single prime, the ray-class case recorded as the true entrance of the class
group (forward reference and well-definedness flag added to docs/ERRATA.md under the
published Paper II, NOT to II's source, per the published-paper policy). (1) Dilation:
∂A^aff ⊗ K ≅ C_0(K_p)⋊(O_K[1/π]⋊Z). (2) Iterated PV over the exterior tower
M_r = colim(Λ^rO_K, t_r), transfer t_r = ±(Λ^{n-r}π)^∨ (integral — the transfer is the
adjugate), scaling α_* = q^{-1}Λ^rπ; two calibrations at n=1 (Bunce–Deddens; the coset
unitary maps to class 1, the pivot), anchored at p=2 against Larsen–Li. Result: Z in each
K-group (Nπ=+q; Z/2 in parity n if Nπ=−q); [1] of EXACT order q−1 (II's bound attained);
middle-layer torsion of order the regularized |det(q−Λ^rπ)|; real quadratic:
K_1 ⊇ Z/|q±1−Tr π|′. (3) The unexpected finding: the invariant hears the unit orbit of π
(Q(√2): π=3+√2 gives Z/2, u²π gives Z/18) — the affine boundary is not canonical in the
prime, explaining II §6's "fixed uniformizers" clause. Three residual problems recorded
(ray-class repair; extension data n≥3, |S|≥2; q-primary bookkeeping). Monograph: added to
Part 2 after XXIX (30 chapters); K_* open-problem item annotated [Partially settled] with
the three challenges; guide/dedicatory counts updated to thirty; zenodo.txt written.

**Paper XXXI — new (5 September 2026): the ray-class repair executed; the class group
enters K-theory as the exact torsion order of [1].**
`papers/XXXI-rayclass/` (3 pp, 0/0/0/0; three bibitems, each cited; [Main] by DOI; II and
XXX by numeral, facts restated). Content: (1) Theorem 1.2, the scaling-index theorem —
globally definable scalings at p form exactly hN, h = ord([p] ∈ Cl_K) (three-line proof
via principality of p^j ⟺ h|j), so the minimal well-defined affine system is the h-step
system with (π) = p^h, reducing to XXX at h=1; intermediate local uniformizers leave the
category of O_K-affine systems (marked-class argument). (2) Theorem 2.1: XXX's machinery
verbatim with (π, q^h): ord[1] = Np^h − 1 EXACTLY — the class-group order survives as
torsion, not rank; quadratic middle layer Z/|q^h±1−Tr π|′. Worked example Q(√−5), p_3 =
(3,1+√−5), h=2, π = 2−√−5 (membership verified digit by digit): K_0 ⊇ Z⊕Z/8 with [1] of
order 8, K_1 ⊇ Z⊕Z/2; a principal prime of the same norm would give ord[1]=2 — the
K-theory separates the two. Bonus remark: imaginary quadratic unit groups are finite, so
there the repaired invariant is canonical up to roots of unity. (3) Three residual
problems recorded (q-vs-h separation via the dual coaction; Hilbert-class-field descent —
capitulation cited to Neukirch VI.7 — whose equivariant K-theory should remember Cl_K
itself; |S|≥2 with definable scalings = ker(Z^S→Cl_K)). ERRATA (published Paper II)
extended: the divisibility statement must read (Np^h−1)[1]=0 in the repaired system,
attained. Monograph: added to Part 2 after XXX (31 chapters); the K_* open-problem
annotation updated (ray-class item settled, three new residuals listed); counts to
thirty-one; zenodo.txt written.

**Paper XXXII — new (5 September 2026): Galois descent executed; the full class group
emerges as the group of descent obstructions.**
`papers/XXXII-descent/` (3 pp, 0/0/0/0; four bibitems, each cited; [Main] by DOI; XXX,
XXXI by numeral, facts restated). Two structural corrections to the commissioning brief
before construction: p SPLITS in H into g = |Cl_K|/h primes of residue degree f = h
(Artin sends Frob_p to [p]), so the top space is the product of g completions, not one;
and G does not act on the minimal system — sigma(Pi) = u_sigma·Pi forces the
unit-extended scaling monoid O_H^×·Pi^N, the twist being the point. Theorems: (1)
Emergence (Thm 2.1): a canonical INJECTION Cl_K ↪ H^1(G,O_H^×), [a] ↦ [σ↦σ(α)/α]
(defined on all of Cl_K by capitulation/PIT, homomorphic, injective via Hilbert 90 +
valuation argument), with δ([p]) = the obstruction cocycle of the affine system;
invariant generator exists iff p principal; descent obstructions of the family of affine
systems = δ(Cl_K) ≅ Cl_K exactly (prime classes generate). (2) Norm relation:
(N_{H/K}(Pi)) = p^{|Cl_K|} = (π)^g, so the XXXI scaling is the norm of the capitulated
scaling up to units (exactly, when [p] generates). (3) Imprimitivity + Julg
(Thm 3.2): X_H = Ind_C^G O_{P_1} gives ∂A_H ⋊ G ∼_Morita (inert local model) ⋊ Z/h — the
equivariant K-theory reduced, integral computation honestly left as Problem (i). (4) The
ladder (Thm 3.3): ord[1] = q^h−1 at the bottom (XXXI) and q^{|Cl_K|}−1 at the top (r=0
layer of XXX's tower on the product space; unit scalings fix the class of 1) — order of
the class below, class NUMBER above, group structure in the cocycles. Remaining problems
recorded: (i) integral K of the inert model ⋊ Z/h (R(Z/h)-structure of the equivariant
exterior tower; first case K=Q(√−5), H=Q(i,√5), p_3 inert, C=Z/2); (ii) fixed-point vs
crossed-product Morita (bottom = C-fixed points of the inert model; fixed locus null in
measure, not in topology — where [c_p] should reappear); (iii) separating the unit-torus
footprint of O_H^×. Monograph: added to Part 2 after XXXI (32 chapters); open-problem
item (b) updated to the reduced form; counts to thirty-two; zenodo.txt written.

**Paper XXXIII — new (5 September 2026): the trivial W_1 upper bound broken by an
adaptive coupling.**
`papers/XXXIII-coupling/` (3 pp, 0/0/0/0; two bibitems, each cited; [Main] by DOI; XXIX
by numeral, setting restated). Content: (1) Lemma 1.1, the shift identity — the
odd-conditioned geometric law is EXACTLY the unit shift of the even-conditioned one
(one-line pointwise check), so the parity channel at coordinate j transports at cost
exactly w_j per unit, capacity τ_j = 2t_j/(1+t_j). (2) Lemma 1.2, the residual identity —
the unmatched mass m_j is, renormalized, the extreme pair of the subsystem without j
tensored with a spectator law, whence the recursion. (3) Theorem 2.1: for every
enumeration, W_1 ≤ w_0Π_∞ + Σ_k w_{j_k}τ_{j_k}∏_{l<k}m_{j_l} = E[cost of first available
cheap flip]; strictly < w_0 when some w_j < w_0; gap to the squeeze lower bound ≤ 2Σw_jt_j
→ 0 in the deep freeze — the pair (lower, upper) now PINCHES as β→∞, replacing the old
[w_0Π_∞, w_0]. (4) Prop 2.2: sorted-by-weight enumeration optimal (three-line exchange
lemma; the swap difference is τ_jτ_{j'}(w_j−w_{j'}), remainder-independent). (5) Toy
evaluation 5/12 ≈ 0.4167 vs certified [0.2254, 0.2288] — consistent, decisively below
w_0=1; the honest residual factor ≈1.8 near criticality attributed structurally (scan
flips the first coordinate; the SOCP optimizer shades continuously), the randomized
multi-channel optimization recorded as the remaining problem. Physical moral stated:
thermal activity τ_j of each prime opens a microscopic arithmetic channel substituting
for the macroscopic symmetry flip; in the deep freeze all channels close and the group
flip recovers its monopoly. Monograph: added to Part 2 directly after XXIX (33 chapters;
XXX–XXXII shift by one, all references by label); W_1 open-problem item (b) updated to
the advanced form, (c) marked numerically answered; counts to thirty-three; zenodo.txt
written.

**Paper XXXIV — new (5 September 2026): the ultimate structural question answered in two
halves — a universal no-go for the scaling route, and the angular Hurwitz programme for
the grail.**
`papers/XXXIV-bottleneck/` (3 pp, 0/0/0/0; four bibitems, each cited; [Main] by DOI; V,
VII, X, XII, XXVII, XXVIII by numeral, facts restated). Content: (1) Theorem 1.2, the
abelian scaling bottleneck: for right LCM P with scalar dynamics N^{it}, KMS states are
tracial on the gauge-fixed algebra (the XXVII Thm 2.1 two-liner), the Neshveyev
parametrization splits into a scaling measure seeing only the P^ab-graded weight and a
β-INDEPENDENT tracial isotropy datum, and no nonabelian residual symmetry can arise on
the scaling side. Worked negative example: braid monoids B_n^+ (right LCM by Garside,
maximally noncommutative, abelianization Z by length) — the entire transition is the
growth series', the braiding surviving only as β-independent traces. Retro-explains VII
(abelian E_β because it had to be), XII (noncommutativity located in the weightless
kernel), XXVIII (those directions hyperfinite for arithmetic orders): one common cause.
(2) The complementary half recalled: XXVII realizes Prob(H\G) transverse to the scaling
— scaling abelian, symmetry arbitrary. (3) The Goldilocks candidate named: the ANGULAR
HURWITZ SYSTEM — radial Nrd carries X's thermodynamics (β_c=2), the discarded angular
part ρ(a)=a/Nrd(a)^{1/2} ∈ SU(2) is an ordered cocycle (XXVIII's self-conjugate level
sets), and Prop 3.1 computes the matrix Kakutani series EXACTLY: the a↦−a symmetry kills
the trace term identically (no Sato–Tate input needed), Ξ_β(ρ) = 96Σ(p+1)p^{−β},
abscissa exactly 2 — the angle turns critical precisely where the radius does. Programme
with the single hard step named: transport XXVII's matrix martingale from the
independent-geometric relation to the Hurwitz tail relation (tree-level filtration of
XXVIII); expected verdict KMS_β ≅ Prob(SU(2)) throughout the Gibbs phase — a simplex
over a genuinely nonabelian compact group on an honest arithmetic semigroup — with LPS
providing the mixing hypothesis at the critical edge. Monograph: added to Part 3 after
XXVII (34 chapters); the closing residual question of open problem (1) updated with the
bottleneck/angular verdict; counts to thirty-four; zenodo.txt written.

**Incidental resolution (5 September 2026): XXXI's Problem (i), q-vs-h separation,
generically settled.** Remark 2.3 added to (unpublished) XXXI with a verified worked
pair: Q(√−5)/p_3 (q=3,h=2) and Q(i)/(3) (inert, q'=9, h'=1) share ord[1]=8, but the
middle layers differ — T_1 = Z/2 (order 2) vs (Z/2)² (order 4, scalar α_*=1/3 on
Z[1/3]², coker(2/3)⊕²) — so the K-groups themselves generically separate (q,h) through
the layer trace data; the residual problem shrinks to the exceptional locus of
layer-coincident pairs, where the dual coaction remains the candidate. §4 problem list
and the monograph open-problem item updated accordingly. Remaining ledger, checked and
NOT incidental: the angular transport (XXXIV's named step — a campaign); the inert
model ⋊ Z/h integral K (XXXII i — a genuine computation); fixed-point vs crossed Morita
(XXXII ii); H^1_meas itself (III Rem 2.5 — non-smooth); the randomized multi-channel W_1
optimization (XXXIII); the q-primary bookkeeping (XXX c); the aggregate-Leopoldt
question (XXIII).

**Incidental resolution (6 September 2026): the twin-prime free-regime problem settled
unconditionally, and the external proposal adjudicated.** A three-scheme external
proposal (fermionic/field-theoretic framing) was audited: Scheme 2 (twin high-temperature
uniqueness via 'gauge-flow circle method') TERMINATED — its displayed asymptotic is
Hardy–Littlewood-conjecture strength and the parity barrier is untouched by the metaphor.
Scheme 1 (Chen uniqueness 'immediately provable') REJECTED as chained: it repeats, for
the third time in this project, the occupancy≠divergence fallacy — [Main, Thm 3.9] needs
per-character detecting-series divergence, i.e. Chen's theorem in arithmetic
progressions, which remains the named sieve gap; the full-series divergence step is
correct but insufficient. Scheme 3 (Brun-identity route to the free regime) contains a
correct identity L_S(1)=B_2/2+Σ1/(p(p+2)) but two numerical errors: Σ1/(p(p+2)) = 0.10798
(verified by direct summation), not 0.21092 (doubled), and B_2 = 1.90216 is the
HL-extrapolated value, not an unconditional theorem — their headline 1.1620 is wrong,
the true conditional value being ≈1.06 (matching the book's own estimate). SALVAGED
UNCONDITIONALLY: since partial sums of a positive series are rigorous lower bounds, a
segmented sieve to 1.1×10^10 (29,889,853 twin pairs; script and output archived in
code/twin-regime/) gives Σ 1/p = 1.00195935 > 1 with no external inputs; hence
L_{S_twin}(1) > 1 and, by Paper V's criterion, the twin free system is in Regime (S)
with β_c^free > 1 — the open problem's regime DICHOTOMY is settled by direct
computation, cross-checked against the HL rate (predicted ≈1.0017). The precise values
β_c^free ≈ 1.0089 (twin) and 1.2114 (Chen) remain tail-conditional estimates and are
NOT asserted. Open-problem item updated in the monograph; book recompiled clean.

**Paper XXXV — new (6 September 2026): the twin-regime resolution written up.**
`papers/XXXV-twin-regime/` (3 pp, 0/0/0/0; three bibitems, each cited; [Main] by DOI; V
and XXIV by numeral, criterion and Brun identity restated). §1: the free dichotomy is the
single comparison L_S(1) vs 1 (geometric Gibbs series); the Brun identity with the
verified 0.10798 and the honest caveat that B_2 = 1.90216 is an HL extrapolation (the
conditional 1.059 decides nothing). §2: Theorem 2.1 — the segmented-sieve partial sum
1.00195935 > 1 at 1.1e10 (29,889,853 pairs; float-error and HL cross-check both
addressed), hence unconditionally Regime (S), β_c^free > 1, and on (1, β_c^free) the
classical system is broken while the free system has no KMS state. The exact β_c^free
left as tail-conditional. §3: two methodological remarks canonizing this project's
recurring adjudications — occupancy ≠ divergence (AP-Chen the named gap) and metaphor ≠
proof (average vs pointwise). Monograph: added to the families-of-primes part after XXV
(35 chapters); open-problem annotation now points to the chapter; counts to thirty-five;
zenodo.txt written.

---


## The corpus: 27 numbered papers (I–XXV, XXVII, XXVIII; XXVI unused) plus two unnumbered Q47 papers, all compiling clean

| | Title | pp | Compile |
|---|---|---|**Paper XXXVIII — new (6 September 2026): the inert integral equivariant K-theory
executed (XXXII Problem (i), first case).** `papers/XXXVIII-inert-ktheory/` (2 pp,
0/0/0/0; scripts in code/xxxviii-inert/). O_H = Z[i]⊗Z[φ] free over Z[C] (Tate); tower
Z_+, Z[C]², Z_−²⊕Z[C]², Z[C]², Z_+; generator Π = −3−i+2φ+iφ (N=+9, Tr=−8); SNF layers
T_1=Z/5⊕Z/5⊕Z/61, T_2=Z/2⊕Z/2⊕Z/5⊕Z/7⊕Z/11 (sign-twisted block inside), T_3=Z/29.
Theorem: K_0 ⊇ Z²⊕(Z/8)²⊕T_2, K_1 ⊇ Z²⊕T_1⊕Z/29; unit class split by (1±U_σ)/2 into a
pair of exact order-8 classes; entanglement law: the class group doubles/twists only the
non-induced strata (Shapiro counts free blocks once) — labels change, Smith orders never.
By-product: the σ-fixed locus is XXXI's h-step system (null in measure, not in topology):
XXXII's Problem (ii) is a direct summand of Problem (i). Gaps recorded: twisted character
bookkeeping; degree-4 extensions. Monograph: Part 2 after XXXII (38 chapters, 258 pp, 0
errors, 0 undefined); open-problem item updated; counts thirty-eight; zenodo.txt written.

**Paper XXXIX — new (6 September 2026): the H^1_meas ledger item closed in the correct
sense.** `papers/XXXIX-cohomology/` (2–3 pp; four bibitems, each cited; [Main] by DOI; I,
III by numeral, facts restated). The commissioned "explicit group structure" was
re-posed: III Rem 2.5's non-smoothness is upgraded to Theorem 1.1 (Z^1 Polish, B^1 dense
meager Borel, quotient Borel structure trivial, coboundary action TURBULENT in Hjorth's
sense ⟹ no classification by countable structures — the exact upper bound on
"computing"); Prop 1.2 (the complete smooth residue = Mackey-range spectrum); Thm 2.1
(canonical injection Ĝ_S/Ξ_β ↪ H^1 into the equicontinuous classes, kernel exactly Ξ_β
by III Thm 2.3 restated; Dye–Krieger orbit-equivalence functoriality ⟹ the ambient group
depends only on the Krieger type — ambient amnesia, arithmetic survives as the embedded
subgroup and its position). §3 verdict: the series' philosophy stated finally — the
arithmetic lives in the measure class, the only equicontinuous thread in a turbulent
sea; the turbulence is the measure-theoretic root of the collective blindness of every
smooth invariant. §4 honest gaps: the third Hjorth condition's literature localization
(flagged lemma); noncompact coefficients open. Monograph: inserted after Chapter III (39
chapters); open-problem item annotated [Settled in the correct sense]; counts to
thirty-nine; zenodo.txt written.

---|
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
| XXVIII | (C4) settled: the Hecke operator on the Bruhat–Tits tree, the Ramanujan bound as the tempered bound, hyperfiniteness | 6 | clean |
| — | Q47: localized BC system of the degree-46 family, $\beta_c=1/46$, congruence invisibility | 12 | clean |
| — | Q47: spacing statistics, Poisson universality and the Hardy–Littlewood pair correlation | 8 | clean |

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
