import pandas as pd
import numpy as np
import os


def importing_csv(origin, file_name):
    """This function import csv and transform in a dataframe"""
    diretory = './data_files'
    df = pd.read_csv(fr'{diretory}/{origin}/{file_name}')
    df['streaming'] = origin
    
    return df


def replacing_strings(df):
    """This function it suits to treat some strings erros"""
    df = df.replace('\t', '', regex=True)
    df = df.replace('\;', ' ', regex=True)
    df = df.replace('\n;', ' ', regex=True)
    df = df.replace('\n;', ' ', regex=True)
    df = df.replace('\\n', ' ', regex=True)
    df = df.replace('\s', ' ', regex=True)

    return df


def comparing_dfs(df1, df2):
    """This functionscompares the dataframes to see if they can be appended"""
    
    # Testing if number of columns are equal
    if df1.shape[1] == df2.shape[1]:
        result1 = True
    else:
        result1 = False

    # Testing if columns have the same name
    df1_columns = df1.columns
    df2_columns = df2.columns
    result2 = np.array_equal(df1_columns, df2_columns)

    # Testing if columns are the same data dtype
    df1_array_types = []
    df2_array_types = []

    for column_name in df1.columns:
        df1_array_types.append(type(df1[column_name]))

    for column_name in df2.columns:
        df2_array_types.append(type(df2[column_name]))

    result3 = np.array_equal(df1_array_types, df2_array_types)

    # Creating a dict for validated tests
    results_dict = {
        'First Test': result1,
        'Second Test': result2,
        'Third Test': result3
    }

    test_list = []
    for element in results_dict:
        if results_dict[element] == False:
            test_list.append(element)

    if result1 == True and result2 == True and result3 == True:
        final_result = True
    else:
        final_result = f'Please check the tests: {test_list}'
    

    return final_result