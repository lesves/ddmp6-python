from plural import name_plural, name_singular


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


def change_stats(changes, stats, visited, next_place):
    for stat, change in changes.items():
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
