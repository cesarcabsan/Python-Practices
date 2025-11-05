from itertools import groupby

L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)] 
  
# Key function 
key_func = lambda x: x[0] 
#Using groupby function
for key, group in groupby(L, key_func): 
    print(key + " :", list(group)) 