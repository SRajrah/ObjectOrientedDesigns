from player import Player
from symbol import Symbol
from game import Game
from board import Board
from humanMoveStrategy import HumanMoveStrategy
from aiMoveStrategy import AIMoveStrategy
from playerFactory import PlayerFactory
# player1 = Player("Shubham", Symbol.X, HumanMoveStrategy())
# player2 = Player("Maitri", Symbol.O, AIMoveStrategy())
player1 = PlayerFactory.create_player("Human", "Shubham", Symbol.X)
player2 = PlayerFactory.create_player("AI", "Robot", Symbol.O)


game = Game(3)
game.add_players(player1, player2)
game.start()