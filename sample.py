class ATM:
    all_notes = [2, 5, 10, 20, 50, 100]
    notes = {}
    amount = 0

    def __init__(self):
        notes = [2, 5, 10, 20, 50, 100]
        quantity = [10, 5, 1, 3, 15, 30]

        for i in range(len(notes)):
            note = notes[i]
            qtd = quantity[i]
            value = note + qtd
            self.notes[note] = qtd
            self.amount += value
        print(self.notes)

    def total(self):
        return self.amount

    def withdraw(self, value):
        result = dict()
        for key in sorted(self.notes, reverse=True):
            while value >= key:
                result[key] = result.get(key, 0) + 1
                value -= key
                self.notes[key] -= 1

        print(self.notes)
        return result

    def __str__(self):
        return self.amount


if __name__ == '__main__':
    machine = ATM()
    print('Valor na maquina:', machine.total())
    print('Saque de R$ 120:', machine.withdraw(120))
