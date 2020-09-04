def bubblesort(A):
    length = len(A)

    for i in range(0, length):
        swap = False
        for j in range(0, length-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swap = True
        if swap == False:
            break

if __name__ == '__main__':
    A = [64,34,25,12,22,11,90]
    bubblesort(A)

    print(A)
    