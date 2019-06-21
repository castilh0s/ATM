import random


class ATM:
    def __init__(self, notes=dict()):
        self.notes = dict()
        self.amount = 0
        self.set_notes(notes)

    def set_notes(self, notes):
        for key, value in notes.items():
            self.set_note(key, value)

    def set_note(self, note, quantity):
        self.notes[note] = quantity
        self.update_amount()

    def update_amount(self):
        self.amount = 0
        for key, value in self.notes.items():
            self.amount += key * value

    def get_amount(self):
        return self.amount

    def get_notes_string(self):
        notes = {note: qtd for note, qtd in self.notes.items() if qtd > 0}
        notes_list = list(notes.keys())
        notes_string = ' | '.join((str(n) for n in notes_list))

        return notes_string

    def get_quantity(self, note):
        return self.notes.get(note, 0)

    def withdraw(self, value):
        result = dict()
        for note in sorted(self.notes, reverse=True):
            if self.get_quantity(note) > 0:
                while value >= note:
                    result[note] = result.get(note, 0) + 1
                    value -= note
                    self.set_note(note, self.get_quantity(note) - 1)

        return result


if __name__ == '__main__':
    notes = dict()
    notes_list = [2, 5, 10, 20, 50, 100]

    for note in notes_list:
        quantity = random.randrange(0, 16, 1)
        notes[note] = quantity

    atm = ATM(notes)

    print('Notas disponíveis:')
    print(atm.get_notes_string())
