from bs4 import BeautifulSoup

import requests, json, re, time
from datetime import date, datetime, timedelta
from functlib import imdbify, numberResults

startDate = date(1878, 1, 1)

endDate = date(1900, 12, 31)

imdb_tts = []

count = 0
page = 1
nextButton = ''

url = 'https://www.imdb.com/search/title?title_type=documentary&release_date=' + str(startDate) + ',' + str(endDate) + '&countries=us&adult=include&sort=release_date,asc&count=250&start=' + str(page)
numResults = numberResults(startDate, endDate)				
while nextButton is not None:

	print('Scraping!')
	
	for results_page in range(10):
		results_page = requests.get(url)
		while True:
	
			try:
			
				page_html = results_page.text

				soup = BeautifulSoup(page_html, 'html.parser')
					
				all_tts = soup.find_all('img', attrs={'class' : 'loadlate'})

				for a_tt in all_tts:
					
					imdb_tts.append(a_tt['data-tconst'])
					
					count = count + 1
				
				nextButton = soup.find('a', attrs={'class' : 'lister-page-next next-page'})
				
				if nextButton is not None:
					print('on to the next page')
					next_page = nextButton['href']
						
					url = imdbify(next_page)
				break
			
			except TimeoutError:
				print('TimeoutError')
				continue
			break
		
	time.sleep(1)	
	print(str(count) + ' out of ' + str(numResults))
	
json.dump(imdb_tts,open('imdb_tts_next.json','w'),indent=2)
