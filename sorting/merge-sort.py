def merge(arr, first, mid, last):

    size1 = mid+1-first
    size2 = last-mid

    temp1 = [x for x in arr[first:mid+1]]
    temp2 = [x for x in arr[mid+1:last+1]]   

    idx1 = 0
    idx2 = 0
    idx = first    

    while idx1 < size1 and idx2 < size2:
        if temp1[idx1] < temp2[idx2]:
            arr[idx] = temp1[idx1]
            idx1 += 1
        elif temp2[idx2] <= temp1[idx1]:
            arr[idx] = temp2[idx2]            
            idx2 += 1
        idx += 1

    while idx1 < size1:
        arr[idx] = temp1[idx1]
        idx = idx + 1
        idx1 = idx1 + 1

    while idx2 < size2:
        arr[idx] = temp2[idx2]
        idx = idx + 1
        idx2 = idx2 + 1


def mergeSort(arr, first, last):
    if first < last:
        mid = int(first + (last - first) / 2)        
        mergeSort(arr, first, mid)
        mergeSort(arr, mid+1, last)
        merge(arr, first, mid, last)


if __name__ == "__main__":
    n = int(input("How many numbers ?\t"))
    arr = [int(x) for x in input("Enter {} numbers\t".format(n)).split()]

    mergeSort(arr, 0, n-1)

    for x in arr:
        print(x, end=" ")
    print()
