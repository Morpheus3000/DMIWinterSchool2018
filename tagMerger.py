import json
from tqdm import tqdm
import pandas as pd
import math

def fixNumbers(x):
    if math.isnan(x):
        return ''
    else:
        return str(int(x))

def merger(jsonFile, csvFile):
    data = json.load(open(jsonFile, 'r'))
    df = pd.read_csv(open(csvFile, 'r'))
    df['themetags'] = ''
    df['memetags'] = ''
    df.imagefile = df.imagefile.apply(pd.to_numeric, errors='coerce')
    total = len(data)
    for i in tqdm(range(total)):
        info = data[i]['tags']
        if len(info['imagename'].strip()) > 0:
            ind = df.index[df['imagefile'] == int(info['imagename'])]
            df.themetags[ind[0]] = info['themetags']
            df.memetags[ind[0]] = info['memetags']
    df.imagefile = df.imagefile.apply(fixNumbers)
    print(df.head())

if __name__ == '__main__':
    merger('07-01-2018-12-00-00-tagdata.json', 'fixed_07-01-2018-12-00-00.csv')

