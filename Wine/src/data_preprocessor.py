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
        print(f'Loaded data from: {source}')

    def perform_all_cleans(self):
        '''Sequentially apply all data cleaning steps'''
        deduped = self.dedup(self.raw_data)
        renamed = self.snobby_rename_columns(deduped)
        grape_renamed = self.match_grape_names(renamed, grape_synonyms)
        return grape_renamed

    def dedup(self, raw_data):
        '''Drop duplicates'''
        deduped = raw_data.drop_duplicates()

        print(f'Removed duplicates, dataframe shape change from\
              {raw_data.shape} to {deduped.shape}')
        return deduped

    def snobby_rename_columns(self, raw_data):
        '''The original dataset calls "varietal"
        "variety" and it bugs me'''
        try:
            renamed = raw_data.rename(
                columns={'variety': 'varietal'})
            print('Renamed variety to varietal')
            return renamed
        except Exception:
            print(f'Maybe you shouldn\'t have been such a snob, error: \
                  {Exception}')

    def replace_name_with_synonyms(self, name, synonym_dict):
        '''Helper for match_grape_names'''
        for grape, synonyms in synonym_dict.items():
            for synonym in synonyms:
                if name == synonym:
                    print(f'Renamed {synonym} to {grape}')
                    return grape
        return name

    def match_grape_names(self, raw_data, grape_dict):
        '''Some grape names are confused to be separate grapes
        while they are actually the same grapes.
        We match them together here.
        Expecting match_list to be a dict:
        {"canon" name you want:[list of synonyms]}'''
        renamed = raw_data.copy()
        renamed['varietal'] = raw_data['varietal'].apply(
            self.replace_name_with_synonyms, synonym_dict=grape_dict)
        return renamed

    def create_class(self, raw_data, char_list):
        """Combine arbitrary list of wordy characteristics
        to form a class.
        The combined characteristics will then be called 'class'"""
        classed = raw_data.copy()

        # initiate column with empty string
        classed['class'] = ''
        for col in char_list:
            classed['class'] = classed['class'] + ' ' + raw_data[col]
        return classed
