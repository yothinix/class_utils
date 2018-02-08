class Orange(object):
    mango = 'This is mango'


class Apple(object):
    orange = Orange()


class Banana(object):
    apple = Apple()


def get_in_class(obj, keys = []):
    if hasattr(obj, keys[0]):
        new_key = keys[1:]
        new_obj = getattr(obj, keys[0])
        if new_key:
            return get_in_class(new_obj, new_key)
        return new_obj


b = Banana()

print(get_in_class(b, ['apple', 'orange', 'mango']))
