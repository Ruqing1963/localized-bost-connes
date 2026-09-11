# Priority analysis: structural collision tests

Part I treats Cuntz–Deninger–Laca (2013). Part II, added later, treats the
multiplicative $S$-integer literature (Bruce, Bruce–Laca, Li) and is the more important
of the two.

**Method.** Claims below are of two kinds and are marked accordingly.

- **[D] Derived.** Consequences of the defining relations of the two algebras, obtained
  here from first principles. These do not depend on recollection and can be checked by
  the reader without consulting any source.
- **[R] Recalled.** Assertions about what Cuntz–Deninger–Laca actually prove. These are
  from memory, without access to the paper, and must be verified.

**The verdict below rests only on [D].** That is the point of separating them: if every
[R] statement turned out to be misremembered, the structural conclusion would survive.

---

## 1. The two algebras

| | CDL (2013) | This work |
|---|---|---|
| semigroup | $ax+b$: $\mathcal{O}_K\rtimes\mathcal{O}_K^\times$ | multiplicative only: $J_S$, ideals supported on $S$ |
| additive part | **present**, acting by unitaries | **absent** |
| diagonal | $C(\widehat{\mathcal{O}}_K)$, additive profinite completion | $C(Y_S)$, $Y_S=\widehat{\mathcal{O}}_S\times_{U_S}G_S$ |
| isometries per ideal $\mathfrak a$ | $N\mathfrak a$ (one per coset $a+\mathfrak a$) | **one** |
| localization at arbitrary $S$ | not part of the construction | the whole point |

The single structural fact that drives everything below: in the $ax+b$ semigroup the
additive translations $b\mapsto b+x$ are **bijections** of the semigroup, hence unitaries
in the left regular representation, hence fixed by any time evolution that is trivial on
the additive part. Our algebra has no such unitaries.

## 2. [D] The additive part forces $\beta\ge1$

In the Toeplitz algebra the isometries $\mu_{(a,\mathfrak a)}$, $a$ running over
$\mathcal{O}_K/\mathfrak a$, have mutually orthogonal ranges and satisfy the sub-Cuntz
relation
$$\sum_{a\in\mathcal{O}_K/\mathfrak a}\mu_{(a,\mathfrak a)}\mu_{(a,\mathfrak a)}^{*}\ \le\ 1 .$$
For a $\mathrm{KMS}_\beta$ state $\varphi$ and any isometry $\mu$ with
$\sigma_t(\mu)=N\mathfrak a^{it}\mu$ one has $\varphi(\mu\mu^*)=N\mathfrak a^{-\beta}$.
Applying $\varphi$ to the displayed relation and using that there are exactly
$N\mathfrak a$ summands,
$$N\mathfrak a\cdot N\mathfrak a^{-\beta}=N\mathfrak a^{\,1-\beta}\ \le\ 1
\qquad\Longrightarrow\qquad \boxed{\beta\ \ge\ 1 } .$$
In the boundary (Cuntz–Pimsner) quotient the relation is an equality, forcing
$N\mathfrak a^{1-\beta}=1$, i.e.\ $\beta=1$ exactly: the quotient carries KMS states at a
**single** inverse temperature.

By contrast, in $\mathcal{A}_{K,S}$ there is one isometry per ideal and
$\mu_\mathfrak a\mu_\mathfrak a^*=\mathbf 1_{\mathfrak aY_S}$, so the same computation
gives only $N\mathfrak a^{-\beta}\le1$, i.e.\ $\beta\ge0$. Our
Theorem 3.6 produces a nonempty $\mathrm{KMS}_\beta$ simplex for **every** $\beta>0$.

**Consequence.** A framework whose KMS states are confined to $\beta\ge1$, and whose
boundary quotient is confined to $\beta=1$, cannot host a classification indexed by
arbitrary $\beta>0$. The parameter range on which $\Xi_\beta(K,S)$ lives is largely
outside CDL's range of definition.

## 3. [D] The additive part annihilates the measure-theoretic freedom

This is the decisive point.

