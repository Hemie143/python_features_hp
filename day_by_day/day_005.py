
def simple_decorator(function):
    return function

def goodbye(function):
    def wrapper(*args, **kwargs):
        original_output = function(*args, **kwargs)
        new_output = original_output + f' Goodbye, have a good day!'
        return new_output
    return wrapper

@goodbye
def say_words(person, words):
    return f"{person} says: '{words}'"

@goodbye
def say_hello():
    return f'Hey there!'

print(say_hello())

print(say_words("Harry", "Hey Ron!"))
