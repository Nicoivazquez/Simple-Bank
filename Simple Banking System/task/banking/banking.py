import random

run = True
storage = []
loged_in = False
created_acct = True
right = False
balance = 0
iin = str(400000)


class CreditCard:
    def __init__(self, num, pin):
        self.num = iin + str(random.choice(range(100000000, 999999999)))
        self.pin = random.choice(range(1000, 9999))


print('1. Create an account \n'
      '2. Log into account\n'
      '0. Exit\n')

action1 = int(input())

if action1 == 0:
    print('Bye!')
    exit()

elif action1 == 1:
    iin = str(400000)
    credit_card = iin + str(random.choice(range(1000000000, 9999999999)))
    pin = random.randrange(1000, 9999)
    storage.append(int(credit_card))
    storage.append(str(pin))
    print('Your card has been created:\n'
          'your card number:')
    print(credit_card)
    print('Your card PIN:')
    print(str(pin))
    created_acct = True

while created_acct and (right is False):
    print('\n1. Create an account \n'
          '2. Log into account\n'
          '0. Exit\n')

    action3 = int(input())
    if action3 == 0:
        print('Bye!')
        exit()
    elif action3 == 1:
        iin = str(400000)
        credit_card = iin + str(random.choice(range(1000000000, 9999999999)))
        pin = random.randrange(1000, 9999)
        storage[0] = (int(credit_card))
        storage[1] = (str(pin))
        print('Your card has been created:\n'
              'your card number:')
        print(credit_card)
        print('Your card PIN:')
        print(str(pin))
        created_acct = True
    elif action3 == 2:
        print('Enter your card number\n')
        user_card_num = int(input())
        print('Enter your PIN:')
        user_pin = str(input())
        if (user_card_num == storage[0]) and (user_pin == storage[1]):
            print('You have successfully logged in!')
            loged_in = True
            right = True
        else:
            print('Wrong card number or PIN!')

while loged_in == True:
    print('1. Balance\n'
          '2. Log out\n'
          '0. Exit\n')
    action2 = int(input())
    if action2 == 0:
        print('Bye!')
        exit()
    elif action2 == 1:
        print('Balance:', balance)
    elif action2 == 2:
        print('You have successfully logged out!')
        loged_in = False
        run = False
