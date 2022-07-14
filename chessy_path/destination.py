from figure import *


class Destination:
    def __init__(self, figures, piece, destination):
        self.figures = figures
        self.piece = piece
        self.destination = destination

        self.initialize_fields()
    
    def initialize_fields(self):
        self.fields = [[-1] * 8 for i in range(8)]
        
        # set distance to piece field as 0
        self.set_field(self.piece.pos_x, self.piece.pos_y, 0)
        
        for figure in self.figures:
            self.set_field(figure.pos_x, figure.pos_y, 'x')
    
    def available_fields(self, pos_x, pos_y, step=0):
        fields = []
        pos = self.piece.all_fields()
        # print(pos_x, pos_y)
        
        for i in range(len(pos)):
            new_x, new_y = chr(ord(pos_x) + pos[i][0]), pos_y + pos[i][1]
            
            if new_x <= 'h' and new_x >= 'a' and new_y <= 8 and new_y >= 1:
                # if on new field isn't any figure then continue
                if self.get_field(new_x, new_y) == 'x':
                    continue
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
    
    def path_map(self):
        # reset path map
        self.initialize_fields()

        self.make_path(self.piece.pos_x, self.piece.pos_y)
    
    def make_path(self, pos_x, pos_y, step=1):
        fields = self.available_fields(pos_x, pos_y, step)
        for field in fields:
            self.set_field(field[0], field[1], step)
            self.make_path(field[0], field[1], step + 1)
    
    def get_distance(self):
        return self.get_field(self.destination[0], self.destination[1])

    def add_figure(self, figure):
        self.figures.append(figure)

        for figure in self.figures:
            self.set_field(figure.pos_x, figure.pos_y, 'x')
