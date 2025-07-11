import sys
input =sys.stdin.readline
N = int(input())
heap_list = [0]
def heap_pop():
    if len(heap_list) == 2:
        heap_list.pop()
        return

    heap_list[1] = heap_list[-1]
    heap_list.pop()
    downheap(1)

def downheap(ind):
    if ind * 2 < len(heap_list):
        left = ind*2
        small = left
        if ind*2 + 1 < len(heap_list):
            right = ind*2 + 1
            if heap_list[left] > heap_list[right]:
                small = right
        if heap_list[ind] > heap_list[small]:
            heap_list[small],heap_list[ind] = heap_list[ind],heap_list[small]
            downheap(small)

def upheap(ind):
    if 1 >= ind:
        return
    parent = ind //2
    if heap_list[parent] > heap_list[ind]:
        heap_list[parent],heap_list[ind] = heap_list[ind],heap_list[parent]
        upheap(parent)




for i in range(N):
    x = int(input())
    if x == 0:
        if len(heap_list) > 1:
            print(heap_list[1])
            heap_pop()
        else:
            print(heap_list[0])

    else:
        heap_list.append(x)
        upheap(len(heap_list)-1)