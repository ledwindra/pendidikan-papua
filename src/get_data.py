import glob
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from random import randint

class Dapodik:

    def __init__(self, semester_id):
        self.semester_id = semester_id

    def get_all(self, url, headers):
        all_url = url + f'progres?id_level_wilayah=0&semester_id={self.semester_id}'
        status_code = None
        if not os.path.exists('./data/all.csv'):
            while status_code != 200:
                try:
                    response = requests.get(all_url, headers=headers, timeout=3)
                    status_code = response.status_code
                    df = pd.DataFrame(response.json())
                    df = df[['nama', 'kode_wilayah']]
                    df.to_csv('./data/all.csv', index=False)
                except requests.exceptions.SSLError:
                    continue
                except requests.exceptions.ConnectTimeout:
                    continue
                except requests.exceptions.ReadTimeout:
                    continue
                except requests.exceptions.ConnectionError:
                    continue
        else:
            print('Province file exists')
    
    def get_province(
        self,
        url,
        headers, 
        columns=['nama', 'kode_wilayah', 'mst_kode_wilayah']
    ):
        all_df = pd.read_csv('./data/all.csv', dtype={'kode_wilayah': object})
        region_id = [x.replace(' ', '') for x in all_df['kode_wilayah']]
        region_name = [x for x in all_df['nama']]
        if os.path.exists('./data/province.csv'):
            df = pd.read_csv('./data/province.csv', dtype=object, header=None)
            df.columns = columns
            mst_region_id = set([x.replace(' ', '') for x in df['mst_kode_wilayah']])
        else:
            mst_region_id = set()
        for i in region_id:
            print(f'Upcoming province ID: {i}')
            if i not in set(mst_region_id):
                province_url = url + f'progres?&id_level_wilayah=1&kode_wilayah={i}&semester_id={self.semester_id}'
                status_code = None
                while status_code != 200:
                    try:
                        response = requests.get(province_url, headers=headers, timeout=3)
                        status_code = response.status_code
                        df = pd.DataFrame(response.json())
                        df = df[columns]
                        df.to_csv('./data/province.csv', index=False, mode='a', header=False)
                    except requests.exceptions.SSLError:
                        continue
                    except requests.exceptions.ConnectTimeout:
                        continue
                    except requests.exceptions.ReadTimeout:
                        continue
                    except requests.exceptions.ConnectionError:
                        continue
            else:
                print(f'Province ID {i} already exists')

    def get_district(
        self,
        url,
        headers, 
        columns=['nama', 'kode_wilayah', 'mst_kode_wilayah']
    ):
        province = pd.read_csv('./data/province.csv', dtype=object, header=None)
        province.columns = columns
        region_id = set([x.replace(' ', '') for x in province['kode_wilayah']])
        region_name = set([x for x in province['nama']])
        if os.path.exists('./data/district.csv'):
            df = pd.read_csv('./data/district.csv', dtype=object, header=None)
            df.columns = columns
            mst_region_id = set([x.replace(' ', '') for x in df['mst_kode_wilayah']])
        else:
            mst_region_id = set()
        for i in region_id:
            print(f'Upcoming district ID: {i}')
            if i not in set(mst_region_id):
                district_url = url + f'progres?&id_level_wilayah=2&kode_wilayah={i}&semester_id={self.semester_id}'
                status_code = None
                while status_code != 200:
                    try:
                        response = requests.get(district_url, headers=headers, timeout=3)
                        status_code = response.status_code
                        df = pd.DataFrame(response.json())
                        df = df[columns]
                        df.to_csv('./data/district.csv', index=False, mode='a', header=False)
                    except requests.exceptions.SSLError:
                        continue
                    except requests.exceptions.ConnectTimeout:
                        continue
                    except requests.exceptions.ReadTimeout:
                        continue
                    except requests.exceptions.ConnectionError:
                        continue
            else:
                print(f'District ID {i} already exists')

    def get_subdistrict(
        self,
        url,
        headers, 
        source_columns=['nama', 'kode_wilayah', 'mst_kode_wilayah'],
        target_columns=[
            'nama',
            'sekolah_id',
            'kode_wilayah_induk_kecamatan',
            'induk_provinsi',
            'kode_wilayah_induk_provinsi',
            'bentuk_pendidikan',
            'status_sekolah',
            'sekolah_id_enkrip'
        ]
    ):
        district = pd.read_csv('./data/district.csv', dtype=object, header=None)
        district.columns = source_columns
        region_id = set([x.replace(' ', '') for x in district['kode_wilayah']])
        region_name = set([x for x in district['nama']])
        if os.path.exists('./data/subdistrict.csv'):
            df = pd.read_csv('./data/subdistrict.csv', dtype=object, header=None)
            df.columns = target_columns
            mst_region_id = set([x.replace(' ', '') for x in df['kode_wilayah_induk_kecamatan']])
        else:
            mst_region_id = set()
        for i in region_id:
            print(f'Upcoming subdistrict ID: {i}')
            if i not in set(mst_region_id):
                subdistrict_url = url + f'progresSP?id_level_wilayah=3&semester_id={self.semester_id}&kode_wilayah={i}'
                status_code = None
                while status_code != 200:
                    try:
                        response = requests.get(subdistrict_url, headers=headers, timeout=3, verify=True)
                        status_code = response.status_code
                        df = pd.DataFrame(response.json())
                        df = df[target_columns]
                        df.to_csv('./data/subdistrict.csv', index=False, mode='a', header=False)
                    except requests.exceptions.SSLError:
                        continue
                    except requests.exceptions.ConnectTimeout:
                        continue
                    except requests.exceptions.ReadTimeout:
                        continue
                    except requests.exceptions.ConnectionError:
                        continue
            else:
                print(f'Subdistrict ID {i}: file exists')

    def get_school(
        self,
        url,
        headers,
        source_columns=[
            'nama',
            'sekolah_id',
            'kode_wilayah_induk_kecamatan',
            'induk_provinsi',
            'kode_wilayah_induk_provinsi',
            'bentuk_pendidikan',
            'status_sekolah',
            'sekolah_id_enkrip'
        ],
        target_columns=[
            'rombel',
            'guru_kelas',
            'guru_matematika',
            'guru_bahasa_indonesia',
            'guru_bahasa_inggris',
            'guru_sejarah_indonesia',
            'guru_pkn',
            'guru_penjaskes',
            'guru_agama_budi_pekerti',
            'guru_seni_budaya',
            'ptk_laki',
            'ptk_perempuan',
            'pegawai_laki',
            'pegawai_perempuan',
            'pd_kelas_1_laki',
            'pd_kelas_1_perempuan',
            'pd_kelas_2_laki',
            'pd_kelas_2_perempuan',
            'pd_kelas_3_laki',
            'pd_kelas_3_perempuan',
            'pd_kelas_4_laki',
            'pd_kelas_4_perempuan',
            'pd_kelas_5_laki',
            'pd_kelas_5_perempuan',
            'pd_kelas_6_laki',
            'pd_kelas_6_perempuan',
            'pd_kelas_7_laki',
            'pd_kelas_7_perempuan',
            'pd_kelas_8_laki',
            'pd_kelas_8_perempuan',
            'pd_kelas_9_laki',
            'pd_kelas_9_perempuan',
            'pd_kelas_10_laki',
            'pd_kelas_10_perempuan',
            'pd_kelas_11_laki',
            'pd_kelas_11_perempuan',
            'pd_kelas_12_laki',
            'pd_kelas_12_perempuan',
            'pd_kelas_13_laki',
            'pd_kelas_13_perempuan',
            'jumlah_kirim',
            'ptk',
            'pegawai',
            'pd',
            'pd_laki',
            'pd_perempuan',
            'jml_rk',
            'jml_lab',
            'jml_perpus',
            'identitas_valid',
            'ptk_valid',
            'pd_valid',
            'prasarana_valid',
            'total_valid',
            'kecukupan_air',
            'memproses_air',
            'minum_siswa',
            'siswa_bawa_air',
            'toilet_siswa_kk',
            'sumber_air_str',
            'ketersediaan_air',
            'tipe_jamban',
            'jml_wastafel',
            'a_sabun_air_mengalir',
            'jml_jamban_digunakan',
            'jml_jamban_tidak_digunakan',
            'sekolah_id_enkrip'
        ]
    ):
        subdistrict = pd.read_csv('./data/subdistrict.csv', dtype=object, header=None)
        subdistrict.columns = source_columns
        source_school_id = set([x.replace(' ', '') for x in subdistrict['sekolah_id_enkrip']])
        if os.path.exists('./data/school.csv'):
            df = pd.read_csv('./data/school.csv', dtype=object, header=None)
            df.columns = target_columns
            target_school_id = set([x.replace(' ', '') for x in df['sekolah_id_enkrip']])
        else:
            target_school_id = set()
        for i in source_school_id:
            print(f'Upcoming school ID: {i}')
            if i not in set(target_school_id):
                school_url = url + f'sekolahDetail?sekolah_id={i}'
                status_code = None
                while status_code != 200:
                    try:
                        response = requests.get(school_url, headers=headers, timeout=3, verify=True)
                        status_code = response.status_code
                        df = pd.DataFrame(response.json())
                        df['sekolah_id_enkrip'] = i
                        df = df[target_columns]
                        df.to_csv('./data/school.csv', index=False, mode='a', header=False)
                    except requests.exceptions.SSLError:
                        continue
                    except requests.exceptions.ConnectTimeout:
                        continue
                    except requests.exceptions.ReadTimeout:
                        continue
                    except requests.exceptions.ConnectionError:
                        continue
            else:
                print(f'School ID {i}: file exists')

    def get_school_profile(
        self,
        url,
        headers,
        target_columns = [
            'sekolah_id_enkrip',
            'accreditation',
            'status_bos',
            'iso_certification',
            'source_electricity',
            'power_electricity',
            'internet_access',
            'school_status',
            'school_level',
            'status_ownership'
        ]
    ):
        subdistrict = pd.read_csv('./data/subdistrict.csv', dtype=object, header=None)
        source_school_id = [x.replace(' ', '') for x in subdistrict.iloc[:,-1]]
        if os.path.exists('./data/school-profile.csv'):
            df = pd.read_csv('./data/school-profile.csv', dtype=object, header=None)
            df.columns = target_columns
            target_school_id = set([x.replace(' ', '') for x in df['sekolah_id_enkrip']])
        else:
            target_school_id = set()
        for i in source_school_id:
            print(f'Upcoming school ID: {i}')
            if i not in set(target_school_id):
                school_url = f'https://dapo.dikdasmen.kemdikbud.go.id/sekolah/{i}'
                status_code = None
                while status_code != 200:
                    try:
                        response = requests.get(school_url, headers=headers, timeout=3, verify=True)
                        status_code = response.status_code
                        content = BeautifulSoup(response.content, features='html.parser')
                        profile_usermenu = content.find('div', {'class': 'profile-usermenu'})
                        identitas_sekolah = content.find('div', id='myTabContent').find_all('div', {'class': 'panel-body'})[0]
                        data_rinci = content.find('div', id='myTabContent').find_all('div', {'class': 'panel-body'})[2]
                        df = pd.DataFrame([{
                            'sekolah_id_enkrip': i,
                            'accreditation': profile_usermenu.find_all('a')[2].text.replace(' ', '').replace('\n', '')[-1],
                            'status_bos': data_rinci.find_all('p')[0].text.split(':')[1],
                            'iso_certification': data_rinci.find_all('p')[2].text.split(':')[1],
                            'source_electricity': data_rinci.find_all('p')[3].text.split(':')[1],
                            'power_electricity': data_rinci.find_all('p')[4].text.split(':')[1],
                            'internet_access': data_rinci.find_all('p')[5].text.split(':')[1],
                            'school_status': identitas_sekolah.find_all('p')[1].text.split(':')[1],
                            'school_level': identitas_sekolah.find_all('p')[2].text.split(':')[1],
                            'status_ownership': identitas_sekolah.find_all('p')[3].text.split(':')[1]
                        }])
                        df.to_csv('./data/school-profile.csv', index=False, mode='a', header=False)
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
            else:
                print(f'School ID {i}: file exists')

def main():
    headers = {'user-agent': str(id(randint(0, 1000000)))}
    url = 'https://dapo.dikdasmen.kemdikbud.go.id/rekap/'
    dapodik = Dapodik('20192')
    # dapodik.get_all(url, headers)
    # dapodik.get_province(url, headers)
    # dapodik.get_district(url, headers)
    # dapodik.get_subdistrict(url, headers)
    # dapodik.get_school(url, headers)
    dapodik.get_school_profile(url, headers)

if __name__ == "__main__":
    main()