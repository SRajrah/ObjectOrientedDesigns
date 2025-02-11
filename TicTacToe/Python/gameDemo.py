from player import Player
from symbol import Symbol
from game import Game
from board import Board
from humanMoveStrategy import HumanMoveStrategy
from aiMoveStrategy import AIMoveStrategy

player1 = Player("Shubham", Symbol.X, HumanMoveStrategy())
player2 = Player("Maitri", Symbol.O, AIMoveStrategy())

game = Game(3)
game.add_players(player1, player2)
game.start()