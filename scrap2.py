# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:09:05 2021

@author: hariramg
"""

from autoscraper import AutoScraper
import pandas as pd
from multiprocessing.pool import ThreadPool as Pool
import os

url="https://www.pgnmentor.com/files.html"
wanted_list_players=["Adams.pgn","MacKenzie.pgn"]

wanted_list_openings=["Modern.pgn","Hodgson.pgn","OwenDefense.pgn",
                      "CenterGame-Danish.pgn","English1b6.pgn"]

wanted_list_events=["Stavanger2020.pgn","Dortmund1973.pgn",
             "Candidates2018.pgn","Interzonal1982a.pgn","WorldChamp2018.pgn","WorldChamp1886.pgn"]


def remove_and_append(your_list,remove_char, append):
    
    new_strings = []
    for string in your_list:
        new_string = string[:-remove_char]
        new_string = new_string + append
        new_strings.append(new_string)

    return new_strings

append_players =  "https://www.pgnmentor.com/players/"
append_openings = "https://www.pgnmentor.com/openings/"
append_events =  "https://www.pgnmentor.com/events/"


scraper=AutoScraper()
scraper.load("autoscraper_models/Players_pgnmentor")
result=scraper.get_result_similar(url)
#result=scraper.build(url,wanted_list_players)
players_list = list(result)
players_list = [append_players + x for x in players_list]
players_list = remove_and_append(players_list , 4, ".zip")
print("Players ", len(players_list))



scraper=AutoScraper()
scraper.load("autoscraper_models/openings_pgnmentor")
result=scraper.get_result_similar(url)
#result=scraper.build(url,wanted_list_openings)
openings_list = list(result)
openings_list = [append_openings + x for x in openings_list]
openings_list = remove_and_append(openings_list , 4, ".zip")
print("openings ", len(openings_list))



scraper=AutoScraper()
scraper.load("autoscraper_models/events_pgnmentor")
result=scraper.get_result_similar(url)
#result=scraper.build(url,wanted_list_events)
events_list = list(result)
events_list = [append_events + x for x in events_list]
print("events ", len(events_list))



master_list = []
master_list.extend(players_list)
master_list.extend(openings_list)
master_list.extend(events_list)


#url="https://theweekinchess.com/twic"
#wanted_list_weekinchess=["920","921"]
#scraper=AutoScraper()
#result=scraper.build(url,wanted_list_weekinchess)
#week_in_chess_list = list(result)
#append_start = "https://theweekinchess.com/zips/twic"
#append_end = "g.zip"
#week_in_chess_list = [append_start + x + append_end for x in week_in_chess_list]

#master_list.extend(week_in_chess_list)


#if (os.path.exists('data/download links') == False):    
    #os.mkdir('data/download links')

textfile = open("data/download links/master_download_links.txt", "w")
for element in master_list:
    textfile.write(element + "\n")
textfile.close()

#print(result)