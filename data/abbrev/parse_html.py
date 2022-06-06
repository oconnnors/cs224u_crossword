#Data from:https://www.unscramblerer.com/crossword-abbreviations/

from bs4 import BeautifulSoup
import pandas as pd
import re

with open("data/abbrev/index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

data = soup.findAll("li")

abbrev = []
meaning = []
for element in data:
    if element is None: continue
    x = re.split('<b>|:|</b>|</li>', str(element))
    if len(x) > 4:
        ab_def = x[3].strip(' ').split(',')
        for example in ab_def: 
            abbrev.append(x[1])
            print(x[1])
            meaning.append(example)
            print(str(example).strip())

df = pd.DataFrame(zip(abbrev, meaning))
df.to_csv('shorthand.csv', index=False
)