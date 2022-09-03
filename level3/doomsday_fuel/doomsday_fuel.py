from fractions import Fraction
from functools import reduce

def swap(m, i, j):
    if i == j:
        return m

    n = []

    for r in range(len(m)):
        res_row = []
        temp_row = m[r]
        if r == i:
            temp_row = m[j]
        if r == j:
            temp_row = m[i]
        for c in range(len(m)):
            temp_cell = temp_row[c]
            if c == i:
                temp_cell = temp_row[j]
            if c == j:
                temp_cell = temp_row[i]
            res_row.append(temp_cell)
        n.append(res_row)

    return n


def sort(m):
    zero_row = -1
    for row in range(len(m)):

        if not any(m[row]):
            zero_row = row

        if any(m[row]) and zero_row > -1:
            swapped = swap(m, row, zero_row)
            return sort(swapped)

    return m
        
def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

def terminalStateFilter(matrix):
    terminalStates = []

    for row in range(len(matrix)):

        if all(x == 0 for x in matrix[row]):
            terminalStates.append(True)

        else:
            terminalStates.append(False)
            
    return terminalStates

def gcd (a, b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def format_solution(arr):
    arr = [Fraction(state).limit_denominator() for state in arr]
    denom = reduce(lcm, [state.denominator for state in arr])
    return [
               int(state.numerator)
               if state.denominator == denom else
               int(state.numerator * denom / state.denominator)
               for state in arr
           ] + [denom]

def solution(m):
    if len(m) == 1:
        return [1, 1]
    
    for r in range(len(m)):
        s = sum(m[r])
        if s != 0:
            for c in range(len(m[r])):
                m[r][c] /= s
    m = sort(m)
    t = sum([any(row) for row in m])
    Q = [row[:t] for row in m][:t]
    R = [row[t:] for row in m][:t]

    for i in range(len(Q)):
        for j in range(len(Q[i])):
            if i == j:
                Q[i][j] = 1 - Q[i][j]
            else:
                Q[i][j] = -Q[i][j]

    N = inverse(Q)
    B = [[0 for i in range(0, len(R[0]))] for j in range(0, t)]
    for i in range(len(N)):
 
        # iterating by column by B
        for j in range(len(R[0])):
    
            # iterating by rows of B
            for k in range(len(R)):
                B[i][j] += N[i][k] * R[k][j] 

    result = B[0]
    result = format_solution(B[0])
    return result




print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))