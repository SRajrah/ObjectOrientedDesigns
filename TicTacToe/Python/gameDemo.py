from player import Player
from symbol import Symbol
from game import Game
from board import Board
player1 = Player("Shubham", Symbol.X)
player2 = Player("Maitri", Symbol.O)

game = Game(3)
game.add_players(player1, player2)
game.start()