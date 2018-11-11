def imdbify(link):
	if link == None:
		return ''
	else:
		link = 'https://www.imdb.com' + link
		
	return link

def mainPage(tt):
	if tt == None:
		return ''
	else:
		tt = 'https://www.imdb.com/title/' + tt
	
	return tt
	
def castPage(tt):
	if tt == None:
		return ''
	else:
		tt = 'https://www.imdb.com/title/' + tt + '/fullcredits'
	
	return tt
	
def numberResults(start, end):
	from bs4 import BeautifulSoup

	import requests, re

	url = 'https://www.imdb.com/search/title?title_type=documentary&release_date=' + str(start) + ',' + str(end) + '&countries=us&adult=include&sort=release_date,asc&count=250&start=' + str(1)

	results_page = requests.get(url)

	page_html = results_page.text

	soup = BeautifulSoup(page_html, 'html.parser')

	#Find number of search results-------------------------------
	desc = soup.find('div', attrs={'class' : 'desc'})

	expr = re.compile( '([^a-z]+?) title' )

	strResults = expr.findall(str(desc))

	#Format number of results as integer--------------------------------
	for aResults in strResults:
		
		global numResults
		numResults = aResults.replace( ',' , '' )
		numResults = numResults.replace('>','')
		
	return int(numResults)
