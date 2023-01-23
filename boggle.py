from typing import Callable
from boggle_gui import *
from boggle_model import *
import ex11_utils as utils

BOARD_SIZE = 4

# receive text and create dict of words



class Boggle:
    def __init(self) -> None:
        self._game = Game()
        self._gui = BoardGUI(self._game.board)
        for location in gui.get_square_locations():
            action = self.create_square_functionality(self, location)
            self._gui.set_square_command(location, action)

    def create_square_functionality(self, location):
        def fun() -> None:
            self._game.type_in(location)
            self._gui.
            return
        return fun