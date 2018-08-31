# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 21:04:47 2018

@author: hareevarshan
"""

import os
os.chdir("D:\\practicum\\euronews\\document-alignment_en-fr_en-de\\euronews\\en-fr")
import numpy as np
import pandas as pd


results = []
with open('2013_images.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split('|||'))
        
t_2014 = []
with open('2014 text.txt') as inputfile:
    for line in inputfile:
        t_2014.append(line.strip().split('|||'))


results[0]

df = pd.DataFrame(np.array(results).reshape(11847,3), columns = list("abc"))

df[0]

df_2014 = pd.DataFrame(np.array(t_2014).reshape(3246,3), columns = list("abc"))

eng = df[['a','b']]

eng_2014 = df_2014[['a','b']]

eng_2014.to_csv('english2014.txt', header=True, index=False, sep='\t', mode='a')
eng.to_csv('english2013.txt', header=True, index=False, sep='\t', mode='a')


sort = []
with open('english_temp.txt') as input_sort:
    for line in input_sort:
        sort.append(line.strip().split('\t'))
        
df_sort = pd.DataFrame(np.array(sort).reshape(11847,2), columns = list("ab"))

df1 = df_sort.iloc[:,0]
df1.to_csv('names.txt', index=False, mode='a')
df1.to_csv('names1.txt', index=False, mode='a')
data_img = pd.read_csv('names1.txt', header=None)
data_img.columns = ['name']


result_df = pd.concat([data_img, df_sort], axis=1)
result_df.dropna(inplace=True)

new = result_df.sort_values(by=['name'])

final = new.drop(['name'], axis=1)
final.to_csv('final.txt', index=False, sep='\t', mode='a')
euronews_sentences_2013 = eng[['b']]
euronews_sentences_2013.to_csv('euronews_sentences_2013.txt', index=False, mode='a')

euronews_sentences_2014 = eng_2014[['b']]
euronews_sentences_2014.to_csv('euronews_sentences_2014.txt', index=False, mode='a')
