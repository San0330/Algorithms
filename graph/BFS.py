from queue import Queue

if __name__ == "__main__":
    v, e = map(int, input().split())

    g = [[_] for _ in range(v)]

    for i in range(e):
        src, dest = map(int, input().split())
        src -= 1
        dest -= 1
        g[src].append(dest)
        g[dest].append(src)

    q = Queue(v)
    q.put(0)
    visited = [0]

    while not q.empty():
        top = q.get()

        print(top + 1, end=" ")

        for n in g[top]:
            if n not in visited:
                visited.append(n)
                q.put(n)
