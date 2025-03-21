import random as rnd

print('guess a number between 0 - 100')
number = rnd.randint(0,100)
loss = False
difficulty = int(input("in easy difficulty you have 10 tries \nin hard difficulty you have 5 tries \nfor easy type '0' \nfor hard type '1'\n"))
if difficulty == 0:
    tries = 10
elif difficulty == 1:
    tries = 5
while not loss:
    print(f"you have {tries} tries")
    guess = int(input())
    if guess == number:
        print('You win')
        break
    elif number - guess > 20 :
        print("it's too higher than your guess")
    elif number - guess >= 1 and number - guess <= 20:
        print("it's higher then your guess")
    elif number - guess < 0 and number - guess >= -20:
        print("it's lower then your guess")
    elif number - guess < -20:
        print("it's too lower than your guess")
    tries -= 1
    if tries == 0:
        print("You lose")
        loss = True
    