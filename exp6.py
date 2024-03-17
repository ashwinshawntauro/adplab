board={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
bot='O'
player='X'

def displayBoard(board):
    print(board[1],' |',board[2],' |',board[3])
    print('---+---+---')
    print(board[4],' |',board[5],' |',board[6])
    print('---+---+---')
    print(board[7],' |',board[8],' |',board[9])

def insertLetter(letter,position):
    if isSpaceEmpty(position):
        board[position]=letter
        displayBoard(board)
        if(checkDraw()):
            print('Draw!')
            sys.exit()
        if(checkWin()):
            if letter=='X':
                print('Player wins!')
            else:
                print("Bot Wins!")
    else:
        print('Cannot place in this position')
        position=int(input('Enter the position again: '))
        insertLetter(letter,position)

def isSpaceEmpty(position):
    if(board[position]==' '):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if(board[key]==' '):
            return False
    return True

def checkWin():
    if(board[1]==board[2] and board[1]==board[3] and board[1]!=' '):
        return True
    elif(board[4]==board[5] and board[4]==board[6] and board[4]!=' '):
        return True
    elif(board[7]==board[8] and board[7]==board[9] and board[7]!=' '):
        return True
    elif(board[1]==board[4] and board[1]==board[7] and board[1]!=' '):
        return True
    elif(board[2]==board[5] and board[2]==board[8] and board[2]!=' '):
        return True
    elif(board[3]==board[6] and board[3]==board[6] and board[3]!=' '):
        return True
    elif(board[1]==board[5] and board[1]==board[9] and board[1]!=' '):
        return True
    elif(board[7]==board[5] and board[7]==board[3] and board[7]!=' '):
        return True
    else:
        return False

def playerMove():
    position=int(input('Enter the position for X: '))
    insertLetter(player,position)
    return

def compMove():
    position=int(input('Enter the position for O: '))
    insertLetter(bot,position)
    return

displayBoard(board)
while not checkWin():
    compMove()
    playerMove()