import enum
from collections import deque

# Enum values for colors
class Colors(enum.Enum):
    none = 2
    black = 1
    white = 0


# inverts the color i.e. white to black and black to white
def invert(color):
    return Colors.white if color is Colors.black else Colors.black


if __name__ == "__main__":

    # v - vertices , e - edges
    v, e = map(int, input().split())

    # adjacency list to store connected paths, 2d lists
    g = [[] for i in range(v)]

    for i in range(e):
        src, dest = map(int, input().split())
        g[src - 1].append(dest - 1)
        g[dest - 1].append(src - 1)

    # initialize all colors with none, none also means unvisited nodes
    color = [Colors.none for _ in range(v)]

    # set the color of source vertex ( root node ) to white or black
    color[0] = Colors.white

    # set this to false if graph is not bipartite
    isBipartite = True

    # initialize queue and add the root node
    q = deque()
    q.append(0)

    # while q is not empty and graph is bipartite, continue
    while len(q) and isBipartite:

        # pop the parent node and get it's color
        p = q.popleft()
        pColor = color[p]

        # for all the node connected to that parent node
        for node in g[p]:

            # assign the invert color of parent node to child node, if it is colorless/unvisited
            if color[node] is Colors.none:
                color[node] = invert(pColor)
                # append visited node to queueu
                q.append(node)

            # if child is already colored/visited, and child's color is same as parent's color
            # graph is not bicolorable (bipartite)
            elif color[node] is pColor:
                # set isBipartite to false and break inner loop(for loop)
                # when isBipartite is set to false, the outer loop (while loop) is also broken
                isBipartite = False
                break

    # print the result
    print("Graph is bicolorable : ", isBipartite)
