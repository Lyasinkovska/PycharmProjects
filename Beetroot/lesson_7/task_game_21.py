"""
задание под звездочкой большое. Но попробуйте.

Пишем игру в 21. Создать массив "карт" рандомно их перемешать и выдавать "игроку" пока не скажет стоп или не проиграет.

карта - словарь. Масть, Название, очки.  Не надо мудрить с "вариантами очков карт" упрощенно.
Интересует работа с циклами, словарями, функциями :)
Помним про единую ответственность. Разбиваем на примитивные действия. С начала пишем каркас с запассенными функциями,
а потом заполняем "пропуски".

пока не стоп или перебор
 предложить карту
 вывести текущие очки.
если не перебор набирать себе карт (я не знаю точных правил как правильно если тоже не в курсе пусть скрипт набирает
до 18ти очков например или проигрыша)
"""
import random


# suits = ['clubs', 'diamonds', 'hearts', 'spades']
# list(cards.keys())#  * 4


def card_points(card_name):
    cards = {'Ace': 11, 'King': 10, 'Queen': 10, 'Jack': 10, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4,
             '3': 3, '2': 2
             }
    return cards[card_name]


def shuffle_deck():
    """
    shuffle a deck
    :return: shuffled deck
    """
    card_list = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2'] * 4
    shuffled_cards = random.sample(card_list, len(card_list))
    return shuffled_cards


def give_card(deck):
    """
    pop one card from a deck and return
    :param deck:
    :return:
    """
    while deck:
        return deck.pop()


def winner(comp_points, user_points):
    result = f"Result: computer {comp_points} -  user {user_points}\n"
    if comp_points > 21 and user_points <= 21:
        return f"{result}The winner is User.\n"
    elif user_points > 21 and comp_points <= 21:
        return f"{result}The winner is Computer.\n"
    elif comp_points > 21 and user_points > 21:
        return f"{result}It's a draw.\n"
    else:
        if comp_points == user_points:
            return f"{result}It's a draw.\n"
        else:
            if user_points > 21 or comp_points > user_points:
                return f"{result}The winner is Computer.\n"
            elif comp_points > 21 or comp_points < user_points:
                return f"{result}The winner is User.\n"


if __name__ == '__main__':
    exit_message = True
    while exit_message:
        print("LET'S PLAY!!!")
        result = {'user': {'points': 0, 'cards': []}, 'computer': {'points': 0, 'cards': []}}
        my_deck = shuffle_deck()
        cards_amount = 2

        for i in range(cards_amount):
            user_card = give_card(my_deck)
            result['user']['cards'].append(user_card)
            result['user']['points'] += card_points(user_card)
            comp_card = give_card(my_deck)
            result['computer']['cards'].append(comp_card)
            result['computer']['points'] += card_points(comp_card)
        print(f"User cards: {result['user']['cards']}, user points: {result['user']['points']}\n"
              f"Computer cards: {result['computer']['cards']}, computer points: {result['computer']['points']}")

        while result['computer']['points'] < 18:
            result['computer']['cards'].append(comp_card)
            result['computer']['points'] += card_points(comp_card)

        while True:
            us_input = input("Enter 'y': to take a card, 'f': to finish the round, 'q': to quit. > ")
            if us_input == 'y':
                user_card = give_card(my_deck)
                if user_card:
                    result['user']['points'] += card_points(user_card)
                    result['user']['cards'].append(user_card)
                    print(f"User cards: {result['user']['cards']}, user points: {result['user']['points']}\n")
                    if result['user']['points'] > 21:
                        print(winner(result['computer']['points'], result['user']['points']))
                        break
            elif us_input == 'f':
                print(winner(result['computer']['points'], result['user']['points']))
                break
            elif us_input == 'q':
                exit_message = False
                break
            else:
                print("Wrong answer.")
