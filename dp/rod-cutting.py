# Top down / memoization solution to the rod-cutting problem
import sys
from collections import defaultdict

# for unset key, the default value is -1
memo = defaultdict(lambda: -1)

def rod_cutting(total, prices, lengths):

    if total <= 0:
        return 0

    # if already calculated, return the ans
    if memo[total] != -1:
        return memo[total]

    # To handle the variant of rod cutting where not every pieces may have cost.
    # that is , when length of rod is 10, but we have prices for the pieces of length 1,2,3...
    # but not all pieces
    remPossibleCuts = min(len(lengths), total)

    ans = -sys.maxsize - 1
    for i in range(remPossibleCuts):        
        ans = max(ans, rod_cutting(total - lengths[i], prices, lengths) + prices[i])

    # store this value for future use
    memo[total] = ans
    return ans


if __name__ == "__main__":
    total = int(input("Enter the size of the rod: "))
    lengths = [
        int(x) for x in input("Enter the size of some or all pieces of rod : ").split()
    ]
    prices = [
        int(x) for x in input("Enter the price of above pieces of rod : ").split()
    ]

    ans = rod_cutting(total, prices, lengths)

    print("Max possible cost is : ", ans)
