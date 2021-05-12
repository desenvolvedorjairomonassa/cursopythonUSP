import pytest
def factorial (n):
#n = int(input("Digite o valor de n:"))
    if n < 0:
        return 0
    fatorial = 1
    while (1 < n):
        fatorial = fatorial * n
        n -= 1
    return fatorial

def test_factorial ():
    assert factorial(0) == 1
def test_factorial1 ():
    assert factorial(1) == 1
def test_factorial2 ():
    assert factorial(2) == 2
def test_factorial5 ():
    assert factorial(5) == 120
