
# single leading underscore
# most Python code
# non-public part of API(might change)
# function, method or data member
_harry = None

# two leading underscores and at most one trailing underscore
# name mangling, internally replaced with _classname__var
# __name becomes _HogwartsMember__name
# may be used to avoid name conflicts (with child classes)
# name mangling enforced by Python interpreter
__harry = None

# double leading and double trailing underscores
# magic objects or attributes
# special meaning
# preferably reserved for Python internal use
__init__ = None

# single underscore on its own _
# temporary variable whose value isn't used
_

# single trailing underscore
# used to avoid conflict with reserved names
list_ = None

