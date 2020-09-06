import heapq as heap

def mosori(elem, first_half, second_healf):
    num = 0 # Number Inserted recently

    if first_half.

if __name__ =='__main__':
    first_half = []  # Here I'll maintain max heap
    second_healf = []  # Here I'll maintain min heap

    heap.heapify(first_half)  # heapify convert a list into a heap ds
    heap.heapify(second_healf)

    print('Please enter the element to insert(Or enter -1 to quit):')
    elem = int(input())
    
    while elem != -1:
        mosori(elem, first_half, second_healf)
    if elem == -1:
        print('The MOSORI algorithm has successfully terminated!')