import pandas as pd
import os

this_dir = os.getcwd()
DATA = os.path.join(this_dir, 'data', 'winemag-data-130k-v2.csv')
grape_synonyms = {'sauvignon blanc': ['sauvignon'],
                  'syrah': ['shiraz'], 'pinot gris': ['pinot grigio']}


class WineMagDataProcessor():
    def __init__(self):
        self.raw_data = pd.DataFrame()
        self.clean_data = pd.DataFrame()

    def load_data(self, source):
        '''Load data from source csv into a pandas dataframe.
        Do some minimal processing like drop duplicates'''
        df = pd.read_csv(source, index_col=0)
        self.raw_data = df
        print('Loaded data from: '+str(source))

    def perform_all_cleans(self):
        '''Sequentially apply all data cleaning steps'''
        self.dedup()
        self.snobby_rename_columns()
        self.match_grape_names(grape_synonyms)

    def dedup(self):
        '''Drop duplicates'''
        old = self.raw_data
        new = old.drop_duplicates()
        self.clean_data = new

        print('Removed duplicates, dataframe shape change from\
        '+str(old.shape)+' to '+str(new.shape))

    def snobby_rename_columns(self):
        '''The original dataset calls "varietal"
        "variety" and it bugs me'''
        try:
            self.clean_data.rename(
                columns={'variety': 'varietal'}, inplace=True)
            print('Renamed variety to varietal')
        except Exception:
            print('Maybe you shouldn\'t have been such a snob,: '
                  + str(Exception))

    def match_grape_names(self, grape_dict):
        '''Some grape names are confused to be separate grapes
        while they are actually the same grapes.
        We match them together here.
        Expecting match_list to be a dict:
        {"canon" name you want:[list of synonyms]}'''
        for grape, synonyms in grape_dict.items():
            for synonym in synonyms:
                self.clean_data['varietal'] = self.clean_data['varietal'].map(
                    lambda name: grape if name == synonym else name
                )
                print('Renamed '+synonym+' to '+grape)

    def create_class(self, char_list):
        """Combine arbitrary list of wordy characteristics
        to form a class.
        The combined characteristics will then be called 'class'"""
        pass
