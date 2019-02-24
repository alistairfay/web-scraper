import requests
from bs4 import BeautifulSoup

root_url="http://www.claythorn.com"
request=requests.get(root_url)
request_text=request.text
#print(request_text)
soup=BeautifulSoup(request_text,"html.parser")
#print(soup.prettify())
for link in soup.find_all('a'):
    print(link)
    #print(link.get('href'))