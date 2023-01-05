import sys
sys.setrecursionlimit(10**6)    # 파이썬이 정한 최대 재귀 깊이 변경
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

visited = [False] * (n + 1)


def dfs(node):
    visited[node] = True

    for i in range(1, n + 1):
        if not visited[i] and graph[node][i]:
            dfs(i)


count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)