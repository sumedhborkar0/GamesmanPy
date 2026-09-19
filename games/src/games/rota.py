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
        self._lines = LINES


    def _unpack(position : int) -> tuple[list[int], int]:
        """_summary_
        takes in the position int and performs bitwise operations to 
        get turn num and position list

        Args:
            position (int): integer storing board position and turn

        Returns:
            tuple[list[int], int]: tuple containing board state, int containing turn num
        """
        
        turn = position & 1 #isolates last bit of the position aka the turn num
        position = position >> 1 #get rid of final turn bit
        board = []
        

        # will shift bits of position by 2 every iteration, since 2 bits to store each cell
        # take those bits rightmost and append them to board
    
        for i in range(9):
            board.append(position & 0b11) # mask to get last two bits of pos
            position = position >> 2 #shift off curr cell bits
        return board, turn


    def _pack(board: list[int], turn: int) -> int:
        """_summary_
    
            Args:
                board (list[int]): list with integers to represent the pieces on the board
                turn (int): 0 or 1, whose turn it is
    
            Returns:
                int: 19 bit integer with whose turn it is and positions of pieces on board
    
            takes in board as list and turn (0 or 1) and encodes those into 19 bit
            value where first bit is whose turn (0 or 1) and rest is what piece in which
            position (01 is X, 10 is 0, 00 is empty)
            Ex. (0b1000000000000000010) means X turn and O in position 0, X in position 8
            """         
        position = turn
        for i in range(9):
            position |= board[i] << (2 * i + 1)
        return position

    def _decode_move(move : int) -> tuple:
        """_summary_

        Args:
            move (int): _description_

        Returns:
            tuple: _description_
        """
        pass

    def start(self) -> int:
        """
        Returns the starting position of the game.
        """
        return 0
    
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
        board, turn = self._unpack(position)
        cells = ''.join(CHARS[c] for c in board)

        if mode == StringMode.AUTOGUI:
            return ('1_' if turn == 0 else '2_') + cells

        if mode == StringMode.TUI:
            rows = [' '.join(cells[r * 3:(r + 1) * 3]) for r in range(3)]
            return '\n'.join(rows)

        return cells + ('x' if turn == 0 else 'o')

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

    