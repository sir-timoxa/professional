class CardDeck:
    def __init__(self):
        self.mast=['пик', 'треф', 'бубен', 'червей']
        self.nominal=['2','3','4','5','6','7','8','9','10','валет','дама','король','туз']
        self.current_mast = 0
        self.current_nominal = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.current_mast >= len(self.mast):
            raise StopIteration

        card = f"{self.nominal[self.current_nominal]} {self.mast[self.current_mast]}"

        self.current_nominal += 1
        if self.current_nominal >= len(self.nominal):
            self.current_nominal = 0
            self.current_mast += 1

        return card



