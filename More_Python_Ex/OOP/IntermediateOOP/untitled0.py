# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 09:19:47 2021

@author: Manisha
"""

dict1 = {"a": 10,
         "b": 20}
# print(dict1.get('a'))
for k in dict1:
    print(dict1.get(k))

print(dict1.items())
# print(dict1.pop('b'))
# print(dict1.items())

# print(dict1.popitem())
# print(dict1.popitem())
# print(dict1.items())

dict1['c'] = 30

print(dict1.items())
print(len(dict1))

dict1.update({'a': 40})
dict1.update({'d': 50})
print(dict1)

try:
    answer =12/0
    print (answer)
except Exception as e:
    print ('Error:', e)
    
def test(a, b):
    print(a+b)
    return
test(10,80)