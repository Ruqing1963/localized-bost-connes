# Proof dependency map

How the main theorem is assembled, and which external results it rests on.

```
                  external inputs
                  ---------------
   Laca, dilation theorem  ──┐
   Neshveyev, groupoid KMS ──┴──▶  Prop 2.7  (KMS states = scaling measures)
                                        │
   class field theory ─▶ Lemma 2.2 ─▶ Prop 2.4  (structure of G_S)
                                        │
                                        ▼
                                   Lemma 2.9
                        (coordinates (v,g); marginal of v is FORCED;
                         cocycle equation rho_{v+a} = (sigma_a)_* rho_v)
                                        │
              ┌─────────────────────────┼─────────────────────────┐
              ▼                         ▼                         ▼
   Kolmogorov 0–1 law          martingale convergence     explicit construction
        Lemma 3.1                    Prop 3.3                   Prop 3.4
   (|f_chi| is constant)         (NECESSITY of the          (SUFFICIENCY: builds
                                  summability condition)     a second KMS state)
              └─────────────────────────┼─────────────────────────┘
                                        ▼
                              ═══════════════════
                                   THEOREM 3.6
                        KMS simplex = Prob(G_S / Xi_beta^perp)
                              ═══════════════════
                                        │
                      ┌─────────────────┴─────────────────┐
                      ▼                                   ▼
              Lemma 3.8 (Frobenius)              Lemma 3.5 (Xi is a
                      │                           subgroup, monotone in beta)
                      ▼                                   │
               THEOREM 3.9                                │
        Chebotarev splitting criterion                    │
                      │                                   │
        ┌─────────────┼─────────────┐                     │
        ▼             ▼             ▼                     ▼
   Cor 3.10      Prop 4.1      Thm 4.10             Prop 4.15
   (classical    (unramified   (density is          (cascades of
    systems,      class-group   not enough;          transitions)
    via           obstruction;  Prop 4.12
    Chebotarev)   Ex 4.2 over   gives Psi)
                  Q(sqrt(-5)))
                                        │
                                        ▼
                                   Thm 5.2, 5.5
                              (sparse sets; closed phase;
                               Sophie Germain, conditional)
```

## The two halves of Theorem 3.6

The theorem is an "if and only if" and each direction has its own engine.

**Necessity (Prop 3.3).** If a nontrivial character survives, its normalized
Fourier coefficient $g=f_\chi/|f_\chi|$ solves the cohomological equation
$g(v+e_\mathfrak{p})=c_\mathfrak{p}g(v)$. Conditioning on finitely many
coordinates and applying martingale convergence forces
$\prod_\mathfrak{p}|m_\mathfrak{p}|$ to converge to a nonzero limit — a Kakutani
product criterion — which is exactly the summability condition defining
$\Xi_\beta$.

**Sufficiency (Prop 3.4).** Conversely, if the condition holds, the infinite
product $\prod\tilde X_\mathfrak{p}$ converges almost surely (it is an
$L^2$-bounded martingale after normalization), producing a solution $g_\chi$;
the measure with density $1+\mathrm{Re}(\overline{g_\chi}\chi)$ is then a second
KMS state.

Bochner's theorem on the discrete group $\Xi_\beta$ assembles the two into the
statement that the simplex is $\mathrm{Prob}$ of the compact dual.

## Where each classical theorem sits

- **Bost–Connes uniqueness for $0<\beta\le1$**: Cor 3.10 with $K=\mathbb{Q}$.
  The input is Dirichlet's theorem; equivalently (Remark 3.11)
  $L(1,\chi)\neq0$.
- **Laca–Larsen–Neshveyev for a number field**: Cor 3.10 in general. The input
  is Chebotarev.
- **The low-temperature phase**: Thm 3.6(2), which is the case
  $\Xi_\beta=\widehat{G_S}$.

So the two classical regimes are the two extreme values of a single invariant,
and everything between them is new territory.
