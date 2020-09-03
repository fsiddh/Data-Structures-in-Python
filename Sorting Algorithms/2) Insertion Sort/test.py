def insertionsort(A):
    length = len(A)
    for i in range(1, length):
        current_value = A[i]
        position = i
        while position > 0 and A[position-1] > current_value:
            A[position] = A[position-1]
            position -= 1
        A[position] = current_value

if __name__ == '__main__':
    array = [3, 5, 8, 9, 5, 2]
    print('Unsorted Array: ',array)
    insertionsort(array)
    print('Sorted Array: ', array)