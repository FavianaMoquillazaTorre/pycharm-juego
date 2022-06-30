import random

def Board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def inputLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('¿Cual quieres ser x - o ?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def First():
    if random.randint(0, 1) == 0:
        return 'computadora'
    else:
        return 'jugador'

def playAgain():
    print('¿Quieres jugar de nuevo? (si o no)')
    return input().lower().startswith('s')

def makeMove(board, letter, move):
    board[move] = letter

def Winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def BoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpace(board, move):
    return board[move] == ' '

def PlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpace(board, int(move)):
        print('¿Cuál es su próximo movimiento? (1-9)')
        move = input()
    return int(move)

def RandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpace(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def ComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = BoardCopy(board)
        if isSpace(copy, i):
            makeMove(copy, computerLetter, i)
            if Winner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = BoardCopy(board)
        if isSpace(copy, i):
            makeMove(copy, playerLetter, i)
            if Winner(copy, playerLetter):
                return i

    move = RandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpace(board, 5):
        return 5

    return RandomMoveFromList(board, [2, 4, 6, 8])

def BoardFull(board):
    for i in range(1, 10):
        if isSpace(board, i):
            return False
    return True
print("Bienvenido al juego")

print(" ///// Tres en raya ///// ")

while True:
    theBoard = [' '] * 50
    playerLetter, computerLetter = inputLetter()
    turn = First()
    print('El ' + turn + ' ira primero.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'jugador':
            Board(theBoard)
            move = PlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if Winner(theBoard, playerLetter):
                Board(theBoard)
                print('El jugador gano a la computadora. ¡Has ganado el juego!')
                gameIsPlaying = False
            else:
                if BoardFull(theBoard):
                    Board(theBoard)
                    print('Esto es un empate!')
                    break
                else:
                    turn = 'computadora'

        else:
            move = ComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if Winner(theBoard, computerLetter):
                Board(theBoard)
                print('La computadora gano al jugador. Perdiste!')
                gameIsPlaying = False
            else:
                if BoardFull(theBoard):
                    Board(theBoard)
                    print('Empate!')
                    break
                else:
                    turn = 'jugador'

    if not playAgain():
        break