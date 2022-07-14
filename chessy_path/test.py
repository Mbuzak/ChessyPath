import unittest

from figure import *
from destination import Destination


class DestinationTest(unittest.TestCase):
    def setUp(self):
        fig = Pawn('f', 2, Color.WHITE)
        p2 = Pawn('c', 2, Color.WHITE)
        p3 = Pawn('c', 3, Color.WHITE)
        p4 = Pawn('c', 4, Color.WHITE)
        p5 = Pawn('c', 5, Color.WHITE)
        self.pawns = [p2, p3, p4, p5]

        self.d = Destination(self.pawns, fig, ('f', 6))
    
    def test_king_path_map(self):
        fig = King('a', 3, Color.WHITE)
        self.d = Destination(self.pawns, fig, ('f', 5))
        
        self.d.path_map()
        
        for field in self.d.fields[::-1]:
            print(field)
        
        result = [[2, 2, 2, 3, 4, 5, 6, 7], [1, 1, 'x', 3, 4, 5, 6, 7], [0, 1, 'x', 4, 4, 5, 6, 7], [1, 1, 'x', 5, 5, 5, 6, 7], [2, 2, 'x', 4, 5, 6, 6, 7], [3, 3, 3, 4, 5, 6, 7, 7], [4, 4, 4, 4, 5, 6, 7, 8], [5, 5, 5, 5, 5, 6, 7, 8]]
        
        self.assertEqual(self.d.fields, result)

    def test_pawn_path_map(self):
        self.d.path_map()
        
        result = [[-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, 'x', -1, -1, 0, -1, -1], [-1, -1, 'x', -1, -1, 1, -1, -1], [-1, -1, 'x', -1, -1, 1, -1, -1], [-1, -1, 'x', -1, -1, 2, -1, -1], [-1, -1, -1, -1, -1, 2, -1, -1], [-1, -1, -1, -1, -1, 3, -1, -1], [-1, -1, -1, -1, -1, 3, -1, -1]]
        
        self.assertEqual(self.d.fields, result)
    
    def test_pawn_get_distance(self):
        self.d.path_map()
        
        self.assertEqual(self.d.get_distance(), 3)


if __name__ == '__main__':
    unittest.main()
