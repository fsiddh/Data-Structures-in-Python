import heapq as heap

l = [-5,-1,-2,-4,-0,-3]

heap.heapify(l)

print(heap.heappop(l))
print(l)
print(len(l))

print(l[0])