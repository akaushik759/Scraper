from bs4 import BeautifulSoup

import requests

def google_search(query,headers):
	result = []
	url_google = 'https://google.com/search?q=' + query

	r = requests.get(url_google, headers=headers)
 
	soup = BeautifulSoup(r.text, 'html.parser')
	print("GOOGLE RESULTS\n\n")
	for info in soup.find_all('h3'):
		result.append(info.text)
	return result

def bing_search(query,headers):
	result = []
	url_bing = 'https://www.bing.com/search?q=' + query
	r = requests.get(url_bing, headers=headers)

	soup = BeautifulSoup(r.text, 'html.parser')
	print("BING RESULTS\n\n")
	for div in soup.find_all('h2'):
		if div is None:
			continue
		res = div.find('a')
		if res is None:
			continue
		res = res.text
		res.replace('<strong>','')
		res.replace('</strong>','')
		result.append(res)
	return result