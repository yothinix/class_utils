class Orange(object):
    mango = 'This is mango'


class Apple(object):
    orange = Orange()


class Banana(object):
    apple = Apple()


def get_in_class(obj, keys=[], default='return-default'):
    if not hasattr(obj, keys[0]):
        return default
    new_obj = getattr(obj, keys[0])
    if keys[1:]:
        return get_in_class(new_obj, keys[1:])
    return new_obj


def get_in_class_recursion(obj, keys, default='return-default'):
    if keys == []:
        return obj
    name = keys[0]
    if hasattr(obj, name):
        return get_in_class_recursion(getattr(obj, name), keys[1:])
    else:
        return default


b = Banana()

print(get_in_class(b, ['apple', 'orange', 'mango']))
print(get_in_class(b, ['apple', 'orange', 'banana']))
print(get_in_class_recursion(b, ['apple', 'orange', 'mango']))
print(get_in_class_recursion(b, ['apple', 'orange', 'banana']))
