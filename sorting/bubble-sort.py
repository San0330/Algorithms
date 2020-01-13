if __name__ == "__main__":
    n = int(input("How many numbers ?\t"))
    nums = [int(x) for x in input("Enter {} numbers\t".format(n)).split()]

    for i in range(n-1):       
        for j in range(n-i-1):
            if(nums[j] > nums[j+1]):
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    for i in nums:
        print(i,end=' ')
    
    print()

    