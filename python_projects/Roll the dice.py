import random as rnd

def generator():
    num1 = rnd.randint(1,6)
    num2 = rnd.randint(1,6)
    print(f'({num1},{num2})')


is_running = True
while is_running:
    choice = input('Roll the dice? (y/n)')
    if choice == 'n' or choice == 'N':
        is_running = False
        print('Thanks for playing!')

    elif choice == 'y' or choice == 'Y':
        generator()

    else:
        print('Invalid choice')