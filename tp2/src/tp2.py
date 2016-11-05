import random


class FourInARow:
    def __init__(self, playerX, playerO):
        self.board = self.getNewBoard()
        self.playerX, self.playerO = playerX, playerO
        self.playerX_turn = random.choice([True, False])
        self.remainingMoves = 42
        self.potentialMoves = [(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6)] # primera fila vacia por cada columna

    def getNewBoard(self):
        board = []
        for x in range(6):
            board.append([' '] * 7)
        return board

    def playGame(self):
        while True:
            if self.playerX_turn:  #definimos al jugador y al rival
                player, char, other_player = self.playerX, 'X', self.playerO
            else:
                player, char, other_player = self.playerO, 'O', self.playerX

            playerMove = player.move(self.board, self.potentialMoves) #asumimos que el movimiento siempre es valido
            self.board[playerMove[0]][playerMove[1]] = char #actualizamos el tablero
            if playerMove[0] == 0: #modificamos los movimientos posibles 
                self.potentialMoves.remove(playerMove)
            else:
                for index,value in enumerate(self.potentialMoves):
                    if value == playerMove:
                        self.potentialMoves[index] = (self.potentialMoves[index][0]-1,self.potentialMoves[index][1])

            self.remainingMoves = self.remainingMoves - 1

            self.displayBoard()

            if self.playerWin():
                player.reward(1, self.board)
                other_player.reward(-1, self.board)
                break
            if self.boardFull(): # tie game
                player.reward(0.5, self.board)
                other_player.reward(0.5, self.board)
                break

            self.playerX_turn = not self.playerX_turn

    def playerWin(self):
        # horizontal
        for x in range(6):
            for y in range(4):
                if self.board[x][y] != ' ' and self.board[x][y] == self.board[x][y+1] and self.board[x][y+1] == self.board[x][y+2] and self.board[x][y+2] == self.board[x][y+3]:
                    return True

        # vertical
        for x in range(3):
            for y in range(7):
                if self.board[x][y] != ' ' and self.board[x][y] == self.board[x+1][y] and self.board[x+1][y] == self.board[x+2][y] and self.board[x+2][y] == self.board[x+3][y]:
                    return True

        # diagonal /
        for x in range(3):
            for y in range(4):
                if self.board[x+3][y] != ' ' and self.board[x+3][y] == self.board[x+2][y+1] and self.board[x+2][y+1] == self.board[x+1][y+2] and self.board[x+1][y+2] == self.board[x][y+3]:
                    return True

        # diagonal \
        for x in range(3):
            for y in range(4):
                if self.board[x][y] != ' ' and self.board[x][y] == self.board[x+1][y+1] and self.board[x+1][y+1] == self.board[x+2][y+2] and self.board[x+2][y+2] == self.board[x+3][y+3]:
                    return True
              
        return False

    def boardFull(self):
        return self.remainingMoves == 0

    def displayBoard(self):
        print "-----------------------------"
        for raw in self.board:
            print '| ' +' | '.join(raw) + ' |'
            print "-----------------------------"

class Player(object):
    def move(self, board, potentialMoves): #devuelve una tupla perteneciente a potentialMoves
        return random.choice(potentialMoves)

    def reward(self, value, board):
        pass

p1 = Player()
p2 = Player()

for i in xrange(0,2):
    t = FourInARow(p1, p2)
    t.playGame()