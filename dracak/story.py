stats = {
    "money": 100,
    "health": 100,
    }

story = {
    "ulice": ["Jsi na ulici", 
              [["Půjdu na černý trh", "obchod", {}]]],
    "obchod": ["Jsi na černém trhu.", 
               [["Koupím si dýku za 10.", "obchod", {"dyka": 1, "money": -10}, {"money": 10}],
                ["Prodám dýku za 7.", "obchod", {"dyka": -1, "money": 7}, {"dyka": 1}],
                ["Koupím ledvinu za 20000.", "obchod", {"health": 50, "money": -20000}, {"money": 20000}],
                ["Prodám ledvinu za 5000.", "obchod", {"health": -50, "money": 5000}],
                ["Odejdu", "ulice", {}],]]
    }

starts = ["ulice"]
