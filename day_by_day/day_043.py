class MySpecificError(ValueError):
  pass

# Custom exception classes
# https://github.com/openai/gym/blob/master/gym/error.py
# https://github.com/pallets/click/blob/master/click/exceptions.py

class BaseError(Exception):
    """ Base class for exception in this module """
    pass


class InvalidBirthyearError(BaseError):
    """ Raised when the birthyear argument is not a valid integer like 1991 """
    pass


if type(birthyear) is not int:
    raise InvalidBirthyearError("The birthyear is not a valid integer. Try something like 1991")