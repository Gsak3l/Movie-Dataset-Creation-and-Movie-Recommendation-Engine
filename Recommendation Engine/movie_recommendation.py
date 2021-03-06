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


def recommend_movies(movie_, df_):
    df_ = pd.read_csv('../Data Collected/many_movies_dataset.csv')

    features = ['keywords', 'cast', 'genres', 'director']
    for feature in features:
        df_[feature] = df_[feature].fillna('')  # cleaning up some data

    df_['combined_features'] = df_.apply(combined_features, axis=1)
    print(df_['combined_features'])

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df_['combined_features'])
    cosine_sim = cosine_similarity(count_matrix)

    movie_index = get_index_from_title(movie_)  # aye aye aye, aye aye aye, fuego
    similar_movies = list(enumerate(cosine_sim[movie_index]))

    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

    i = 0
    for element in sorted_similar_movies:
        if i != 0:
            print(get_title_from_index(element[0]))
        if i >= 10:
            break
        i += 1


if __name__ == '__main__':
    df = pd.read_csv('../Data Collected/many_movies_dataset.csv')
    movie = input('Type a movie that you enjoy watching:')
    recommend_movies(movie, df)

""""
HOW THIS WORKS
This algorithm basically asks the user to type a movie
that he liked, and then compares the description, genre, cast and director of this
movie, with all the other movies in the csv file (about 4000).
"""
