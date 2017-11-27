import pandas as pd
import resources.constants as constants


def get_train_data():
    order_products_train_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'order_products__train.csv'
    order_products_train_df = pd.read_csv(order_products_train_file_path, sep=',', usecols=["order_id", "product_id"])
    return pd.merge(order_products_train_df, get_orders_df())


def get_test_data():
    order_products_test_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'order_products__prior.csv'
    order_products_test_df = pd.read_csv(order_products_test_file_path, sep=',', usecols=["order_id", "product_id"])
    return pd.merge(order_products_test_df, get_orders_df())


def get_orders_df():
    orders_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'orders.csv'
    return pd.read_csv(orders_file_path, sep=',', usecols=["order_id", "order_hour_of_day"])
