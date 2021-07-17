import chess
import chess.pgn
import os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 
import pandas as pd

def game_detail_extraction(filename,dir= "data/pgn/",output_dir = "data/csv/"):
    to_extract = ["Black", "BlackElo", "Date", "ECO", "Event", "Result", "Round", "Site", "White", "WhiteElo"]
    if filename.endswith(".pgn"): 
        pgn = open(dir + filename)
        game_data = pd.DataFrame()
        while(True):
            game = chess.pgn.read_game(pgn)
            row = []
            try:
                for ext in to_extract:
                    row.append(game.headers[ext])
                    #print(row)
                row_series = pd.Series(row, index = to_extract)
                game_data = game_data.append(row_series, ignore_index=True)
            except:
                try:
                    game_data.columns = to_extract
                    csv_file_name = f"{filename[:-4]}.csv"
                    game_data.to_csv(f"{output_dir}{csv_file_name}",index = False)
                    print(f"End of PGN {filename}")
                    break #Break when PGN ends
                except:
                    print(f"Not even one game found in {filename} or some other error")
                    break #Break also when no games are in PGN
    return "Process done"
    


if (os.path.exists('data/csv') == False):
    os.mkdir('data/csv/')


dir = "data/pgn/"
pgn_files = list(os.listdir(dir))
print(pgn_files)


dir_list = [dir] *len(pgn_files)
output_dir = "data/csv/"
output_dir_list = [output_dir] *len(pgn_files)

pool = ThreadPool(20)
pool.starmap(game_detail_extraction, zip(pgn_files,dir_list,output_dir_list)) 
pool.close() 
pool.join()