Let $\varphi$ be a $\mathrm{KMS}_\beta$ state of the $ax+b$ Toeplitz algebra and let
$\nu=\varphi|_{C(\widehat{\mathcal{O}}_K)}$. The additive translations
$u_x$, $x\in\mathcal{O}_K$, are unitaries with $\sigma_t(u_x)=u_x$, so the KMS condition
gives $\varphi(u_xcu_x^*)=\varphi(c)$ for every $c$: **$\nu$ is invariant under the
additive action of $\mathcal{O}_K$**. Since $\mathcal{O}_K$ is dense in
$\widehat{\mathcal{O}}_K$ and the projections $\mathbf 1_{a+\mathfrak a}$,
$a\in\mathcal{O}_K/\mathfrak a$, are permuted transitively by that action,
$$\nu\bigl(\mathbf 1_{a+\mathfrak a}\bigr)=\frac{1}{N\mathfrak a}\qquad\text{for every }a,\mathfrak a .$$
These values determine $\nu$ on a generating family of clopen sets, so
$$\nu=\text{normalized Haar measure on }\widehat{\mathcal{O}}_K,\qquad\text{uniquely.}$$

There is no freedom whatsoever in the base measure. Whatever parametrizes the
$\mathrm{KMS}_\beta$ states of a Toeplitz algebra of $ax+b$ type, it is **not** a measure
on the diagonal.

In $\mathcal{A}_{K,S}$ the corresponding constraint is only the scaling relation
$\nu(\mathfrak aE)=N\mathfrak a^{-\beta}\nu(E)$. By Lemma 2.9 of the master paper this
pins the valuation marginal completely and leaves the conditional measure on $G_S$
entirely free; the whole content of Theorem 3.6 is the determination of that freedom,
namely $\mathrm{Prob}(G_S/\Xi_\beta^\perp)$. The obstruction group is a statement about
**which measures on the base are admissible**. In CDL's setting that question has the
one-line answer "Haar", and $\Xi_\beta$ has nothing to be a group of.

**This is the structural divergence.** It is not a matter of degree of generality: the
additive unitaries destroy exactly the degrees of freedom our theorem classifies.

## 4. [D] Localization does not repair the discrepancy

One might ask whether an $S$-localized $ax+b$ algebra would recover our setting. It would
not. If the additive part is retained, §2 and §3 apply verbatim: the count of cosets
$a+\mathfrak a$ is still $N\mathfrak a$, so $\beta\ge1$ is still forced, and the base
measure is still rigid. If the additive part is dropped, one is back in the multiplicative
world — which for $S=P_K$ is precisely the Laca–Larsen–Neshveyev system, already cited as
the special case of our Theorem 3.6, and for general $S$ is $\mathcal{A}_{K,S}$.

So the landscape is coherent:

```
   ax + b, additive present         CDL (2013)          beta >= 1, base measure rigid
   multiplicative only, S = P_K     LLN (2009)          our Theorem 3.6, special case
   multiplicative only, S arbitrary  this work           Xi_beta(K,S), all beta > 0
```

## 5. [R] What I recall of CDL's actual results

To be verified, and not relied upon.

- The set of $\beta$ admitting $\mathrm{KMS}_\beta$ states is, I believe,
  $\{1\}\cup[2,\infty]$. The lower endpoint $1$ matches the derivation in §2. The value
  $2$ should be the point where the partition function
  $\sum_\mathfrak a N\mathfrak a\cdot N\mathfrak a^{-\beta}=\zeta_K(\beta-1)$ converges,
  which happens for $\beta>2$ — consistent, and itself a [D] observation.
- For $\beta>2$ the extremal $\mathrm{KMS}_\beta$ states are, I believe, parametrized by
  the **class group** $\mathrm{Cl}_K$ (equivalently by tracial states on
  $C^*(\mathrm{Cl}_K)$), hence by a **finite** set. Our simplex
  $\mathrm{Prob}(G_S/\Xi_\beta^\perp)$ is finite-dimensional only when $\Xi_\beta$ is
  finite, and in the cascade constructions it is infinitely generated.
- I do not recall any Dirichlet-series convergence condition, any Kakutani-type
  dichotomy, or any localization to a proper subset of primes appearing in CDL.

## 6. Verdict

