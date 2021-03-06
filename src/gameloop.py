# Razttthon, a python-implemented Tic-tac-toe game.

# Copyright Eetu 'Razbit' Pesonen, 2014
#
# This file is a part of Razttthon, which is free software: you can redistribute
# it and/or modify it under the terms of the GNU General Public License
# version 3 as published by the Free Software Foundation.
#
# Razttthonis distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

#This file contains the game functionality and the game loop

from mainc import cMain
from player import cPlayerHandler
from razlib import printf, clearScr
from random import sample

class cGame(cMain, cPlayerHandler):

    def __init__(self, pid1, pid2):
        if pid1 > pid2: #Flip so that player 0 has smaller pid (cpu is always player 0 in that case)
            tempPid = pid2
            pid2 = pid1
            pid1 = tempPid

        self.players = [[pid1, cMain.playerlist[pid1][0], 'x'], [pid2, cMain.playerlist[pid2][0], 'o']] #name and mark for both

        #init vars
        self.cont = True
        self.turns = 0
        self.status = 0
        self.gameGrid = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']] #contains the game grid and marks

        #Being game
        self.loop()
        return self.status

    def getNames(self):
        return [self.players[0][1], self.players[1][1]]

    def loop(self): #Main game loop, loops until stop() is called.
        
        self.printGame()

        while self.cont == True:
            self.turns += 1

            if self.turns % 2 == 0:
                self.turn(0)
                self.printGame()
                self.over(0)
            else:
                self.turn(1)
                self.printGame()
                self.over(1)         
            
    def printGame(self):
        clearScr()
        printf("   # A | B | C \n")
        printf("###############\n")
        printf(" 1 # %s | %s | %s \n", self.gameGrid[0][0], self.gameGrid[0][1], self.gameGrid[0][2])
        printf("---#-----------\n")
        printf(" 2 # %s | %s | %s \n", self.gameGrid[1][0], self.gameGrid[1][1], self.gameGrid[1][2])
        printf("---#-----------\n")
        printf(" 3 # %s | %s | %s \n\n", self.gameGrid[2][0], self.gameGrid[2][1], self.gameGrid[2][2])

    def turn(self, player):
        pid = self.players[player][0]
        if pid == 0: #CPU
            print "CPU's turn"

            if self.twoInaRow(0) == True:
                return
            elif self.twoInaRow(1) == True:
                return
            else: #We cannot win nor block, time for random placement
                #Generate random arrays of rows and 
                rows = sample(range(3),3)
                cols = sample(range(3),3)
                row = 0
                col = 0
                
                valid = False
                
                for i in range(3):
                    for j in range(3):
                        row = rows[i]
                        col = cols[j]
                        if self.gameGrid[row][col] == ' ':
                            valid = True
                            break
                    if valid == True:
                        break

                self.gameGrid[row][col] = self.players[player][2]
        
        else: #non-cpu            
            valid = False
            while valid == False:
                #Get input from player
                printf("%s, your turn (eg. A2, s to stop): ", self.players[player][1])
                temp = raw_input()
                temp = temp.upper()
                
                try:
                    if temp[0] == 'S':
                        self.stop(-1) #Stopcode for user quit
                        return
                except IndexError:
                    pass

                try:
                    pos = [temp[0], temp[1]]
                except IndexError:
                    valid = False
                    print "Invalid input!"
                    continue
            
                #Check for validity
                if not pos[0] in ['A', 'B', 'C'] or not pos[1] in ['1','2','3']:
                    print "Invalid input!"
                    valid = False
                    continue

                #Convert
                else:
                    if pos[0] == 'A':
                        pos[0] = 0
                    elif pos[0] == 'B':
                        pos[0] = 1
                    else:
                        pos[0] = 2

                    pos[1] = int(pos[1]) - 1 #list indices start from 0
                    valid = True

                #Check if cell is free
                if self.gameGrid[pos[1]][pos[0]] == ' ' and valid == True:
                    valid = True
                else:
                    print "Position already taken!"
                    valid = False

            self.gameGrid[pos[1]][pos[0]] = self.players[player][2]

    def twoInaRow(self, mode): #Mode = 0: check if cpu can win mode = 1: check if opponent can win, try to block if so.
        if mode == 0: #game pid = 0, in this case the cpu
            mark = self.players[0][2] #Cpu's mark
            opMark = self.players[1][2] #Opponent's mark
        else:
            mark = self.players[1][2] #Opponent's mark
            opMark = self.players[0][2] #Cpu's mark
            

        #generate array of possible "winning rows"
        indexList = []
        indexList.append([[0,0],[0,1],[0,2]]) #row 1
        indexList.append([[1,0],[1,1],[1,2]]) #row 2
        indexList.append([[2,0],[2,1],[2,2]]) #row 3
        indexList.append([[0,0],[1,0],[2,0]]) #col 1
        indexList.append([[0,1],[1,1],[2,1]]) #col 2
        indexList.append([[0,2],[1,2],[2,2]]) #col 3
        indexList.append([[0,0],[1,1],[2,2]]) #\
        indexList.append([[0,2],[1,1],[2,0]]) #/

        occurences = []

        for index in indexList:
            temp = []

            for i in range(3):
                temp.append(self.gameGrid[index[i][0]][index[i][1]])

            if temp.count(opMark) == 0: #No opposite marks found, this row can be a winning one
                occurences.append(temp.count(mark)) #Count occurences of mark
            else:
                occurences.append(0) #Opposite mark found, this cant win

        for index, row in enumerate(occurences):
            if row == 2: #Can win by placing one tic
                break
            elif index == 7 and row < 2: #We have searched all, no matches
                return False

        for i in range(3): #Find the empty cell
            row = indexList[index][i][0]
            col = indexList[index][i][1]

            if self.gameGrid[row][col] == ' ': #And place the appropriate tic
                if mode == 0:
                    self.gameGrid[row][col] = mark #Place CPU's tic, CPU won.
                else:
                    self.gameGrid[row][col] = opMark #Place CPU's tic, opponent's winning blocked.
        return True
    
    def over(self, player):
        #Generate arrays of possible winning rows
        rows = []
        rows.append(self.gameGrid[0]) #row 1
        rows.append(self.gameGrid[1]) #row 2
        rows.append(self.gameGrid[2]) #row 3
        rows.append([self.gameGrid[0][0],self.gameGrid[1][0], self.gameGrid[2][0]]) #col 1
        rows.append([self.gameGrid[0][1],self.gameGrid[1][1], self.gameGrid[2][1]]) #col 2
        rows.append([self.gameGrid[0][2], self.gameGrid[1][2], self.gameGrid[2][2]]) #col 3
        rows.append([self.gameGrid[0][0], self.gameGrid[1][1], self.gameGrid[2][2]]) #\
        rows.append([self.gameGrid[0][2], self.gameGrid[1][1], self.gameGrid[2][0]]) #/
        
        for i in range(len(rows)):
            count = rows[i].count(self.players[player][2])
            if count == 3:
                self.stop(player)
                return

        count = 0

        for i in range(3): #count empty cells
            for j in range(3):
                if self.gameGrid[i][j] == ' ':
                    count += 1
        if count == 0: #quit if board is full
            self.stop(2)
            return

    def stop(self, status):
        self.cont = False
    
        #+1 game for both
        cPlayerHandler.addGame(self, self.players[0][0])
        cPlayerHandler.addGame(self, self.players[1][0])

        #Exit status
        if status == -1: #Normal quit
             #+1 quit for both
            cPlayerHandler.addQuit(self, self.players[0][0])
            cPlayerHandler.addQuit(self, self.players[1][0])
        elif status == 0: #P0 won
            cPlayerHandler.addWin(self, self.players[0][0])
            cPlayerHandler.addLose(self, self.players[1][0])
        
        elif status == 1: #P1 won
            cPlayerHandler.addWin(self, self.players[1][0])
            cPlayerHandler.addLose(self, self.players[0][0])
        
        elif status == 2: #Draw
            cPlayerHandler.addLose(self, self.players[0][0])
            cPlayerHandler.addLose(self, self.players[1][0])

        self.status = status
        
        #clear and print, nicer that way
        clearScr()
        self.printGame()
