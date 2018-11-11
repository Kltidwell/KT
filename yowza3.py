from bs4 import BeautifulSoup

import requests, json, re, time
from datetime import date, datetime, timedelta
from functlib import imdbify

startDate = date(1878, 1, 1)

endDate = date(1899, 12, 31)

imdb_tts = []

count = 0
page = 1
nextButton = ''

url = 'https://www.imdb.com/search/title?title_type=documentary&release_date=' + str(startDate) + ',' + str(endDate) + '&countries=us&adult=include&sort=release_date,asc&count=250&start=' + str(page)
				
while nextButton is not None:

	print('Scraping!',url)
	results_page = requests.get(url)

	page_html = results_page.text

	soup = BeautifulSoup(page_html, 'html.parser')
		
	all_tts = soup.find_all('img', attrs={'class' : 'loadlate'})

	for a_tt in all_tts:
		
		imdb_tts.append(a_tt['data-tconst'])
		
		count = count + 1
	
	nextButton = soup.find('a', attrs={'class' : 'lister-page-next next-page'})
	
	if nextButton is not None:
		
		next_page = nextButton['href']
			
		url = imdbify(next_page)
	else:
		continue
		
	time.sleep(1)	
	print(count)
	
json.dump(imdb_tts,open('imdb_tts_next.json','w'),indent=2)
