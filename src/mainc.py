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

#This file contains the main class and save io

class cMain:
    
    playerlist=[]
    nPlayers=0 #Number of players

    def __init__(self):
        pass

from time import sleep
from razlib import printf, fprintf, clearScr, sort2d
from player import cPlayerHandler
from gameloop import cGame

class cRazttthon(cMain, cPlayerHandler, cGame):

    def parsePlayerFile(self):
        try:
            playerfile = open("players.save", "r")
        except IOError:
            print "No players.save file available, creating.."
            cMain.playerlist = [['CPU', 0, 0, 0, 0]] #No file available, create a new one.
            cMain.nPlayers = len(cMain.playerlist)
            return

        line = "a"
        while line != "": #Read through the file
            line = playerfile.readline()
            
            try:
                if line[0] == '#': # comments
                    continue
            except IndexError:
                pass

            line[:-1] #Remove leading newline
            cMain.playerlist.append(line.split())
            
        playerfile.close()

        try:
            cMain.playerlist.pop() #Remove last item, it is garbage
        except IndexError:
            pass
        
        for index in range(len(cMain.playerlist)):
            try:
                cMain.playerlist[index][1] = int(cMain.playerlist[index][1])
                cMain.playerlist[index][2] = int(cMain.playerlist[index][2])
                cMain.playerlist[index][3] = int(cMain.playerlist[index][3])
                cMain.playerlist[index][4] = int(cMain.playerlist[index][4])
            except ValueError:
                cMain.playerlist.pop(index) #Remove corrupted line

        if len(cMain.playerlist) == 0: #If file was corrupted we have to create a new one
            cMain.playerlist = [['CPU', 0, 0, 0, 0]]

        cMain.nPlayers = len(cMain.playerlist)

    def savePlayerFile(self):
        try:
            playerfile = open("players.save", "w")
        except IOError:
            print "Saving unsuccessful."
            return

        fprintf(playerfile, "# name games wins losses quits\n")
        for player in cMain.playerlist:
            fprintf(playerfile, "%s %i %i %i %i\n", player[0], player[1], player[2], player[3], player[4])
        playerfile.close()

    def newGame(self):
        
        pid1, pid2 = 0,0

        while 1:
            mode = raw_input("Enter 1 for singleplayer, 2 for multiplayer: ")
            try:
                mode = int(mode)
            except ValueError:
                print "Please, enter 1 or 2"
                continue

            if mode == 1:
                pid1 = 0
                
                while 1:
                    pName = raw_input("Enter your name: ")
                    if pName != '' and pName.lower() != 'cpu':
                        break
                    else:
                        print "Try again"

                pid2 = cPlayerHandler.getPID(self, pName)
                if pid2 == -1:
                    print "No such player found. Creating.."
                    pid2 = cPlayerHandler.addPlayer(self, pName)
                break
        
            elif mode == 2:
                while 1:
                    p1name = raw_input("Player 1, enter your name: ")
                    if p1name != '' and p1name.lower() != 'cpu':
                        break
                    else:
                        print "Try again"

                pid1 = cPlayerHandler.getPID(self, p1name)
                if pid1 == -1:
                    print "No such player found. Creating.."
                    pid1 = cPlayerHandler.addPlayer(self, p1name)

                while 1:
                    p2name = raw_input("Player 2, enter your name: ")
                    if p2name != '' and p2name.lower() != 'cpu':
                        break
                    else:
                        print "Try again"

                pid2 = cPlayerHandler.getPID(self, p2name)
                if pid2 == -1:
                    print "No such player found. Creating.."
                    pid2 = cPlayerHandler.addPlayer(self, p2name)

                break

            print "Please, enter 1 or 2" #If mode wasn't 1 or 2, loop again.
        
        sleep(0.5) #Why sleep? Because why not?

        status = cGame.__init__(self, pid1, pid2) #Start new game
                
        if status == -1 or status == 2:
            print "Game ended to a draw"
        elif status == 0 or status == 1:
            printf("%s won the game\n", cGame.getNames(self)[status])
    
    def stats(self, name):
        #Get player ID, return if not found
        pid = cPlayerHandler.getPID(self, name)
        if pid == -1:
            print "No such player found."
            return

        pData = cPlayerHandler.getData(self, pid)
        printf("The player %15.15s has played %i games, of which they have won %i and lost %i. They have quit %i times.\n", pData[0], pData[1], pData[2], pData[3], pData[4])
        
    def leaderboard(self, strMode):
        mode = -1

        if strMode[0] == 'g':
            mode = 1 #games
            strMode = "played"

        elif strMode[0] == 'w':
            mode = 2 #wins
            strMode = "won"

        elif strMode[0] == 'l':
            mode = 3 #losses
            strMode = "lost"

        else:
            print "An error occured."
            return
        
        data = []
        
        #Retrieve player data
        for pid in range(cPlayerHandler.getPlayers(self)):
            data.append(cPlayerHandler.getData(self, pid))
        
        sort2d(data, mode)

        printf("Leaderboard in order of games %s.\n", strMode)
        
        for player in range(len(data)):
            printf("%i. %-15.15s %i games played, %i games won, %i games lost, %i quits.\n", player +1, str(data[player][0])+":", data[player][1], data[player][2], data[player][3], data[player][4])
        
