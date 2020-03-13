# Weight of the minimum spanning tree of a graph using disjoint set

# get the root node i.e. node with no parent
# also assign each intermediate nodes with found root node,
# so that intermediate nodes directly points to root node on next iteration
def findParent(x, parent):
    if x is parent[x]:
        return x
    parent[x] = findParent(parent[x], parent)
    return parent[x]


# combine the two nodes as single group by having their parents same
def unite(s1, s2, parent, rank):
    s1 = findParent(s1, parent)
    s2 = findParent(s2, parent)

    if rank[s1] > rank[s2]:
        parent[s2] = s1
    elif rank[s2] > rank[s1]:
        parent[s1] = s2
    else:
        parent[s1] = s2
        rank[s2] += 1


def kruskal(g, v, e):

    # intially each node is their own parent i.e. every node is disjoint
    parent = [i for i in range(v)]

    # rank is 0, higher rank nodes will be parent of lower rank nodes on unite function
    # node with more children have higher ranks
    # reassigning the parent node (of higher rank nodes) to lower rank node will be less iterative
    # than reassigning the parent node (of lower rank nodes) to higher rank nodes
    rank = [0 for i in range(v)]

    totalWt = 0

    for i in range(e):
        wt, src, dest = g[i]

        # if disjoint, sum the wt and unite them,
        # may save these nodes in a variable to detect which nodes makes the spanning tree.
        if findParent(src, parent) is not findParent(dest, parent):
            unite(src, dest, parent, rank)
            totalWt += wt

    return totalWt


if __name__ == "__main__":
    v, e = map(int, input().split())

    g = []
    for i in range(e):
        src, dest, wt = map(int, input().split())
        g.append((wt, src - 1, dest - 1))

    g.sort()

    ans = kruskal(g, v, e)
    print(f"The wt of the min spanning tree is {ans}")
