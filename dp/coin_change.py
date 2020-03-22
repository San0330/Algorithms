# coin-change problem using bottom-up approach


def cc(n, amount, coins):
    size = n
    table = [[0 for _ in range(amount + 1)] for _ in range(size + 1)]
    # base condition: for any coin if amount = 0, set value to 1
    for i in range(size + 1):
        table[i][0] = 1
    for i in range(1, size + 1):
        for j in range(amount + 1):
            x = 0
            y = 0
            # no. of ways we can get the remaining amount (j - coins[i])
            if j >= coins[i - 1]:
                x = table[i][j - coins[i - 1]]
            # no. of ways we can get the j amount without using current coin
            if i > 0:
                y = table[i - 1][j]
            table[i][j] = x + y
    # print the table generated
    for i in range(size + 1):
        print(table[i])

    return table[size][amount]


# space optimized method
def cc2(n, amount, coins):
    size = n
    table = [0 for _ in range(amount + 1)]

    # base condition
    table[0] = 1

    for c in coins:
        for j in range(c, amount + 1):
            table[j] += table[j - c]

    return table[amount]


if __name__ == "__main__":
    n, amount = map(int, input("Enter number of coins and total amount : ").split())
    coins = [int(x) for x in input(f"Enter {n} coins value : ").split()]

    ans = cc(n, amount, coins)

    print(ans)
