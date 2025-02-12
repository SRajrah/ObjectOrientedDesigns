
from board import Board
from player import Player
from moveValidator import MoveValidator
from winChecker import WinChecker
from observable import Observable
class Game(Observable):
    __instance = None
    def __new__(cls,  *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Game, cls).__new__(cls)
        return cls.__instance
    
    def __init__(self, size):
        super().__init__() #initialze observable
        self.board = Board(size)
        self.players: list[Player] = []
        self.current_player: Player = None
        self.winner: Player = None
    
    def add_players(self, player1: Player, player2: Player):
        self.players = [player1, player2]
        self.current_player = player1
    
    def switch_turn(self):
        self.notify_observers("switching Turns.")
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
    
    def play_turn(self, row : int, col : int):
        if not MoveValidator.is_valid_move(self.board, row, col):
            self.notify_observers("Invalid Move! Try again :/")
            return False
        
        #make the move - mark the move on the board and display
        self.board.mark_cell(row, col, self.current_player.symbol)
        self.board.display()

        #check for win condition
        if WinChecker.check_winner(self.board, self.current_player.symbol):
            self.notify_observers("winner validated")
            self.winner = self.current_player
            return True

        #check for draw or game over
        if self.board.is_full():
            self.notify_observers('board full validated')
            return True

        #game continues if above conditions fail -> switch turn
        self.switch_turn()
        return False

    def start(self):
        self.notify_observers("Welcome to TIC-TAC-TOE, Aasha karte hain aap tic tac ho!")
        self.board.display()

        #start the game loop
        while not self.winner and not self.board.is_full():
            #current players's turn.
            self.notify_observers(f"{self.current_player}'s Turn. ")
            row, col = self.current_player.make_move(self.board)
            self.play_turn(row, col)
            
        
        if self.winner:
            self.notify_observers(f'Congratulations! Player : {self.winner} wins.')
        else:
            self.notify_observers("It's a draw")
        
        self.notify_observers("Game Over.")



    



    

    

