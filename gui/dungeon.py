import random
import tkinter as tk
from tkinter import ttk

SIZE = 50
BACKGROUND = "dark slate gray"
TITLE = "white"
PLAYER = "tomato"
EXIT = "yellow"
LINE = "black"
ITEMS = ["coins", "coin bag", "gold jewelry", "gemstones", "small treasure chest"]

m = 8

player_name = ""


def center_window(root, width, height):
    """ Center the window on the screen when creating a new window, otherwise will pop up in the top left corner."""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


class Map:
    """ Create a map of rooms. """

    def __init__(self, master, s):
        self.master = master
        self.s = s
        start_positions = [[0, 0], [s*SIZE - SIZE, 0], [s*SIZE - SIZE, s*SIZE - SIZE], [0, s*SIZE - SIZE]]
        self.start = random.choice(start_positions)
        self.canvas = tk.Canvas(master, width=s*SIZE, height=s*SIZE)
        self.canvas.pack()
        self.draw_map()
        self.draw_player_piece()
        self.finish()
        self.index_rooms()
        self.populate_rooms()
        self.traverse_map()
        self.canvas.bind('<Button-1>', self.move_player_piece)
        self.canvas.bind('<w>', self.move_player_piece)
        self.canvas.bind('<a>', self.move_player_piece)
        self.canvas.bind('<s>', self.move_player_piece)
        self.canvas.bind('<d>', self.move_player_piece)
        # self.canvas.focus_set()

    def draw_map(self):
        """ Draw the map grid. """
        self.canvas.create_rectangle(0, 0, self.s*SIZE, self.s*SIZE, fill=BACKGROUND)
        for i in range(1, self.s):
            self.canvas.create_line(0, i*SIZE, self.s*SIZE, i*SIZE, fill=LINE)
            self.canvas.create_line(i*SIZE, 0, i*SIZE, self.s*SIZE, fill=LINE)

    def draw_player_piece(self):
        """ Draw the player piece. """
        self.piece = self.canvas.create_rectangle(
            self.start[0], self.start[1], self.start[0] + SIZE, self.start[1] + SIZE, fill=PLAYER)

    def move_player_piece(self, event):
        """ Move the player piece using WASD keys or the mouse. Keys only work if the canvas is in focus."""
        if event.keysym == 'w':
            self.canvas.move(self.piece, 0, -SIZE)
        elif event.keysym == 'a':
            self.canvas.move(self.piece, -SIZE, 0)
        elif event.keysym == 's':
            self.canvas.move(self.piece, 0, SIZE)
        elif event.keysym == 'd':
            self.canvas.move(self.piece, SIZE, 0)

        piece_coords = self.canvas.coords(self.piece)
        tile_coords = (event.x // SIZE * SIZE, event.y // SIZE * SIZE,
                       event.x // SIZE * SIZE + SIZE, event.y // SIZE * SIZE + SIZE)
        if (piece_coords[0] == tile_coords[0]
            and abs(piece_coords[1] - tile_coords[1]) == SIZE) or (piece_coords[1] == tile_coords[1]
                                                                   and abs(piece_coords[0] - tile_coords[0]) == SIZE):
            self.canvas.coords(self.piece, tile_coords)
            for item in self.canvas.find_overlapping(*tile_coords):
                if self.canvas.itemcget(item, "fill") == "white":
                    self.canvas.delete(item)
            self.canvas.create_rectangle(
                piece_coords[0], piece_coords[1], piece_coords[0] + SIZE, piece_coords[1] + SIZE, fill="black")
            # If the player is moved to a tile that is black, change the color of the tile to player color
            if self.canvas.itemcget(self.canvas.find_closest(event.x, event.y), "fill") == LINE:
                self.canvas.create_rectangle(
                    tile_coords[0], tile_coords[1], tile_coords[0] + SIZE, tile_coords[1] + SIZE, fill=PLAYER)

        if self.canvas.coords(self.piece) == self.finish():
            self.canvas.create_text(self.s*SIZE/2, self.s*SIZE/2, text="You Win!", fill="red", font=("Arial", 30))
            restart_button = tk.Button(self.master, text="Restart", command=self.restart)
            restart_button.pack()
            quit_button = tk.Button(self.master, text="Quit", command=self.quit)
            quit_button.pack()

    def restart(self):
        """ Restart the game """
        self.canvas.destroy()
        self.master.destroy()
        main()

    def quit(self):
        """ Quit the game """
        self.canvas.destroy()
        self.master.destroy()

    def index_rooms(self):
        """ Index the rooms in the map and their contents"""
        self.rooms = {}
        for i in range(1, self.s**2 + 1):
            self.rooms[i] = None
        for i in range(1, self.s**2 + 1):
            print("Room {}: {}".format(i, self.rooms[i]))

    def populate_rooms(self):
        """ Populate the rooms with items """
        for i in range(1, self.s**2 + 1):
            self.rooms[i] = random.choice(ITEMS)
        for i in range(1, self.s**2 + 1):
            print("Room {}: {}".format(i, self.rooms[i]))

    def traverse_map(self):
        player_items = []
        print("You have collected the following items: {}".format(player_items))

    def finish(self):
        """ Draw the finish square in diagonal of the starting point
        and return the coordinates of the square as a list for checking when the player reaches the finish """

        if self.start == [0, 0]:
            self.canvas.create_rectangle(
                self.s*SIZE - SIZE, self.s*SIZE - SIZE, self.s*SIZE, self.s*SIZE, fill=EXIT)
            return [self.s*SIZE - SIZE, self.s*SIZE - SIZE, self.s*SIZE, self.s*SIZE]
        elif self.start == [self.s*SIZE - SIZE, 0]:
            self.canvas.create_rectangle(
                0, self.s*SIZE - SIZE, SIZE, self.s*SIZE, fill=EXIT)
            return [0, self.s*SIZE - SIZE, SIZE, self.s*SIZE]
        elif self.start == [self.s*SIZE - SIZE, self.s*SIZE - SIZE]:
            self.canvas.create_rectangle(0, 0, SIZE, SIZE, fill=EXIT)
            return [0, 0, SIZE, SIZE]
        elif self.start == [0, self.s*SIZE - SIZE]:
            self.canvas.create_rectangle(
                self.s*SIZE - SIZE, 0, self.s*SIZE, SIZE, fill=EXIT)
            return [self.s*SIZE - SIZE, 0, self.s*SIZE, SIZE]


class Menu:
    """ The menu screen for the game """

    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=m*SIZE, height=m*SIZE)
        self.canvas.pack()
        self.draw_canvas()
        self.draw_buttons()
        self.draw_text()
        self.canvas.bind("<Button-1>", self.click)

    def draw_canvas(self):
        """ Draw the background of the menu """
        self.canvas.create_rectangle(0, 0, m*SIZE, m*SIZE, fill=BACKGROUND)

    def draw_buttons(self):
        """ Draw the buttons for the menu """
        self.canvas.create_rectangle(
            m*SIZE/2 - 50, m*SIZE/4 - 25, m*SIZE/2 + 50, m*SIZE/4 + 25, fill=TITLE)
        self.canvas.create_rectangle(
            m*SIZE/2 - 50, m*SIZE/4 + 50, m*SIZE/2 + 50, m*SIZE/4 + 100, fill=TITLE)
        self.canvas.create_rectangle(
            m*SIZE/2 - 50, m*SIZE/4 + 125, m*SIZE/2 + 50, m*SIZE/4 + 175, fill=TITLE)

    def draw_text(self):
        """ Draw the text for the menu """
        self.canvas.create_text(
            m*SIZE/2, SIZE/2, text="Raiders Of The Lost Kebab", font=("Times", 30), fill=TITLE)
        self.canvas.create_text(
            m*SIZE/2, m*SIZE/4, text="Play", font=("Times", 20), fill=BACKGROUND)
        self.canvas.create_text(
            m*SIZE/2, m*SIZE/4 + 75, text="Exit", font=("Times", 20), fill=BACKGROUND)
        self.canvas.create_text(
            m*SIZE/2, m*SIZE/4 + 150, text="Name", font=("Times", 20), fill=BACKGROUND)

    def click(self, event):
        """ Check if the user clicked on a button """
        click_coords = (event.x, event.y)

        if click_coords[0] >= m*SIZE/2 - 50 and click_coords[0] <= m*SIZE/2 + 50 and click_coords[1] >= m*SIZE/4 - 25 and click_coords[1] <= m*SIZE/4 + 25:
            self.canvas.destroy()

        elif (click_coords[0] >= m*SIZE/2 - 50 and click_coords[0] <= m*SIZE/2 + 50
              and click_coords[1] >= m*SIZE/4 + 50 and click_coords[1] <= m*SIZE/4 + 100):
            self.master.destroy()

        elif (click_coords[0] >= m*SIZE/2 - 50 and click_coords[0] <= m*SIZE/2 + 50
              and click_coords[1] >= m*SIZE/4 + 125 and click_coords[1] <= m*SIZE/4 + 175):
            popup()


