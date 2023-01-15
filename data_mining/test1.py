a = [1,2,3]
b = [4]
c = [7,9]

from itertools import product 

product = list(product(a,b,c))
print(len(product))
print(product)
