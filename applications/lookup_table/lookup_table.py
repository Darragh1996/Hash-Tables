import math
import random

cache = {}


def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    search_string = f"{x}^{y}"
    if search_string in cache:
        return cache[search_string]
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    cache[search_string] = v
    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
