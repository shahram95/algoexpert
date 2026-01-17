from math import sqrt

def getNthFib(n):
    sqrt5 = sqrt(5)
    phi = (1+sqrt5)/2
    psi = (1-sqrt5)/2
    count = (phi**(n-1) - psi**(n-1))//sqrt5
    return count