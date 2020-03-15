import sys

def minKey(keys,visited):
    minValue = sys.maxsize
    minIdx = -1

    for i in range(len(keys)):
        if (not visited[i]) and minValue > keys[i]:
            minValue = keys[i]
            minIdx = i
    
    return minIdx

def prims(graph):
    v = len(graph)

    parent = [-1] * v
    keys = [sys.maxsize] * v
    visited = [False] * v

    keys[0] = 0

    for i in range(v-1):
        u = minKey(keys,visited)
        visited[u] = True

        for node,wt in graph[u]:
            if not visited[node] and keys[node] >  wt:
                keys[node] =  wt
                parent[node] = u

    for i in range(1,len(parent)):
        print(f"{i} -- {parent[i]} :: {keys[i]}")

        
if __name__ == "__main__":
    v,e = map(int,input().split())

    graph = [[] for i in range(v)]
    
    for i in range(e):
        src,dest,wt = map(int,input().split())
        graph[src].append((dest,wt))
        graph[dest].append((src,wt))

    prims(graph)