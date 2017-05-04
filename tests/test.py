import rgr
import unittest



class TestRGR(unittest.TestCase):
    
    def test_d(self):
        roller = rgr.compile("3d6")
        result, _ = roller.roll()
        self.assertTrue(result >= 3)
        self.assertTrue(result <= 18)
        
    def test_e(self):
        pass


if __name__ == '__main__':
    unittest.main()
