import requests
from bs4 import BeautifulSoup
import re

class Lenta:

	def __init__(self):
		url = 'https://lenta.ru/rss/top7'
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')
		self.titles = [q.text for q in soup.find_all('title') if re.search('Lenta.ru', str(q)) == None]
		self.links = [l.text for l in soup.find_all('guid')]
		#self.image = [i.text for i in soup.find_all('enclosure')]
		self.index = -1

	def __iter__(self):
		return self

	def __next__(self):
		self.index+=1
		if self.index<len(self.titles):
			return self.titles[self.index], self.links[self.index]
		else:
			raise StopIteration




class Obj:
	def __init__(self, title, link):
		self.title = title
		self.link = link

if __name__ == '__main__':
	obj = Lenta()
	for i in obj:
		print(i)
