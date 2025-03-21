tasks ={}
keys = []

def generate_key():
    for n in range(1,200):
        if n not in keys:
            keys.append(n)
            key = n
            break
    return key


def new_task():
    title = input('Enter the title of the task: ')
    tasks[generate_key()] = title


def remove_task():
    number = int(input('Please enter the number of the task that you want to delete: '))
    tasks.pop(number)
    key = keys.index(number)
    keys.pop(key)

def done_task():
    key = int(input('Please enter the number of task: '))
    tasks[key] += ' -> Done!'
    

is_running = True
while is_running:
    print('Your tasks :')
    for key, value in tasks.items():
        print(f'{key}. {value}')

    print('What do you want to do? ')
    print('1. Add a new task ')
    print('2. remove a task ')
    print('3. chick if done ')
    print('4. Exit')
    choice = int(input('Please enter your choice (1-4): '))
    
    if choice == 4:
        is_running = False
        print('Thanks for using me (^_^)')

    elif choice == 1:
        new_task()

    elif choice == 2:
        remove_task()

    elif choice == 3:
        done_task()