"""
File: web_crawler_avg.py
Name:
--------------------------
This file demonstrates how to get
average grades on www.imdb.com/chart/top.
You should see the output around 8.2543999999
"""


import requests 
from bs4 import BeautifulSoup


def main():
	url = 'http://www.imdb.com/chart/top'
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html)
	#########################
	items = soup.find_all('td', {'class': 'ratingColumn imdbRating'})
	total = 0
	for item in items:
		rate = item.strong.text
		total += float(rate)
	print(total/250)
	#########################


if __name__ == '__main__':
	main()
