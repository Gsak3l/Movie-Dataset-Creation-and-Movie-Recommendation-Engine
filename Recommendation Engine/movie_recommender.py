import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]


def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


def combined_features(row):
    try:  # getting a float somewhere
        return row['keywords'] + ' ' + row['cast'] + ' ' + row['genres'] + ' ' + row['director']
    except:
        print('Error', row)


if __name__ == '__main__':
    df = pd.read_csv('../Data Collected/many_movies_dataset.csv')

    features = ['keywords', 'cast', 'genres', 'director']
    for feature in features:
        df[feature] = df[feature].fillna('')  # cleaning up some data

    df['combined_features'] = df.apply(combined_features, axis=1)
    print(df['combined_features'])

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['combined_features'])
    cosine_sim = cosine_similarity(count_matrix)

    movie_index = get_index_from_title('Avatar')  # aye aye aye, aye aye aye, fuego
    similar_movies = list(enumerate(cosine_sim[movie_index]))

    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

    i = 0
    for movie in sorted_similar_movies:
        if i != 0:
            print(get_title_from_index(movie[0]))
        if i >= 10:
            break
        i += 1
