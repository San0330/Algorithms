# Kadane's algorithm to find the maximum subarray sum

if __name__ == "__main__":
    arr = [10, 5, -12, 7, -10, 20, 30, -10, 50, 60]
    size = len(arr)

    # To calculate the sum while iterating the array,
    # may reset value if sum is negative
    max_end_here = 0

    # To store the largest possible ans at any instance
    # don't set to 0, as all negative element may also be present where ans < 0
    max_so_far = arr[0]

    for i in range(0, len(arr)):
        # reset if negative
        if max_end_here < 0:
            max_end_here = 0

        # add the array element
        # since we reset earlier,
        # so if current element is negative it won't be replaced by 0 &
        # it may be counted as ans if it is max
        max_end_here += arr[i]

        # if it is max at current instance, store it in max_so_far
        if max_so_far < max_end_here:
            max_so_far = max_end_here

    print(max_so_far)

