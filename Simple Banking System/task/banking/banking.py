import random

run = True
logged_in = False
created_acct = False
right = False
iin = str(400000)
balance = 0
card_counter = 0

def luhn_algorithem(card_minus_checksum):
    luhn_formula = []
    check_sum = 0
    potential_num = 0
    for idx, num in enumerate(card_minus_checksum):
        if (idx+1) % 2 != 0:
            luhn_formula.append(int(num) * 2)
        else:
            luhn_formula.append(int(num))
    for num in luhn_formula:
        if num >= 10:
            luhn_formula.remove(num)
            luhn_formula.append(num - 9)
        else:
            continue
    while (sum(luhn_formula) + potential_num) % 10 != 0:
        potential_num += 1
    return str(card_minus_checksum) + str(potential_num)

class CreditCard:


    iin = str(400000)
    def __init__(self):
        self.bank_num = str(random.choice(range(100000000, 999999999)))
        self.pin = random.choice(range(1000, 9999))
        self.card_minus_checksum = self.iin + self.bank_num
        self.credit_card = str(luhn_algorithem(self.card_minus_checksum))
        self.storage = []
        self.storage.append(int(self.credit_card))
        self.storage.append(str(self.pin))

    def check_sum(self):
        card_minus_checksum = self.credit_card[:-1]
        if str(self.credit_card) in luhn_algorithem(card_minus_checksum):
            return True
        else:
            return False
    def balance(self):
        balance = 0
        print(balance)

cards = list()
for i in range(1000):
    cards.append(CreditCard())

while run:
    while not logged_in and not created_acct:
        print('1. Create an account \n'
              '2. Log into account\n'
              '0. Exit')

        action1 = int(input())
        if action1 == 0:
            print('Bye!')
            exit()

        elif action1 == 1:
            card_counter += 1
            print('Your card has been created:\n'
                  'your card number:')
            print(cards[card_counter].credit_card)
            print('Your card PIN:')
            print(str(cards[card_counter].pin))
            created_acct = True

    while created_acct and (not right):
        print('\n1. Create an account \n'
              '2. Log into account\n'
              '0. Exit')
        action3 = int(input())
        if action3 == 0:
            print('Bye!')
            exit()
        elif action3 == 1:
            card_counter += 1
            print('Your card has been created:\n'
                  'your card number:')
            print(cards[card_counter].credit_card)
            print('Your card PIN:')
            print(str(cards[card_counter].pin))
            created_acct = True
        elif action3 == 2:
            print('Enter your card number')
            user_card_num = int(input())
            print('Enter your PIN:')
            user_pin = str(input())
            if (user_card_num == cards[card_counter].storage[0]) and (user_pin == cards[card_counter].storage[1]):
                print('You have successfully logged in!')
                logged_in = True
                right = True
            else:
                print('Wrong card number or PIN!')

    while logged_in:
        print('1. Balance\n'
              '2. Log out\n'
              '0. Exit')
        action2 = int(input())
        if action2 == 0:
            print('Bye!')
            exit()
        elif action2 == 1:
            print('Balance:', balance)
        elif action2 == 2:
            print('You have successfully logged out!')
            logged_in = False
            right = False

