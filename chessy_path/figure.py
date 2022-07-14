from enum import Enum


class Color(Enum):
    WHITE = 1
    BLACK = 2


class Figure:
    def __init__(self, pos_x, pos_y, color):
        self.pos_x = self.is_pos_x_valid(pos_x)
        self.pos_y = self.is_pos_y_valid(pos_y)
        self.color = color
    
    # https://towardsdatascience.com/6-approaches-to-validate-class-attributes-in-python-b51cffb8c4ea
    def is_pos_x_valid(self, pos_x):
        if ord(pos_x) < 97 or ord(pos_x) > 104:
            raise ValueError('X-axis can have values [a-h]')
        return pos_x
    
    def is_pos_y_valid(self, pos_y):
        if pos_y < 1 or pos_y > 8:
            raise ValueError('Y-axis can have values [1-8]')
        return pos_y


class Pawn(Figure):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)
    
    def all_fields(self):
        pos = []
        if self.color == Color.WHITE:
            pos.append([0, 1])
            if self.pos_y == 2:
                pos.append([0, 2])
        else:
            pos.append([0, -1])
            if self.pos_y == 2:
                pos.append([0, -2])
        return pos


class King(Figure):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)
    
    # all available fields on board in one move
    def all_fields(self):
        pos = []
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                pos.append([i, j])
        
        pos.remove([0, 0])
        return pos


class Rook(Figure):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)


class Bishop(Figure):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)


class Knight(Figure):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)


class Queen(Figure):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)
