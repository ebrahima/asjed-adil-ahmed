__author__ = 'asjed'


def f(x):
    return x+1


def secant_method(f, a, b, err):
    a=0
    b=1
    c = b-f(a)*(b-a)/(f(b)-f(a))
    while abs (f(a))> err and f(0)!=f(b):
        c = b-f(b)*(b-a)/(f(b)-f(a))
        a=b
        b=c
        root = c
    return root
print(secant_method(f,0,1,0.00001))


def test_secant_method():
    err = 1e-5
    assert 1.5-err < secant_method(f, 0, 1, err) < 1.5+err
