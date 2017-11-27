import tarfile
import os
import resources.constants as constants

from pathlib import Path

os.chdir("..")
if Path(constants.DATA_SET_DIRECTORY_NAME).is_dir():
    print("The data set has been already extracted.")
elif Path(constants.DATA_SET_ARCHIVE_FILE_NAME).is_file():
    print("The data set archive has not been extracted yet.")
    print("Extracting the archive...")
    tarfile = tarfile.open(constants.DATA_SET_ARCHIVE_FILE_NAME, "r:gz")
    tarfile.extractall(".")
else:
    print("The data set archive is not downloaded!")
    print("Please, get it manually from https://www.instacart.com/datasets/grocery-shopping-2017.")
