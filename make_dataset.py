'''
Author: Sean O'Connor 
Date: June 4th, 2022
Use: creates a dataset of valid English reversals
'''

import pandas
import json
import collections

f = open('data/words_dictionary.json')
dict_dict = json.load(f)

valid_words = dict_dict.keys()
reversal_dict = collections.defaultdict(list)
count = 0
for word in valid_words: 
    if word[::-1] in valid_words:
        count += 1
        reversal_dict[word].append(word[::-1])
print(count)

with open('reversal.json', 'w') as outfile:
    json.dump(reversal_dict, outfile)
