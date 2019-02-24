import requests
from bs4 import BeautifulSoup
import pprint
from urllib.parse import urlparse

def visit_page(page, allowed_domain):
    '''analyse a page for internal links, external links, static resources''' 
    print("visiting " + str(page) + "...")
    internal_urls=[]
    external_urls=[]
    static_resources=[]
    request=requests.get(page)
    if request.status_code==200:
        request_text=request.text
        soup=BeautifulSoup(request_text,"html.parser")
        for link in soup.find_all('a'):
            href=link.get('href')
            url = urlparse(href)
            if allowed_domain in url:
                if href not in internal_urls:
                    internal_urls.append(href)
            else:
                if not href.startswith("#") and href not in external_urls:
                    external_urls.append(href)
        for link in soup.find_all(True):
            src=link.get('src')
            if src !=None and src not in static_resources:
                static_resources.append(src)
        page_data={"address":page,"internal_urls":internal_urls,"external_urls":external_urls,"static_resources":static_resources}
    else:
        page_data={"address":page,"internal_urls":[],"external_urls":[],"static_resources":[]}
    #print(page_data)
    return page_data

root_url="http://wiprodigital.com/"
allowed_domain="wiprodigital.com"
internal_urls=[]
visited_urls=[]
site_data=[]

internal_urls.append(root_url)
while len(internal_urls) > 0:
    print("internal urls count " + str(len(internal_urls)))
    print("visited urls count " + str(len(visited_urls)))
    this_page=internal_urls[0]
    page_data=visit_page(this_page, allowed_domain)
    site_data.append(page_data)
    for url in page_data["internal_urls"]:
        if url not in internal_urls and url not in visited_urls:
            internal_urls.append(url)
    internal_urls.remove(this_page)
    visited_urls.append(this_page)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(site_data)
