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
            if len(title) == 0:
                title = [page[:-25]]
            Titles.append(';'.join(title))
            Pages.append(page[:-25])

d = {'Page':Pages, 'See Also':Titles}
df = pd.DataFrame(d)
df.to_csv('Processed links.csv', index=False)
