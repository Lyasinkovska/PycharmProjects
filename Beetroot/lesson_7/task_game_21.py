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


def count_points(card_name):
	cards = {'Ace': 11, 'King': 10, 'Queen': 10, 'Jack': 10, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4,
			 '3': 3, '2': 2}
	return cards[card_name]


def shuffle_deck():
	"""
	shuffle a deck
	:return: shuffled deck
	"""
	card_list = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2',
				 'Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2',
				 'Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2',
				 'Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
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


if __name__ == '__main__':
	my_deck = shuffle_deck()
	while True:
		us_input = input("Enter: ")
		if us_input == 'y':
			card = give_card(my_deck)
			if card:
				points = count_points(card)
				print(card, points)
			else:
				break
		else:
			break
