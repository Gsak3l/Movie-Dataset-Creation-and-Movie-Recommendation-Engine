import pandas as pd
import spicy
from sklearn.metrics.pairwise import cosine_similarity

if __name__ == '__main__':
    ratings = pd.read_csv('user_example.csv', index_col=0)
    print(ratings)

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
