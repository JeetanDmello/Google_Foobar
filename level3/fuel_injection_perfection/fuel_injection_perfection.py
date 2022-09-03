def solution(n):
    n = int(n)
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        elif n % 3 == 0 or n % 4 == 1:
            n = n - 1
        else:
            n = n + 1
        count += 1
    return count

if __name__ == "__main__":
    n = 4
    res = solution(n)
    print(res)