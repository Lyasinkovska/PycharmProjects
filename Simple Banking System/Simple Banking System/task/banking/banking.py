import random
import sqlite3


class CardDataBase:

    def __init__(self):
        self.connection = sqlite3.connect("card.s3db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS card
                                                    (
                                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    number TEXT,
                                                    pin TEXT,
                                                    balance INTEGER DEFAULT 0
                                                    )"""
                            )

    def data_insertion(self, card_number, pin):
        self.cursor.execute("INSERT INTO card ( number, pin)  VALUES (?,?);", (str(card_number), str(pin)))
        self.connection.commit()

    def select_data(self, input_card_number, input_pin):
        self.cursor.execute("SELECT number, pin FROM card WHERE number = '{}' AND pin = '{}'".format(input_card_number,
                                                                                                input_pin))
        if self.cursor.fetchone() is None:
            return False
        else:
            return True

    def add_income(self, input_card_number, input_money):
        query = f"UPDATE card " \
                f"SET balance = balance + {input_money} " \
                f"WHERE number = {input_card_number}"
        self.cursor.execute(query)
        self.connection.commit()

    def balance(self, input_card_number, input_pin):
        query = f"SELECT balance FROM card WHERE number = {input_card_number} AND pin = {input_pin}"
        self.cursor.execute(query)
        self.connection.commit()
        balance = self.cursor.fetchone()[0]
        return balance

    def check_balance(self, input_card_number, money_to_transfer):
        query = "SELECT balance FROM card WHERE number = '{}'".format(input_card_number)
        self.cursor.execute(query)
        self.connection.commit()
        balance = self.cursor.fetchone()[0]
        return money_to_transfer > balance

    def substract_income(self, input_card_number, money_to_transfer):
        query = f"UPDATE card " \
                f"SET balance = balance - {money_to_transfer} " \
                f"WHERE number = {input_card_number}"
        self.cursor.execute(query)
        self.connection.commit()

    def close_account(self, input_card_number, input_pin):
        query = f"DELETE FROM card WHERE number = {input_card_number} AND pin = {input_pin}"
        self.cursor.execute(query)
        self.connection.commit()
        print("The account has been closed!")

    def card_in_db(self, card_to_transfer):
        query = f"SELECT number FROM card WHERE number = {card_to_transfer}"
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.fetchone()

class Account:

    def __init__(self):
        self.first_level_menu = "1. Create an account\n2. Log into account\n0. Exit\n"
        self.second_level_menu = "1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n"
        self.card_db = CardDataBase()
        self.choice()

    @staticmethod
    def user_choice(action):
        user_input = input(action)
        return user_input.isnumeric() and int(user_input)

    @staticmethod
    def luhn_algorithm(init_card_number):
        luhn_card_1 = [int(digit) * 2 for digit in init_card_number[::2]] + [int(digit) for digit in
                                                                             init_card_number[1::2]]
        luhn_card_2 = [(digit - 9) if digit > 9 else digit for digit in luhn_card_1]
        if sum(luhn_card_2) % 10 == 0:
            last_digit = 0
        else:
            last_digit = (sum(luhn_card_2) // 10 + 1) * 10 - sum(luhn_card_2)
        return int(init_card_number + str(last_digit))

    def card_number_generation(self):
        random.seed(random.random())
        iin = "400000"
        init_card_number = iin + str(random.sample(range(100000000, 999999999), 1)[0])
        return self.luhn_algorithm(init_card_number)

    @staticmethod
    def pin_generation():
        random.seed(random.random())
        return random.sample(range(1000, 9999), 1)[0]

    def account_creation(self):
        card_number = self.card_number_generation()
        pin = self.pin_generation()
        self.card_db.data_insertion(card_number, pin)
        print("Your card has been created\nYour card number:\n{}\nYour card PIN:\n{}".format(card_number, pin))

    def log_in(self):
        input_card_number = self.user_choice('Enter your card number:\n')
        input_pin = self.user_choice("Enter your PIN:\n")
        self.verification(input_card_number, input_pin)

    def do_transfer(self, input_card_number):
        card_to_transfer = int(input("Transfer.\nEnter card number:\n"))
        card_in_db = self.card_db.card_in_db(card_to_transfer)

        if card_to_transfer != self.luhn_algorithm(str(card_to_transfer)[:-1]):
            print("Probably you made mistake in the card number. Please try again!\n")
        elif card_to_transfer == input_card_number:
            print("You can't transfer money to the same account!\n")
        elif card_in_db is None:
            print("Such a card does not exist.\n")
        else:
            money_to_transfer = int(input("Enter how much money you want to transfer:\n"))
            if self.card_db.check_balance(input_card_number, money_to_transfer):
                print("Not enough money!\n")
            else:
                self.card_db.add_income(card_to_transfer, money_to_transfer)
                self.card_db.substract_income(input_card_number, money_to_transfer)
                print("Success!\n")

    @staticmethod
    def exit():
        print("Bye!")
        quit()

    def verification(self, input_card_number, input_pin):
        if self.card_db.select_data(input_card_number, input_pin):
            print("You have successfully logged in!\n")
            while True:
                action = self.user_choice(self.second_level_menu)
                if action == 1:
                    balance = self.card_db.balance(input_card_number, input_pin)
                    print(f"Balance: {balance}\n")
                    continue
                elif action == 2:
                    input_money = int(input("Enter income:\n"))
                    self.card_db.add_income(input_card_number, input_money)
                    print ("Income was added!\n")
                elif action == 3:
                    self.do_transfer(input_card_number)
                elif action == 4:
                    self.card_db.close_account(input_card_number, input_pin)
                elif action == 5:
                    print("You have successfully logged out!\n")
                    break
                elif action == 0:
                    self.exit()
                    break
        else:
            print("Wrong card number or PIN!\n")

    def choice(self):
        while True:
            action = self.user_choice(self.first_level_menu)

            if action == 1:
                self.account_creation()

            elif action == 2:
                self.log_in()

            elif action == 0:
                self.exit()


my_account = Account()

