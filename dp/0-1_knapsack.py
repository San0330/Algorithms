def knapsack(total, wt, val):
    n = len(val)
    k = [[0 for x in range(total + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(total + 1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif wt[i - 1] <= w:
                k[i][w] = max(val[i - 1] + k[i - 1][w - wt[i-1]], k[i - 1][w])
            else:
                k[i][w] = k[i - 1][w]
    return k[n][total]


if __name__ == "__main__":
    totalCap = 12
    val = [10,12,11]
    wt = [5,6,3]

    print(knapsack(totalCap, wt, val))

