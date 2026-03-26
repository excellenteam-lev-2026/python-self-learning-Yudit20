def long_cat_is_long(text):
    """
    Return a dictionary {word: length} for each unique word in the text.

    :param text: The text to analyze
    :return: dict {word: len(word)}
    """
    # Step 1: Clean punctuation (keep letters and spaces)
    cleaned_text = "".join(c for c in text if c.isalpha() or c.isspace())

    # Step 2: Lowercase + split into words
    words = cleaned_text.lower().split()

    # Step 3: Dictionary comprehension
    return {word: len(word) for word in words}