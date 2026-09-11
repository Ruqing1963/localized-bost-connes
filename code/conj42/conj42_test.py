"""
Numerical test of Conjecture 4.2 (Paper XXIX): does the degree-1 odd Walsh chaos
saturate the truncated distance W_1^{(N)}?

Model (after the odd reduction f = chi(g) h(x), Prop 4.1):
  maximize   2 * sum_x mu(x) * h(x) * prod_j (-1)^{x_j}
  subject to 4 h(x)^2 / w0^2 + sum_j (h(x+e_j)-h(x))^2 / w_j^2 <= 1   for every x
with mu = product of Geometric(1-t_j) on {0..M}^N (Neumann at x_j = M).

Three quantities per N:
  (A) degree-1 closed form  Pi_N * sqrt(w0^2 + sum_j w_j^2 kappa_j^2),  kappa_j = 2t_j/(1-t_j)
  (B) parity-measurable optimum: h depends only on parities pi in {0,1}^N.  A forward step
      always flips parity, so the pointwise constraint closes EXACTLY on the 2^N parity
      classes (no M-truncation): 4 h(pi)^2/w0^2 + sum_j (h(pi^j)-h(pi))^2/w_j^2 <= 1.
      This is the value of the full odd-chaos hierarchy at level N (Conjecture 4.2's object).
  (C) full grid optimum on {0..M}^N.
Interpretation: (C) > (B)  <=> the optimizer is NOT parity-measurable (open question (c));
               (B) > (A)  <=> higher-degree chaos genuinely participates.
The feasible set is convex and the objective linear, so any KKT point is the global max;
SLSQP from a feasible interior start therefore certifies the optimum (up to tolerance).
"""
import itertools, numpy as np
from scipy.optimize import minimize, NonlinearConstraint

w0 = 1.0
def weights(N): return np.array([1.0/(j+2) for j in range(N)])      # w_j=(j+1)^-1, j=1..N
def tees(N):    return np.array([1/2, 1/3, 1/5][:N])                # t_j = p_j^{-1}

def closed_form(N):
    w, t = weights(N), tees(N)
    m = (1-t)/(1+t); kap = 2*t/(1-t)
    assert w0**2 >= np.sum(w**2*kap), "interior condition"
    return np.prod(m)*np.sqrt(w0**2 + np.sum(w**2*kap**2)), np.prod(m)

def solve_socp(points, nbr, mu, sign, w, x0):
    """max 2*sum mu*sign*h  s.t. per-point cone; nbr[i][j] = index of x+e_j or -1 (Neumann)."""
    P, N = len(points), len(w)
    c = 2*mu*sign
    def cons(h):
        g = 1 - 4*h**2/w0**2
        for j in range(N):
            k = nbr[:, j]
            d = np.where(k >= 0, h[np.maximum(k, 0)] - h, 0.0)
            g -= d**2/w[j]**2
        return g
    def cons_jac(h):
        J = np.zeros((P, P)); J[np.arange(P), np.arange(P)] = -8*h/w0**2
        for j in range(N):
            k = nbr[:, j]; msk = k >= 0; i = np.arange(P)[msk]; kk = k[msk]
            d = h[kk] - h[i]
            J[i, i] += 2*d/w[j]**2; J[i, kk] -= 2*d/w[j]**2
        return J
    res = minimize(lambda h: -c @ h, x0, jac=lambda h: -c, method="SLSQP",
                   constraints=[NonlinearConstraint(cons, 0, np.inf, jac=cons_jac)],
                   options=dict(maxiter=800, ftol=1e-14))
    viol = max(0.0, -cons(res.x).min())
    return -res.fun, viol, res.x

