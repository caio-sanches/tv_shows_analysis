#Importing libs
import pandas as pd
import numpy as np
import pyodbc
import os


#Input path



#Functions
def importing_df(origin, diretory):
    df = pd.read_csv(fr'{input_path}{diretory}')
    df['streaming'] = origin

    return df


def comparing_dfs(df1, df2):

    # First Test
    if df1.shape[1] == df2.shape[1]:
        result1 = True
    else:
        result1 = False


    # Second Test
    netflix_columns = df1.columns
    prime_columns = df2.columns
    result2 = np.array_equal(netflix_columns, prime_columns)

    
    # Third Test
    netflix_array_types = []
    prime_array_types = []

    for column_name in netflix_credits_df.columns:
        netflix_array_types.append(type(netflix_credits_df[column_name]))

    for column_name in prime_credits_df.columns:
        prime_array_types.append(type(prime_credits_df[column_name]))

    result3 = np.array_equal(netflix_array_types, prime_array_types)


    #Creating a list for validated tests
    results_dict = {
        'First Test': result1,
        'Second Test':result2,
        'Third Test':result3
    }

    test_list = []
    for element in results_dict:
        if results_dict[element] == False:
            test_list.append(element)
    
    if result1 == True and result2 == True and result3 == True:
        final_result = 'Datasets can be attached'
    else:
        final_result = f'Please check the tests: {test_list}'

    
    
    return final_result


def attaching_dfs(df1, df2):
    if comparing_dfs(df1, df2) == 'Datasets can be attached':
        df = df1.append(df2, ignore_index = True)

    # df.dropna(inplace=True)

    return df


def connection():    
    conn =  pyodbc.connect(
        'Driver={SQL Server};'
        'Server=LAPTOP-57CRI1KL\SQLEXPRESS;'
        'Database=tv_shows;'
        'Trusted_Connection=yes;'
    )

    return conn


def insert_into_credits(df):
    cnxn = connection()
    cursor = cnxn.cursor()
    cursor.fast_executemany = True
    
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO tv_shows.dbo.credits (person_id, id, person_name, character, role, streaming) values(?,?,?,?,?,?)", str(row.person_id), str(row.id), str(row.person_name), str(row.character), str(row.role), str(row.streaming))
    cnxn.commit()
    cursor.close()

    print("Insert was finish")


def insert_into_titles(df):
    cnxn = connection()
    cursor = cnxn.cursor()
    cursor.fast_executemany = True

    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO tv_shows.dbo.titles (id, title, show_type, description, release_year, age_certification, runtime, genres, production_countries, seasons, imdb_id, imdb_score, imdb_votes, tmdb_popularity, tmdb_score, streaming) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", str(row.id), str(row.title), str(row.show_type), str(row.description), str(row.release_year), str(row.age_certification), str(row.runtime), str(row.genres), str(row.production_countries), str(row.seasons), str(row.imdb_id), str(row.imdb_score), str(row.imdb_votes), str(row.tmdb_popularity), str(row.tmdb_score), str(row.streaming)
            )
    cnxn.commit()
    cursor.close()

    print("Insert was finish")


#Reading csv files
netflix_credits_df = importing_df('Netflix', '/netflix/credits.csv')
netflix_titles_df = importing_df('Netflix', '/netflix/titles.csv')

prime_credits_df = importing_df('Prime Video', '/prime_video/credits.csv')
prime_titles_df = importing_df('Prime Video', '/prime_video/titles.csv')

if comparing_dfs(netflix_credits_df, prime_credits_df) == 'Datasets can be attached':
    final_df = attaching_dfs(netflix_credits_df, prime_credits_df)
    final_df = final_df.rename(columns={"name": "person_name"})
    insert_into_credits(final_df)


if comparing_dfs(netflix_titles_df, prime_titles_df) == 'Datasets can be attached':
    final_df2 = attaching_dfs(netflix_titles_df, prime_titles_df)
    final_df2 = final_df2.rename(columns={"type": "show_type"})
    insert_into_titles(final_df2)
