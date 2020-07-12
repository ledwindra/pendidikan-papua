import matplotlib.pyplot as plt
import pandas as pd
import re
import seaborn as sns
from bs4 import BeautifulSoup
from functools import reduce
from json import load


class DataFrame:

    def __init__(self, nrows):
        self.nrows = nrows

    def get_columns(self):
        """
        Returns the list of columns for each region level.
        """
        with open('./util/columns.json', 'r') as f:
            columns = load(f)

        return columns

    def get_subdistrict(self, columns, identifier='sekolah_id_enkrip'):
        """
        Returns the DataFrame for subdistrict/kecamatan.
        """
        df = pd.read_csv('./data/subdistrict.csv', header=None, nrows=self.nrows)
        df.columns = columns['subdistrict']
        df[identifier] = df.apply(
            lambda x: x[identifier].replace(' ', ''), axis=1
        )

        return df

    def get_school(self, columns):
        """
        Returns the DataFrame for school level.
        """
        df = pd.read_csv('./data/school.csv', header=None, nrows=self.nrows)
        df.columns = columns['school']

        return df

    def get_school_profile(self, columns):
        """
        Returns the DataFrame for school profile.
        """
        df = pd.read_csv('./data/school-profile.csv', header=None, nrows=self.nrows)
        df.columns = columns['school_profile']

        return df

    def is_papua(self, df):
        """
        Returns the DataFrame with an added column that tells True if the province
        is either Papua or West Papua. Otherwise it will be False.
        """
        df['is_papua'] = df.apply(
            lambda x: (
                x['induk_provinsi'] == 'Prov. Papua'
            ) | (
                x['induk_provinsi'] == 'Prov. Papua Barat'
            ), axis=1
        )

        return df

    def recode_province(self, df):
        """
        Returns values to code a province.
            - 1 = Papua or West Papua
            - 2 = Other than 1.
        """
        if (
            df['induk_provinsi'] == 'Prov. Papua'
        ) | (
            df['induk_provinsi'] == 'Prov. Papua Barat'
        ):
            return 'Papua or West Papua'
        else:
            return 'Non-Papua'

    def apply_recode_province(self, df):
        """
        Recodes provinces to the DataFrame.
        """
        df['groups'] = df.apply(self.recode_province, axis=1)
        groups_num = {'Papua or West Papua': 1, 'Non-Papua': 2}
        df = df.replace({'groups': groups_num})

        return df

    def content(self):
        """
        Returns the cleaned DataFrame.
        """
        columns = self.get_columns()
        dfs = [
            self.get_subdistrict(columns),
            self.get_school(columns),
            self.get_school_profile(columns)
        ]
        df = reduce(lambda left, right: pd.merge(left, right, on='sekolah_id_enkrip'), dfs)
        df = self.is_papua(df)
        df = self.apply_recode_province(df)

        return df

class Calculation:

    def get_aggregation(self, data, column_agg, aggregation):
        """
        Returns an aggregation.
        Args:
            - data = specifiy the name of the data
            - column_agg = specifiy which to column to aggregate
            - aggregation = specifiy which kind of aggregation (e.g. mean, median)
        """
        mean = data.groupby('groups')[column_agg].agg(aggregation).reset_index()

        return mean

    def get_count(
        self,
        data,
        column_name,
        column_count,
        value,
        identifier='sekolah_id_enkrip'
    ):
        """
        Returns total count by groups.
        Args:
            - data = specifiy the name of the data
            - column_name = column name to be assigned
            - column_count = column name to be counted
            - value = value that needs to be counted
            - identifier = unique identifier in the dataframe (default = sekolah_id_enkrip)
        """
        data[column_name] = data.apply(
            lambda col: col[column_count] == value, axis=1
        )
        count = data.groupby(['groups', column_name])[identifier]\
            .agg('count')\
            .to_frame()\
            .reset_index()

        return count
    
    def get_categorical(
        self,
        data,
        column_name,
        value
    ):
        return data.apply(lambda x: x[column_name] == value, axis=1)
    
    def get_count_categorical(
        self,
        data,
        column_name
    ):
        return data.groupby(['groups', column_name])['sekolah_id_enkrip']\
            .agg('count')\
            .to_frame()\
            .reset_index()

    def get_percentage(self, data, column_pct):
        """
        Returns the grouped percentage values for a specified column.
        Args:
            - data = specifiy the name of the data
            - column_pct = column name that needs to be counted
        """
        papua = {
            'groups': 'Papua',
            f'{column_pct}_pct': len(data[(data['groups'] == 1) & (data[column_pct] == True)]) / len(data[data['groups'] == 1])
        }
        non_papua = {
            'groups': 'Non-Papua',
            f'{column_pct}_pct': len(data[(data['groups'] == 2) & (data[column_pct] == True)]) / len(data[data['groups'] == 2])
        }
        
        return pd.DataFrame([papua, non_papua])

class Visualization(Calculation):

    def get_bar(
        self,
        data,
        column_agg,
        aggregation,
        title,
        groups=['Papua', 'Non-Papua']
    ):
        """
        Produce a bar chart from an aggregation.
        """
        ax = sns.catplot(
            x=groups,
            y=column_agg,
            data=self.get_aggregation(data, column_agg, aggregation),
            kind='bar'
        )
        ax.set(
            xlabel='',
            ylabel='',
            title=title
        )
    
    def get_multiple_bar(
        self,
        df,
        metrics,
        aggregation,
        title
    ):
        """
        Produce multiple bar charts one at a time.
        """
        data = list(set((df[metrics])))
        data = [str(x) for x in data]
        data = sorted(data)
        data = dict(zip(data, data))
        data = dict((re.sub(' |\/', '_', key).lower(), value) for (key, value) in data.items())
        for key, value in data.items():
            if key != 'nan':
                df[key] = df.apply(lambda x: x[metrics] == value, axis=1)
                data = df.groupby(['groups', key])['sekolah_id_enkrip'].agg('count').to_frame().reset_index()
                self.get_bar(self.get_percentage(df, key), f'{key}_pct', aggregation, f'{title}: {value}')
