import pickle
import random
from story import stats, story, starts, death, names


def satisfies(stats, requirements):
    for name in requirements:
        if name in stats:
            if requirements[name] <= stats[name]:
                return True
    return False


def missing(stats, requirements):
    missing_items = {}

    for name in requirements:
        d = requirements[name]-stats.get(name, 0)
        if d > 0:
            missing_items[name] = d

    return missing_items


visited = set()

name_singular = {}
name_plural = {}
for n in names:
    name_singular[n] = names[n][0]
    name_plural[n] = names[n][1]


print("Vždy napiš číslo možnosti, jež zvolena tebou jest.")
print("Pro zobrazení balancu tvého konta napiš money")

place = random.choice(starts)
while True:
    dead = False

    for condition in death:
        if stats[condition] <= 0:
            print("Přišel jsi o všechny", name_plural[condition] + "...")
            dead = True
            break

    if dead:
        print("Hra končí.")
        break
    
    print(story[place][0])
    for option in range(len(story[place][1])):
        option_text = story[place][1][option][0]

        if len(story[place][1][option]) > 3:
            requirements = story[place][1][option][3]

            if satisfies(stats, requirements):
                print(str(option+1) + ".", option_text)
            else:
                print(str(option+1) + ".", option_text)
                print("nelze zvolit, chybí: ", end="")
                for item, val in missing(stats, requirements).items():
                    if val == 1:
                        print(val, name_singular[item], end=", ")
                    else:
                        print(val, name_plural[item], end=", ")
                print()

        else:
            print(str(option+1) + ".", option_text)

    visited.add(place)

    text = input()
    if text == "stats":
        for stat, value in stats.items():
            if value == 1:
                print(name_singular[stat] + ":", value)
            else:
                print(name_plural[stat] + ":", value)
        continue
    elif text == "load":
        with open("save.pkl", "rb") as f:
            stats, place = pickle.load(f)
    # elif text in stats:
    #     if not text.startswith("_"):
    #         print("Máš", stats[text], text + ".")
    #         continue
    try:
        chose = int(text)-1
    except ValueError:
        print("Zadej něco normálního...")
        continue

    if chose >= len(story[place][1]):
        print("Máš jenom", len(story[place][1]), "možnosti.")
        continue

    if len(story[place][1][chose]) > 3:
        if not satisfies(stats, story[place][1][chose][3]):
            print("Nesplňuješ požadavky.")
            continue

    next_places = story[place][1][chose][1]
    if isinstance(next_places, str):
        next_place = next_places
    else:
        next_place = random.choice(next_places)

    for stat, change in story[place][1][chose][2].items():
        if stat.startswith("first_"):
            if next_place in visited:
                continue
            stat = stat[6:]

        if stat in stats:
            stats[stat] = stats[stat] + change
        else:
            stats[stat] = change
            
        if change == float("-inf"):
            print("Přišel jsi o všechny", name_plural[stat] + ".")
        if change == -1:
            print("Přišel jsi o", name_singular[stat] + ".")
        elif change < 0:
            print("Přišel jsi o", -change, stat + ".")
        elif change == 0:
            pass
        elif change == 1:
            print("Získal jsi", name_singular[stat] + ".")
        else:
            print("Získal jsi", change, stat + ".")

    place = next_place

    with open("save.pkl", "wb") as f:
        pickle.dump([stats, place], f)
