from main import main, pattern

order = int(input("Enter the order of tic tac toe: "))

board = [["-" for i in range(order)] for i in range(order)]
cords = [(j, i) for j in range(order) for i in range(order)]

status = False

i = 0
while not status:
    print(*(i for i in pattern(board)), sep="\n")
    status, player = main(board, order, i)

    if len(player) > 1 and player[-1] in ("A", "B"):
        print(player)
    i += 1
print(*(i for i in pattern(board)), sep="\n")
print(f"Player {player} won!" if len(player) == 1 else player)
