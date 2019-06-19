class ATM:
    notes = dict()
    amount: int = 0

    def set_note(self, note, quantity):
        self.notes[note] = quantity
        self.update_amount()

    def update_amount(self):
        self.amount = 0
        for key, value in self.notes.items():
            self.amount += key * value
