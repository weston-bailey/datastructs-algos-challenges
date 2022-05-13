from unittest import TestCase, main
from random_list import random_list


class Test_Random_Chars(TestCase):
    def test_is_list(self):
        random_li = random_list()
        self.assertIsInstance(random_li, list)

    def test_char_type(self):
        random_li = random_list(type_of='char')
        for char in random_li:
            self.assertIsInstance(char, str)

    def test_int_type(self):
        random_li = random_list(type_of='int')
        for num in random_li:
            self.assertIsInstance(num, int)

    def test_float_type(self):
        random_li = random_list(type_of='float')
        for num in random_li:
            self.assertIsInstance(num, float)

    def test_length(self):
        random_li = random_list(length=50)
        for num in random_li:
            self.assertEqual(len(random_li), 50)


if __name__ == '__main__':
    main()
