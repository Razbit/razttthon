# Razbit's python library
#
# Copyright Eetu 'Razbit' Pesonen, 2014
#
# This library is free software: you can redistribute
# it and/or modify it under the terms of the GNU General Public License
# version 3 as published by the Free Software Foundation.
#
# Razlib is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import sys
import os
import time

#C-style printf function, for easy and formatted printing
def printf (format, *args):
    sys.stdout.write(format % args)

#C-style fprintf function, for easy and formatted file output
def fprintf (file, format, *args):
    #Check if file is open and writable
    if file.closed == True:
        return False
    if not file.mode in ["r+", "w", "w+"]:
        return False

    #ok, file is open and writable, lets form the string and write it in
    file.write(str(format % args))
    return True

#Clears the screen
def clearScr():
    os.system(['clear','cls'][os.name == "nt"])
    
#Gets current time in milliseconds
def getTime():
    return int(round(time.time() * 1000))

#Sorts a list of lists in descending order by lst[][sortBy]
#Integer and floating-point values only, no strings!
def sort2d(lst, sortBy):
    for i in range(1,len(lst)):
        for j in range(1,len(lst)):
            if lst[j][sortBy] > lst[j-1][sortBy]: #swap items if preceding one is smaller
                temp = lst[j]
                lst[j] = lst[j-1]
                lst[j-1] = temp
    return lst
