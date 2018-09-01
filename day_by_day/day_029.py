'''
for component in item:
    print(component)
'''

# https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration
# Iterable: object we can iterate over
# Objects defines:
#    1. __iter__ method: returns iterator. iter(object) = object.__iter__()
#    2. or __getitem__ method
# Iterator: object with a __next__ method. Methods returns next element of the object. If there are no elements left,
#       raise StopIteration exception.
#       next(object) = object.__next__()

# Goal:
# for ingredient in potion:
#       print(ingredient)

# __iter__: