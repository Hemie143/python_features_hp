# https://docs.python.org/3/tutorial/classes.html#iterators

'''
potion = Potion(...)
for ingredient in potion:
    print(ingredient)
'''

'''
1. for calls iter() on object: iter(potion)
2. iter() calss __iter__(): potion.__iter__()
3. __iter__() returns an iterator
4. iterator implements __next__(): potion.__next__(). If no element left, raise StopIteration exception: end loop
'''

'''
potion = Potion(...)
iterator = iter(Potion)
while True:
    ingredient = next(potion)
    print(ingredient)
'''