from unittest import TestCase
from atm.atm import ATM


class ATMTests(TestCase):
    notes = {2: 30, 5: 25, 10: 20, 20: 15, 50: 10, 100: 5}
    amount = 1685

    def test_init(self):
        atm = ATM()

        self.assertEqual(atm.amount, 0)
        self.assertEqual(atm.notes, dict())

    def test_set_note(self):
        atm = ATM()

        for key, value in self.notes.items():
            atm.set_note(key, value)

        self.assertEqual(atm.notes, self.notes)
        self.assertEqual(atm.amount, self.amount)

        atm.set_note(2, 10)

        self.assertEqual(atm.notes[2], 10)
        self.assertEqual(atm.amount, self.amount - (2 * 20))

    def test_update_amount(self):
        atm = ATM()

        atm.notes = self.notes
        atm.update_amount()

        self.assertEqual(atm.amount, self.amount)
