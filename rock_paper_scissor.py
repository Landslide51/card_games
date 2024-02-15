import random
from time import sleep

txt = {"к": "н", "н": "б", "б": "к"}

player1 = input("камень, ножницы, бумага?\n").lower()[0]
player2 = input("камень, ножницы, бумага?\n").lower()[0]

# print(player1, player2)

if player1 == player2:
    print("Ничья!!!")
elif txt[player1] == player2:
    print("Игрок 1 победил")
else:
    print("Игрок 2 победил")