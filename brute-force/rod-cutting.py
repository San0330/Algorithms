# Brute-force solution to the rod-cutting problem
import sys


def rod_cutting(total, prices, lengths):

    if total <= 0:
        return 0

    # To handle the variant of rod cutting where not every pieces may have cost.
    # that is , when length of rod is 10, but we have prices for the pieces of length 1,2,5...
    # but not all pieces
    remPossibleCuts = min(len(prices), total)

    ans = -sys.maxsize - 1
    for i in range(remPossibleCuts):
        ans = max(ans, rod_cutting(
            total-lengths[i], prices, lengths)+prices[i])

    return ans


if __name__ == "__main__":
    total = int(input("Enter the size of the rod: "))
    lengths = [int(x) for x in input(
        "Enter the size of some or all pieces of rod : ").split()]
    prices = [int(x) for x in input(
        "Enter the price of above pieces of rod : ").split()]

    ans = rod_cutting(total, prices, lengths)

    print("Max possible cost is : ", ans)
