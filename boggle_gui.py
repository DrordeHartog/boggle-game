import tkinter as tki
from typing import Callable, Dict, List, Any

SQUARE_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
SQUARE_ACTIVE_COLOR = 'slateblue'

SQUARE_STYLE = {"font": {"Courier", 30},
                "borderwidth": 1,
                "relief": tki.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": SQUARE_ACTIVE_COLOR}

'''

Here are the steps you can follow to create a Boggle GUI using Tkinter and OOP:

Create a Board class that will represent the overall Boggle board.
This class should have methods for initializing the board, displaying the board,
and checking for valid words.

Create a Square class that will represent each individual square on the board.
This class should have methods for displaying the square and checking if it has been selected.

Use Tkinter to create a GUI for the Boggle game. This could include a button
for starting the game, a display for the current word, and a display for the score.

Use Tkinter to create a grid of Square widgets. Each widget should be
associated with a square on the Board object.

Add event handlers to the Square widgets so that they can be selected
by the player. These event handlers should update the Board object to
keep track of the current word and update the GUI to reflect the current word.

Once the player has selected all the squares for a word, the program
should check if the word is valid and update the score accordingly.

Create a method that will create a random board everytime the game starts.
import tkinter as tk

class Square(tk.Button):
    def __init__(self, parent, row, col, letter):
        super().__init__(parent)
        self.row = row
        self.col = col
        self.letter = letter
        self.config(text=self.letter)
        self.config(width=5, height=2)
        self.config(font=("Courier", 24))
        self.config(bg="white", activebackground="white", relief="solid")
        self.config(command=self.handle_click)
        self.is_selected = False
        
    def handle_click(self):
        self.config(bg="yellow")
        self.is_selected = True
        
        
        
        '''


class Square:
    def __init__(self, location: tuple[int, int], letter: str):
        self.button = tki.Button(text=letter, **SQUARE_STYLE)

    def light_up(self):
        ...

    def cursor_tickle(self):
        ...

    def add_to_bar(self):

        ...


class BoardGUI():
    def __init__(self) -> None:
        pass


class Word_board():
    def __init__(self) -> None:

        pass

    def add_letters(self):
        ...


def zipper(head1, head2) -> None:
    head = head1


def is_repetative(lst):
    while head:
        for i in range(len(lst)):
            if head == lst[i]:
                head = head.next
            else:
                return False
