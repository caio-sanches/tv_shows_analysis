#Importing libs
import os
import logging
from dotenv import load_dotenv
from utils.df_processing import *
from utils.sqlserver_connection import *


logging.basicConfig(
    filename='application.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s'
)

def main():
    # Load variabels
    load_dotenv()

    # Starting script
    logging.info('Started')

    # Estabilishing connection
    sql_connection = connect_sql()

    # Importing csv files
    disney_credits = replacing_strings(importing_csv('disney_plus','credits.csv'))
    disney_titles = replacing_strings(importing_csv('disney_plus','titles.csv'))

    hbo_credits = replacing_strings(importing_csv('hbo_max','credits.csv'))
    hbo_titles = replacing_strings(importing_csv('hbo_max','titles.csv'))
    
    netflix_credits = replacing_strings(importing_csv('netflix','credits.csv'))
    netflix_titles = replacing_strings(importing_csv('netflix','titles.csv'))

    prime_credits = replacing_strings(importing_csv('prime_video','credits.csv'))
    prime_titles = replacing_strings(importing_csv('prime_video','titles.csv'))

    # Comparing dataframes and append
    credits_list = [hbo_credits, netflix_credits, prime_credits]
    final_credits = pd.DataFrame(disney_credits)
    for i in range(len(credits_list)):
        if comparing_dfs(final_credits, credits_list[i]) == True:
            final_credits = pd.concat([final_credits, credits_list[i]], ignore_index=True)
    logging.info('Credits have finished being attached')
    final_credits.rename(columns = {'name':'person_name'}, inplace = True)

    titles_list = [hbo_titles, netflix_titles, prime_titles]
    final_titles = pd.DataFrame(disney_titles)
    for i in range(len(credits_list)):
        if comparing_dfs(final_credits, credits_list[i]) == True:
            final_titles = pd.concat([final_titles, titles_list[i]], ignore_index=True)
    final_titles.rename(columns = {'type':'show_type', }, inplace = True)
    logging.info('Titles have finished being attached')

    
    # Insert into credits
    insert_into_credits(final_credits)
    insert_into_titles(final_titles)

    logging.info('Finished')


if __name__ == '__main__':
    main()
