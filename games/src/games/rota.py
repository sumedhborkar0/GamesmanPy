from models import Game, Value, StringMode
from typing import Optional

EMPTY, X, O = 0, 1, 2 # integers for cell status
CHARS = ['-', 'x', 'o'] # chars for cell status

RING = [0, 1, 2, 5, 8, 7, 6, 3] # ring of cell numbers around the board
CENTER = 4
NEIGHBORS = [None] * 9 # list of 9 elements
for idx, cell in enumerate(RING):
    NEIGHBORS[cell] = [RING[idx - 1], RING[idx + 1], CENTER] # creating adjacency list
NEIGHBORS[CENTER] = RING[:] # all elems adjacent to center

# winning lines below
DIAMETERS = [(0, 4, 8), (2, 4, 6), (3, 4, 5), (1, 4, 7)]
RIM_LINES = [(RING[i], RING[(i+1) % 8], RING[(i+2) % 8]) for i in range(8)]
LINES = DIAMETERS + RIM_LINES # winning positions

class Rota(Game):
    id = 'rota'
    variants = ["regular"]
    n_players = 2
    cyclic = True

    def __init__(self, variant_id: str):
        """
        Define instance variables here (i.e. variant information)
        """
        if variant_id not in Rota.variants:
            raise ValueError("Variant not defined")
        self._variant_id = variant_id
        self.

    def start(self) -> int:
        """
        Returns the starting position of the game.
        """
        pass
    
    def generate_moves(self, position: int) -> list[int]:
        """
        Returns a list of positions given the input position.
        """
        pass
    
    def do_move(self, position: int, move: int) -> int:
        """
        Returns the resulting position of applying move to position.
        """
        pass

    def primitive(self, position: int) -> Optional[Value]:
        """
        Returns a Value enum which defines whether the current position is a win, loss, or non-terminal. 
        """
        pass

    def to_string(self, position: int, mode: StringMode) -> str:
        """
        Returns a string representation of the position based on the given mode.
        """
        pass

    def from_string(self, strposition: str) -> int:
        """
        Returns the position from a string representation of the position.
        Input string is StringMode.Readable.
        """
        pass

    def move_to_string(self, move: int, mode: StringMode) -> str:
        """
        Returns a string representation of the move based on the given mode.
        """
        pass

    