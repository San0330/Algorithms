def knapsack(total, wt, val):
    n = len(val)

    # make a table to store solution for x totalCapacity & y items cost
    k = [[0 for _ in range(total + 1)] for _ in range(n + 1)]

    # i = current item being observed 
    for i in range(n + 1):

        # w = current capacity of the knapsack
        for w in range(total + 1):

            # if either current item's wt = 0 or current totalCapacity of knapsack is 0,store 0
            if i == 0 or w == 0:
                k[i][w] = 0

            # if wt of current item is less than wt of knapsack, either include the item or exclude it
            # if including item gets more value, get the cost of item and add it to previous item's (i-1) cost when capacity = w - wt[i-1] 
            # else store the value of the previous item (i-1) for weight = w
            elif wt[i - 1] <= w:
                k[i][w] = max(val[i - 1] + k[i - 1][w - wt[i-1]], k[i - 1][w])
            
            # if wt of current item is more than current capacity of knapsack, 
            # store the value of previous item (i-1) for weight = w
            else:
                k[i][w] = k[i - 1][w]

    return k[n][total]


if __name__ == "__main__":
    totalCap = 10   
    wt = [2, 3, 4, 1, 3]
    val = [12, 11, 5, 2, 13]


    print(knapsack(totalCap, wt, val))
