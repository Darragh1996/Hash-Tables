cache = {}


def exps(x, y, z):
    search_string = f"num_{x}"
    if search_string in cache:
        return cache[search_string]
    if x <= 0:
        cache[search_string] = y + z
        return cache[search_string]
    if x > 0:
        cache[search_string] = exps(x-1, y+1, z) + exps(x-2, y+2, z*2) + \
            exps(x-3, y+3, z*3)
        return cache[search_string]


if __name__ == "__main__":
    for i in range(10):
        x = exps(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(exps(150, 400, 800))
