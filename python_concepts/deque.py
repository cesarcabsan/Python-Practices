import collections
from collections import deque

#adding items to queue left and right
queue = deque(['game', 'name', 'time'])
queue.append('prime')
print('Add item to the right of', queue)
queue.appendleft('frame')
print('Add item to the left of', queue)

#remove items 
queue2 = deque(['Item1', 'Item2', 'Item3'])
queue2.pop()
print("Removed item from right", queue2)
queue2.popleft()
print('Removed item from left', queue2)

#size of deque
de = deque([1,2,3,4,5,6])
print(f'Size of deque: {len(de)}')
#print front and back elements
print(de[0])
print(de[-1])

#accesing items 
de = collections.deque([6, 8, 5, 6, 1, 2])
print(de.index(6, 1))
de.insert(3, 2)
print('Adding new number', de)
de.remove(1)
print('Removing 1 from', de)

#different operations for queue
de2 = collections.deque([1,2,3])
de2.extend([4,5,6])
de2.extendleft([0,-1,-2])
print("Extended", de2)
de2.reverse()
print("Reversed", de2)
de2.rotate(-3)
print("Rotated", de2)
