import random
from time import sleep

print("Поиграем в очко?))")

number_of_players = input("Сколько человек будет играть?\n")
number_of_players = int(number_of_players)
if number_of_players > 6:
    print("Вы ввели количество игроков превышающее возможное(max6)")
    exit()
else:
    print("Играть будет {} человека".format(number_of_players))

deck = [6,7,8,9,10,2,3,4,11] * 4
random.shuffle(deck)
players = {}

for i in range(number_of_players):
    name = input("Введите имена игроков:\n")
    players[name] = 0
    sleep(1)

for player in players:
    card1 = deck.pop()
    card2 = deck.pop()
    sum_card = card1 + card2
    print("{} попалась карта достоинством {} и {} их сумма: {}".format(player, card1, card2, sum_card))
    players[player] += sum_card
    sleep(1)
    if sum_card == 22:
        print("Игрок {} победил".format(player))
        exit()

for player in players:
    while True:
        choice = input("{} Будете брать карту?(Ваш текущий счет {}) y/n\n".format(player, players[player]))
        if choice == "y":
            card1 = deck.pop()
            print("Вам попалась карта достоинством {}".format(card1))
            players[player] += card1
            if players[player] > 21:
                print("Извините, но вы проиграли)")
                break
            elif players[player] == 21:
                print("Поздравляю, вы набрали 21")
                break
            else:
                print("У вас {} очков".format(players[player]))
        elif choice == "n":
            print("У вас {} очков и вы закончили, ждите результат".format(players[player]))
            break
sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
max_score = 0
winners = []
for name, score in sorted_players:
    if score < 22 and score >= max_score:
        max_score = score
        winners.append(name)

print("Победитель игры: {}".format(" ".join(winners)) if winners else "Победило казино(как и всегда)")