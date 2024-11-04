# Given a string (with only uppercase letters and numbers), return the total distance traveled by the robot. 
# The robot can move only left, right, top, and bottom. It can't move diagonally.
# 1 2 3 4 5 6 7 8 9 0
# Q W E R T Y U I O P
# A S D F G * H J K L 
#   Z X C V B N M


# example 0 :
#     Input : "HELLO123"
#     Output : 24


import math
import os
import random
import re
import sys

def getDistance(word):
    # Write your code here
    # qwert_pos = {'1': (-5, 2), '2': (-4, 2), '3': (-3, 2), '4': (-2, 2), '5': (-1, 2), '6': (0, 2), '7': (1, 2), '8': (2, 2), '9': (3, 2), '0': (4, 2),
    #     'Q': (-5, 1), 'W': (-4, 1), 'E': (-3, 1), 'R': (-2, 1), 'T': (-1, 1), 'Y': (0, 1), 'U': (1, 1), 'I': (2, 1), 'O': (3, 1), 'P': (4, 1),
    #     'A': (-5, 0), 'S': (-4, 0), 'D': (-3, 0), 'F': (-2, 0), 'G': (-1, 0), '*': (0, 0), 'H': (1, 0), 'J': (2, 0), 'K': (3, 0), 'L': (4, 0),
    #     'Z': (-4, -1), 'X': (-3, -1), 'C': (-2, -1), 'V': (-1, -1), 'B': (0, -1), 'N': (1, -1), 'M': (2, -1)
    # }
    
    qwert_pos = { 
                 '1':(-5,2),'2':(-4,2),'3':(-3,2),'4':(-2,2),'5':(-1,2),'6':(0,2),'7':(1,2),'8':(2,2),'9':(3,2),'0':(4,2),
                 'Q':(-5,1),'W':(-4,1),'E':(-3,1),'R':(-2,1),'T':(-1,1),'Y':(0,1),'U':(1,1),'I':(2,1),'O':(3,1),'P':(4,1),
                 'A':(-5,0),'S':(-4,0),'D':(-3,0),'F':(-2,0),'G':(-1,0),'*':(0,0),'H':(1,0),'J':(2,0),'K':(3,0),'L':(4,0),
                            'Z':(-4,-1),'X':(-3,-1),'C':(-2,-1),'V':(-1,-1),'B':(0,-1),'N':(1,-1),'M':(2,-1)
                }
    # qwert_pos = {
    #     '1': (5, 3), '2': (1, 3), '3': (2, 3), '4': (3, 3), '5': (4, 3),
    #     '6': (5, 3), '7': (6, 3), '8': (7, 3), '9': (8, 3), '0': (9, 3),
    #     'Q': (0, 2), 'W': (1, 2), 'E': (2, 2), 'R': (3, 2), 'T': (4, 2),
    #     'Y': (5, 2), 'U': (6, 2), 'I': (7, 2), 'O': (8, 2), 'P': (9, 2),
    #     'A': (0, 1), 'S': (1, 1), 'D': (2, 1), 'F': (3, 1), 'G': (4, 1),
    #     '*': (5, 1), 'H': (6, 1), 'J': (7, 1), 'K': (8, 1), 'L': (9, 1),
    #     'Z': (1, 0), 'X': (2, 0), 'C': (3, 0), 'V': (4, 0), 'B': (5, 0),
    #     'N': (6, 0), 'M': (7, 0)
    # }
    
    # for let in qwert_pos:
    #     if qwert_pos[let] == k[let]:
    #         print(let)
    
    prev_word = qwert_pos['*']
    tot_dis = 0
    for i in word:        
        curr_pos = qwert_pos[i]
        dis = abs(curr_pos[0] - prev_word[0]) + abs(curr_pos[1] - prev_word[1])
        # if ((curr_pos[1] == 0 or prev_word[1] == 0) and ((curr_pos[0]<0 and prev_word[0]>0) or (curr_pos[0]>0 and prev_word[0]<0))):
        #     dis -= 1
        tot_dis += dis
        prev_word = curr_pos
    return tot_dis    
    # return 0

word = input()

result = getDistance(word)

print(result)
