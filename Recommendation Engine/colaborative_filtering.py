import pandas as pd
import spicy
from sklearn.metrics.pairwise import cosine_similarity


def standardize(row):
    return (row - row.mean()) / (row.max() - row.min())


def get_similar_movies(movie_name, user_rating):
    # 2.5 is the mean, not sure if this is right but it works
    similar_score = item_similarity_df[movie_name] * (user_rating - 2.5)
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score


if __name__ == '__main__':
    ratings = pd.read_csv('user_example.csv', index_col=0)
    ratings = ratings.fillna(0)

    ratings_std = ratings.apply(standardize)
    print(ratings_std)
    print('--------------------------------------------------------')

    # taking a transpose since we want similarity between items which need to be in rows
    item_similarity = cosine_similarity(ratings_std.T)
    print(item_similarity)
    print('--------------------------------------------------------')

    item_similarity_df = pd.DataFrame(item_similarity, index=ratings.columns, columns=ratings.columns)
    print(item_similarity_df)
    print('--------------------------------------------------------')

    print(get_similar_movies('romantic3', 1))
    print('--------------------------------------------------------')

    action_lover = [('action1', 5), ('romantic2', 1), ('romantic3', 1)]
    similar_movies = pd.DataFrame()
    for movie, rating in action_lover:
        similar_movies = similar_movies.append(get_similar_movies(movie, rating), ignore_index=True)
    print(similar_movies.head())
    print('--------------------------------------------------------')
    print(similar_movies.sum().sort_values(ascending=False))

""""
HOW THIS IS SUPPOSED TO WORK
This algorithm is supposed to compare the movies
of two different users, and if like similar movies 
recommend to each other movies they haven't watched yet.
Example:
    Mike likes: Avatar, Avengers, Dark Knight
    Michelangelo likes: Dark Knight, Spider-man, Avengers
then the engine should recommend Mike to watch the movie Spider-man
and Michelangelo to watch the movie Avengers, or something like that 
"""
