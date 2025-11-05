#print even numbers
num_list = [16, 21, 2, 42, 67, 90]
for i in num_list:
  if i % 2 == 0:
       print(i, '', end='')
print('\n')
#print even numbers
num_list2 = [11, 64, 51, 23, 9, 88]
for num in num_list2:
   if num % 2 != 0:
       print(num, '', end='')

print('\n')
#check which numbers are even and which ones are odd 
def odd_or_even():
    lst = [10, 6, 25, 13, 24]
    for num in lst:
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
odd_or_even()

#multiply the even numbers with list comprehension
even_nums = [2,4,6,8,10,12,14,16,18,20]
lst_comp = [num ** 2 for num in even_nums]
print(lst_comp)
          
#with for loop range
def rangeoddeven(n):
    for n in range(1, 5):
        if n % 2 == 0:
            print(n, "(Even)")
        else:
            print(n, "(Odd)")
rangeoddeven(0)