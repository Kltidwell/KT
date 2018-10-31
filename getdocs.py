from bs4 import BeautifulSoup

import requests, json, re, time

page = 1

imdb_ts = []

while page <= 1:

	url = 'https://www.imdb.com/search/title?title_type=documentary&release_date=1874-01-01,1937-12-31&countries=us&sort=year,asc&count=50&page=' + str(page)
	print('Scraping!',url)
	results_page = requests.get(url)

	page_html = results_page.text

	soup = BeautifulSoup(page_html, 'html.parser')
		
	all_urls = soup.find_all('h3', attrs={'class' : 'lister-item-header'})
	
	for a_link in all_urls:

		the_link = a_link.find('a')
		
		imdb_ts.append(the_link['href'])
		
		time.sleep(1)

	page = page + 1
print(imdb_ts)
# json.dump(imdb_ts,open('t_numbs.json','w'),indent=2)
