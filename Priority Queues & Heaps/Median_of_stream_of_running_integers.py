import heapq as heap

def isempty(heap_list):
    return len(heap_list) == 0

def mosori(elem, first_half, second_half):
    # num = 0 # Number Inserted recently


    if isempty(first_half) or first_half[0]*-1 > elem:
        heap.heappush(first_half, -1*elem)
    else:
        heap.heappush(second_half, elem)

    if len(first_half) > len(second_half)+1:
        heap.heappush(second_half, -1*heap.heappop(first_half))
    elif len(second_half) > len(first_half)+1:
        heap.heappush(first_half, -1*heap.heappop(second_half))

    if len(first_half) == len(second_half):
        median = ((first_half[0]*-1)+(second_half[0]))/2
        print(median)
    elif len(first_half) > len(second_half)    :
        median = first_half[0]*-1
        print(median)
    else:
        median = second_half[0]
        print(median)


if __name__ =='__main__':
    first_half = []  # Here I'll maintain max heap
    second_half = []  # Here I'll maintain min heap

    heap.heapify(first_half)  # heapify convert a list into a heap ds
    heap.heapify(second_half)

    print('Please enter the element to insert(Or enter -1 to quit):')
    elem = 0
    
    while elem != -1:
        elem = int(input())

        if elem == -1:
            print('The MOSORI algorithm has successfully terminated!')
            break
        
        mosori(elem, first_half, second_half)
        