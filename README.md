# Pembukaan
Assalamualaikum warahmatullahi wabarakatuh. Mohon ijin pimpinan. Dengan ini saya sampaikan data mengenai persekolahan di Indonesia, wabil khusus perbandingan antara kondisi nasional dan Papua (Provinsi Papua dan Provinsi Papua Barat). Data diperoleh dari situs [Data Pokok Pendidikan Dasar dan Menengah](https://dapo.dikdasmen.kemdikbud.go.id/). Maksud dan tujuan dari ini adalah untuk belajar apa yang sekiranya terjadi di Papua, setidaknya dari segi pendidikan 🙏🏽.

Lihat slide presentasi di [sini](https://ledwindra.github.io/pendidikan-papua/#/).

# Lakukan di komputer Anda
Pastikan Anda sudah menginstall Python 3.x. Dalam kasus ini, saya menggunakan versi 3.8.1. Lakukan hal di bawah ini di terminal:

```
git clone https://github.com/ledwindra/pendidikan-papua.git
cd pendidikan-papua
```

# Struktur folder

```
.
├── README.md
├── data
│   ├── all.csv
│   ├── district.csv
│   ├── province.csv
│   ├── school.csv
│   └── subdistrict.csv
├── index.ipynb
├── requirements.txt
└── src
    └── get_data.py
```


# Virtual environment
Aktifkan virtual environment jika ada tidak ingin modul yang bentrok saat menjalankan projek ini dengan modul lainnya yang sudah terpasang di komputer Anda. Lakukan hal di bawah ini di terminal:

```
python3 -m venv .venv
source .venv/bin/activate
```

# Install modul
Projek ini membutuhkan modul eksternal. Lakukan hal di bawah ini di terminal:

```
pip3 install --upgrade pip
pip3 -r install requirements.txt
```

# Memperoleh data
Data dikumpulkan melalui cara *web scraping*. Silakan jalan program berikut di terminal:

```
python3 src/get_data.py
```

# Data
Jika ada enggan untuk menjalankan program tersebut, silakan langsung gunakan data yang sudah disajikan di folder `data`.

# Penjelasan kolom
Berikut adalah penjelasan setiap kolom dari sumber data yang digunakan. Kolom tambahan yang dihasilkan saat analisis dapat dilihat di *notebook* berujudul `index.ipynb`:

## TO-DO: penjelasan kolom

|nama_kolom|tipe_data|penjelasan|
|-|-|-|
|nama|string||,
|sekolah_id|string||,
|kode_wilayah_induk_kecamatan|string||,
|induk_provinsi|string||,
|kode_wilayah_induk_provinsi|string||,
|bentuk_pendidikan|string||,
|status_sekolah|string||,
|sekolah_id_enkrip|string||,
|rombel|integer||,
|guru_kelas|integer||,
|guru_matematika|integer||,
|guru_bahasa_indonesia|integer||,
|guru_bahasa_inggris|integer||,
|guru_sejarah_indonesia|integer||,
|guru_pkn|integer||,
|guru_penjaskes|integer||,
|guru_agama_budi_pekerti|integer||,
|guru_seni_budaya|integer||,
|ptk_laki|integer||,
|ptk_perempuan|integer||,
|pegawai_laki|integer||,
|pegawai_perempuan|integer||,
|pd_kelas_1_laki|integer||,
|pd_kelas_1_perempuan|integer||,
|pd_kelas_2_laki|integer||,
|pd_kelas_2_perempuan|integer||,
|pd_kelas_3_laki|integer||,
|pd_kelas_3_perempuan|integer||,
|pd_kelas_4_laki|integer||,
|pd_kelas_4_perempuan|integer||,
|pd_kelas_5_laki|integer||,
|pd_kelas_5_perempuan|integer||,
|pd_kelas_6_laki|integer||,
|pd_kelas_6_perempuan|integer||,
|pd_kelas_7_laki|integer||,
|pd_kelas_7_perempuan|integer||,
|pd_kelas_8_laki|integer||,
|pd_kelas_8_perempuan|integer||,
|pd_kelas_9_laki|integer||,
|pd_kelas_9_perempuan|integer||,
|pd_kelas_10_laki|integer||,
|pd_kelas_10_perempuan|integer||,
|pd_kelas_11_laki|integer||,
|pd_kelas_11_perempuan|integer||,
|pd_kelas_12_laki|integer||,
|pd_kelas_12_perempuan|integer||,
|pd_kelas_13_laki|integer||,
|pd_kelas_13_perempuan|integer||,
|jumlah_kirim|integer||,
|ptk|integer||,
|pegawai|integer||,
|pd|integer||,
|pd_laki|integer||,
|pd_perempuan|integer||,
|jml_rk|integer||,
|jml_lab|integer||,
|jml_perpus|integer||,
|identitas_valid|integer||,
|ptk_valid|integer||,
|pd_valid|integer||,
|prasarana_valid|integer||,
|total_valid|integer||,
|kecukupan_air|string||,
|memproses_air|string||,
|minum_siswa|string||,
|siswa_bawa_air|string||,
|toilet_siswa_kk|string||,
|sumber_air_str|string||,
|ketersediaan_air|string||,
|tipe_jamban|string||,
|jml_wastafel|integer||,
|a_sabun_air_mengalir|string||,
|jml_jamban_digunakan|integer||,
|jml_jamban_tidak_digunakan|integer||,
|accreditation|string||,
|status_bos|string||,
|iso_certification|string||,
|source_electricity|string||,
|power_electricity|integer||,
|internet_access|string||,
|school_status|string||,
|school_level|string||,
|status_ownership|string||

# Hasil deskriptif
Data yang dijadikan di slide presentasi dapat diperoleh dengan menjalankan *notebook*. Silakan jalankan `index.ipynb` di komputer Anda.

# Keluar dari virtual environment
Ketik `deactivate` di terminal.

# Penutup
Demikian saya ucapkan wabillahi taufiq wal hidayah, wassalamualikum warahmatullahi wabarakatuh. 🙏🏽.
