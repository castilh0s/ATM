import unittest
from atm.atm import ATM


class ATMTests(unittest.TestCase):
    notes = {2: 30, 5: 25, 10: 20, 20: 15, 50: 10, 100: 5}
    amount = 1685

    def test_init(self):
        atm = ATM()

        self.assertEqual(atm.get_amount(), 0)
        self.assertEqual(atm.notes, dict())

    def test_set_notes(self):
        atm = ATM()
        atm.set_notes(self.notes)

        self.assertEqual(atm.notes, self.notes)

    def test_set_note(self):
        atm = ATM(self.notes)

        self.assertEqual(atm.notes, self.notes)
        self.assertEqual(atm.get_amount(), self.amount)

        atm.set_note(2, 10)

        self.assertEqual(atm.notes[2], 10)
        self.assertEqual(atm.get_amount(), 1645)

    def test_update_amount(self):
        atm = ATM()

        atm.notes = self.notes
        atm.update_amount()

        self.assertEqual(atm.get_amount(), self.amount)

    def test_get_amount(self):
        atm = ATM(self.notes)

        self.assertEqual(atm.amount, self.amount)

    def test_get_notes_string(self):
        atm = ATM(self.notes)

        self.assertEqual(atm.get_notes_string(), '2 | 5 | 10 | 20 | 50 | 100')

        atm.set_note(5, 0)
        atm.set_note(20, 0)

        self.assertEqual(atm.get_notes_string(), '2 | 10 | 50 | 100')

    def test_withdraw(self):
        atm = ATM(self.notes)
        self.assertEqual(atm.withdraw(150), {100: 1, 50: 1})
        self.assertEqual(atm.notes, {2: 30, 5: 25, 10: 20, 20: 15, 50: 9, 100: 4})

        atm = ATM({2: 3, 5: 1, 50: 5})
        self.assertEqual(atm.withdraw(202), {50: 4, 2: 1})
        self.assertEqual(atm.notes, {2: 2, 5: 1, 50: 1})
