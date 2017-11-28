import pandas as pd
import resources.constants as constants

product_columns = ["order_id", "product_id"]


def get_train_data(nrows=None):
    order_products_train_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'order_products__train.csv'
    order_products_train_df = pd.read_csv(order_products_train_file_path, sep=',', usecols=product_columns, nrows=nrows)
    train_data = pd.merge(order_products_train_df, get_orders_df())
    return train_data[['order_hour_of_day']].values, train_data[['product_id']].values


def get_test_data(nrows=None):
    order_products_test_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'order_products__prior.csv'
    order_products_test_df = pd.read_csv(order_products_test_file_path, sep=',', usecols=product_columns, nrows=nrows)
    test_data = pd.merge(order_products_test_df, get_orders_df())
    return test_data[['order_hour_of_day']].values, test_data[['product_id']].values


def get_orders_df():
    orders_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'orders.csv'
    return pd.read_csv(orders_file_path, sep=',', usecols=["order_id", "order_hour_of_day"])
