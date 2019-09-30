import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split

def classifiers(data_path):
    data = pd.read_csv(data_path)

    x_data = data['text_string']
    y_data = data['sport']

    count_vect = CountVectorizer()
    x_data = count_vect.fit_transform(x_data)
    tf_transformer = TfidfTransformer(use_idf=False).fit(x_data)
    x_data = tf_transformer.transform(x_data)

    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.3, random_state=42)

    knn_model = KNeighborsClassifier(n_neighbors = 15)
    knn_model.fit(x_train, y_train)

    naives_model = MultinomialNB()
    naives_model.fit(x_train, y_train)

    predicted_values_knn = knn_model.predict(x_test)
    predicted_values_naives = naives_model.predict(x_test)

    print("KNN SUMARY")
    print(accuracy_score(predicted_values_knn, y_test))
    print(confusion_matrix(predicted_values_knn, y_test))
    print(classification_report(predicted_values_knn, y_test))


    print("NAIVES SUMMARY")
    print(accuracy_score(predicted_values_naives, y_test))
    print(confusion_matrix(predicted_values_naives, y_test))
    print(classification_report(predicted_values_naives, y_test))


classifiers('../data_set_tweets/cleaned_tweets.csv')
