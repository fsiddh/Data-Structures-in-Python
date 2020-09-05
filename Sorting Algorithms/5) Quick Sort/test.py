def partition(A, lb, ub):
    pivot = A[lb]
    start = lb
    end = ub

    while start < end:
        while A[start]<=pivot:
            start += 1
        while A[end]>pivot:
            end -= 1
        if start < end:
            A[start], A[end] = A[end], A[start]
        else:
            break
    A[lb], A[end] = A[end], A[lb]
    return end

def quicksort(A, lb, ub):
    if lb < ub:
        loc = partition(A, lb, ub)
        quicksort(A, lb, loc-1)
        quicksort(A, loc+1, ub)


A = [5,2,1,6,4,8]
print(A)
quicksort(A, 0, 5)
print(A)