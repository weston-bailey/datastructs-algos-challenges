from unittest import TestCase, main
from ....lib.data.float_to_str import float_to_str


class Test_Float_To_Strong(TestCase):
    def test_type(self):
        fl = 10.1
        fl_str = float_to_str(fl)
        self.assertIsInstance(fl_str, str)

    def test_return(self):
        sci_note = 1e-15
        str_repr = "0.000000000000001"
        return_test = float_to_str(sci_note)
        self.assertEqual(str_repr, return_test)


if __name__ == '__main__':
    main()
