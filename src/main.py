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
    arg = [] #an array of arguments from user.
    temp = ""
    
    while 1: #Continue asking user for an argument if not recognized
        del arg[:] #Empty the argument array

        temp = raw_input("> ")
        temp = temp.lower()

        temp[:-1] #Last char is garbage

        try:
            arg.append(temp.split()[0])
        except IndexError:
            print "Type 'help' if you need help."
            continue
        
        try:
            arg.append(temp.split()[1])
        except IndexError:
            pass #Second argument is not always mandatory

        if arg[0] in ['play', 'p', 'quit', 'q', 'help', 'h', 'stats', 's']:
            break

        elif arg[0] in ['leader', 'l']:
            try:
                if arg[1] in ['wins', 'w', 'losses', 'l', 'games', 'g']:
                    break
            except IndexError:
                pass

        print "Type 'help' if you need help."

    if arg[0] in ['play', 'p']:
        game.newGame()

    elif arg[0] in ['leader', 'l']:
        game.leaderboard(arg[1])

    elif arg[0] in ['stats', 's']:
        if len(arg) > 1:
            game.stats(arg[1])
        else:
            print "Type 'help' if you need help."

    elif arg[0] in ['quit', 'q']:
        if raw_input("Are you sure (y/N)? ").lower() in ['y', 'yes']:
            break

    elif arg[0] in ['help', 'h']:
        print "help, h: get help"
        print "quit, q: quit"
        print "play, p: start a new game"
        print "stats, s <player>: show stats for <player>"
        print "leader, l [wins, w, losses, l, games, g]: show leaderboard"

game.savePlayerFile()
print " Bye!"