On the strength of §§2–4, all of which are [D]:

> Theorem 3.6 and the criterion $\Xi_\beta(K,S)$ are **not** a corollary of CDL (2013),
> and the two constructions diverge at the level of the dynamical system rather than at
> the level of generality. The additive part of the $ax+b$ semigroup both restricts the
> admissible inverse temperatures to $\beta\ge1$ and rigidifies the base measure to Haar,
> and the obstruction group is precisely a classification of base measures at arbitrary
> $\beta>0$.

This is a strong structural argument. It is **not** a literature check, and it does not
establish independence, for three reasons:

1. My [R] recollections could be wrong in ways that matter — e.g.\ if CDL also treat a
   purely multiplicative algebra in a later section.
2. CDL is one paper. The result could appear in a follow-up, or in adjacent work.
3. Structural divergence of the *algebras* does not by itself preclude someone having
   written down the same *criterion* for the multiplicative system.

## 7. The higher-priority target

Given §4, the real collision risk is not CDL but **work on multiplicative or $ax+b$
systems over $S$-integers and congruence monoids**, where localization is already present.
The following should be checked before CDL:

- **C. Bruce**, on $C^*$-algebras from actions of congruence monoids, and on Toeplitz
  algebras of $S$-integer rings — this is the closest structural match to
  $\mathcal{A}_{K,S}$ that I am aware of.
- **C. Bruce, M. Laca** and coauthors on KMS states for such systems.
- **M. Laca, N. Larsen, S. Neshveyev**, work subsequent to the 2009 paper.
- **Z. Afsar, A. an Huef, I. Raeburn**, KMS states of semigroup $C^*$-algebras.
- **X. Li**, semigroup $C^*$-algebras and their boundary quotients, for the general
  framework in which an $S$-localized construction would most naturally be phrased.

If a localized multiplicative system with an arbitrary prime set has been studied, the
question is then narrow and answerable: does the classification there produce a subgroup
of $\widehat{G_S}$ cut out by convergence of $\sum_{\mathfrak p\in S}N\mathfrak p^{-\beta}
|1-\chi(\mathrm{Frob}_\mathfrak p)|^2$? That is a specific thing to look for, and §§2–4
above at least guarantee that the search space is the multiplicative literature, not the
$ax+b$ literature.


---

# Part II. The multiplicative $S$-integer literature

The redirection in §7 was acted on. A report was supplied to the effect that Bruce,
Bruce–Laca and Li establish the algebraic skeleton of $S$-localized Toeplitz systems and
congruence monoids, parametrize extremal states by ray class groups, and treat **finite
$S$ or $S=P_K$**. That report is [R]: it has not been checked at the source and is
recorded here as a hypothesis, not a finding.

What follows does not depend on it being right. One piece of it — that the standard
choices of $S$ are the finite ones and $P_K$ — turns out to be enough to settle the
question structurally, because of the following.

## 8. [D] The intermediate regime is invisible to both standard choices of $S$

**Proposition.** Let $\Xi_\beta=\Xi_\beta(K,S)$ be as in the master paper.

1. If $S$ is finite, then $\Xi_\beta=\widehat{G_S}$ for **every** $\beta>0$.
2. If $S=P_K$, then $\Xi_\beta=\{1\}$ for $0<\beta\le1$ and $\Xi_\beta=\widehat{G_S}$ for
   $\beta>1$.

In both cases $\Xi_\beta$ takes only its two extreme values, the $\mathrm{KMS}_\beta$
simplex is either a single point or all of $\mathrm{Prob}(G_S)$, and no intermediate
residual symmetry occurs.

*Proof.* (1) For finite $S$, $\zeta_{K,S}(\beta)=\prod_{\pp\in S}(1-\Ns\pp^{-\beta})^{-1}<\infty$
for every $\beta>0$; apply Lemma 3.5 of the master paper. (2) For $S=P_K$ and
$\beta\le1$, Corollary 3.10 gives $\Xi_\beta=\{1\}$ via Chebotarev; for $\beta>1$,
$\zeta_K(\beta)<\infty$ and Lemma 3.5 applies again. $\square$

