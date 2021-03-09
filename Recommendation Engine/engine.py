import pandas as pd


def read_data():
    ratings_ = pd.read_csv('ratings.csv')
    movies_ = pd.read_csv('movies.csv')
    combined = pd.merge(movies_, ratings_).drop(['genres', 'timestamp'], axis=1)
    return combined


def drop_movies(user_ratings_):  # drop movies that have less than 10 ratings
    user_ratings_ = user_ratings_.dropna(thresh=10, axis=1).fillna(0)
    return user_ratings_


def get_similar_movies(movie_name, user_rating):
    # 2.5 is the mean, not sure if this is right but it works
    similar_score = item_similarity_df[movie_name] * (user_rating - 2.5)
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score


if __name__ == '__main__':
    ratings = read_data()
    user_ratings = ratings.pivot_table(index=['userId'], columns=['title'], values='rating')
    user_ratings = drop_movies(user_ratings)
    item_similarity_df = user_ratings.corr(method='pearson')

    random_user = [('300 (2007)', 5), ('8MM (1999)', 1), ('13th Warrior, The (1999)', 1)]
    similar_movies = pd.DataFrame()
    for movie, rating in random_user:
        similar_movies = similar_movies.append(get_similar_movies(movie, rating), ignore_index=True)
    print(similar_movies.head())
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
