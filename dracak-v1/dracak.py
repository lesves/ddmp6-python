import pickle
import random
from story import banner, stats, story, starts, death, names
from plural import name_plural, name_singular
from stats import change_stats, missing, satisfies


def user_input(story, place, stats):
    text = input()
    if text in ("stats", "load"):
        return text

    try:
        chose = int(text)-1
    except ValueError:
        print("Zadej něco normálního...")
        return None

    if chose >= len(story[place][1]):
        print("Máš jenom", len(story[place][1]), "možnosti.")
        return None

    if len(story[place][1][chose]) > 3:
        if not satisfies(stats, story[place][1][chose][3]):
            print("Nesplňuješ požadavky.")
            return None
    return chose


def print_options(story, place):
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


visited = set()


print(banner)
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

    print_options(story, place)

    visited.add(place)


    chose = user_input(story, place, stats)
    if chose is None:
        continue
    elif chose == "stats":
        for stat, value in stats.items():
            if value == 1:
                print(name_singular[stat] + ":", value)
            else:
                print(name_plural[stat] + ":", value)
        continue
    elif chose == "load":
        with open("save.pkl", "rb") as f:
            stats, place = pickle.load(f)

    # elif text in stats:
    #     if not text.startswith("_"):
    #         print("Máš", stats[text], text + ".")
    #         continue

    next_places = story[place][1][chose][1]
    if isinstance(next_places, str):
        next_place = next_places
    else:
        next_place = random.choice(next_places)

    change_stats(story[place][1][chose][2], stats, visited, next_place)

    place = next_place

    with open("save.pkl", "wb") as f:
        pickle.dump([stats, place], f)
