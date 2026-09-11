# Errata for the published papers

Corrections found after deposit. None affects a stated theorem's conclusion in the paper
concerned unless said so; each is cited by the later papers where relevant.

## Foundational paper (DOI 10.5281/zenodo.22152101)

**Proposition 2.7 (inductive limit; inclusion in the full system).** The proposition asserts
that for $S\subseteq S'$ the coordinate projection $\widehat{\mathcal O}_{S'}\to\widehat{\mathcal O}_S$
induces a projection $\mathrm{pr}:Y_{S'}\to Y_S$ and hence an embedding
$\mathcal A_{K,S}\hookrightarrow\mathcal A_{K,S'}$, and that $G_S=\varprojlim G_{S_k}$.
By the exact sequence (2.1), $Y_S$ is a disjoint union over $\mathrm{Cl}^+_S$ of copies of
$\widehat{\mathcal O}_S/\overline{\mathcal O^\times_{K,+}}$, and $\mathrm{Cl}^+_S$ is a
*subgroup* of $\mathrm{Cl}^+_{S'}$, not a quotient. The projection is canonical exactly when
$\mathrm{Cl}^+_{S'}=\mathrm{Cl}^+_S$, i.e. when the primes of $S'\setminus S$ have classes in
$\mathrm{Cl}^+_S$ (always true for $K=\mathbb Q$): then
$G_{S'}\to G_S$, $[y]\mapsto[(y\beta^{-1})|_S]$ with $\beta\in K^\times_{S',+}$ chosen so that
$\mathrm{div}(y)\,\mathrm{div}(\beta)^{-1}$ is supported on $S$, is a well-defined continuous
homomorphism, and $[x,g]\mapsto[x|_S,\,\mathrm{pr}(g)]$ is the required $I_S$-equivariant map.
Otherwise a map exists but depends on the choice of a $\mathrm{Cl}^+_S$-equivariant retraction
$\mathrm{Cl}^+_{S'}\to\mathrm{Cl}^+_S$.

Consequences. (i) For a chain $S_1\subseteq S_2\subseteq\cdots$ with union $S$ the finite groups
$\mathrm{Cl}^+_{S_k}$ stabilize, so the direct-limit statement
$\varinjlim\mathcal A_{K,S_k}\cong\mathcal A_{K,S}$ and $G_S=\varprojlim G_{S_k}$ hold as stated,
read along the tail of the chain. (ii) The inclusion $\mathcal A_{K,S}\subseteq\mathcal A_{K,P_K}$
is canonical iff $S$ generates the narrow class group, and otherwise involves a choice.
(iii) Both uses of the proposition in the paper (Sections 5.3 and 6, Sophie Germain primes
and the restriction of BC phases) are over $\mathbb Q$ and are unaffected. Paper II,
Remark 5.1, records the qualification and assumes $\mathrm{Cl}^+_{S_2}=\mathrm{Cl}^+_{S_1}$
throughout its index section.

## Paper II (published)

**Remark 2.3 (resolution note, not a correction).** The remark leaves open whether the
isotropy of the intermediate strata is trivial for general K, calling it a Leopoldt-type
closure question and noting that nothing in the paper depends on it. The question is now
settled in Paper XXIII (Theorem 1.2): the isotropy is identified exactly as the kernel of
the map from T-supported principal divisors to the complementary unit factors modulo the
projected closure of the global units, and it is nontrivial as soon as the unit rank is at
least one with a one-dimensional complementary block — already for real quadratic fields,
unconditionally. Triviality tracks the finiteness of the unit group, not Leopoldt, which
enters only as the rank budget. Every statement of Paper II is unaffected, as the remark
itself anticipated.

**Section 6 (well-definedness of the affine monoid; forward reference).** The semigroup
law of the affine system, scalings by fixed uniformizers, is well defined over O_K only
when the uniformizers are global elements: for non-principal primes the published
definition needs a ray-class enlargement of the acting monoid. Paper XXX of the series
computes the K-theory of the boundary quotient at a principal single prime under this
repair — the divisibility bound (Np-1)[1]=0 of Section 6 is attained exactly there — and
records the non-principal repair as the point where the class group enters. Every
statement of Section 6 stands in the principal case as published.

**Section 6, the divisibility of [1] (correction in the repaired system).** For
non-principal p the well-defined (h-step) affine system of Paper XXXI has Cuntz relation
over O_K/p^h, and the divisibility statement must read (Np^h - 1)[1] = 0, h the order of
[p] in the class group; Paper XXXI proves the order of [1] is exactly Np^h - 1. For
principal p the published statement stands and is attained (Paper XXX).
