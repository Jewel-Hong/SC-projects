import requests 
from bs4 import BeautifulSoup


def main():
	url = 'https://www.imdb.com/chart/top/'
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html)
	items = soup.find_all('span', {'class': 'secondaryInfo'})
	items = items.span.text
	print(items)
	# d = {}
	# for item in items:
	# 	year = item.span.text
	# 	if year in d:
	# 		d[year] += 1
	# 	else:
	# 		d[year] = 1
	#
	# for year, count in sorted(d.items(), key=lambda t: t[1]):
	# 	print(f'{year} -> {count}')


if __name__ == '__main__':
	main()
