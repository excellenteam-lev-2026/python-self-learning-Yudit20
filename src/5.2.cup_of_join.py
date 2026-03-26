def join(*listes, sep="-"):
    if not listes:
        return None

    resultat = []
    resultat.extend(listes[0])

    for liste in listes[1:]:
        resultat.append(sep)
        resultat.extend(liste)

    return resultat


# --- Tests ---
print(join([1, 2], [8], [9, 5, 6], sep='@'))  # [1, 2, '@', 8, '@', 9, 5, 6]
print(join([1, 2], [8], [9, 5, 6]))            # [1, 2, '-', 8, '-', 9, 5, 6]
print(join([1]))                                # [1]
print(join())                                   # None