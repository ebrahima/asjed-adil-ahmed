__author__ = 'asjed'



def f(x):
    return x**2+1


def simp_meth(f, a, b, N):
    h = (b-a)/N
    s = f(a)+f(b)
    for i in range(1, N, 2):
        s += 4*f(a+(i*h))
    for i in range(2, N-1, 2):
        s += 2*f(a+(i*h))
    return (h/3) * s

print(simp_meth(f,0,1,10))