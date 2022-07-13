import unittest

from figure import *


class KingTest(unittest.TestCase):
    def test_available_fields(self):
        king = King('a', 1, Color.WHITE)
        fields = [['a', 2], ['b', 1], ['b', 2]]
        
        self.assertEqual(king.available_fields('a', 1), fields)
    
    def test_path_map(self):
        king = King('d', 3, Color.WHITE)
        king.path_map('d', 3)
        
        #print(king.fields)
        
        #for field in king.fields[::-1]:
        #    print(field)
        
        result = [[3, 2, 2, 2, 2, 2, 3, 4], [3, 2, 1, 1, 1, 2, 3, 4], [3, 2, 1, 0, 1, 2, 3, 4], [3, 2, 1, 1, 1, 2, 3, 4], [3, 2, 2, 2, 2, 2, 3, 4], [3, 3, 3, 3, 3, 3, 3, 4], [4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5]]
        
        
        self.assertEqual(king.fields, result)


if __name__ == '__main__':
    unittest.main()