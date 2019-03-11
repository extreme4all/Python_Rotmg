import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from os.path  import basename
import requests

def scrape(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    text = urlopen(req).read()
    soup = BeautifulSoup(text,'html.parser')
    return soup
def save_image(lnk):
    with open(basename(lnk),'wb') as f:
            f.write(requests.get(lnk).content)
def get_images(url):
    soup = scrape(url)
    tabel = soup.findAll('div',attrs={'id':'d'})
    for div in tabel:
        images = div.findAll('img')
        for image in images:
            try:
                save_image('http:'+image['src'])
                print ('http:'+image['src'])
            except:
                pass
            
    
url = "https://www.realmeye.com/wiki/monster-index"
soup = scrape (url)
tabel = soup.findAll('div',attrs={'id':'d'})

i=1
while i==1:
    for p in tabel:
        data = p.findAll('p')
        for div in data:
            links = div.findAll('a')
            for a in links:
                print ('https://www.realmeye.com' + a['href'])
                get_images('https://www.realmeye.com' + a['href'])
                i =i+1

