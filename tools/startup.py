import tarfile
import os

from pathlib import Path

DATA_SET_ARCHIVE_FILE_NAME = "instacart_online_grocery_shopping_2017_05_01.tar.gz"
DATA_SET_DIRECTORY_NAME = "instacart_2017_05_01"

os.chdir("..")
if Path(DATA_SET_DIRECTORY_NAME).is_dir():
    print("The data set has been already extracted.")
elif Path(DATA_SET_ARCHIVE_FILE_NAME).is_file():
    print("The data set archive has not been extracted yet.")
    print("Extracting the archive...")
    tarfile = tarfile.open(DATA_SET_ARCHIVE_FILE_NAME, "r:gz")
    tarfile.extractall(".")
else:
    print("The date set archive is not downloaded! Please, do it manually.")
