#Find squared of the list element (using lambda)

lst = [1,2,3,4,5,6,7,8,9] 

squared = map(lambda x:x**2, lst)
print(list(squared))

#add two lists with map and lambda

list1 = [2, 5, 8]
list2 = [3, 6, 9]

result = map(lambda x, y:x + y, list1, list2)
print(list(result))