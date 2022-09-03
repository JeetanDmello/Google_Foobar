from decimal import Decimal, getcontext

def sol(n, r, s):
    if  n == 0:
        return 0
    N = int(n * r)
    m = int(Decimal(N) / s)
    return ((N * (N + 1)) / 2) - sol(m, r, s) - (m * (m + 1))

def solution(str_n):
    n = Decimal(str_n)
    if n < 0:
        return "ERROR"
    getcontext().prec = 101
    r = Decimal(2).sqrt()
    s = r / (r - 1)
    return str(int(sol(n, r, s)))

