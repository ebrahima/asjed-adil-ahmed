__author__ = 'asjed'

def f(x):
    return 2 + x + x**2


def trap_meth(f, a, b, N):
    h = (b-a)/N
    y = 0
    for i in range(1, N):
        a =a+ h
        y = y + 2*f(a)
        ans = h/2 * (y-f(b)-f(a))
    return ans

print(trap_meth(f, 0, 1, 100))


def test_trap_meth():
    err = 1e-6
    assert 2.826334999500009-err < trap_meth(f, 0, 1, err) < 2.826334999500009+err





