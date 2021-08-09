# merge function merge two arrays
# of different or same length
# if n = max(n1, n2)
# time complexity of merge is (o(n log(n)))

from heapq import merge

# function for meging k arrays
def mergeK(arr, k):
    l = arr[0]
    for i in range(k-1):
        # when k = 0 it merge arr[1]
        # with arr[0] here in l arr[0]
        # is stored
        l = list(merge(l, arr[i + 1]))
    return l

# for printing array
def printArray(arr):
    print(*arr)

# driver code
arr =[[2, 6, 12 ],
    [ 1, 9 ],
    [23, 34, 90, 2000 ]]
k = 3
l = mergeK(arr, k)
printArray(l)