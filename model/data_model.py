import os
import model.dataset_tools as tl

os.chdir("..")

test_data = tl.get_test_data()
train_data = tl.get_train_data()

print("The data set has been processed.")
