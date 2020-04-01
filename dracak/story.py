stats = {
    "money": 100,
    "health": 100,
    }

story = {
    "hospoda": ["Jsi v hospode, co udelas?", 
                [["Půjdu do lesa", "les", {}],
                 ["Začnu rvačku", ["rvacka1", "rvacka1", "rvacka1", "rvacka2"], {"health": -20, "money": 5}]]],
    "les": ["Jsi v lese",
            [["Půjdu do hospody", "hospoda", {}],
             ["Projdu se", "les2", {"dyka": 1}]]],
    "les2": ["Našel jsi dýku...",
             [["Půjdu dál", "les", {}]]],
    "rvacka1": ["Perete se, ale někdo se vás pokouší uklidnit.",
                [["Nechám toho", "hospoda", {}]]],
    "rvacka2": ["Vytáhli na tebe nůž.",
                [["Nechám se zabít", "end", {"health": float("-inf")}],
                 ["Bodnu ho dýkou", "hospoda", {}, {"dyka"}]]]
    }

starts = ["hospoda", "les"]
