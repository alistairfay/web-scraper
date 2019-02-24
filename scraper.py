import requests
from bs4 import BeautifulSoup
import pprint

def visit_page(page, allowed_domain):
    '''analyse a page for internal links, external links, static resources''' 
    internal_urls=[]
    external_urls=[]
    static_resources=[]
    request=requests.get(page)
    request_text=request.text
    soup=BeautifulSoup(request_text,"html.parser")
    #print(soup)
    for link in soup.find_all('a'):
        href=link.get('href')
        if allowed_domain in href:
            if href not in internal_urls:
                internal_urls.append(href)
        else:
            if not href.startswith("#") and href not in external_urls:
                external_urls.append(href)
    for link in soup.find_all('img'):
        src=link.get('src')
        if src not in static_resources:
            static_resources.append(src)
    page_data={"address":page,"internal_urls":internal_urls,"external_urls":external_urls,"static_resources":static_resources}
    return page_data

root_url="https://www.claythorn.com"
allowed_domain="claythorn.com"
internal_urls=[]
visited_urls=[]
site_data=[]

internal_urls.append(root_url)
while len(internal_urls) > 0:
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





#for url in site_urls:
#    if allowed_domain in url:
#        #visit page
#    else:
#        #update external_urls
##output sitemap
