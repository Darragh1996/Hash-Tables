import re


def word_count(s):
    count = {}
    # s = s.translate({ord(c): None for c in ':,.- += /\\|[](}{)*^'})
    s = re.sub(r'[^a-zA-Z\']', ' ', s)
    s = s.strip().lower()
    word_arr = s.split(" ")
    if len(word_arr) == 1 and word_arr[0] == "":
        return count
    for word in word_arr:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    if "" in count:
        del count[""]
    return count


if __name__ == "__main__":
    print(word_count("a a\ra\na\ta \t\r\n"))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
