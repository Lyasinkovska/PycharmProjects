import random


class Account:

    def __init__(self):
        self.first_level_menu = "1. Create an account\n2. Log into account\n0. Exit\n"
        self.second_level_menu = "1. Balance\n2. Log out\n0. Exit\n"
        self.credentials = dict()
        self.choice()

    @staticmethod
    def user_choice(action):
        user_input = input(action)
        return user_input.isnumeric() and int(user_input)

    def luhn_algorithm(self, init_card_number):
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
        self.add_credentials(pin, card_number)
        print("Your card has been created\nYour card number:\n{}\nYour card PIN:\n{}" \
              .format(card_number, pin))

    def add_credentials(self, pin, card_number):
        self.credentials[card_number] = pin

    def log_in(self):
        input_card_number = self.user_choice('Enter your card number:\n')
        input_pin = self.user_choice("Enter your PIN:\n")
        self.verification(input_card_number, input_pin)

    @staticmethod
    def balance(balance):
        print(f"Balance: {balance}\n")

    @staticmethod
    def exit():
        print("Bye!")
        quit()

    def verification(self, input_card_number, input_pin):
        if input_card_number in self.credentials and self.credentials[input_card_number] == input_pin:
            print("You have successfully logged in!\n")
            while True:
                action = self.user_choice(self.second_level_menu)
                if action == 1:
                    self.balance(0)
                    continue
                elif action == 2:
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
