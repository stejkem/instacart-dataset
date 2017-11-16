import urllib.request
import tarfile
import os

from pathlib import Path

URL_FOR_DATA_SET = open("dataset_url.txt", "r").read()
DATA_SET_ARCHIVE_FILE_NAME = "instacart_online_grocery_shopping_2017_05_01.tar.gz"

data_set_directory = Path("instacart_2017_05_01")
data_set_archive = Path(DATA_SET_ARCHIVE_FILE_NAME)

os.chdir("..")
if data_set_directory.is_dir():
    print("The data set has been already extracted.")
else:
    if data_set_archive.is_file():
        print("The data set archive has been already downloaded.")
        print("Extracting the archive...")
        tarfile = tarfile.open(DATA_SET_ARCHIVE_FILE_NAME, "r:gz")
        tarfile.extractall(".")
        print("Extraction is completed!")
    else:
        print("The data set archive has not been downloaded yet.")
        print("Downloading the archive...")
        print("The approximate size is 200MB...")
        urllib.request.urlretrieve(URL_FOR_DATA_SET, filename=DATA_SET_ARCHIVE_FILE_NAME)
        print("Download is completed!")
