
def dfs(g, visited=[], start=0):
    visited.append(start)

    print(start+1, end=' ')

    for node in g[start]:
        if node not in visited:
            dfs(g, visited, node)


if __name__ == "__main__":
    v, e = [int(x) for x in input().split()]
    g = [[_] for _ in range(v)]

    for i in range(e):
        src, dest = map(int, input().split())
        g[src-1].append(dest-1)
        g[dest-1].append(src-1)

    dfs(g)
    print()
