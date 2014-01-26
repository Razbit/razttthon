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

from mainc import cRazttthon

game = cRazttthon()

print "Welcome to Razttthon, a Tic Tac Toe -game!"

game.parsePlayerFile()

while 1:
    arg = ""
    
    while 1:
        arg = raw_input(" >: ")
        if arg in ['play', 'p', 'quit', 'q', 'help', 'h']:
            break
        print "Type 'help' if you need help."

    if arg in ['play', 'p']:
        game.newGame()

    elif arg in ['quit', 'q']:
        if raw_input("Are you sure (Y/n)? ").upper() in ['N', 'NO']:
            continue
        break

    elif arg in ['help', 'h']:
        print "  help, h: get help"
        print "  quit, q: quit"
        print "  play, p: start a new game"

#game.savePlayerFile()
print "Bye!"
