'''
Author: Sean O'Connor 
Date: June 4th, 2022
Use: creates a dataset of valid English reversals
'''

from random import random
import pandas as pd
import json
import collections
import random

f = open('data/words_dictionary.json')
dict_dict = json.load(f)

valid_words = dict_dict.keys()
reversal_dict = collections.defaultdict(list)
for word in valid_words: 
    if word[::-1] in valid_words:
        reversal_dict[word].append(word[::-1])

f.close()

indicators = []
with open('/Users/seanoconnor/Desktop/cs224u_crossword/data/indic/rev.txt') as f:
    lines = f.readlines()
    lines = [x.strip('\n') for x in lines]
    indicators = lines


input_sequence = []
output_sequence = []

for word, rev in reversal_dict.items():
    ind = random.choice(indicators).replace("_", " ")
    inputs = [ind + " " + word, word + " " + ind]
    input_sequence.append(random.choice(inputs))
    output_sequence.append(rev[0])



df = pd.DataFrame(zip(input_sequence, output_sequence))
df.to_csv('reversal.csv', index=False)

