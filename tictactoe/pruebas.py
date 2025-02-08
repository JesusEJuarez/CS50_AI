from tictactoe import initial_state, player, actions,result,winner,terminal, utility

X = "X"
O = "O"
EMPTY = None

board =    [[O, X, O],
            [O, O, O],
            [EMPTY, X, X]]
if not None:
    print(utility(board))