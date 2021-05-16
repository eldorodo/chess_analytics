import requests
from multiprocessing import Pool
from zipfile import ZipFile
import os

os.chdir("D:/Others/Personal projects/Sports analysis - git/chess_analytics")

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

# Thread function
def process_url(line_url):
    line_url = line_url.rstrip()
    line_url = line_url.lstrip()
    line_url = line_url.strip()
    last_slash_index = line_url.rfind("/")
    file_name = line_url[last_slash_index+1:]

        #continue

    print(f"Downloading {file_name}")
    download_url(line_url, "Data/" + file_name)
    


    if (file_name.endswith("zip")):

        with ZipFile("Data/"+ file_name, 'r') as zipObj:
            print(f"Extracting pgn file from zip file {file_name}")
            zipObj.extractall("Data")

        print(f"Deleting {file_name}")
        os.remove("Data/" + file_name)
        

# main starts here

f = open("master_download_links.txt", "r")

all_lines = list(f.readlines())

if __name__ == '__main__':
    with Pool(15) as p:
        p.map(process_url, all_lines)

f.close()