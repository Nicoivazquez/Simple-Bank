# Write your code here
import random
import sqlite3

run = True
logged_in = False
created_acct = False
right = False
iin = str(400000)
balance = 0
card_counter = 0
#id_ = 0


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('DROP TABLE card;')
cur.execute('CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INT DEFAULT 0);')
conn.commit()


def sql_save(num, pin, bal):
    cur.execute("INSERT INTO card(number, pin, balance) VALUES (?,?,?);", (num, pin, bal))
    conn.commit()


def sql_fetch_new(idx):
    #global id_
    id_ = (random.choice(range(100)),)
    cur.execute("SELECT id, number, pin, balance FROM card WHERE id=?", id_)
    conn.commit()
    for row in cur.fetchall():
        return row[idx+1]


def sql_fetch(num, idx):
    lookup_num = (num,)
    cur.execute("SELECT id, number, pin, balance FROM card WHERE number=?;", lookup_num)
    conn.commit()
    for row in cur.fetchall():
        return row[idx+1]


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
        self.balance = 0
        self.storage = []
        self.storage.append(int(self.credit_card))
        self.storage.append(str(self.pin))
        self.storage.append(int(self.balance))

    def __getitem__(self, item):
        return self.storage[item]

    def check_sum(self):
        card_minus_checksum = self.credit_card[:-1]
        if str(self.credit_card) in luhn_algorithem(card_minus_checksum):
            return True
        else:
            return False
    def balance(self):
        balance = 0
        print(balance)

cards = list() # create all the credit cards 1000 of them in one loop
for i in range(100):
    cards.append(CreditCard())

# save all cards into the sql database in one loop
for i in cards:
    sql_save(i[0], i[1], i[2])

# for row in cur.execute('SELECT * FROM card;'):
#     print(row)


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
            new_card = sql_fetch_new(0)
            print(int(new_card))
            print('Your card PIN:')
            print(str(sql_fetch(new_card, 1)))
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
            print(sql_fetch_new(0))
            print('Your card PIN:')
            print(str(sql_fetch_new(1)))
            created_acct = True
        elif action3 == 2:
            print('Enter your card number')
            user_card_num = int(input())
            print('Enter your PIN:')
            user_pin = str(input())
            if (user_card_num == int(sql_fetch(user_card_num, 0))) and (user_pin == str(sql_fetch(user_card_num, 1))):
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

