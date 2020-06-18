"""
This class represents something similar to a JS object literal.
Tentatively, I'll use Object instances in order to replace variables for use like an enumeration without increasing integer values.
"""

class Object:
   def __init__(self, **attributes):
      self.__dict__.update(attributes)

def __getattribute__(self, item):
   attr = super().__getattribute__(item)
   if hasattr(attr, "__get__"):
      return attr.__get__(self, Object)
   else:
      return attr

def __setattr__(self, key, value):
   attr = super().__getattribute__(key)
   if hasattr(attr, '__set__'):
      attr.__set__(self, value)
   elif hasattr(attr, '__delete__'):
      raise AttributeError(key + ' has no attribute, "__set__"')
   else:
      self.__dict__[key] = value

def __delattr__(self, item):
   attr = super().__getattribute__(item)
   if hasattr(attr, '__delete__'):
      attr.__delete__(self, item)
   elif hasattr(attr, '__set__'):
      raise AttributeError(item + ' has no attribute, "__delete__"')
   else:
      del self.__dict__[item] 
