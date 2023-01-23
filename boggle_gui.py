import tkinter as tki
import tkmacosx as tk
from typing import Callable, Dict, List, Any

SQUARE_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
SQUARE_ACTIVE_COLOR = 'slateblue'
SQUARE_SPECIAL_COLOR = 'green'

SQUARE_STYLE = {"font": {"Courier", 30},
                "borderwidth": 5,
                "relief": tki.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": SQUARE_ACTIVE_COLOR}

'''

Here are the steps you can follow to create a Boggle GUI using tkiinter and OOP:

Create a Board class that will represent the overall Boggle board.
This class should have methods for initializing the board, displaying the board,
and checking for valid words.

Create a Square class that will represent each individual square on the board.
This class should have methods for displaying the square and checking if it has been selected.

Use tkiinter to create a GUI for the Boggle game. This could include a button
for starting the game, a display for the current word, and a display for the score.

Use tkiinter to create a grid of Square widgets. Each widget should be
associated with a square on the Board object.

Add event handlers to the Square widgets so that they can be selected
by the player. These event handlers should update the Board object to
keep track of the current word and update the GUI to reflect the current word.

Once the player has selected all the squares for a word, the program
should check if the word is valid and update the score accordingly.

Create a method that will create a random board everytime the game starts.
import tkinter as tki


        
        
        
        '''

class BoardGUI:
    def __init__(self, board) -> None:
        root = tki.Tk()
        root.title = "Boggle"
        root.resizable(True, True)
        root.geometry("800x800")

        self._squares: Dict[str, tki.Button] = {}

        self._main_window = root
        self._outer_frame = tki.Frame(root,  bg=REGULAR_COLOR)
        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self._game_frame = tki.Frame(self._outer_frame, bg=REGULAR_COLOR)
        self._game_frame.place(relx=0.5, rely=0.5, anchor='center')

        self._timer = tki.Label(self._game_frame, text="Time: 0", font=("Courier", 30), bg=REGULAR_COLOR, width=10, relief=tki.SUNKEN)
        self._timer.grid(row=0, column=1, columnspan=4, sticky="nsew")

        self._board_frame = tki.Frame(self._game_frame, bg=REGULAR_COLOR, highlightbackground=REGULAR_COLOR, width=400, height=400, highlightthickness=5)
        self._board_frame.grid(row=1, column=1, columnspan=4, rowspan=4)

        # Current word object
        self._current_word = tki.Label(self._game_frame, font=("Courier", 30), bg=REGULAR_COLOR, width=10,
                                relief=tki.SUNKEN)
        self._current_word.grid(row=5, column=1, columnspan=4, sticky="nsew")

        # Found words object
        self._found_words = tki.Listbox(self._game_frame, font=("Courier", 30), bg=REGULAR_COLOR, width=10, relief=tki.SUNKEN)
        self._found_words.grid(row=2, column=5, sticky="new")
        #
        #
        self._score_board = tki.Label(self._game_frame, text="Score: 0", font=("Courier", 30), bg=REGULAR_COLOR, relief=tki.SUNKEN)
        self._score_board.grid(row=1, column=5, rowspan=1, columnspan=1, pady=10, sticky="new")
        #
        self._new_game_button = tki.Button(self._game_frame, text="New Game", font=("Courier", 30), command=self._new_game)
        self._new_game_button.grid(row=1, column=0, sticky="new")
        #
        self._create_squares_in_board_frame(board)


    def run(self) -> None:
        self._main_window.mainloop()

    def _new_game(self):
        pass


    def on_square_clicked(self, square):
        print("clicked")
        if square["relief"] == tki.SUNKEN:
            square.config(relief=tki.RAISED)
        else:
            square.config(relief=tki.SUNKEN)
        return

    def _create_squares_in_board_frame(self, board):
        for i in range(4):
            self._board_frame.rowconfigure(i, weight=1)

        for i in range(4):
            self._board_frame.columnconfigure(i, weight=1)

        for i in range(4):
            for j in range(4):
                square = tki.Button(self._board_frame, text=board[i][j], width=10, height=5, **SQUARE_STYLE)
                square.grid(row=i, column=j)
                square.bind("<Button-1>", lambda event, square=square: self.on_square_clicked(square))






#                 return False
board = [['A', 'T', 'R', 'Q'],
         ['Q', 'L', 'E', 'Q'],
         ['Q', 'Q', 'B', 'Q'],
         ['Q', 'Q', 'Q', 'Q']]

gui = BoardGUI(board)
gui.run()
