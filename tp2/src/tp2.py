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
        self.playerX.start_game(self.board)
        self.playerO.start_game(self.board)
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
            if self.playerWin():
                player.reward(1, self.board, self.potentialMoves)
                other_player.reward(-1, self.board, self.potentialMoves)
                break
            if self.boardFull(): # tie game
                player.reward(0.5, self.board, self.potentialMoves)
                other_player.reward(0.5, self.board, self.potentialMoves)
                break
            other_player.reward(0, self.board, self.potentialMoves) # Le avisa al otro jugador que aprenda que su jugada no lo hizo perder ni empatar (si uhbiese ganado, se daba cunta en la ronda anterior)
            self.playerX_turn = not self.playerX_turn

        #self.displayBoard()


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
        print("-----------------------------")
        for raw in self.board:
            print('| ' +' | '.join(raw) + ' |')
            print("-----------------------------")


class Player(object):
    def __init__(self):
        self.breed = 'random'
        self.win = 0

    def move(self, board, potentialMoves): #devuelve una tupla perteneciente a potentialMoves
        return random.choice(potentialMoves)

    def start_game(self, board):
        pass

    def reward(self, value, board, potentialMoves):
        if value == 1:
            self.win += 1
            
    def score(self):
        return self.win


class QLearningPlayer(object):
                        #epsilon=0.2, alpha=0.3, gamma=0.9
    def __init__(self, epsilon=0.2, alpha=0.3, gamma=0.9):
        self.breed = "Qlearner"
        self.q = {} # (state, action) keys: Q values
        self.epsilon = epsilon # e-greedy chance of random exploration
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor for future rewards
        self.win = 0
        self.escenario = 0

    def start_game(self, board):
        self.last_board = [x[:] for x in board]
        self.last_move = None

    def make_str(self, state, action):
        action_str = str(action[0]) + str(action[1])
        state_str = [''.join(rows) for rows in state]
        state_str = '_'.join(state_str)
        
        return state_str, action_str

    def getQ(self, state, action):
        # encourage exploration; "optimistic" 1.0 initial values
        # paso a string el estado y decision para crear las claves del dict
        state_str, action_str = self.make_str(state, action)
        
        if self.q.get((state_str, action_str)) is None:
            self.q[(state_str, action_str)] = 0.0
            self.escenario += 1
        return self.q.get((state_str, action_str))

    def setQ(self, state, action, value):
        state_str, action_str = self.make_str(state, action)
        self.q[(state_str, action_str)] = value

    def move(self, board, actions): 
        self.last_board = [x[:] for x in board] #last_board = S
        #elijo la mejor accion (last_move) para el S actual
        if random.random() < self.epsilon: # explore!
            self.last_move = random.choice(actions)
            return self.last_move
        qs = [self.getQ(self.last_board, a) for a in actions] #elijo la accion con mejor Q
        maxQ = max(qs)

        if qs.count(maxQ) > 1:
            # more than 1 best option; choose among them randomly
            best_options = [i for i in range(len(actions)) if qs[i] == maxQ]
            i = random.choice(best_options)
        else:
            i = qs.index(maxQ)

        self.last_move = actions[i]
        return actions[i]

    def reward(self, value, board, actions=[]):
        if self.last_move:
            self.learn(self.last_board, self.last_move, value, tuple(board), actions)
        if value == 1:
            self.win += 1

    def learn(self, state, action, reward, result_state, actions):
        prev = self.getQ(state, action)
        if reward == 0: #no estoy seguro de esto pero es para que no vea las acciones siguientes a un estado ganador/perdedor/empatado
            try:
            	maxqnew = max([self.getQ(result_state, a) for a in actions])
            except ValueError:
            	maxqnew = 0
        else:
            maxqnew = 0
        new_value = prev + self.alpha * ((reward + self.gamma*maxqnew) - prev)
        self.setQ(state, action, new_value)

    def score(self):
        return self.win
    
    def set_epsilon(self, eps):
        self.epsilon = eps
    
    def set_alpha(self, al):
        self.alpha = al
    
    def set_gamma(self, ga):
        self.gamma = ga

#%% Funciones de los distintos test a correr
def Sweep_param():
    epsilones = [0, 0.2, 0.4, 0.6, 0.8, 1]
    #alfas = [0, 0.2, 0.4, 0.6, 0.8, 1]
    #gammas = [0, 0.2, 0.4, 0.6, 0.8, 1]
    
    #epsilon=0.2, alpha=0.3, gamma=0.9
    for eps in epsilones:
        for n in range(0, 6):
            p1 = QLearningPlayer(epsilon=eps)
            p2 = Player()
            
            saveName = r'Resultados\Optimizacion_e'+str(round(10*eps))+'_n'+str(n)+'.txt'
            newfile = open(saveName, 'w')
            newfile.close()
            
            for i in range(0,200000):
                t = FourInARow(p1, p2)
                t.playGame()
                """ No hace falta mostrar nada si uno tiene Fe
                print "epsilon=0.2, alpha=0.3, gamma=0.9"
                print "Round: " + str(i)
                print "QLearning win: " + str(p1.score())
                print "Random win: " + str(p2.score())
                print "tie: " + str(i - p1.score() - p2.score())
                t.displayBoard()
                """
                res = [str(i+1), str(p1.score()), str(p2.score())]
                str_to_append = '\t'.join(res)
                str_to_append = '\n' + str_to_append
                
                with open(saveName, "a") as myfile:
                    myfile.write(str_to_append)

def Train_Until(partida):
    for n in range(0, 6):
        p1 = QLearningPlayer(epsilon=1)
        p2 = Player()
        
        saveName = r'Resultados\PreEntrenamiento_partidas'+str(partida)+'_n'+str(n)+'.txt'
        newfile = open(saveName, 'w')
        newfile.close()
        
        for i in range(0,200000):
            t = FourInARow(p1, p2)
            t.playGame()
            
            res = [str(i+1), str(p1.score()), str(p2.score())]
            str_to_append = '\t'.join(res)
            str_to_append = '\n' + str_to_append
            
            with open(saveName, "a") as myfile:
                myfile.write(str_to_append)
            
            if i==partida:
                p1.set_epsilon(0)

def QvsQ():
    for n in range(0, 6):
        p1 = QLearningPlayer()
        p2 = QLearningPlayer()
        
        saveName = r'Resultados\QvsQ_n'+str(n)+'.txt'
        newfile = open(saveName, 'w')
        newfile.close()
        
        for i in range(0,200000):
            t = FourInARow(p1, p2)
            t.playGame()
            
            res = [str(i+1), str(p1.score()), str(p2.score())]
            str_to_append = '\t'.join(res)
            str_to_append = '\n' + str_to_append
            
            with open(saveName, "a") as myfile:
                myfile.write(str_to_append)
        
        p2.set_alpha(0) # deja de aprender
        
        for i in range(200000,600000):
            t = FourInARow(p1, p2)
            t.playGame()
            
            res = [str(i+1), str(p1.score()), str(p2.score())]
            str_to_append = '\t'.join(res)
            str_to_append = '\n' + str_to_append
            
            with open(saveName, "a") as myfile:
                myfile.write(str_to_append)

#%% Pruebas a correr

hasta_partida = [500, 1000, 5000, 10000, 50000, 100000]

for this_partida in hasta_partida:
    Train_Until(this_partida)

QvsQ()