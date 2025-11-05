#simple dictionary example

#exampledict = {"Name": "Tyson", "Age": 24, "Residence": "Chile"}
#print(exampledict)

#update and remove key items
market = {"Market": "WalMart", "State": "Closed", "Location": "at Street"}
print(market)
market["State"] = "Open"
del market["Location"]
print(market)

#for loop item iteration  
fruit_and_veg = {"Apple": "Fruit", "Carrot": "Vegetable"}
print(fruit_and_veg)
for key, value in fruit_and_veg.items():
    print(key, '->', value)

#dictionary comprehension 
a_dict = {'a': 1, 'b':2, 'c': 3, 'd': 4, 'e':5}
dict_compr = {k:v**2 for (k,v) in a_dict.items()}
print(dict_compr)

#copying
original_dict = {'name': 'Daniel', 'age': 24, 'city': 'Monterrey'}
#use copy(), or dict(x) to actually copy the dict and prevent the original from being modified
copy_dict = original_dict.copy()
copy_dict['name'] = 'Roberto'
print(copy_dict)
print(original_dict)

#merge dictionaries(any existing keys get overwritten)
a_feline_dict = {'Animal': 'Lion', 'Breed': 'Feline', 'Type': 'Carnivore'}
a_canine_dict = dict(Animal='Fox', Breed='Canine', Color='Red')
a_feline_dict.update(a_canine_dict)
print(a_feline_dict)

#nested dictionaries
dict1 = {'Language': 'Python', 'Type': 'Interpreted'}
dict2 = {'Language': 'C++', 'Type': 'Compiled'}
nested_dict = {"Dict1": dict1, 'Dict2': dict2}
print(nested_dict)