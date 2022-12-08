playedMoves = []


def isWinner(rows, index, symbol, player):
    forward = [[rows[i][i] for i in range(len(rows))]]
    backward = [[rows[::-1][i][i] for i in range(len(rows))][::-1]]
    transpose = [[rows[j][i] for j in range(len(rows[i]))] for i in range(len(rows))]

    temp = [rows, transpose, forward, backward]
    tiestatus = [True if "X" in j and "O" in j else False for i in temp for j in i]

    if all(tiestatus):
        return True, "Its a tie!"

    for i in forward + backward + transpose + rows:
        if i.count(symbol) == index:
            return True, player
    return False, player


def main(board, index, iteration):
    player, symbol = ("A", "X") if iteration % 2 == 0 else ("B", "O")
    row, column = [int(i) for i in input(f"Player {player} your postion : ").split()]

    if row not in range(1, (index + 1)) or column not in range(1, (index + 1)):
        return False, f"invalid input! You lost your turn {player}"

    elif (row, column) not in playedMoves:
        playedMoves.append((row, column))

        board[row - 1][column - 1] = symbol
        return isWinner(board, index, symbol, player)

    else:
        return False, f"No repetition! You lost you turn {player}"


def pattern(val):
    for i in val:
        yield " ".join(i)
