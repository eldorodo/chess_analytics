import requests
from multiprocessing import Pool
from zipfile import ZipFile
from converter.pgn_data import PGNData
import os
#import shutil
#import glob

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


""" def pgn_to_csv(pgn_file_name):

    try:
        pgn_data = PGNData(pgn_file_name)
        result = pgn_data.export()
        result.print_summary()
        #shutil.copy(f"{pgn_file_name}_Akobian_moves.csv", "data/csv")
        #os.remove(f"{pgn_file_name}_Akobian_moves.csv")
        #shutil.copy(f"{pgn_file_name}_game_info.csv", "data/csv")
        #os.remove(f"{pgn_file_name}_game_info.csv")
    
    except:
        print(f"Some error occured in extraction for {pgn_file_name}")
        return """


# Thread function
def process_url(line_url):
    line_url = line_url.rstrip()
    line_url = line_url.lstrip()
    line_url = line_url.strip()
    last_slash_index = line_url.rfind("/")
    file_name = line_url[last_slash_index+1:]

        #continue

    print(f"Downloading {file_name}")
    download_url(line_url, "data/pgn/"+file_name)

    if (file_name.endswith("zip")):

        with ZipFile("data/pgn/"+file_name, 'r') as zipObj:
            print(f"Extracting pgn file from zip file {file_name}")
            zipObj.extractall("data/pgn")
            zipObj.close()
            print (f"deleting zip file {file_name}")
            os.remove("data/pgn/"+file_name)

    #pgn_file_name = f"{file_name[:-4]}.pgn"

    #pgn_to_csv(pgn_file_name)  #Commented as it takes lot of space for a single pgn

    #print(f"Removing pgn file: {pgn_file_name}")
    #os.remove(pgn_file_name)


# main starts here
if __name__ == '__main__':

    import scrap2
    
    #Remove existing csv files and make a new directory
    if (os.path.exists('data/pgn') == False):
        os.mkdirs('data/pgn')

    if (os.path.exists('data/download links') == False):
        os.mkdirs('data/download links')
                
    f = open("data/download links/master_download_links.txt", "r")
        
    all_lines = list(f.readlines())

    with Pool(20) as p:
        p.map(process_url, all_lines)   
        
    #for pgnfile in glob.iglob(os.path.join("*.pgn")):
        #shutil.move(pgnfile, "data/pgn")
        #pgnfile.close()   

    f.close()