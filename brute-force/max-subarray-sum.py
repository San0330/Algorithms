# finding the max subarray sum using bruteforce method:

def maxsubarraysum(arr):
    m = -10000
    for i in range(0, len(arr)):             # i determines the start
        for j in range(i, len(arr)):         # j determines the end
            # set sum to 0 and find sum of array[i] to array[j]
            sum = 0
            for k in range(j, len(arr)-i):   # k loops from i to j and finds sum in that section
                sum += arr[k]
                m = max(m, sum)

    return m

# minor improvement on the brute-force algorithm
# instead of looping from i to j and finding sum, we may add a single new element to previous sum


def maxsubarraysum2(arr):
    m = -10000
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
