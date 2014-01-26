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

import mainc

class cPlayer(mainc.cMain):
    def __init__(self, id):
        self.id = id
        self.name = mainc.cMain.playerlist[id][0]
        self.gamesPlayed = mainc.cMain.playerlist[id][1]

    def getID(self): return self.id
    def getName(self): return self.name
    def getGames(self): return self.gamesPlayed
    def getData(self):
        return [self.name, self.gamesPlayed]
    
class cPlayerHandler(mainc.cMain):
    def __init__(self):
        pass

    def addPlayer(self, name):
        #Adds a new player with name 'name' to the cMain's list
        if self.getPID(name) == -1: #If player doesn't exist yet
            mainc.cMain.playerlist.append([name, 0]) #Add player
            return True
        else:
            return False

    def modPlayer(self, id):
        try:
            mainc.cMain.playerlist[id][1] += 1 #Plus 1 played games
            return True
        except IndexError:
            return False

    def getPID(self, name):
        #Search the playerlist, return index where player 'name' was found
        for index in range(len(mainc.cMain.playerlist)):
            if mainc.cMain.playerlist[index][0].upper() == name.upper():
                return index
        
        return -1 #If item isn't found, return -1
        
        
