resources_requirement = {'latte':{'water':100, 'coffee':10, 'milk':20, 'money':3},
                         'coffee':{'water':50, 'coffee':40, 'milk':0, 'money':4},
                         'copocceno':{'water':150, 'coffee':10, 'milk':10, 'money':2}}

resources = {'water':300, 'coffee':50, 'milk':50, 'money':0}
ON = True

while ON:
    request = input('Please chose your drink: \nfor latte press latte 3$\nfor copocceno press copocceno 2$\nfor coffee press coffee 4$\n')
    money = int(input('Please enter the requested amount of money:'))
    resources['money'] = money
    print('checking resources')

    if resources_requirement[request]['water'] > resources['water']:
        print('please full the water and retry again ')
        resources['water'] += int(input('how much water (ml): '))
        continue

    if resources_requirement[request]['coffee'] > resources['coffee']:
        print('please full the coffee and retry again ')
        resources['coffee'] += int(input('how much coffee (g): '))
        continue

    if resources_requirement[request]['milk'] > resources['milk']:
        print('please full the milk and retry again ')
        resources['milk'] += int(input('how much milk (g): '))
        continue

    if resources_requirement[request]['money'] > resources['money']:
        print('please put money and retry again ')
        resources['money'] += int(input('how much money ($): '))
        continue

    resources['coffee'] -= resources_requirement[request]['coffee']
    resources['milk'] -= resources_requirement[request]['milk']
    resources['water'] -= resources_requirement[request]['water']

    print('Done! \nThanks for using me')