'''
A Library of useful pandas helper functions
SOLUTION FILE!!!!
'''
import pandas as pd

def get_column_names(df : pd.DataFrame) -> list[str]:
    '''
    Get all column names of a pandas dataframe df
    Returns the names as a list of string
    '''
    return list(df.columns)


def get_columns_of_type(df : pd.DataFrame, numpy_type: any) -> list[str]:
    '''
    Return the column names of a pandas dataframe only when 
    the values in the column match the numpy_type
    '''
    return [col for col in df.columns if df[col].dtype == numpy_type]


def get_unique_values(df : pd.DataFrame, column_name: str) -> list:
    '''
    Get a list of unique values of a column in a pandas dataframe
    '''
    if column_name in df.columns:
        return df[column_name].dropna().unique().tolist()
    return []

def get_file_extension(file_path : str) -> str:
    '''
    Return the file extension of a file_path for example:
    '/some/file/data.csv' -> 'csv'
    '/home/important_grades.xlsx' -> 'xlsx'
    'countries.json' -> 'json'

    '''
    return file_path.split('.')[-1].lower()

def load_file(file, file_type: str) -> pd.DataFrame:
    '''
    Load a file into a pandas dataframe assumed the file type from the extension
    return a pandas dataframe
    only suppose csv, excel and json file extensions
    - when csv assume first row is header
    - when json assume record-oriented data
    '''
    if file_type == 'csv':
        return pd.read_csv(file)
    elif file_type == 'xlsx':
        return pd.read_excel(file)
    elif file_type == 'json':
        return pd.read_json(file, orient="records")
    else:
        raise ValueError("Unsupported file type. Use CSV, XLSX, or JSON.")

if __name__ == '__main__':
    df = pd.DataFrame({ 
        "name": ["Alice", "Bob", "Chris", "Dee", "Eddie", "Fiona"],
        "age": [25, 30, 35, 40, 45, 50],
        "state": ["NY", "PA", "NY", "NY", "PA", "NJ"],
        "balance": [100.0, 200.0, 250.0, 310.0, 100.0, 60.0]
        })
    cols = get_column_names(df)
    print(f"Columns: {cols}")
    cols = get_columns_of_type(df, 'object')
    print(f"Object Columns: {cols}")
    cols = get_columns_of_type(df, 'int64')
    print(f"Int64 Columns: {cols}")
    cols = get_columns_of_type(df, 'float64')
    print(f"Float64 Columns: {cols}")
    unique = get_unique_values(df, 'state')
    print(f"Unique States: {unique}")





    # solution pandaslib.py