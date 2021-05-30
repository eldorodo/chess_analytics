import requests
from multiprocessing import Pool
from zipfile import ZipFile
from converter.pgn_data import PGNData
import os

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


def pgn_to_csv(pgn_file_name):

    pgn_data = PGNData(pgn_file_name)
    result = pgn_data.export()
    result.print_summary()


# Thread function
def process_url(line_url):
    line_url = line_url.rstrip()
    line_url = line_url.lstrip()
    line_url = line_url.strip()
    last_slash_index = line_url.rfind("/")
    file_name = line_url[last_slash_index+1:]

        #continue

    print(f"Downloading {file_name}")
    download_url(line_url, file_name)

    if (file_name.endswith("zip")):

        with ZipFile(file_name, 'r') as zipObj:
            print(f"Extracting pgn file from zip file {file_name}")
            zipObj.extractall()
            print (f"deleting zip file {file_name}")
            os.remove(file_name)

    pgn_file_name = f"{file_name[:-4]}.pgn"
    print(f"pgn file name: {pgn_file_name}")

    pgn_to_csv(pgn_file_name)

    print(f"Deleting {pgn_file_name}")
    os.remove(pgn_file_name)

# main starts here

f = open("master_download_links.txt", "r")

all_lines = list(f.readlines())

if __name__ == '__main__':

    if (os.path.exists('data') == False):
        os.mkdir('data')

    with Pool(20) as p:
        p.map(process_url, all_lines)

f.close()