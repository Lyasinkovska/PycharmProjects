
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


url="https://context.reverso.net/translation/english-french/hello"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')

soup = BeautifulSoup(webpage, 'html.parser')

only_words = soup.find_all(id='translations-content')
only_translations_list = []
for word in only_words:
	only_translations_list.append(word.text.split())
print(only_translations_list)

translations_with_examples = soup.find_all(id='examples-content')
translations_with_examples_list = []
for example in translations_with_examples:
	translations_with_examples_list.append(example.text.replace('\n', '').strip().split(10*' '))
print(translations_with_examples_list)



#document.querySelector('#translations-content').querySelectorAll('a').forEach(el=>console.log(el.innerText))
#document.querySelector('#examples-content').querySelectorAll('.text').forEach(el=>console.log(el.innerText))