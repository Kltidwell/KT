from bs4 import BeautifulSoup

import requests, json, re, time

Year = 1878

imdb_tts = []

count = 0


while Year < 2018:

	page = 1

	nextButton = ""
	
	while nextButton is not None:
		
		url = 'https://www.imdb.com/search/title?title_type=documentary&release_date=' + str(Year) + '-01-01,' + str(Year) + '-12-31&countries=us&adult=include&sort=release_date,asc&count=250&start=' + str(page)
		print('Scraping!',url)
		results_page = requests.get(url)

		page_html = results_page.text

		soup = BeautifulSoup(page_html, 'html.parser')
		
		nextButton = soup.find('a', attrs={'class' : 'lister-page-next next-page'})
			
		all_tts = soup.find_all('img', attrs={'class' : 'loadlate'})
		
		for a_tt in all_tts:
			
			imdb_tts.append(a_tt['data-tconst'])
			
			count = count + 1
			
		page = page + 250
	
	time.sleep(1)	
	Year = Year + 1
	print(count)
	
json.dump(imdb_tts,open('imdb_tts.json','w'),indent=2)
