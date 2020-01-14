#insertion sort using only for loops
def insertion_sort(nums):    
    for i in range(1,len(nums)):        
            val = nums[i]  
            for j in range(i-1,-2,-1):           
                if (j < 0 or nums[j] < val) : break                                    
                else:                                
                    nums[j+1] = nums[j]
            nums[j+1] = val        
    return nums
    
#insertion sort using while loop
def insertion_sort2(nums):
    for i in range(1,len(nums)):
        val = nums[i]
        pos = i

        while (pos > 0 and val < nums[pos-1]):            
            nums[pos] = nums[pos-1]
            pos = pos - 1
        
        nums[pos] = val

    return nums

if __name__ == "__main__":
        n = int(input("How many numbers ?\t"))    
        nums = [int(x) for x in input("Enter {} numbers\t".format(n)).split()]    
        
        for num in insertion_sort2(nums):
            print(num,end=' ')

        print()