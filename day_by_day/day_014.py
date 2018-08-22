from abc import ABCMeta, abstractmethod

@property
@abstractmethod
def defining_feature(self):
    pass


defining_feature = property(abstractmethod(defining_feature))

# https://stackoverflow.com/questions/3570796/why-use-abstract-base-classes-in-python
#
# a) It should be impossible to instantiate the base class
# b) All subclasses should have a common base class
# c) All subclasses should implement certain methods defined in the base class