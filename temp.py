import os
from zipfile import ZipFile
#import scrap
#os.system('scrap.py')    
from autoscraper import AutoScraper
import numpy as np
from bs4 import BeautifulSoup

#print(list(set([1,1,1,2,3,4,32,324,1]) - set([2,912])))
#print(os.getcwd())

#with ZipFile("data/" + "Aronian.zip", 'r') as zipObj:
#    print("Extracting pgn file from zip file")
#    zipObj.extractall("data")
#    zipObj.close()

#import shutil
#shutil.move("Akobian_moves.csv", "data/csv")

import pandas as pd



to_extract = ["Event", "Site", "Date", "Round", "White", "Black", "Result", "WhiteElo", "BlackElo","ECO"]

df = pd.DataFrame(columns=to_extract)

#df = df.append(pd.Series(), ignore_index=True)
#print(df)

#df2 = pd.DataFrame(index = list(range(2000000)),columns=to_extract)

#df2.to_csv("a.csv",chunksize=10000)

#print("data/pgn2/" + os.listdir("data/pgn2"))

#print(["data/pgn2"]*10)

#print(np.array(['Aachen MT', 'Aachen', '1868.??.??', '5', 'Paulsen, Wilfried', 'Zukertort, Johannes Hermann', '0-1', '', '', 'C65']))


#from itertools import repeat
#print(repeat(2))

from multiprocessing.dummy import Pool as ThreadPool 

#def write(i, x):
    #print(i, "---", x)

#a = ["1","2","3"]
#b = ["4","5","6"] 

#pool = ThreadPool(2)
#pool.starmap(write, zip(a,b)) 
#pool.close() 
#pool.join()

""" url = "https://www.pgnmentor.com/files.html"
wanted_list=["View the chess"]
scraper=AutoScraper()
result=scraper.build(url,wanted_list)
print(result) """

import urllib.request
url = "https://www.pgnmentor.com/files.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

for script in soup(["script", "style"]):
    script.decompose()
#delete out tags


strips = list(soup.stripped_strings)
print(strips[:5])