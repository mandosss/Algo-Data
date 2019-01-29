import heapq

treeArray = [1,3,4,7,9,0,99,4,7,10]

heapq._heapify_max(treeArray)

print("new  max heap: %s" % ", ".join(map(str, treeArray)))

#using this lib and depending whether is a min or max queue,
#a corresponding pop method should be used. 
print("max popped: %d" % heapq._heappop_max(treeArray))

print("after pop: %s" % ", ".join(map(str, treeArray)))
