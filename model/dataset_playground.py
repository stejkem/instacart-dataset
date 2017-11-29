from sklearn.naive_bayes import GaussianNB
import model.dataset_tools as tls

train_order_hour_of_day, train_product_id = tls.get_train_data(10000)
tls.plot_data(train_product_id, train_order_hour_of_day)

# clf = GaussianNB()
# # clf.fit(train_order_hour_of_day, train_product_id.ravel())
# print("The model is ready.")
#
# test_order_hour_of_day, test_product_id = tls.get_test_data(1000)
# print("The current model's score is", clf.score(test_order_hour_of_day, test_product_id))
