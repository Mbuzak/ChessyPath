from enum import Enum


class Color(Enum):
    WHITE = 1
    BLACK = 2


class Figure:
    def __init__(self, pos_x, pos_y, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        
        self.initialize_fields()
        #self.step = 0
    
    def initialize_fields(self):
        self.fields = [[-1] * 8 for i in range(8)]


class King(Figure):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)
        self.set_field(pos_x, pos_y, 0)
    
    # all available fields on board in one move
    def all_fields(self):
        pos = []
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                pos.append([i, j])
        
        pos.remove([0, 0])
        return pos
    
    def available_fields(self, pos_x, pos_y, step=0):
        fields = []
        pos = self.all_fields()
        # print(pos_x, pos_y)
        
        for i in range(len(pos)):
            new_x, new_y = chr(ord(pos_x) + pos[i][0]), pos_y + pos[i][1]
            
            if new_x <= 'h' and new_x >= 'a' and new_y <= 8 and new_y >= 1:
                # if path doesn't already exists, then add this field
                if self.get_field(new_x, new_y) == -1:
                    fields.append([new_x, new_y])
                # if path exists, then check out does new path is shorter than previous path
                elif step < self.get_field(new_x, new_y):
                    fields.append([new_x, new_y])
        
        return fields
    
    def get_field(self, pos_x, pos_y):
        return self.fields[pos_y - 1][ord(pos_x) - 97]
    
    def set_field(self, pos_x, pos_y, value):
        self.fields[pos_y - 1][ord(pos_x) - 97] = value
    
    def path_map(self, pos_x, pos_y, step=1):
        # print('pos', pos_x, pos_y)
        fields = self.available_fields(pos_x, pos_y, step)
        # print('fields', fields)
        for field in fields:
            # print(field)
            # print('index', ord(field[0])-97, field[1], '\n')
            self.set_field(field[0], field[1], step)
            self.path_map(field[0], field[1], step + 1)
