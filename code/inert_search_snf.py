# Paper XXXVIII: generator search and Smith normal forms for the inert local model.
# O_H = Z[i,phi], phi=(1+sqrt5)/2; basis (1,i,phi,i*phi).
# Output: Pi = -3-i+2*phi+i*phi, N=+9, Tr=-8, det(mult)=+9.
# SNF of 9I-Lambda^r(Pi), prime-to-3 regularized cokernels:
#   r=1: Z/5+Z/5+Z/61 (det 13725);  r=2: Z/2+Z/2+Z/5+Z/7+Z/11 (det -1122660);
#   r=3: Z/29 (det 21141).
import sympy as sp
from itertools import product, combinations
from sympy.matrices.normalforms import smith_normal_form as SNF
i5=sp.sqrt(5)
def NQ(v):
    a,b,c,d=v; P=1
    for si,sf in [(1,1),(-1,1),(1,-1),(-1,-1)]:
        I=sp.I*si; ph=(1+sf*i5)/2; P*=a+b*I+c*ph+d*I*ph
    return sp.expand(P)
hit=next(v for v in product(range(-3,4),repeat=4)
         if v!=(0,0,0,0) and not all(x%3==0 for x in v) and sp.simplify(NQ(v))==9)
a,b,c,d=hit
cols=[[a,b,c,d],[-b,a,-d,c],[c,d,a+c,b+d],[-d,c,-(b+d),a+c]]
A=sp.Matrix(4,4,lambda r,s: cols[s][r])
def compound(M,k):
    idx=list(combinations(range(4),k))
    return sp.Matrix(len(idx),len(idx),lambda r,s: M[idx[r],idx[s]].det() if k>1 else M[r,s])
print('Pi =',hit,' detA =',A.det(),' Tr =',A.trace())
for r in (1,2,3):
    D=9*sp.eye([4,6,4][r-1])-compound(A,r)
    S=SNF(D); print(r, D.det(), [S[k,k] for k in range(S.shape[0])])
