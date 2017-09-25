# -*- coding: utf-8 -*-
import sys, timeit

# sys.getsizeof()

lista = [1,2,3,4,5,'ABC',2.34,True]
tupla = (1,2,3,4,5,'ABC',2.34,True)

print(sys.getsizeof(lista)) # 136 bytes
print(sys.getsizeof(tupla)) # 120 bytes
 
mysetup = "from math import sqrt"
 
mylist = "[1, 2, 3, 4, 5]"
mytuple = "(1, 2, 3, 4, 5)"

print timeit.timeit(setup = mysetup,
                    stmt = mylist,
                    number = 10000)

print timeit.timeit(setup = mysetup,
                    stmt = mytuple,
                    number = 10000)