**Consequence.** Intermediate values of $\Xi_\beta$ require $S$ to be infinite with
$\beta_c(S)>0$ **and** to fail the equidistribution criterion of Theorem 3.9 — that is,
to be a sparse set concentrating $\beta$-negligibly in a proper subgroup. Neither
condition can be met by a finite set, and $P_K$ fails the second by Chebotarev.

So a treatment confined to finite $S$ and to $S=P_K$ could not have discovered
$\Xi_\beta$ even in principle: in those settings the invariant is constant on each phase
and carries no information. The phenomenon lives exactly in the gap between the two
standard choices. This is a stronger statement than "the mechanism does not appear in
their papers", and it is derived rather than recalled.

## 9. Falsifiable predictions

Priority is the lesser risk; **incompatibility** is the greater one. If the literature
contains a classification for some $S$ that our Theorem 3.6 also covers, the two must
agree. The following are what our theorem predicts, stated so that a single reading of a
source can confirm or refute them.

| # | Setting | Our theorem predicts | Refuted if a source shows |
|---|---|---|---|
| P1 | $S$ finite | KMS$_\beta$ simplex $\cong\mathrm{Prob}(G_S)$ for every $\beta>0$; **no phase transition**; extremal states in bijection with $G_S$, an **infinite** compact group (extension of the finite $\Cl^+_S$ by $U_S/\overline{\cO^\times_{K,+}}$) | a phase transition for finite $S$, or a **finite** set of extremal states |
| P2 | $S=P_K$, $\beta>1$ | extremal states $\leftrightarrow\Gal(K^{ab}/K)$ | any other parametrization |
| P3 | $S=P_K$, $\beta\le1$ | unique KMS state | non-uniqueness |
| P4 | any $S$, $\beta>\beta_c(S)$ | simplex $=\mathrm{Prob}(G_S)$, extremal states of type $\mathrm I_\infty$ | intermediate residual symmetry above $\beta_c$ |
| P5 | any $S$ | $\beta\mapsto\Xi_\beta$ nondecreasing; transition set countable | a continuum of transitions |

P1 deserves attention. A parametrization of extremal KMS states by a **ray class group**
is by a finite object. Our $G_S$ is infinite whenever $U_S/\overline{\cO^\times_{K,+}}$ is,
which is the generic case. If a source states a finite parametrization for a system whose
diagonal is $C(Y_S)$, then either the algebra there is a different one — for instance a
finite-level or boundary quotient, where the diagonal has been collapsed — or one of the
two classifications is wrong. Determining which is a higher priority than the priority
question itself.

## 10. Status

Part I (§§2–4) and §8 are [D] and stand on their own. The reports concerning what CDL,
Bruce, Bruce–Laca and Li actually prove remain [R] and unverified. The recommended order
of work is now:

1. **Check P1 against any source treating finite $S$.** This is a correctness check, not a
   priority check, and it is the fastest way to find a bug if there is one.
2. Then P2, P3 against Laca–Larsen–Neshveyev (2009), already cited as the $S=P_K$ case.
3. Only then the priority question proper, which §8 has already narrowed to: has anyone
   treated an infinite sparse $S$ with $0<\beta_c(S)<\infty$?

---

# Part III. The $S$-integer terminology trap, and a worked consistency check

## 11. [D] "Finite $S$" means opposite things in the two literatures

For a finite set $S$ of primes of $K$, the ring of $S$-integers is
$\mathcal{O}_{K,S}=\{x\in K:\ v_\pp(x)\ge0\ \ \forall\pp\notin S\}$, in which every prime of
$S$ has been **inverted**. Consequently the nonzero prime ideals of $\mathcal{O}_{K,S}$ are
in bijection with $P_K\setminus S$, and the ideal monoid acting in any Toeplitz or
semigroup crossed product built from $\mathcal{O}_{K,S}$ is $J_{P_K\setminus S}$.

