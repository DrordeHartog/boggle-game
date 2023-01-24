import tkinter as tki
from typing import Callable, Dict, List, Any
from datetime import timedelta

SQUARE_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'gray'
SQUARE_ACTIVE_COLOR = 'slateblue'
SQUARE_SPECIAL_COLOR = 'green'

SQUARE_STYLE = {"font": {"Courier", 60},
                "borderwidth": 5,
                "relief": tki.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": SQUARE_ACTIVE_COLOR
                }


class GUI:
    def __init__(self, board) -> None:
        root = tki.Tk()
        root.title("Boggle")
        root.resizable(True, True)
        root.geometry("1600x1600")  # double check default size
        self._board = board

        self._squares: Dict[tuple, tki.Button] = {}
        self.pressed_squares: [tki.Button] = []
        self._last_clicked_square = None
        self._current_word = []

        self._main_window = root
        self._outer_frame = tki.Frame(root,  bg=REGULAR_COLOR)
        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self._game_frame = tki.Frame(self._outer_frame, bg=REGULAR_COLOR)
        self._game_frame.place(relx=0.5, rely=0.5, anchor='center')

        # timer
        self._timer = tki.Label(self._game_frame, text="3:00", font=(
            "Courier", 30), bg=REGULAR_COLOR, width=10, relief=tki.SUNKEN)
        self._timer.grid(row=0, column=1, columnspan=4, sticky="nsew")
        self._time_left = timedelta(minutes=3)
        self.timer_id = None

        # the board
        self._board_frame = tki.Frame(self._game_frame, bg=REGULAR_COLOR,
                                      highlightbackground=REGULAR_COLOR, width=400, height=400, highlightthickness=5)
        self._board_frame.grid(row=1, column=1, columnspan=4, rowspan=4)

        # display label
        self._display_label = tki.Label(self._game_frame, font=("Courier", 30), bg=REGULAR_COLOR,
                                        width=10, relief=tki.SUNKEN)
        self._display_label.grid(
            row=5, column=1, columnspan=4, sticky="nsew")

        # Found words object
        self._found_words = tki.Listbox(self._game_frame, font=(
            "Courier", 30), bg=REGULAR_COLOR, width=10, relief=tki.SUNKEN)
        self._found_words.grid(row=2, column=5, sticky="new")

        # score_board
        self._score_board = tki.Label(self._game_frame, text="Score: 0", font=(
            "Courier", 30), bg=REGULAR_COLOR, relief=tki.SUNKEN)
        self._score_board.grid(row=1, column=5, rowspan=1,
                               columnspan=1, pady=10, sticky="new")
        # start and new game buttons
        self._start_game_button = tki.Button(
            self._game_frame, text="Start Game", font=("Courier", 30))
        self._start_game_button.grid(row=2, column=0, sticky="new")

        #
        self._new_game_button = tki.Button(
            self._game_frame, text="New Game", font=("Courier", 30))
        self._new_game_button.grid(row=3, column=0, sticky="new")

        #
        self._create_squares_in_board_frame()
    # remove?

    def get_square_locations(self) -> list:
        return list(self._squares.keys())

    def run(self) -> None:
        self._main_window.mainloop()

    def get_display_label(self):
        print("sending display_text")
        return self._display_label['text']
    
    def reset_display_label(self):
        self._display_label['text'] = ''
    
    def update_display_label(self, letter: str):
        self._display_label['text'] += letter

    def _create_squares_in_board_frame(self):
        for i in range(4):
            self._board_frame.rowconfigure(i, weight=1)

        for i in range(4):
            self._board_frame.columnconfigure(i, weight=1)

        for i in range(4):
            for j in range(4):
                self._create_square(i, j, self._board[i][j])

    def press_square(self, coor):
        self._squares[coor]["relief"] = tki.SUNKEN
        self.pressed_squares.append(coor)

    def depress_square(self, coor):
        self._squares[coor]["relief"] = tki.RAISED

    def _create_square(self, row, col, char):
        square = tki.Button(self._board_frame, text=char,
                            width=10, height=5, state='disabled', **SQUARE_STYLE)
        square.grid(row=row, column=col)
        square.location(row, col)
        self._squares[(row, col)] = square

        def _on_enter(event: Any, square) -> None:
            self._squares[(row, col)]['background'] = SQUARE_HOVER_COLOR

        def _on_leave(event: Any, square) -> None:
            self._squares[(row, col)]['background'] = REGULAR_COLOR

        square.bind("<Enter>", lambda event,
                    square=square: _on_enter(event, square))
        square.bind("<Leave>", lambda event,
                    square=square: _on_leave(event, square))

        return square

    def start_timer(self):
        self._start_game_button.config(state='disabled')
        self.countdown()

    def countdown(self):
        print("timer started")
        if self._time_left > timedelta(0):
            self._time_left -= timedelta(seconds=1)
            self._timer.config(text=str(self._time_left))
            self.timer_id = self._game_frame.after(1000, self.countdown)
        else:
            self.reset_display_label()
            self.update_display_label('Times Up!')

    def stop_timer(self):
        print("timer_stopped")
        self._game_frame.after_cancel(self.timer_id)

    def reset_timer(self):
        self.stop_timer()
        self._time_left = timedelta(minutes=3)
        self._timer['text'] = "3:00"
        self._start_game_button.config(state='normal')

    def reset_score(self):
        self.set_score(0)

    def set_score(self, score: int = 0):
        self._score_board['text'] = "Score:" + str(score)

    def add_found_word(self, word):
        self._found_words.insert(self._found_words.size() + 1, word)

    def reset_found_words(self):
        self._found_words.delete(0, self._found_words.size())

    def set_square_command(self, location, cmd) -> None:
        self._squares[location].configure(command=cmd)

    def reset_path_gui(self):
        for location in self.pressed_squares:
            print("location depressed = " + str(location))
            self.depress_square(location)
        self.pressed_squares = []

    def reset_board_frame(self):
        for location in self._squares:
            self._squares[location]['text'] = self._board[location[0]][location[1]]

    def disable_board(self):
        for location in self._squares:
            self._squares[location]["state"] = 'disabled'

    def activate_board(self):
        for location in self._squares:
            self._squares[location]["state"] = 'normal'

    def reset_gui(self, board):
        self._board = board
        self.reset_score()
        self.reset_path_gui()
        self.reset_display_label()
        self.reset_found_words()
        self.reset_board_frame()
        self.reset_timer()
        self.disable_board()
