def solution(s):
    if len(s) < 1 or len(s) > 100:
        return None

    s = s.replace('-', '')
    length = len(s)
    goingRight = 0
    salute = 0
    for j in range(0, length):
        if s[j] == '>':
            goingRight += 1
        elif s[j] == '<':
            salute = salute + 2 * goingRight
    return salute

if __name__ == "__main__":
    salute = solution("<<>><")
    print(salute)

