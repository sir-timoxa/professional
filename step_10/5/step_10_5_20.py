
def card_deck(suit):
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    card_mast = ["пик", "треф", "бубен", "червей"]
    card_mast.remove(suit)
    while True:
        for mast in card_mast:
            for value in card_values:
                yield f"{value} {mast}"


