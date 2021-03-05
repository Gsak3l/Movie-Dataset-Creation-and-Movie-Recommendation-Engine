from data import save_data, load_data, save_json_data, load_json_data, \
    save_data_pickle, load_data_pickle, save_data_csv, load_data_csv

if __name__ == '__main__':
    save_json_data('disney_movie_data_cleaned_with_scores.json')
    save_data_pickle('disney_movie_data_cleaned_with_scores.pickle')
    save_data_csv('disney_movie_data_cleaned_with_scores.csv')
