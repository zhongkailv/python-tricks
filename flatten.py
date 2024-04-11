# -*- coding: utf-8 -*-


from collections.abc import Iterable

def flatten(items, ignore_types = (str, bytes)):
    """
    该函数用于将一个多层嵌套的序列展开成一个单层列表。
    items = [1, {2}, [3, 4, [5, (6,7),[8,[9,[10]]]], 11], 12]
    for x in flatten(items):
        print(x)
        
    #将打印  1 2 3 4 5 6 7 8 9 10 11 12
    """
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x



if __name__ == '__main__':
    items = [1, {2}, [3, 4, [5, (6,7),[8,[9,[10]]]], 11], 12]
    # Produces 1 2 3 4 5 6 7 8 9 10 11 12
    for x in flatten(items):
        print(x)




