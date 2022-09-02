# python function that takes a nested dictionary and key as input and returns a nested value

def get_nested(data, *args):
    if args and data:
        element  = args[0]
        if element:
            value = data.get(element)
            return value if len(args) == 1 else get_nested(value, *args[1:])

# test 1

obj1 = {'a': {'b': {'c': 'd'}}}
print(get_nested(obj1, 'a', 'b', 'c')) # should return 'd'

# test 2

obj2 = {'x': {'y': {'z': 'a'}}}
print(get_nested(obj2, 'x', 'y', 'z')) # should return 'a'

# test 3 for my understanding

obj3 = {'foo': {'bar': {'one': 1, 'two': 2}, 'misc': [1, 2, 3]},
       'foo2': 123}
print(get_nested(obj3, "foo", "bar", "one")) # should return 1
print(get_nested(obj3, "foo", "bar", "two")) # should return 2
print(get_nested(obj3, "foo", "misc")) # should return [1, 2, 3]
