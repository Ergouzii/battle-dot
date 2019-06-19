import random
from threading import Thread

class Player(Thread):
    def __init__(self, name):
        Thread.__init__(self) # overriding Thread, need to call init

        self.win = False

        self.nextPlayer = None
        self.name = name # player name will be from 0 to some larger integer

        self.shipPosition = self.randCoord() # ship position for each player is fixed in one game
        self.bombPosition = None

    def randCoord(self):
        # return a random coordinate on 10x10 grid, indexes from 0 - 9
        randRow = random.randint(0, 10)
        randCol = random.randint(0, 10)
        return [randRow, randCol]

    def run(self):
        self.bombPosition = self.randCoord() # a random guess
        # current player wins if bomb position equals next player's ship position
        self.win = (self.bombPosition == self.nextPlayer.shipPosition)

    def join(self):
        Thread.join(self)
        return self.win

# this class stores all players, it uses the idea of circular linked list
class PlayerList():
    def __init__(self, numOfPlayers):
        self.numOfPlayers = numOfPlayers

        self.firstPlayer = Player(None)
        self.lastPlayer = Player(None)
        self.firstPlayer.nextPlayer = self.lastPlayer
        self.lastPlayer.nextPlayer = self.firstPlayer

    def addPlayer(self, name):
        newPlayer = Player(name)
        if self.firstPlayer.name is None or self.firstPlayer.name == 'None':
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

        # start a thread for each player
        for i in range(self.numOfPlayers):
            cur.start() # called exactly once for each Player object
            cur = cur.nextPlayer

        roundCount = 0
        while cur.nextPlayer != cur: # stop condition: next player is itself (only 1 player left)
            roundCount += 1
            cur.run()
            win = cur.join() # get the return value from thread
            if win:
                print('--------------------------')
                print('Current round: {}'.format(roundCount))
                print('The winner is: {}'.format(cur.name))
                print('The loser is: {}'.format(cur.nextPlayer.name))
                print('{} is now bombing {}'.format(cur.name, cur.nextPlayer.nextPlayer.name))
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

    players = PlayerList(numOfPlayers)
    for num in range(numOfPlayers): # add each player to the circular linked list
        players.addPlayer(num)

    print('\n--------Battle Dot--------')
    print('Player names: {}'.format(' -> '.join(str(x) for x in list(range(numOfPlayers)))) + ' -> 0\n')

    players.playGame()
    
if __name__ == "__main__":
    main()