class Dificulty(Menu):
    """ The dificulty screen for the game """

    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=m*SIZE, height=m*SIZE)
        self.canvas.pack()
        self.draw_canvas()
        self.draw_buttons()
        self.draw_text()
        self.canvas.bind("<Button-1>", self.click)

    def draw_canvas(self):
        """ Draw the background of the menu """
        self.canvas.create_rectangle(0, 0, m*SIZE, m*SIZE, fill=BACKGROUND)

    def draw_buttons(self):
        """ Draw the buttons for the menu """
        self.canvas.create_rectangle(
            m*SIZE/2 - 50, m*SIZE/4 - 25, m*SIZE/2 + 50, m*SIZE/4 + 25, fill=TITLE)
        self.canvas.create_rectangle(
            m*SIZE/2 - 50, m*SIZE/4 + 50, m*SIZE/2 + 50, m*SIZE/4 + 100, fill=TITLE)
        self.canvas.create_rectangle(
            m*SIZE/2 - 50, m*SIZE/4 + 125, m*SIZE/2 + 50, m*SIZE/4 + 175, fill=TITLE)

    def draw_text(self):
        """ Draw the text for the menu """
        self.canvas.create_text(
            m*SIZE/2, SIZE/2, text="Raiders Of The Lost Kebab", font=("Times", 30), fill=TITLE)
        self.canvas.create_text(
            m*SIZE/2, m*SIZE/4, text="Small", font=("Times", 20), fill=BACKGROUND)
        self.canvas.create_text(
            m*SIZE/2, m*SIZE/4 + 75, text="Medium", font=("Times", 20), fill=BACKGROUND)
        self.canvas.create_text(
            m*SIZE/2, m*SIZE/4 + 150, text="Big", font=("Times", 20), fill=BACKGROUND)

    def click(self, event):
        """ Check if the user clicked on a button """
        click_coords = (event.x, event.y)

        if click_coords[0] >= m*SIZE/2 - 50 and click_coords[0] <= m*SIZE/2 + 50 and click_coords[1] >= m*SIZE/4 - 25 and click_coords[1] <= m*SIZE/4 + 25:
            self.canvas.destroy()
            Map(self.master, 4)

        elif (click_coords[0] >= m*SIZE/2 - 50 and click_coords[0] <= m*SIZE/2 + 50
              and click_coords[1] >= m*SIZE/4 + 50 and click_coords[1] <= m*SIZE/4 + 100):
            self.canvas.destroy()
            Map(self.master, 5)

        elif (click_coords[0] >= m*SIZE/2 - 50 and click_coords[0] <= m*SIZE/2 + 50
              and click_coords[1] >= m*SIZE/4 + 125 and click_coords[1] <= m*SIZE/4 + 175):
            self.canvas.destroy()
            Map(self.master, 8)


