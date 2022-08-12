import logging
import os
import pyodbc

def connect_sql():
    driver = os.getenv('DRIVER_SQL')
    host = os.getenv('SERVER_SQL')
    db = os.getenv('DATABASE_SQL')
    
    try:
        conn =  pyodbc.connect(
            f'Driver={driver};'
            f'Server={host};'
            f'Database={db};'
            'Trusted_Connection=yes;'
        )
        logging.info("Connection succeeded")
        return conn
    except pyodbc.Error as err:
        sqlstate = err.args[1]
        logging.error(sqlstate)


def insert_into_credits(df):
    cnxn = connect_sql()
    cursor = cnxn.cursor()
    cursor.fast_executemany = True

    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO tv_shows.dbo.credits (person_id, id, person_name, character, role, streaming) values(?,?,?,?,?,?)", str(row.person_id), str(row.id), str(row.person_name), str(row.character), str(row.role), str(row.streaming)
        )
    cnxn.commit()
    cursor.close()


def insert_into_titles(df):
    cnxn = connect_sql()
    cursor = cnxn.cursor()
    cursor.fast_executemany = True

    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO tv_shows.dbo.titles (id, title, show_type, description, release_year, age_certification, runtime, genres, production_countries, seasons, imdb_id, imdb_score, imdb_votes, tmdb_popularity, tmdb_score, streaming) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", str(row.id), str(row.title), str(row.show_type), str(row.description), str(row.release_year), str(row.age_certification), str(row.runtime), str(row.genres), str(row.production_countries), str(row.seasons), str(row.imdb_id), str(row.imdb_score), str(row.imdb_votes), str(row.tmdb_popularity), str(row.tmdb_score), str(row.streaming)
            )
    cnxn.commit()
    cursor.close()