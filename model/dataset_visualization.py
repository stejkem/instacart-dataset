import matplotlib.pyplot as plt
import seaborn as sns

import model.dataset_tools as tls


def draw_heat_map():
    train_data_cross_tab_df = tls.get_train_data_cross_tab_df('aisle_id', 'order_hour_of_day', 10000)
    df_norm_col = (train_data_cross_tab_df - train_data_cross_tab_df.mean()) / train_data_cross_tab_df.std()
    sns.heatmap(df_norm_col, cmap='viridis')
    plt.show()
