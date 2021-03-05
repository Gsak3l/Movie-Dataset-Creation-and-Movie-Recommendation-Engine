import pandas as pd



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
