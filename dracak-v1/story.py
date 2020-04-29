banner = """8888b.  88""Yb    db     dP""b8    db    88  dP 
 8I  Yb 88__dP   dPYb   dP   `"   dPYb   88odP  
 8I  dY 88"Yb   dP__Yb  Yb       dP__Yb  88"Yb  
8888Y"  88  Yb dP\"\"\"\"Yb  YboodP dP\"\"\"\"Yb 88  Yb """

stats = {
    "money": 100,
    "health": 100,
    "kidney": 2,
    "karma": 0,
    }

names = {
    "money": ["zlaťák", "zlaťáky"],
    "health": ["zdraví", "zdraví"],
    "dagger": ["dýka", "dýky"],
    "kidney": ["ledvina", "ledviny"],
    "karma": ["karma", "karma"]
}

death = ["health", "kidney"]


story = {
    "ulice": ["Jsi na ulici", 
              [["Půjdu na černý trh", "obchod", {"first_dagger": 1}],
               ["Napadnu náhodného kolemjdoucího", "boj_ulice", {}]]],
    "obchod": ["Jsi na černém trhu.", 
               [["Koupím si dýku za 10.", "obchod", {"dagger": 1, "money": -10}, {"money": 10}],
                ["Prodám dýku za 7.", "obchod", {"dagger": -1, "money": 7}, {"dagger": 1}],
                ["Koupím ledvinu za 20000.", "obchod", {"kidney": 1, "money": -20000}, {"money": 20000}],
                ["Prodám ledvinu za 5000.", "obchod", {"kidney": -1, "money": 5000}],
                ["Odejdu", "ulice", {}],]],
    "boj_ulice": ["Zápasíte..", 
                  [["Dám mu ránu", ["boj_ulice", "vyhra_ja", "vyhra_kolemjdouci"], {}],
                   ["Bodnu ho dýkou", "vyhra_ja", {"karma": -100}, {"dagger": 1}]]],
    "vyhra_kolemjdouci": ["Dopadlo to s tebou špatně", 
                          [["ach jo", "", {"health": -float("inf")}]]],
    "vyhra_ja": ["Porazil jsi ho.", 
                 [["Okradnu ho", "ulice", {"money": 5, "karma": -5}],
                  ["Prodám ho na orgány", "obchod", {"money": 10000, "karma": -500}]]]
    }


starts = ["ulice"]
