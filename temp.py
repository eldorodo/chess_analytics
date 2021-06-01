import os
from zipfile import ZipFile
#import scrap
#os.system('scrap.py')    
from autoscraper import AutoScraper
print(list(set([1,1,1,2,3,4,32,324,1]) - set([2,912])))
print(os.getcwd())

#with ZipFile("data/" + "Aronian.zip", 'r') as zipObj:
#    print("Extracting pgn file from zip file")
#    zipObj.extractall("data")
#    zipObj.close()

import shutil
shutil.move("Akobian_moves.csv", "data/csv")