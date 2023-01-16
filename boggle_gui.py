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

class Square:
    def __init__(self, location, letter):
        self.button = tki.Button(text = letter, **SQUARE_STYLE)

    def light_up():
        ...

    def cursor_tickle():
        ...

    def add_to_bar():

        ...


class BoardGUI():
    def __init__(self) -> None:
        self.
        pass


class Word_board():
    def __init__(self) -> None:

        pass

    def add_letters(self):
        ...

class sco

def zipper(head1, head2) -> None:
    head = head1

def is_repetative(lst):
    while head:
        for i in range(len(lst)):
            if head == lst[i]:
                head = head.next
            else:
                return False
