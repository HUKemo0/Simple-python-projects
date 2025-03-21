import random

customers ={}
existing_id = []

def id_generator():
    id = random.randint(10**11, 10**12 - 1)
    if id not in existing_id:
        existing_id.append(id)
        return id
    else :
        id_generator()

def new_customer():
    name = input('Please enter your name: ')
    address = input('Please enter your home address: ')
    phone = input("Please enter your phone number: ")
    balance = input('enter your amount of money: ')
    id = id_generator()
    print(f'Your id is: {id}')
    customers[id] = {'name':name,
                    'address':address,
                    'phone':phone,
                    'balance':balance}
    

is_running = True

while is_running:
    print('Banking program is running')
    print('1. New customer')
    print('2. Show balance')
    print('3. Search by id')
    print('4. Exit')

    choice = int(input('Enter your choice (1-4): '))

    if choice == 4:
        is_running = False

    elif choice == 1:
        new_customer()

    elif choice == 2:
        search = int(input('Please enter the customer id: '))
        print(customers[search]['balance'])

    elif choice == 3:
        search = int(input('Please enter the customer id: '))
        print(f'name: {customers[search]['name']}')
        print(f'address: {customers[search]['address']}')
        print(f'phone: {customers[search]['phone']}')