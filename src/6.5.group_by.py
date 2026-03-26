def group_by(f, iterable):
    """
    Group elements from an iterable according to the result of f.

    :param f: Function applied to each element
    :param iterable: Collection of elements to group
    :return: dict {result_of_f: [elements]}
    """
    result = {}

    for element in iterable:
        key = f(element)
        result.setdefault(key, []).append(element)

    return result


# --- Tests ---
print(group_by(len, ["hi", "bye", "yo", "try"]))

print(group_by(lambda value: value % 2, [1, 2, 3, 4, 5, 6]))

print(group_by(str.upper, ["hello", "HELLO", "world", "WORLD"]))
