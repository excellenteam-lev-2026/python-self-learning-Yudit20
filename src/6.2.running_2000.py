import time

def timer(f, *args, **kwargs):
    """
    Measure the execution time of f(*args, **kwargs) over 2000 repetitions.

    :param f: The function to measure
    :param args: Positional arguments for f
    :param kwargs: Keyword arguments for f
    :return: Total execution time in seconds
    """
    start = time.time()

    for _ in range(2000):
        f(*args, **kwargs)

    end = time.time()

    return end - start


# --- Tests ---
print(timer(print, "Hello"))
# Prints "Hello" 2000 times, then returns the elapsed time

print(timer(zip, [1, 2, 3], [4, 5, 6]))
# Runs zip([1,2,3],[4,5,6]) 2000 times, then returns the elapsed time

print(timer("Hi {name}".format, name="Bug"))
# Runs "Hi {name}".format(name="Bug") 2000 times, then returns the elapsed time