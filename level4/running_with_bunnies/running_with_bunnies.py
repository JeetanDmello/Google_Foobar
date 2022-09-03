import time
from itertools import permutations

def findDistance(graph, src):
    n = len(graph)
    distances = [float('inf')] * n
    distances[src] = 0

    for i in range(n):
        for u in range(n):
            for v in range(n):
                weight = graph[u][v]
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    return distances

def negetiveCycle(graph):
    distance = graph[0]
    n = len(graph)
    for u in range(n):
        for v in range(n):
            weigth = graph[u][v]
            if distance[u] + weigth < distance[v]:
                return True
    return False

def bellmanFord(graph):
    distances = []
    for vertex in range(len(graph)):
        distances.append(findDistance(graph, vertex))

    return distances

def getPathTime(bunnies, graph):
    time = 0
    time += graph[0][bunnies[0]]
    time += graph[bunnies[-1]][len(graph) - 1]
    for i in range(1, len(bunnies)):
        u = bunnies[i - 1]
        v = bunnies[i]
        time += graph[u][v]
    return time

def solution2(times, times_limit):
    n_bunnies = len(times) - 2
    bunnies = [x for x in range(1, n_bunnies + 1)]

    distances = bellmanFord(times)
    if negetiveCycle(distances):
        return range(n_bunnies)

    for i in range(n_bunnies, 0, -1):
        for perm in permutations(bunnies, i):
            time = getPathTime(perm, distances)
            if time <= times_limit:
                return [x - 1 for x in sorted(perm)]
    return[]

if __name__ == "__main__":
    sol = solution2([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
    print(sol)