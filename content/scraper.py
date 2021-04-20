import requests
from bs4 import BeautifulSoup
import re


class Lenta:

	def __init__(self):
		url = 'https://lenta.ru/rss/top7'
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'html.parser')
		self.titles = [q.text for q in soup.find_all('title') if re.search('Lenta.ru', str(q)) == None]
		self.links = [l.text for l in soup.find_all('guid')]
		self.image = [i.get('url') for i in soup.find_all('enclosure')]
		self.description = [i.text for i in soup.find_all('description')][1:]
		self.date = [i.text for i in soup.find_all('pubDate')]
		self.index = -1

	def __iter__(self):
		return self

	def __next__(self):
		self.index+=1
		if self.index<len(self.titles):
			return self.titles[self.index], self.links[self.index], self.image[self.index], self.description[self.index]
		else:
			raise StopIteration


class Obj:
	def __init__(self, title, link, image, description):
		self.title = title
		self.link = link
		self.image = image
		self.description = description

a = Lenta()
print(a)
for i in a:
	print(i)