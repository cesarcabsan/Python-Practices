from array import * 
arr = array('i', [1,3,5,7,9])
arr.remove(5)
arr.pop(0)
arr.append(11)
print(arr)
print("Lengths in bytes of one item: ", arr.itemsize)


arr2 = array('i', [2,4,6,8,10])
for i in arr:
    print(i)
print("Individual indexes:")
print(arr2[0])
print(arr2[1])
print(arr2[2])

arr3 = array('i', [1,2,3,4,5])
arr3_sechalf = list([6,7,8,9,10])
arr3.extend(arr3_sechalf)
print(arr3)

arr_ints = array('i', ([10, 20, 30, 40, 50, 60]))
for i in arr_ints:
  print(i)

length_arr = array('i', ([1,2,3,4,5]))
print("Length of the array:", len(length_arr))

arr10 = array('i', ([1,3,5,7,9]))
arr10.insert(1,4)
print(arr10)

int_a = array('I', (12, 25))
print(int_a.itemsize)
float_a = array('f', (13.5, 4.6))
print(float_a.itemsize)

b_to_str = array('b', [99, 44, 111, 115, 116, 118, 119, 121])
s = b_to_str.tobytes()
print("Bytes to strings:", s)

item_list = [1,2,6,-8] 
add_array = array('i', [])
add_array.fromlist(item_list)
print(add_array)

#unicode
u_array = array('u', ['\u00A9', '\u00D1', '\u00E3'])
uni_char = list(u_array)
print(uni_char)

#float
arr_float = array('f', [4, -51, 10, 3, 6])
print(arr_float)


#append items from an specified list
lst = [1, 2, 6, -8]
new_arr = array('i', [])
new_arr.fromlist(lst)
print(new_arr)

#find largest number in array(with for loop)
a = [10,5,15,4,6,20,9]
max_num = a[0]
for i in range(len(a)):
  if a[i] > max_num:
    max_num = a[i]
print(f'Largest num in array is {max_num}')
#find smallest num in array(with for loop)
min_num = a[0]
for i in range(len(a)):
  if a[i] < min_num:
    min_num = a[i]
print(f'Smallest num in array is {min_num}')

#find average of all numbers
arrlst = array('i', [10,5,15,4,6,20,9])
s = 0 
avg = sum(arrlst) / len(arrlst)
print("Average of array:", avg)