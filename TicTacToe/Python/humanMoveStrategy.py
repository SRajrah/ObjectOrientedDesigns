from moveStrategy import MoveStrategy


class HumanMoveStrategy(MoveStrategy):
    def get_move(self, board):
        row, col = map(int, input("Enter row, col for your move: ").split())
        return row, col
