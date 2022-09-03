def explode(m, f, cycles):
    if f == m == 1:
        return str(cycles)
    elif f == 0 or m == 0 or f == m != 1:
        return "impossible"

    if m > 100 or f > 100:
        if f > m:
            if m == 1:
                return cycles + int(f / m) - 1
            cycles += int(f / m)
            return explode(m, f - m * int(f / m), cycles)
        else:
            if f == 1:
                return cycles + int(f / m) - 1
            cycles += int(m / f)
            return explode(m - f * int(m / f), f, cycles)
    else:
        if f > m:
            cycles += 1
            return explode(m, f - m, cycles)
        else:
            cycles += 1
            return explode(m - f, f, cycles)

def solution(M, F):
    if int(M) > 10**50 or int(F) > 10**50:
        return "impossible"

    return explode(int(M), int(F), 0)

if __name__ == "__main__":
    M = '4'
    F = '7'
    outpt = solution(M, F)
    print(outpt)