# Kadane's algorithm to find the maximum subarray sum

if __name__ == "__main__":
    arr = [10, 5, -12, 7, -10, 20, 30, -10, 50, 60]
    size = len(arr)

    max_end_here = 0
    max_so_far = arr[0]

    for i in range(0, len(arr)):
        if max_end_here < 0:
            max_end_here = 0
        max_end_here += arr[i]
        if max_so_far < max_end_here:
            max_so_far = max_end_here

    print(max_so_far)

