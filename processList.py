import SeeAlsoLogy
import pandas as pd

Titles = []
Links = []

with open('Links.txt', 'r') as f:
    for link in f:
        print('Processing: ', link)
        title, link = SeeAlsoLogy.getSeeAlsos(link)
        Titles.append(';'.join(title))
        Links.append(';'.join(link))
d = {'Titles':Titles, 'Links':Links}
df = pd.DataFrame(d)
df.to_csv('Processed links.csv', index=False)
