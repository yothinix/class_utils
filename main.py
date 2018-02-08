import copy


class Orange(object):
    mango = 'This is mango'


class Apple(object):
    orange = Orange()


class Banana(object):
    apple = Apple()


def get_in_class(obj, keys):
    new_key = copy.copy(keys)
    for key in keys:
        if hasattr(obj, key):
            new_key.remove(key)
            new_obj = getattr(obj, key)
            if len(new_key) == 0:
                return new_obj
            else:
                return get_in_class(new_obj, new_key)


b = Banana()

print(get_in_class(b, ['apple', 'orange', 'mango']))
