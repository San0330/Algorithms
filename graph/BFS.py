from collections import deque

if __name__ == "__main__":
    v, e = map(int, input().split())

    g = [[_] for _ in range(v)]

    for i in range(e):
        src, dest = map(int, input().split())       
        g[src-1].append(dest-1)
        g[dest-1].append(src-1)

    q = deque([0])
    visited = [0]

    while len(q):
        top = q.pop()

        print(top + 1, end=" ")

        for n in g[top]:
            if n not in visited:
                visited.append(n)
                q.appendleft(n)
    print()
