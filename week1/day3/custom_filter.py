def custom_filter(higher_order_function, iterable):
    # * This will ensure that return type is same as the iterable we passed
    iterable_type = type(iterable)

    res = iterable_type(x for x in iterable if higher_order_function(x))
    return res


def checker(x):
    try:
        if(isinstance(x, int)):
            return True
    except:
        return False


vals = (-1, 0, 2, 4, 1.367, -5, 3, True, "Hello World")
vals1 = (-1, 0, 2, 4, 1.367, -5, 3, -10)
res = custom_filter(checker, vals)
res1 = custom_filter(lambda x: x >= 0, vals1)
print(res)
print(res1)
