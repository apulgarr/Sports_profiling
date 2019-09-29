import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split


def knn_classifier(data_path):
    data = pd.read_csv(data_path)
    x_data = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
    y_data = data['Species']

    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.3)

    knn_model = KNeighborsClassifier(n_neighbors = 5)
    knn_model.fit(x_train, y_train)

    predicted_values = knn_model.predict(x_test)

    print(accuracy_score(predicted_values, y_test))
    print(confusion_matrix(predicted_values, y_test))
    print(classification_report(predicted_values, y_test))


knn_classifier('Iris.csv')
