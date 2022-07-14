import tkinter as tk
from tkinter import ttk

from destination import Destination
from figure import *
from option import *


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()

        # load images
        self.img = tk.PhotoImage(file='img/pawn.png')
        self.king_img = tk.PhotoImage(file='img/king.png')

        # configure the root window
        self.title('Chessy Path')
        self.geometry('1200x700')

        # combobox parameters
        self.color = None
        self.x_axis, self.y_axis = None, None

        # init figures
        self.selected_figure = King('e', 1, Color.WHITE)
        self.d = Destination([], self.selected_figure, ('e', 8))

        for i in range(7):
            fig = Pawn(chr(i + 97), 2, Color.WHITE)
            #self.d.figures.append(fig)
            self.d.add_figure(fig)

        self.d.path_map()

        # main canvas
        self.canvas = tk.Canvas(self, bg='#5252b2', width=660, height=660)

        self.show()

        self.canvas.pack(side=tk.LEFT, padx=20)

        # add figure button
        self.add_b = tk.Button(self, text='Dodaj figurę', command=self.figure_menu)
        self.add_b.pack(pady=20, anchor='nw')

    def update(self):
        self.canvas.delete('all')
        self.show()

    def show(self):
        self.show_board()
        self.show_numeration()
        self.show_figures()
        self.show_distances()

    def show_board(self):
        for i in range(8):
            for j in range(8):
                if (j % 2 == 0 and i % 2 == 0) or (j % 2 == 1 and i % 2 == 1):
                    self.canvas.create_rectangle(j * 80, i * 80, (j + 1) * 80, (i + 1) * 80, fill='#ffffff',
                                                 outline='#121270')

    def show_numeration(self):
        # board letters
        for i in range(8):
            self.canvas.create_text((i * 80) + 40, 650, text=chr(i + 65), fill='#ffffff', font=font_numeration())

        # board numbers
        for i in range(8, 0, -1):
            self.canvas.create_text(650, (abs(i - 8) * 80) + 40, text=i, fill='#ffffff', font=font_numeration())

    def show_distances(self):
        for i in range(8):
            for j in range(8):
                text = self.d.fields[::-1][i][j]
                color = '#00ff00'
                if text == -1 or text == 'x':
                    color = '#ff0000'
                self.canvas.create_text((j * 80) + 40, (i * 80) + 40, text=self.d.fields[::-1][i][j], fill=color,
                                        font=distance_font())

    def show_figures(self):
        for figure in self.d.figures:
            self.canvas.create_image(self.get_pos(figure)[0], self.get_pos(figure)[1], image=self.img, anchor='nw')

        self.canvas.create_image(self.get_pos(self.selected_figure)[0], self.get_pos(self.selected_figure)[1],
                                 image=self.king_img, anchor='nw')

    def figure_menu(self):
        def set_color(event):
            self.color = self.color_lb.get()

        def set_x_axis(event):
            self.x_axis = self.x_axis_lb.get()

        def set_y_axis(event):
            self.y_axis = int(self.y_axis_lb.get())

        self.color_lb = ttk.Combobox(self)
        self.color_lb['values'] = ('Białe', 'Czarne')
        self.color_lb['state'] = 'readonly'
        self.color_lb.bind("<<ComboboxSelected>>", set_color)
        self.color_lb.pack()

        self.x_axis_lb = ttk.Combobox(self)
        self.x_axis_lb['values'] = [chr(i + 97) for i in range(8)]
        self.x_axis_lb['state'] = 'readonly'
        self.x_axis_lb.bind("<<ComboboxSelected>>", set_x_axis)
        self.x_axis_lb.pack()

        self.y_axis_lb = ttk.Combobox(self)
        self.y_axis_lb['values'] = [i for i in range(1, 9)]
        self.y_axis_lb['state'] = 'readonly'
        self.y_axis_lb.bind("<<ComboboxSelected>>", set_y_axis)
        self.y_axis_lb.pack()

        self.apply_b = tk.Button(self, text='Zapisz', command=self.add_figure)
        self.apply_b.pack()

    def add_figure(self):
        color = Color.WHITE if self.color == 'white' else Color.BLACK
        print(self.x_axis, self.y_axis)
        fig = Pawn(self.x_axis, self.y_axis, color)
        self.d.add_figure(fig)
        self.d.path_map()

        self.update()



        #self.canvas.create_image(self.get_pos(fig)[0], self.get_pos(fig)[1], image=self.img, anchor='nw')

    def get_pos(self, figure):
        return ((ord(figure.pos_x) - 97) * 80), abs(figure.pos_y - 8) * 80


if __name__ == '__main__':
    app = App()
    app.mainloop()
