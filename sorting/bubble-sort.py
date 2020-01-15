if __name__ == "__main__":
    n = int(input("How many numbers ?\t"))
    nums = [int(x) for x in input("Enter {} numbers\t".format(n)).split()]    

    for i in range(n-1):       

        #set changed to false, false means no swapping of elements occured
        changed = False

        for j in range(n-i-1):
            if(nums[j] > nums[j+1]):
                nums[j],nums[j+1] = nums[j+1],nums[j]              
                changed = True             #some element is swapped

        #if no element is swapped then no need for further looping , break outer loop
        if not changed :             
            break

    for i in nums:
        print(i,end=' ')
    
    print()

    