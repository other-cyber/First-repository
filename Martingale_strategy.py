import random

COIN_VALUES = ["орел", "решка"]
MIN_BET = 50


def choice_of_side() -> str:
    while True:
        chance = input("На что ставим? (Орел или решка) ").lower()
        if chance == "орел" or chance == "решка":
            return chance
        else:
            print("Нужно выбрать либо орел либо решка") 


def flip_coin() -> int:
    return random.choice(COIN_VALUES)


def play(bet: int, choice: str) -> int:
    while True:
        if choice != flip_coin():
            print("Ты проиграл")
            bet *= 2
        else:
            print("Ты выйграл")
            return bet * 2


print("Минимальная ставка 50 рублей")
while True:
    bet = int(input("Введите свою ставку: "))
    if bet >= MIN_BET:
        break
    else:
        print("Минимальная ставка 50 рублей")
choice = choice_of_side() 
print(play(bet, choice))

