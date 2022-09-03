def getParent(q, root, h):
    if q == (root - 2**(h - 1)) or q == root - 1:
        return root
    elif q < (root - 2**(h - 1)):
        return getParent(q, (root - 2**(h - 1)), h - 1)
    else:
        return getParent(q, root - 1, h - 1)

def solution(h, q):
    p = []
    if h < 1 or h > 30:
        if len(q) < 1 or len(q) > 10000:
            print("Invalid Input!")
            return None

    root = (2**h) - 1
    for item in q:
        if(item == root or item < 1 or item > root):
            p.append(-1)
        else:
            p.append(getParent(item, root, h))
    return p

if __name__ == "__main__":
    h = 5
    q = [19, 14, 28]
    p = solution(h, q)
    print(p)