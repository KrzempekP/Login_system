import unittest
from Logging import login


class Test_Login(unittest.TestCase):
    # Tests
    def test_set_log(self):
        data1 = ""
        data2 = ""
        l1 = login(data1, data2)
        with self.assertRaises(TypeError):
            l1.log = 23

    def test_set_pas(self):
        data1 = ""
        data2 = ""
        l1 = login(data1, data2)
        with self.assertRaises(TypeError):
            l1.pas = 23
