import numpy as np

class Player():
    
    def __init__(self, name):

        self.nextPlayer = None
        self.name = name # player name will be from 0 to some larger integer

        # self.board = self.createBoard()
        self.shipPosition = self.randCoord() # ship position for each player is fixed in one game
        self.bombPosition = None

    """
    def createBoard(self):
        board = np.zeros((10, 10), int) # empty game board
        return board
    """

    def randCoord(self):
        randRow = np.random.randint(0, 10)
        randCol = np.random.randint(0, 10)
        return [randRow, randCol]

    def checkWin(self):
        self.bombPosition = self.randCoord() # a random guess
        # current player wins if bomb position equals next player's ship position
        return self.bombPosition == self.nextPlayer.shipPosition

# this class stores all players, it uses the idea of circular linked list
class PlayerList():
    def __init__(self):
        self.firstPlayer = Player(None)
        self.lastPlayer = Player(None)
        self.firstPlayer.nextPlayer = self.lastPlayer
        self.lastPlayer.nextPlayer = self.firstPlayer

    def addPlayer(self, name):
        newPlayer = Player(name)
        if self.firstPlayer.name is None:
            self.firstPlayer = newPlayer
            self.lastPlayer = newPlayer
            newPlayer.nextPlayer = self.firstPlayer
        else:
            self.lastPlayer.nextPlayer = newPlayer
            self.lastPlayer = newPlayer
            self.lastPlayer.nextPlayer = self.firstPlayer
    
    def removePlayer(self, name):
        if self.firstPlayer.name == name:
            cur = self.firstPlayer
            while cur.nextPlayer != self.firstPlayer:
                cur = cur.nextPlayer
            cur.nextPlayer = self.firstPlayer.nextPlayer
            self.firstPlayer = self.firstPlayer.nextPlayer
        else:
            cur = self.firstPlayer
            prev = None
            while cur.nextPlayer != self.firstPlayer:
                prev = cur
                cur = cur.nextPlayer
                if cur.name == name:
                    prev.nextPlayer = cur.nextPlayer
                    cur = cur.nextPlayer

    def playGame(self):
        cur = self.firstPlayer
        count = 0
        while cur.nextPlayer != cur: # stop condition: next player is itself (only 1 player left)
            win = cur.checkWin()
            count += 1
            if win:
                print('\nNumber of guesses: {}'.format(count))
                print('The loser is: {}'.format(cur.nextPlayer.name))
                print('The winner is: {}'.format(cur.name))
                print('{} is now bombing {}'.format(cur.name, cur.nextPlayer.nextPlayer.name))
                print('--------------------------')
                self.removePlayer(cur.nextPlayer.name) # remove next player if cur wins
                cur = cur.nextPlayer
                
            else:
                cur = cur.nextPlayer
        print('\nThe final winner is: {}\n'.format(cur.name))
        
    def showPlayers(self):
        current = self.firstPlayer
        if current is None:
            print('No players!')
            return
        else:
            print(current.name)
            while current.nextPlayer != self.firstPlayer:
                current = current.nextPlayer
                print(current.name) 

def main():
    # modify the number of players here
    numOfPlayers = 10

    players = PlayerList()
    for num in range(numOfPlayers): # add each player to the circular linked list
        players.addPlayer(num)

    print('\nPlayer names: {}'.format(' -> '.join(str(x) for x in list(range(numOfPlayers)))) + ' -> 0')

    players.playGame()
    

if __name__ == "__main__":
    main()
