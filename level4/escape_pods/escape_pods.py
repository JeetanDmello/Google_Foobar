def Preflow(s, G):
    ver = [{"h": 0, "e": 0} for r in range(len(G))]
    edge = [[{"f": 0, "c": G[r][j]} for j in range(len(G[r]))]for r in range(len(G))]
    for ele in s:
        ver[ele]["h"] = len(G)
    for ele in s:
        for c in range(len(edge[ele])):
            if edge[ele][c]["c"] > 0:
                edge[ele][c]["f"] =  edge[ele][c]["c"]
                edge[c][ele]["c"] = edge[ele][c]["c"]
                ver[c]["e"] += edge[ele][c]["c"]

    return ver, edge

def checkExcess(s, t, ver):
    vertex = [node for node in range(len(ver)) if node not in s and node not in t and ver[node]["e"] > 0]
    return vertex if len(vertex) > 0 else False

def getNode(cE, ver):
    maxi = 0
    maxNode = cE[0]
    for ele in range(len(cE)):
        if ver[ele]["h"] > maxi:
            maxi = ver[ele]["h"]
            maxnode = ele
    return maxNode

def checkPush(ver, edge, node):
    adjNodes = [c for c in range(len(edge[node])) if edge[node][c]["c"] > 0]
    adjNodes = [c for c in adjNodes if ver[node]["h"] == ver[c]["h"] + 1]
    if len(adjNodes) == 0:
        return False
    res = False
    for ele in adjNodes:
        if edge[node][ele]["c"] != edge[node][ele]["f"]:
            res = ele
    return res

def Push(ver, edge, u, v, s, t):
    delta = min(ver[u]["e"], edge[u][v]["c"] - edge[u][v]["f"])
    ver[u]["e"] -= delta
    edge[u][v]["f"] += delta
    edge[v][u]["c"] += delta
    if v not in s:
        ver[v]["e"] += delta
    return ver, edge

def Relabel(ver, u):
    ver[u]["h"] += 1
    return ver

def solution(s, t, G):
    
    ver, edge = Preflow(s, G)

    cE = checkExcess(s, t, ver)
    while cE:
        node = getNode(cE, ver)
        cP = checkPush(ver, edge, node)
        if str(cP).isdigit():
            ver, edge = Push(ver, edge, node, cP, s, t)
        else:
            ver = Relabel(ver, node)
        cE = checkExcess(s, t, ver)

    res = 0
    for ele in t:
        res += ver[ele]["e"]
    
    return res


if __name__ == "__main__":
    s = solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    print(s)