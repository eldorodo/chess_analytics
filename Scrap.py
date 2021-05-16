from autoscraper import AutoScraper
import pandas as pd
from multiprocessing.pool import ThreadPool as Pool
# from multiprocessing import Pool
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

file_name  = "Container_chess_analytics"
"Data_for_blob/live_ratings.csv"





def upload_to_blob(container_name,upload_file_path,file_name,create_blob = False):
    
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    #connect_str="DefaultEndpointsProtocol=https;AccountName=chessstorage101;AccountKey=hDD9/P7bxlbK38oMxA2eec7dgPwJ1BI+FGVNT57KmFaRgwkzGK94NBuAspza/+nJkpJhCGjvIgviQrr9AhEzrg==;EndpointSuffix=core.windows.net"
    
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    if(create_blob):        
        container_client = blob_service_client.create_container(container_name)


    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + file_name)
    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data,overwrite = True)
        
    print("**completed**")



scraper=AutoScraper()
scraper.load('top-chess-players')
base_url = url="https://www.chess.com/ratings"

df = pd.DataFrame(None,columns=["Name","Classical", "Rapid", "Blitz"])
for i in range(1,6):
    new_url= base_url + "?page=" + str(i)
    this_page_data = pd.DataFrame(scraper.get_result_similar(new_url,group_by_alias=True))
    df = df.append(this_page_data,ignore_index=True)

print(df.head(100))

pool_size = 4  # your "parallelness"

scraper=AutoScraper()   
base_url="https://www.chess.com/games"
scraper.load('list-of-top-players')
list_of_top_players = []

new_url = []
for i in range(1,50):
    new_url.append(base_url + "?page=" + str(i))

# define worker function before a Pool is instantiated
def worker(item):
    try:
        list_of_top_players.extend(list(scraper.get_result_similar(item)))
    except:
        print('error with item')

pool = Pool(pool_size)

for item in new_url:
    pool.apply_async(worker, (item,))

pool.close()
pool.join()

df.to_csv("Data_for_blob/live_ratings.csv")

upload_to_blob("containercchessnalytics","Data_for_blob/live_ratings.csv","live_ratings.csv")
               
#file_name = "live_ratings.csv"
#container_name = "containercchessnalytics"
#upload_file_path = "Data_for_blob/live_ratings.csv"

