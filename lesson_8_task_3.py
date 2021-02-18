# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
import random

n=int(input('количество вершин графа: '))
def graph(n):
    x = dict.fromkeys([f'{i}' for i in range(n)])
    for key in x.keys():
        for i in range(len(x)):
            links = [f'{random.randint(0, 1)}' for _ in range(n) ]
            links[i]='0'
            x[key] = links
    return x
g=graph(n)
print(graph(n))

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in set(graph[start]) - set(visited):
        dfs(graph, next, visited)
    return visited
print(dfs(g,'2'))