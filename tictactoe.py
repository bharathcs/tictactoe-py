board = ['x']
ingame = True

for _ in range(9):
    board.append(' ')

def display(board):
    print(' | '.join(board[1:4]),)
    print('-' * 15)
    print(' | '.join(board[4:7]))
    print('-' * 10)
    print(' | '.join(board[7:]))
    print()

def userinput(board):
    print("Next Player: ", board[0])
    possible_moves = []
    for i in range(1,10):
        if board[i] == ' ':
            possible_moves.append(str(i))
    result = input("Enter your next position or press 'h' for help\n")
    
    while result not in possible_moves:
        print(possible_moves)
        display(board)
        print("Type a number that corresponds to the position you want")
        display(['','1','2','3','4','5','6','7','8','9'])
        result = input("Enter your next position or press 'h' for help\n")
    
    return int(result)

def update(next_move,board):
    if board[next_move] != ' ':
        raise Exception("Trying to change a mark")

    board[next_move] = board[0]
    players = ['o','x']

    if board[0] == 'x':
        nextplayer = 0
    elif board[0] == 'o':
        nextplayer = 1

    board[0] = players[nextplayer]
    return(board)

def checkgame(board):
    lines = []
    lines.append(board[1::3])
    lines.append(board[2::3])
    lines.append(board[3::3])
    lines.append(board[1:4])
    lines.append(board[4:7])
    lines.append(board[7:])
    lines.append([board[1],board[5],board[9]])
    lines.append([board[3],board[5],board[7]])
    if ['x','x','x'] in lines:
        return False, 'x'
    elif ['o','o','o'] in lines:
        return False, 'o'
    
    flattenlines = ""
    noblank = True
    for i in lines:
        for j in i:
            flattenlines += j
            if j == ' ':
                noblank = False
    
    if noblank:
        return False, "NA"
    return True, "NA"
    

while ingame:
    display(board)
    next_move = userinput(board)
    board = update(next_move,board)
    ingame, whowon = checkgame(board)

display(board)
if whowon == "NA":
    print("Draw.")
    display(board)
else:
    print("Congratulations, Player", whowon, "has won.")
    display(board)