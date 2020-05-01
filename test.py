import unittest
from main import main


class MainTestCase(unittest.TestCase):
    def test_test(self):
        self.assertTrue(main())

if  __name__ == '__main__':
    unittest.main()