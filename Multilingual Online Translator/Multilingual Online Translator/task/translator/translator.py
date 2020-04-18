from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests


def lang_from(lang_abbreviation):
	if lang_abbreviation == "en":
		return "french"
	elif lang_abbreviation == "fr":
		return "english"


def language_from_user():
	lang_abbreviation = input(f"Type \"en\" if you want to translate from French into English, "
							  f"or \"fr\" if you want to translate from English into French:\n")
	return lang_abbreviation


def lang_to(lang_abbreviation):
	if lang_abbreviation == "en":
		return "english"
	elif lang_abbreviation == "fr":
		return "french"


def word_to_translate():
	word = input("Type the word you want to translate:\n")
	return word


def result_message(lang_abbreviation, word):
	print(f"You chose \"{lang_abbreviation}\" as a language to translate \"{word}\"")


lang_abbreviation = language_from_user()
lang_from = lang_from(lang_abbreviation)
lang_to = lang_to(lang_abbreviation)
word = word_to_translate()
result_message(lang_abbreviation, word)

url = "https://context.reverso.net/translation/{}-{}/{}".format(lang_from, lang_to, word)

user_agent = {'User-agent': 'Mozilla/5.0'}
response = requests.get(url=url, headers=user_agent)
print(response.status_code)

req = Request(url, headers=user_agent)

web_byte = urlopen(req).read()

web_page = web_byte.decode('utf-8')
soup = BeautifulSoup(web_byte, 'html.parser')

translations = soup.find_all(['div', 'a'],  {'class': ['translation']})
only_words = []
for tag in translations:
	only_words.append(tag.text.replace('\n', '').strip())
print(only_words)

translations_with_examples = soup.find_all(['div', 'a'],  {'class': ['example']})
example_words = []
for tag in translations_with_examples:
	examples = tag.text.replace('\n', '').strip().split(10*' ')
	for ex in examples:
		example_words.append(ex)
print(example_words)



#document.querySelector('#translations-content').querySelectorAll('a').forEach(el=>console.log(el.innerText))
#document.querySelector('#examples-content').querySelectorAll('.text').forEach(el=>console.log(el.innerText))