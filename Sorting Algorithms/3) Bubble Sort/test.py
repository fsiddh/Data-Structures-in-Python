def bubblesort(A):
    length = len(A)

    for i in range(0, length):
        for j in range(1, length):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]

if __name__ == '__main__':
    A = [1,3,4,2]
    bubblesort(A)

    print(A)
    