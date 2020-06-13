import argparse
import glob
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from json import load
from multiprocessing import Pool
from random import randint

class Dapodik:

    def __init__(
        self,semester_id,
        url, 
        headers,
        timeout,
        columns
    ):
        self.semester_id = semester_id
        self.url = url
        self.headers = headers
        self.timeout = timeout
        self.columns = columns

    def get_target_list(
        self,
        source_file_name,
        source_columns,
        source_identifier,
        target_file_name,
        target_columns,
        target_identifier
    ):
        # read source file
        source = pd.read_csv(
            f'./data/{source_file_name}.csv',
            dtype=object,
            header=None
        )
        source.columns = source_columns
        source[source_identifier] = source.apply(
            lambda x: x[source_identifier].replace(' ', ''), axis=1
        )

        # if target file exists, read it
        # if there is any match between source & target IDs, remove it
        # the output list should be either:
        #   1. a list of unmatched IDs
        #   2. an empty list (if target file doesn't exist)
        if os.path.exists(f'./data/{target_file_name}.csv'):
            target = pd.read_csv(
                f'./data/{target_file_name}.csv',
                dtype=object,
                header=None
            )
            target.columns = target_columns
            target[target_identifier] = target.apply(
                lambda x: x[target_identifier].replace(' ', ''), axis=1
            )
            matched = source[source_identifier].isin(target[target_identifier])
            df = source[~matched].copy()
            target_id = [x for x in df[source_identifier]]
        else:
            target_id = []
        
        return target_id

    def get_all(self, target_columns):
        all_url = self.url \
            + f'progres?id_level_wilayah=0&semester_id={self.semester_id}'
        status_code = None
        while status_code != 200:
            try:
                response = requests.get(
                    all_url,
                    headers=self.headers,
                    timeout=self.timeout
                )
                status_code = response.status_code
                df = pd.DataFrame(response.json())
                df = df[self.columns['all']]
                df.to_csv(
                    './data/all.csv',
                    index=False,
                    header=False
                )
            except requests.exceptions.SSLError:
                continue
            except requests.exceptions.ConnectTimeout:
                continue
            except requests.exceptions.ReadTimeout:
                continue
            except requests.exceptions.ConnectionError:
                continue
    
    def get_province(self, i, target_columns):
        print(f'Upcoming province ID: {i}')
        province_url = self.url \
            + f'progres?&id_level_wilayah=1&kode_wilayah={i}' \
            + f'&semester_id={self.semester_id}'
        status_code = None
        while status_code != 200:
            try:
                response = requests.get(
                    province_url,
                    headers=self.headers,
                    timeout=self.timeout
                )
                status_code = response.status_code
                df = pd.DataFrame(response.json())
                df = df[self.columns['province']]
                df.to_csv(
                    './data/province.csv',
                    index=False,
                    mode='a',
                    header=False
                )
            except requests.exceptions.SSLError:
                continue
            except requests.exceptions.ConnectTimeout:
                continue
            except requests.exceptions.ReadTimeout:
                continue
            except requests.exceptions.ConnectionError:
                continue

    def get_district(self, i, target_columns):
        print(f'Upcoming district ID: {i}')
        district_url = self.url \
            + f'progres?&id_level_wilayah=2&kode_wilayah={i}' \
            + f'&semester_id={self.semester_id}'
        status_code = None
        while status_code != 200:
            try:
                response = requests.get(
                    district_url,
                    headers=self.headers,
                    timeout=self.timeout
                )
                status_code = response.status_code
                df = pd.DataFrame(response.json())
                df = df[self.columns['district']]
                df.to_csv(
                    './data/district.csv',
                    index=False,
                    mode='a',
                    header=False
                )
            except requests.exceptions.SSLError:
                continue
            except requests.exceptions.ConnectTimeout:
                continue
            except requests.exceptions.ReadTimeout:
                continue
            except requests.exceptions.ConnectionError:
                continue

    def get_subdistrict(self, i, target_columns):
        print(f'Upcoming subdistrict ID: {i}')
        subdistrict_url = self.url \
            + f'progresSP?id_level_wilayah=3&semester_id={self.semester_id}' \
            + f'&kode_wilayah={i}'
        status_code = None
        while status_code != 200:
            try:
                response = requests.get(
                    subdistrict_url,
                    headers=self.headers,
                    timeout=self.timeout
                )
                status_code = response.status_code
                df = pd.DataFrame(response.json())
                df = df[self.columns['subdistrict']]
                df.to_csv(
                    './data/subdistrict.csv',
                    index=False,
                    mode='a',
                    header=False
                )
            except requests.exceptions.SSLError:
                continue
            except requests.exceptions.ConnectTimeout:
                continue
            except requests.exceptions.ReadTimeout:
                continue
            except requests.exceptions.ConnectionError:
                continue

    def get_school(self, i, target_columns):
        print(f'Upcoming school ID: {i}')
        school_url = self.url + f'sekolahDetail?sekolah_id={i}'
        status_code = None
        while status_code != 200:
            try:
                response = requests.get(
                    school_url,
                    headers=self.headers,
                    timeout=self.timeout
                )
                status_code = response.status_code
                df = pd.DataFrame(response.json())
                df['sekolah_id_enkrip'] = i
                df = df[self.columns['school']]
                df.to_csv(
                    './data/school.csv',
                    index=False,
                    mode='a',
                    header=False
                )
            except requests.exceptions.SSLError:
                continue
            except requests.exceptions.ConnectTimeout:
                continue
            except requests.exceptions.ReadTimeout:
                continue
            except requests.exceptions.ConnectionError:
                continue

    def get_school_profile(self, i):
        print(f'Upcoming school ID: {i}')
        school_url = f'https://dapo.dikdasmen.kemdikbud.go.id/sekolah/{i}'
        status_code = None
        while status_code != 200:
            try:
                response = requests.get(
                    school_url,
                    headers=self.headers,
                    timeout=self.timeout
                )
                status_code = response.status_code
                content = BeautifulSoup(
                    response.content,
                    features='html.parser'
                )
                profile_usermenu = content.find(
                    'div',
                    {'class': 'profile-usermenu'}
                )
                identitas_sekolah = content.find(
                    'div',
                    id='myTabContent').find_all(
                        'div',
                        {'class': 'panel-body'}
                    )[0]
                data_rinci = content.find(
                    'div',
                    id='myTabContent').find_all(
                        'div',
                        {'class': 'panel-body'}
                    )[2]
                df = pd.DataFrame([{
                    'sekolah_id_enkrip': i,
                    'accreditation': profile_usermenu\
                        .find_all('a')[2]\
                        .text\
                        .replace(' ', '')\
                        .replace('\n', '')[-1],
                    'status_bos': data_rinci\
                        .find_all('p')[0]\
                        .text.split(':')[1],
                    'iso_certification': data_rinci\
                        .find_all('p')[2]\
                        .text.split(':')[1],
                    'source_electricity': data_rinci\
                        .find_all('p')[3]\
                        .text\
                        .split(':')[1],
                    'power_electricity': data_rinci\
                        .find_all('p')[4]\
                        .text\
                        .split(':')[1],
                    'internet_access': data_rinci\
                        .find_all('p')[5]\
                        .text\
                        .split(':')[1],
                    'school_status': identitas_sekolah\
                        .find_all('p')[1]\
                        .text\
                        .split(':')[1],
                    'school_level': identitas_sekolah\
                        .find_all('p')[2]\
                        .text\
                        .split(':')[1],
                    'status_ownership': identitas_sekolah\
                        .find_all('p')[3]\
                        .text\
                        .split(':')[1]
                }])
                df.to_csv(
                    './data/school-profile.csv',
                    index=False,
                    mode='a',
                    header=False
                )
            except requests.exceptions.SSLError:
                continue
            except requests.exceptions.ConnectTimeout:
                continue
            except requests.exceptions.ReadTimeout:
                continue
            except requests.exceptions.ConnectionError:
                continue
            except AttributeError:
                pass

