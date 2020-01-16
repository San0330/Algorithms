def partition(arr,start,end):
    pivot = arr[end]
    idx = start

    for i in range(start,end):
        if arr[i] < pivot:
            arr[i],arr[idx] = arr[idx],arr[i]
            idx += 1
    
    arr[end],arr[idx] = arr[idx],arr[end]

    return idx


def quickSort(arr, start, end):
    if start < end:
        p = partition(arr,start,end)
        quickSort(arr,start,p-1)
        quickSort(arr,p+1,end)


if __name__ == "__main__":
    arr = [12, 9, 1, 15, 0, 11, 40, 30, 22]    

    quickSort(arr, 0, len(arr) - 1)

    for num in arr:
        print(num, end=" ")
    print()
