import matplotlib.pyplot as plt
import seaborn as sns

import model.dataset_tools as tls

train_data_cross_tab_df = tls.get_train_data_cross_tab_df('aisle_id', 'order_hour_of_day')

ax = sns.heatmap(train_data_cross_tab_df)
plt.show()
