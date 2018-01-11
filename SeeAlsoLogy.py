from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

def getSeeAlsos(url):

    # html = urlopen("https://encyclopediadramatica.rs/Logan_Paul")
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req)
    content = html.read().decode('utf-8')

    soup = BeautifulSoup(content, 'html.parser')
    main_tag = soup.findAll('span',{'class':'mw-headline'})
    seeAlsoTitles = []
    seeAlsoLinks = []
    for headline in main_tag:
         # print(headline.text)
         if headline.text.lower() == 'see also':
                 links = headline.find_next('ul').find_all('a')
                 for link in links:
                     seeAlsoTitles.append(link.text)
                     seeAlsoLinks.append('https://encyclopediadramatica.rs'
                                         + link['href'])
                     # print('* ', link.text)
                     # print(link['href'])
    return seeAlsoTitles, seeAlsoLinks, soup.title.text

if __name__ == '__main__':
    Titles, Links, page = getSeeAlsos("https://encyclopediadramatica.rs/2016_Presidential_Election")
    print(page)
    print(Titles)
    print(Links)
