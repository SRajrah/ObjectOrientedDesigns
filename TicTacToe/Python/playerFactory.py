from symbol import Symbol
from humanMoveStrategy import HumanMoveStrategy
from aiMoveStrategy import AIMoveStrategy
from player import Player
class PlayerFactory:
    @staticmethod
    def create_player(player_type: str, name: str, symbol: Symbol):
        if player_type == 'Human':
            return Player(name, symbol, HumanMoveStrategy())
        elif player_type == 'AI':
            return Player(name, symbol, AIMoveStrategy())
        else:
            raise ValueError("Invalid Player type. Please choose 'Human' or 'AI' :/")