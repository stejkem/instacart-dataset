import os

import pandas as pd

import resources.constants as constants

PRODUCT_COLUMNS = ["order_id", "product_id"]

os.chdir("..")


def get_train_data(selected_feature, selected_label, nrows=None):
    order_products_train_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'order_products__train.csv'
    order_products_train_df = pd.read_csv(order_products_train_file_path, sep=',', usecols=PRODUCT_COLUMNS, nrows=nrows)
    train_data_df = pd.merge(order_products_train_df, get_products_df())
    train_data_df = pd.merge(train_data_df, get_orders_df())
    return train_data_df[[selected_feature]].values, train_data_df[[selected_label]].values


def get_train_data_cross_tab_df(selected_feature, selected_label, nrows=None):
    order_products_train_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'order_products__train.csv'
    order_products_train_df = pd.read_csv(order_products_train_file_path, sep=',', usecols=PRODUCT_COLUMNS, nrows=nrows)
    train_data_df = pd.merge(order_products_train_df, get_products_df())
    train_data_df = pd.merge(train_data_df, get_orders_df())
    return pd.crosstab(index=train_data_df[selected_label], columns=train_data_df[selected_feature])


def get_test_data(selected_feature, selected_label, nrows=None):
    order_products_test_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'order_products__prior.csv'
    order_products_test_df = pd.read_csv(order_products_test_file_path, sep=',', usecols=PRODUCT_COLUMNS, nrows=nrows)
    test_data_df = pd.merge(order_products_test_df, get_products_df())
    test_data_df = pd.merge(test_data_df, get_orders_df())
    return test_data_df[[selected_feature]].values, test_data_df[[selected_label]].values


def get_orders_df():
    orders_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'orders.csv'
    return pd.read_csv(orders_file_path, sep=',', usecols=["order_id", "order_hour_of_day"])


def get_products_df():
    products_file_path = constants.DATA_SET_DIRECTORY_NAME + "/" + 'products.csv'
    return pd.read_csv(products_file_path, sep=',', usecols=["product_id", "product_name", "aisle_id", "department_id"])
