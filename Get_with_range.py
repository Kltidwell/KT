from bs4 import BeautifulSoup

import requests, json, re, time
from datetime import date, datetime, timedelta
from functlib import numberResults

startDate = date(1878, 1, 1)

endDate = date(1900, 12, 31)

imdb_tts = []

count = 0

testEnd = date(1, 1, 1)

numResults = numberResults(startDate, endDate)

while startDate <= endDate:
	page = 1
	testEnd = endDate
	nextButton = ''
	
	print('Testing Range from ' + str(startDate) + ' to ' + str(testEnd))
	while numberResults(startDate, testEnd) >= 500:
		testEnd = (testEnd-startDate)/2 + startDate
		print('Adjusting Range')
		time.sleep(5)
					
	while nextButton is not None:
		url = 'https://www.imdb.com/search/title?title_type=documentary&release_date=' + str(startDate) + ',' + str(testEnd) + '&countries=us&adult=include&sort=release_date,asc&count=250&start=' + str(page)
			
		results_page = requests.get(url)

		page_html = results_page.text
				

		soup = BeautifulSoup(page_html, 'html.parser')
			
		all_tts = soup.find_all('img', attrs={'class' : 'loadlate'})
		
		print('Scraping : from ' + str(startDate) + ' to ' + str(testEnd))
		
		for a_tt in all_tts:
			
			imdb_tts.append(a_tt['data-tconst'])
			
			count = count + 1
				
		page = page + 250
						
		nextButton = soup.find('a', attrs={'class' : 'lister-page-next next-page'})
		time.sleep(10)	

	time.sleep(1)	
	startDate = testEnd + timedelta(days = 1)
	print(str(count) + ' out of ' + str(numResults))
	
json.dump(imdb_tts,open('imdb_tts_10000.json','w'),indent=2)
