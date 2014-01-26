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

    def __init__(self):
        pass

from razlib import fprintf
from player import cPlayerHandler
from gameloop import cGame

class cRazttthon(cMain, cPlayerHandler, cGame):

    def parsePlayerFile(self):
        try:
            playerfile = open("players.save", "r")
        except IOError:
            print "No players.save file available."
            cMain.playerlist = []
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
            cMain.playerlist[index][1] = int(cMain.playerlist[index][1])
            cMain.playerlist[index][2] = int(cMain.playerlist[index][2])
            cMain.playerlist[index][3] = int(cMain.playerlist[index][3])
            cMain.playerlist[index][4] = int(cMain.playerlist[index][4])

    def savePlayerFile(self):
        try:
            playerfile = open("players.save", "w")
        except IOError:
            print "Saving unsuccesful."
            return

        fprintf(playerfile, "# name games wins losses quits\n")
        for player in cMain.playerlist:
            fprintf(playerfile, "%s %i %i %i %i\n", player[0], player[1], player[2], player[3], player[4])
        playerfile.close()

    def newGame(self):
        p1name = raw_input("Player 1, enter your name: ")
        pid1 = cPlayerHandler.getPID(self, p1name)
        if pid1 == -1:
            print "No such player found. Creating.."
            pid1 = cPlayerHandler.addPlayer(self, p1name)

        p2name = raw_input("Player 2, enter your name: ")
        pid2 = cPlayerHandler.getPID(self, p2name)
        if pid2 == -1:
            print "No such player found. Creating.."
            pid2 = cPlayerHandler.addPlayer(self, p2name)

        cGame.__init__(self, pid1, pid2) #Start new game
