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

#This file contains the player class

from mainc import cMain
    
class cPlayerHandler(cMain):
    def __init__(self):
        pass

    def getName(self, id): return cMain.playerlist[id][0]
    def getGames(self, id): return cMain.playerlist[id][1]
    def getWins(self, id): return cMain.playerlist[id][2]
    def getLosses(self, id): return cMain.playerlist[id][3]
    def getQuits(self, id): return cMain.playerlist[id][4]
    def getData(self, id):
        return [self.getName(id), self.getGames(id), self.getWins(id), self.getLosses(id), self.getQuits(id)]

    def addPlayer(self, name):
        #Adds a new player with name 'name' to the cMain's list
        if self.getPID(name) == -1: #If player doesn't exist yet
            cMain.playerlist.append([name, 0]) #Add player
            return True
        else:
            return False

    def modPlayer(self, id):
        try:
            cMain.playerlist[id][1] += 1 #Plus 1 played games
            return True
        except IndexError:
            return False

    def addGame(self, id):
        try:
            cMain.playerlist[id][1] += 1
            return True
        except IndexError:
            return False

    def addWin(self, id):
        try:
            cMain.playerlist[id][2] += 1
            return True
        except IndexError:
            return False

    def addLose(self, id):
        try:
            cMain.playerlist[id][3] += 1
            return True
        except IndexError:
            return False

    def addQuit(self, id):
        try:
            cMain.playerlist[id][4] += 1
            return True
        except IndexError:
            return False

    def getPID(self, name):
        #Search the playerlist, return index where player 'name' was found
        for index in range(len(cMain.playerlist)):
            if cMain.playerlist[index][0].upper() == name.upper():
                return index
        
        return -1 #If item isn't found, return -1
        
        
