import os
import pandas as pd
import resources.constants as constants

os.chdir("..")

orders_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'orders.csv'
orders_df = pd.read_csv(orders_file_path, sep=',', usecols=["order_id", "order_hour_of_day"])

order_products_train_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'order_products__train.csv'
order_products_train_df = pd.read_csv(order_products_train_file_path, sep=',', usecols=["order_id", "product_id"])

train_data = pd.merge(order_products_train_df, orders_df)