class Intro:
    """ The intro screen for the game """

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Raiders Of The Lost Kebab')
        self.window.geometry('512x550')
        center_window(self.window, 512, 550)
        self.canvas = tk.Canvas(self.window, height=512, width=512)
        self.image_file = tk.PhotoImage(file='img/final/splash.png')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        self.canvas.pack(side='top')
        self.button = tk.Button(self.window, text='Play', command=self.close_window)
        self.button.pack(side='top')
        self.window.mainloop()

    def close_window(self):
        self.window.destroy()
        Menu(self.window)


def popup():
    """ Create a popup window, ask for the player's name and return it """
    popup = tk.Tk()
    center_window(popup, 200, 100)
    popup.wm_title("Name")
    label = ttk.Label(popup, text="Enter your name: ")
    label.pack(side="top", fill="x", pady=10)
    entry = ttk.Entry(popup)
    entry.pack()
    button = ttk.Button(popup, text="Enter", command=popup.destroy)
    button.pack()
    player_name = entry.get()
    popup.mainloop()
    return player_name


def start_game():
    """ The main function, create the window and start the game """
    root = tk.Tk()
    root.title("Raiders Of The Lost Kebab")
    center_window(root, m*SIZE, m*SIZE)
    Menu(root)
    Dificulty(root)
    root.mainloop()


def main():
    """ Start the game """
    # Create the intro window
    Intro()
    # Start the game
    start_game()


if __name__ == '__main__':
    main()
