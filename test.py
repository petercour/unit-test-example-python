# mymodule
import unittest
import program

class MyModuleTest(unittest.TestCase):

    def test_inc_by_one(self):
        assert(program.inc_by_one(2) == 3)

if __name__ == '__main__':
    unittest.main()
