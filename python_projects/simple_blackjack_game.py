import random as rnd
def summ(player_cards):
    sum = 0
    for n in player_cards:
        sum += n
    return sum

def computer_sum(computer_cards):
    sum = 0
    for n in computer_cards:
        sum += n
    return sum

main_cads = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards = [rnd.choice(main_cads),rnd.choice(main_cads)]
computer_cards = [rnd.choice(main_cads),rnd.choice(main_cads)]
print(f"your cards are {player_cards}")
print(f"computer cards are [{computer_cards[0]},*]")
draw = input("draw another card? if yes type 'y' if no type 'n' :")
sum = summ(player_cards)
computer_sum = computer_sum(computer_cards)
if draw == 'n':
    if sum > computer_sum:
        print(f"computer cards are {computer_cards}")
        print('You win')
        
    elif sum == computer_sum:
        print(f"computer cards are {computer_cards}")
        print('Draw')
        
    else :
        print(f"computer cards are {computer_cards}")
        print('You lose')

while draw == 'y':
    player_cards.append(rnd.choice(main_cads))
    sum = summ(player_cards)
    print(f"your cards are {player_cards}")
    if sum > 21:
        print(f"computer cards are {computer_cards}")
        print("You lose")
        break
    draw = input("draw another card? if yes type 'y' if no type 'n' :")
    if draw == 'n':
        if sum > computer_sum:
            print(f"computer cards are {computer_cards}")
            print('You win')
            break
        elif sum == computer_sum:
            print(f"computer cards are {computer_cards}")
            print('Draw')
            break
        else :
            print(f"computer cards are {computer_cards}")
            print('You lose')
            break

