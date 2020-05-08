def no_dups(s):
    cache = {}
    unique_string = ""
    arr = s.split(" ")
    for word in arr:
        if word in cache:
            continue
        else:
            if unique_string and word != "":
                cache[word] = 1
                unique_string = unique_string + " " + word
            elif word != "":
                cache[word] = 1
                unique_string = word
    return unique_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
