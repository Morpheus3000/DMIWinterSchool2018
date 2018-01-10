import SeeAlsoLogy
import pandas as pd

Titles = []
Links = []
Pages = []

with open('Links.txt', 'r') as f:
    for link in f:
        link = link.strip()
        if len(link) > 0:
            print('Processing: ', link)
            title, links, page = SeeAlsoLogy.getSeeAlsos(link)
            Titles.append(';'.join(title))
            Links.append(';'.join(links))
            Pages.append(page[:-25])
            print('Getting first degree connections: ')
            for lin in links:
                print('Processing: ', lin)
                title, linky, page = SeeAlsoLogy.getSeeAlsos(lin)
                Titles.append(';'.join(title))
                Links.append(';'.join(linky))
                Pages.append(page[:-25])

d = {'Page':Pages, 'See Also':Titles, 'Links':Links}
df = pd.DataFrame(d)
df.to_csv('Processed links.csv', index=False)
