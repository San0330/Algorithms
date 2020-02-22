import enum

# Enum values for colors
class Colors(enum.Enum):
    none = 2
    black = 1
    white = 0


# inverts the color i.e. white to black and black to white
def invert(color):
    return Colors.white if color is Colors.black else Colors.black


def dfs(g, color, src=0):

    # for all neighbours of source node
    for node in g[src]:

        # if node is uncolored , color it with invert of parent color
        if color[node] is Colors.none:
            color[node] = invert(color[src])

            # continue the process by setting current node as parent
            if not dfs(g, color, node):
                # if the process backtracks returning true, continue checking other nodes
                # else backtrack and return false until recursive calls ends
                return False

        # if node is already colored and color[node] == color[src] , return false
        elif color[node] is color[src]:
            return False

    # if no further child nodes for current parent is present,
    # return true & backtrack to parent node
    return True


if __name__ == "__main__":
    v, e = map(int, input().split())
    g = [[] for _ in range(v)]

    for i in range(e):
        src, dest = map(int, input().split())
        g[src - 1].append(dest - 1)
        g[dest - 1].append(src - 1)

    color = [Colors.none] * v
    color[0] = Colors.white

    isBipartite = dfs(g, color)

    print(isBipartite)

