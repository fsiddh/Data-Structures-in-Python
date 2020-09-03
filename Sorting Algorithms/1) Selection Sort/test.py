def selectionsort(A):
    length = len(A)
    for i in range(0, length-1):
        position = i
        for j in range(i+1, length):
            if A[j] < A[position]:
                position = j
        temp = A[i]             # To SWAP one can also write 
        A[i] = A[position]      # A[i], A[position] = A[position], A[i]
        A[position] = temp


if __name__ == '__main__':
    unsorted_array = [3, 5, 8, 9, 5, 2]
    print('Unsorted Array: ', unsorted_array)
    selectionsort(unsorted_array)
    print('Sorted Array: ',unsorted_array)