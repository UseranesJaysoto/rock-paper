#!/bin/python3

from random import randint

player = input("rock(r), paper(p), scissors(s)?")
print (player, 'vs',  end='')

chosen = randint(1,3)
#print(chosen)

if chosen ==1:
    computer = "r"
elif chosen ==2:
    computer = "p"
else :
    computer = "s"
print(computer)


if player == computer:
    print('Draw!')
elif  player =='r' and computer =='p':
    print('computer won!')
elif  player =='r' and computer =='s':
    print('player won!')
elif  player =='p' and computer =='r':
    print('player won!')
elif  player =='s' and computer =='r':
    print('computer won!')




#Jaysoto