def main():
    with open('./util/columns.json', 'r') as f:
        columns = load(f)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--pool',
        type=int,
        default=2,
        help='numbers of pool used for multiprocessing',
        metavar=''
    )
    parser.add_argument(
        '-t',
        '--timeout',
        type=int,
        default=5,
        help='number of seconds Requests will wait for your client to establish a connection to a remote machine (corresponding to the connect()) call on the socket',
        metavar=''
    )
    args = parser.parse_args()
    pool = args.pool
    timeout = args.timeout
    dapodik = Dapodik(
        '20192',
        'https://dapo.dikdasmen.kemdikbud.go.id/rekap/',
        {'user-agent': str(id(randint(0, 1000000)))},
        timeout,
        columns
    )
    dapodik.get_all(columns['all'])

    # produce province.csv
    Pool(pool).map(
        dapodik.get_province,
        dapodik.get_target_list(
            'all',
            columns['all'],
            'kode_wilayah',
            'province',
            columns['province'],
            'mst_kode_wilayah'
        )
    )

    # produce district.csv
    Pool(pool).map(
        dapodik.get_district,
        dapodik.get_target_list(
            'province',
            columns['province'],
            'kode_wilayah',
            'district',
            columns['district'],
            'mst_kode_wilayah'
        )
    )

    # produce subdistrict.csv
    Pool(pool).map(
        dapodik.get_subdistrict,
        dapodik.get_target_list(
            'district',
            columns['district'],
            'kode_wilayah',
            'subdistrict',
            columns['subdistrict'],
            'kode_wilayah_induk_kecamatan'
        )
    )

    # produce school.csv
    Pool(pool).map(
        dapodik.get_school,
        dapodik.get_target_list(
            'subdistrict',
            columns['subdistrict'],
            'sekolah_id_enkrip',
            'school',
            columns['school'],
            'sekolah_id_enkrip'
        )
    )

    # produce school-profile.csv
    Pool(pool).map(
        dapodik.get_school_profile,
        dapodik.get_target_list(
            'subdistrict',
            columns['subdistrict'],
            'sekolah_id_enkrip',
            'school-profile',
            columns['school_profile'],
            'sekolah_id_enkrip'
        )
    )

if __name__ == "__main__":
    main()