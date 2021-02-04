from django.test import TestCase

from app.calc import addition


class CalcTests(TestCase):

    def test_add_numbers(self):
        self.assertEqual(addition(3, 8), 11)


