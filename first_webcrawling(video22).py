import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


links_todo = ['http://www.webscrapingfordatascience.com/crawler/']
links_seen = set()

def visit(url, links_seen):
	html = requests.get(url).text
	html_soup = BeautifulSoup(html, 'html.parser')
	new_links = []
	for link in html_soup.find_all('a'):
		link_url = link.get('href')
		if link_url is None:
			continue
		full_url = urljoin(url, link_url)
		if full_url in links_seen:
			continue
		new_links.append(full_url)
	return new_links

while links_todo:
	url_to_visit = links_todo.pop()
	links_seen.add(url_to_visit)
	print('Now Visiting: ', url_to_visit)
	new_links = visit(url_to_visit, links_seen)
	print(len(new_links), 'new link(s) found...')
	links_todo += new_links