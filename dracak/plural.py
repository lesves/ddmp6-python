from story import names


name_singular = {}
name_plural = {}
for n in names:
    name_singular[n] = names[n][0]
    name_plural[n] = names[n][1]
