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

#This file contains the main loop

from mainc import cMain
from player import cPlayerHandler
from gameloop import cGame

def parsePlayerFile():
    try:
        playerfile = open("players.save", "r+")
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
    
    try:
        cMain.playerlist.pop() #Remove last item, it is garbage
    except IndexError:
        pass
    
    for index in range(len(cMain.playerlist)):
        cMain.playerlist[index][1] = int(cMain.playerlist[index][1])
        cMain.playerlist[index][2] = int(cMain.playerlist[index][2])
        cMain.playerlist[index][3] = int(cMain.playerlist[index][3])
        cMain.playerlist[index][4] = int(cMain.playerlist[index][4])
        

parsePlayerFile()
phandler = cPlayerHandler()

#Testing...
game = cGame(1,2)

print phandler.getData(1)
print phandler.getData(2)
print "Bye!"
