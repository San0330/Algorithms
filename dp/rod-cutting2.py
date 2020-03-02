# bottom-up solution to the rod-cutting problem

def rod_cutting(total, prices, lengths):

    # initialize an array of size "total+1" to zero
    # it stores the max cost for a rod of size x
    val = [0] * (total + 1)

    # for every possible size of rod starting from 1
    for i in range(1, total + 1):
        # initialize ans(maxsize for rod of length i) to 0
        ans = 0

        # iterate over the all the possible lenght pieces
        for j in range(len(lengths)):

            # if current total length (i) is greater than piece's length
            if i >= lengths[j]:

                # set ans to store the max  of previous value or
                # current piece's price + remaining piece price
                ans = max(ans, val[i - lengths[j]] + prices[j])

        # store the value at index i, max possible price for rod of length i
        val[i] = ans

    # return the max price for rod of length total
    return val[total]


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
