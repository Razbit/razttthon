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

class Player(mainc.Main):
    def __init__(self, id):
        self.id = id
        self.name = mainc.Main.playerlist[id][0]
        self.gamesPlayed = mainc.Main.playerlist[id][1]

    def getName(self): return self.name
    def getGames(self): return self.gamesPlayed
    
