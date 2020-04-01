inventory = []


stats = {
    "money": 100,
    "health": 100,
    }

story = {
    "hospoda": ["Jsi v hospode, co udelas?", 
                [["Půjdu do lesa", "les", {}],
                 ["Začnu rvačku", ["rvacka1", "rvacka1", "rvacka1", "rvacka2"], {"health": -20, "money": 5}]]],
    "les": ["Jsi v lese",
            [["Půjdu do hospody", "hospoda", {}]]],
    "rvacka1": ["Perete se, ale někdo se vás pokouší uklidnit.",
               [["Nechám toho", "hospoda", {}]]],
    "rvacka2": ["Někdo tě zabil.",
                [["Smířím se s tím", "end", {"health": float("-inf")}]]]
    }

starts = ["hospoda", "les"]
