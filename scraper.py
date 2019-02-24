import requests
from bs4 import BeautifulSoup

def get_urls(page):
    '''given a page, returns all the urls from that page''' 
    request=requests.get(page)
    request_text=request.text
    soup=BeautifulSoup(request_text,"html.parser")
    hrefs=[]
    for link in soup.find_all('a'):
        href=link.get('href')
        if not href.startswith("#"):
            hrefs.append(href)
    return hrefs

root_url="http://www.claythorn.com"
allowed_domain="claythorn.com"
hrefs=get_urls(root_url)
print(hrefs)
