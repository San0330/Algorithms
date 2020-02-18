from collections import deque

if __name__ == "__main__":
    v, e = [int(x) for x in input().split()]
    g = [[_] for _ in range(v)]

    for i in range(e):
        src, dest = map(int, input().split())
        g[src-1].append(dest-1)
        g[dest-1].append(src-1)

    stack = deque([0])
    visited = [0]

    while len(stack):
        top = stack.pop()
        print(top+1, end=' ')

        for node in g[top]:
            if node not in visited:
                stack.append(node)
                visited.append(node)
        
    print()