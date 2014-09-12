__author__ = 'asjed'


def euler1_():
    sumall = 0
for x in range(1, 1000):
    if x%3 == 0 or x%5 == 0:
     sumall=sum (x)
print(euler1_(x))



def euler2_(n):
    x1 = 1
    x2 = 2
    sum = 0
    for n in range(1, 4000):
        sum =  x1 + x2
    return (sum)
print(sum)