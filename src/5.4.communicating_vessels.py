# --- Version 1 ---
def interleave(*iterables):
    
    return [element for groupe in zip(*iterables) for element in groupe]


# ---generative Version  ---
def interleave_generator(*iterables):
   
    for groupe in zip(*iterables):
        for element in groupe:
            yield element


# --- Tests ---
print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
# ✅ ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']

print(list(interleave_generator('abc', [1, 2, 3], ('!', '@', '#'))))
# ✅ ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']