So a study of "$S$-integers with $S$ finite" is, in the notation of the master paper, a
study of the **co-finite** dynamical prime set $S'=P_K\setminus S$, for which
$\beta_c(S')=1$. It is not the finite case of our Theorem 3.6.

This dissolves the apparent tension recorded as P1 in §9 without either side being wrong,
and it is worth stating explicitly in any comparison, since the same symbol $S$ denotes
complementary objects in the two settings.

**Our theorem covers the co-finite case too, and agrees.** For $S'=P_K\setminus S$ with $S$
finite: removing finitely many primes changes neither the Chebotarev density argument of
Corollary 3.10 nor the convergence of $\zeta_K$, so $\Xi_\beta=\{1\}$ for $0<\beta\le1$ and
$\Xi_\beta=\widehat{G_{S'}}$ for $\beta>1$. Same two-valued behaviour as $S=P_K$; still no
intermediate regime, consistent with §8.

## 12. [D] Worked check: $K=\Q$, $S=\{\ell\}$

This is the genuinely finite case in our sense. Two independent routes to $G_S$.

*Route 1, from Definition 2.1.* $\Idl_S=\Q_\ell^\times$ and
$\Q^\times_{S,+}=\{\alpha\in\Q^\times:\ v_p(\alpha)=0\ \forall p\ne\ell,\ \alpha>0\}=\ell^{\Z}$,
which is discrete and closed in $\Q_\ell^\times$. Since
$\Q_\ell^\times=\ell^{\Z}\times\Z_\ell^\times$,
$$G_{\{\ell\}}=\Q_\ell^\times/\overline{\ell^{\Z}}\ \cong\ \Z_\ell^\times .$$

*Route 2, from the exact sequence (2.1).* $U_S=\Z_\ell^\times$,
$\cO^\times_{\Q,+}=\{1\}$, and $\Cl^+_{\{\ell\}}$ is the subgroup of $\Cl^+_\Q=1$ generated
by $[\ell]$, hence trivial. The sequence
$1\to U_S/\overline{\cO^\times_{\Q,+}}\to G_S\to\Cl^+_S\to1$ collapses to
$G_S\cong\Z_\ell^\times$. ✓ The two routes agree.

*Prediction.* $\zeta_{\{\ell\}}(\beta)=(1-\ell^{-\beta})^{-1}<\infty$ for every $\beta>0$,
so $\Xi_\beta=\widehat{G_S}$ always and the $\mathrm{KMS}_\beta$ simplex is
$\mathrm{Prob}(\Z_\ell^\times)$ at every $\beta>0$, with no phase transition. The extremal
states are the Gibbs states of the Fock representations indexed by $\Z_\ell^\times$, an
**infinite** compact group.

Directly: a measure $\nu$ on $\Z_\ell$ with $\nu(\ell E)=\ell^{-\beta}\nu(E)$ has
$\nu(\ell^k\Z_\ell^\times)=(1-\ell^{-\beta})\ell^{-k\beta}$ forced, while its conditional
law on $\Z_\ell^\times$ is unconstrained — exactly $\mathrm{Prob}(\Z_\ell^\times)$. ✓

So P1 is internally coherent and produces an infinite parametrization for a genuinely
finite $S$, as it must.

## 13. Where this leaves the two risks

**Correctness risk: substantially reduced.** §11 explains the finite-versus-infinite
tension as a terminology mismatch rather than a contradiction, and §12 confirms our
prediction for a truly finite $S$ by two independent computations internal to the paper.
No source is needed for either. P2 and P3 concern $S=P_K$, which the master paper already
treats as the classical case and which was checked when Corollary 3.10 was written.

**Priority risk: unchanged, and slightly sharpened.** §11 has a second consequence. If the
$S$-integer literature works with co-finite sets, then by §8 and §11 the settings covered
there are $\beta_c=1$ with two-valued $\Xi_\beta$ — still not the intermediate regime. But
this is an inference from a description of that literature, not from the literature. The
open question is unchanged and now stated as sharply as it can be without reading:

> Has any published classification treated a dynamical prime set that is infinite, sparse,
> with $0<\beta_c(S)<\infty$, and failing the equidistribution criterion of Theorem 3.9?

Nothing in Parts I–III answers this. What Parts I–III do establish, from the defining
relations alone, is that the answer cannot be found in the $ax+b$ literature (Part I), nor
in treatments confined to finite or co-finite or full prime sets (Parts II–III).
