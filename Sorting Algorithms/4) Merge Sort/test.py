def mergesort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mergesort(arr, left, mid)
        mergesort(arr, mid+1, right)
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    i = left
    j = mid+1
    k = left
    B = [0] * (right+1)

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            B[k] = arr[i]
            i += 1
        else:
            B[k] = arr[j]
            j += 1
        k += 1
    
    while i <= mid:
        B[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        B[k] = arr[j]
        j += 1
        k += 1
        
    for i in range(left, right+1):
        arr[i] = B[i]


A = [3, 5, 8, 9, 6, 2]
print('Original Array:',A)
mergesort(A,0,len(A)-1)
print('Sorted Array:',A)