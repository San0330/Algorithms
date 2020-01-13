if __name__ == "__main__":
    n = int(input("How many numbers ?\t"))
    nums = [int(x) for x in input("Enter {} numbers:\t".format(n)).split()]

    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]

    print("The numbers in ascending order are:")
    for num in nums:
        print(num,end=' ')                
    print()

