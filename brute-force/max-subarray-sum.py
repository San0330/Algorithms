# finding the max subarray sum using bruteforce method:

import sys  # to get the minimum value


def maxsubarraysum(arr):
    # initially set m to min possible value
    m = -sys.maxsize - 1

    # i determines the start
    for i in range(0, len(arr)):
        # j determines the end
        for j in range(i, len(arr)):
            # set sum to 0 and find sum of array[i] to array[j]
            sum = 0
            # k loops from i to j and finds sum in that section
            for k in range(i,j+1):                
                sum += arr[k]
            # sum in that section is saved to m only if it is max than previous sum
            m = max(m, sum)

    return m


# minor improvement on the brute-force algorithm
# instead of looping from i to j and finding sum, we may add a single new element to previous sum

def maxsubarraysum2(arr):
    m = -sys.maxsize - 1
    for i in range(0, len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            m = max(m, sum)
    return m


if __name__ == "__main__":

    arr = [int(x) for x in input().split()]

    print(maxsubarraysum(arr))
    print(maxsubarraysum2(arr))
