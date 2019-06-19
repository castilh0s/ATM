class ATM:
    notes = dict()
    amount: int = 0

    def set_note(self, note, quantity):
        self.notes[note] = quantity
        self.amount += (note * quantity)