def parity_program(N):
    w, t = weights(N), tees(N)
    pts = list(itertools.product([0, 1], repeat=N))
    idx = {p: i for i, p in enumerate(pts)}
    nbr = np.array([[idx[tuple(1-p[j] if jj == j else p[jj] for jj in range(N))]
                    for j in range(N)] for p in pts])
    Pev = 1/(1+t); mu = np.array([np.prod(np.where(np.array(p) == 0, Pev, 1-Pev)) for p in pts])
    sign = np.array([(-1)**sum(p) for p in pts], float)
    x0 = 0.05*sign*w0/2
    return solve_socp(pts, nbr, mu, sign, w, x0)

def grid_program(N, M):
    w, t = weights(N), tees(N)
    pts = list(itertools.product(range(M+1), repeat=N))
    idx = {p: i for i, p in enumerate(pts)}
    nbr = np.array([[idx.get(tuple(p[jj]+(jj == j) for jj in range(N)), -1)
                    for j in range(N)] for p in pts])
    mu = np.array([np.prod([(1-t[j])*t[j]**p[j] for j in range(N)]) for p in pts])
    sign = np.array([(-1)**sum(p) for p in pts], float)
    x0 = 0.05*sign*w0/2
    return solve_socp(pts, nbr, mu, sign, w, x0)

for N in (1, 2, 3):
    A, PiN = closed_form(N)
    B, vB, _ = parity_program(N)
    print(f"N={N}:  (A) degree-1 closed form = {A:.10f}")
    print(f"       (B) parity-measurable opt = {B:.10f}   (viol {vB:.1e})   B-A = {B-A:+.3e}")
    for M in (6, 9):
        C, vC, _ = grid_program(N, M)
        print(f"       (C) full grid  M={M}      = {C:.10f}   (viol {vC:.1e})   C-B = {C-B:+.3e}")
    print()

# Apples-to-apples: parity-restricted optimum ON THE SAME truncated grid (same Neumann
# boundary, same truncated measure), so C_full - C_parity isolates non-parity gain exactly.
def grid_parity(N, M):
    import itertools
    w, t = weights(N), tees(N)
    pts = list(itertools.product(range(M+1), repeat=N))
    mu = np.array([np.prod([(1-t[j])*t[j]**p[j] for j in range(N)]) for p in pts])
    sign = np.array([(-1)**sum(p) for p in pts], float)
    pi = np.array([[p[j] % 2 for j in range(N)] for p in pts])
    pidx = np.array([int("".join(map(str, r)), 2) for r in pi])
    P2 = 2**N
    c2 = np.zeros(P2)
    for i, s in enumerate(sign): c2[pidx[i]] += 2*mu[i]*s
    def expand(hp): return hp[pidx]
    def cons(hp):
        h = expand(hp); g = 1 - 4*h**2/w0**2
        for j in range(N):
            nb = [tuple(p[jj]+(jj == j) for jj in range(N)) for p in pts]
            ok = np.array([q[j] <= M for q in nb])
            hq = np.array([hp[int("".join(str(q[jj] % 2) for jj in range(N)), 2)] if o else 0
                           for q, o in zip(nb, ok)])
            d = np.where(ok, hq - h, 0.0)
            g -= d**2/w[j]**2
        return g
    from scipy.optimize import minimize, NonlinearConstraint
    res = minimize(lambda hp: -c2 @ hp, 0.05*np.array([(-1)**bin(k).count("1") for k in range(P2)]),
                   jac=lambda hp: -c2, method="SLSQP",
                   constraints=[NonlinearConstraint(cons, 0, np.inf)],
                   options=dict(maxiter=600, ftol=1e-14))
    return -res.fun, max(0.0, -cons(res.x).min())

print("Apples-to-apples on the truncated grid (isolates the non-parity gain):")
for N in (1, 2, 3):
    for M in (6, 9):
        Cp, vp = grid_parity(N, M)
        Cf, vf, _ = grid_program(N, M)
        print(f"  N={N} M={M}: C_parity={Cp:.10f}  C_full={Cf:.10f}  gain={Cf-Cp:+.3e}  (viol {vp:.0e}/{vf:.0e})")
