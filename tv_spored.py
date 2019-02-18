# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:10:42 2019

@author: andreask
"""

from requests import get
from bs4 import BeautifulSoup


url = 'http://www.rtv.si/'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

programi = []
trenutno = []
ura = []

sedaj = html_soup.find_all('tr', class_ = 'spored_now')

for program in sedaj:
    programi.append(program.td.center.a.text)
    trenutno.append(program.find("td", class_="spored").text)
    ura.append(program.find("td", class_="ura").text)

import pandas as pd

programi_df = pd.DataFrame({'Program': programi,                       
                       'Trenutno': trenutno,  
                       'Zacetek': ura, 
                       })
#print programi_df

#programi_df.to_csv('spored.csv', header=None, index=None, sep=' ', mode='a', encoding = 'utf-8')

'''
for n in programi_df['Zacetek']:
    print n
    
'''