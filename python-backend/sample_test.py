def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def test_fib():
    assert fib(1) == 1
    assert fib(0) == 0
    assert fib(2) == 1
    # assert fib(3) == 1
