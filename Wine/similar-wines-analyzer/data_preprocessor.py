import pandas as pd 
import os

this_dir = os.getcwd()
DATA = os.path.join(this_dir,'data','winemag-data-130k-v2.csv')

def load_and_clean_data(source):
    '''Load data from source csv into a pandas dataframe.
    Do some minimal processing like drop duplicates'''
    df = pd.read_csv(source, index_col=0)
    print('Loaded data from: '+str(source))

    old_shape = df.shape
    df = df.drop_duplicates()
    new_shape = df.shape

    print('Removed duplicates, dataframe shape change from\
     '+str(old_shape)+' to '+str(new_shape))
    return df

def rename_columns(df):
    '''The original dataset calls "varietal"
    "variety" and it bugs me'''
    try:
        df.rename(columns={'variety': 'varietal'}, inplace=True)
    except Exception:
        print('Maybe you shouldn\'t have been such a snob,: '
        +str(Exception))

def match_grape_names(df, grape_dict):
    '''Some grape names are confused to be separate grapes
    while they are actually the same grapes.
    We match them together here.
    Expecting match_list to be a dict:
    {"canon" name you want:[list of synonyms]}'''
    for grape, synonyms in grape_dict.items():
        for synonym in synonyms:
            df['varietal'] = df['varietal'].map(
                lambda name: grape if name == synonym else name
            )

def group_by_characteristics(df, char_list):
    """Group by arbitrary list of wordy characteristics.
    The combined characteristics will then be called 'class'"""
    

    