
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


url="https://context.reverso.net/translation/english-french/hello"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')

soup = BeautifulSoup(webpage, 'html.parser')

translations_with_examples = soup.find_all(['div', 'a'], {'class':['translation']})
only_words=[]
for tag in translations_with_examples:
	only_words.append(tag.text.replace('\n', '').strip())
print(only_words)
