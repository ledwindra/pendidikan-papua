# Pembukaan
Assalamualaikum warahmatullahi wabarakatuh. Mohon ijin pimpinan. Dengan ini saya sampaikan data mengenai persekolahan di Indonesia, wabil khusus perbandingan antara kondisi nasional dan Papua (Provinsi Papua dan Provinsi Papua Barat). Data diperoleh dari situs [Data Pokok Pendidikan Dasar dan Menengah](https://dapo.dikdasmen.kemdikbud.go.id/). Maksud dan tujuan dari ini adalah untuk belajar apa yang sekiranya terjadi di Papua, setidaknya dari segi pendidikan 🙏🏽.

Lihat slide presentasi di [sini](https://ledwindra.github.io/pendidikan-papua/#/).

# Permisi
Tok-tok-tok, bolehkah saya melakukan *web scraping* di situs Dapodik? Menurut [laman](https://dapo.dikdasmen.kemdikbud.go.id/robots.txt) ini, boleh! Berikut pernyataannya:

```
User-agent: *
Disallow:
Sitemap: http://dapo.dikdasmen.kemdikbud.go.id/sitemap.xml
```

Artinya, setiap pengguna (*), tidak dilarang untuk melakukan apa pun di situ ini (Disallsow:). Trims ya! 🙏🏽

# Lakukan di komputer Anda
Pastikan Anda sudah menginstall Python 3.x. Dalam kasus ini, saya menggunakan versi 3.8.1. Lakukan hal di bawah ini di terminal:

```
git clone https://github.com/ledwindra/pendidikan-papua.git
cd pendidikan-papua
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
python3 src/get_data.py --help
```

Kemudian akan muncul pesan sebagai berikut:

```
usage: get_data.py [-h] [-p] [-t]

optional arguments:
  -h, --help       show this help message and exit
  -p , --pool      numbers of pool used for multiprocessing
  -t , --timeout   number of seconds Requests will wait for your client to establish a connection to a remote machine
                   (corresponding to the connect()) call on the socket
```

Terdapat dua argumen yang bisa digunakan dalam program ini, yaitu *pool* dan *timeout*. 

Pertama, *multiprocessing* digunakan untuk mempercepat proses dalam memperoleh data. Pada dasarnya, jumlah *pool* yang digunakan adalah 2. Namun jumlah ini bisa digunakan sesuai dengan kebutuhan, namun bergantung kepada jumlah CPU di komputer Anda. Bagaimana mengetahuinya? Secara sederhana bisa jalankan perintah berikut di terminal:

```
# macOS
sysctl -n hw.ncpu
```

Kedua, *timeout*. Menurut dokumentasi dalam modul [requests](https://requests.readthedocs.io/en/master/user/advanced/#advanced), ada baiknya menetapkan jumlah *timeout* sedikit di atas kelipatan tiga. Di sini saya menggunakan angka dasar lima detik. Berikut kalimat yang digunakan:

```
It’s a good practice to set connect timeouts to slightly larger than a multiple of 3, which is the default TCP packet retransmission window.
```

Oke, penjelasan mengenai argumen selesai. lalu setelahnya bisa jalankan program berikut di terminal:

```
# pool = 2 dan timeout = 5
python3 src/get_data.py

# pool = 4 dan timeout = 10
python3 src/get_data.py --pool 4 --timeout 10
```

# Data
Jika ada enggan untuk menjalankan program tersebut, silakan langsung gunakan data yang sudah disajikan di folder `data`. Omong-omong, karena ukuran data melampaui batas yang dimaklumi oleh GitHub (terutama `subdistrict.csv`, `school.csv`, dan `school-profile.csv`), saya menggunakan [Git Large File Storage](https://git-lfs.github.com/). Jika Anda merasa membutuhkan ini, silakan pasang di komputer Anda. Tautan [ini](https://help.github.com/en/github/managing-large-files/configuring-git-large-file-storage) mungkin juga membantu.

# Penjelasan kolom
Berikut adalah penjelasan setiap kolom dari sumber data yang digunakan. Kolom tambahan yang dihasilkan saat analisis dapat dilihat di *notebook* berujudul `index.ipynb`:

## TO-DO: penjelasan kolom

|nama_kolom|tipe_data|penjelasan|
|-|-|-|
|nama|string|Nama sekolah|,
|sekolah_id|string|ID sekolah|,
|kode_wilayah_induk_kecamatan|string|ID kecamatan|,
|induk_provinsi|string|Nama provinsi|,
|kode_wilayah_induk_provinsi|string|ID provinsi|,
|bentuk_pendidikan|string|Jenjang pendidikan (SD, SMP, SMA, SLB, atau sederajat)|,
|status_sekolah|string||,
|sekolah_id_enkrip|string|ID sekolah 2|,
|rombel|integer|Jumlah rombongan belajar per sekolah|,
|guru_kelas|integer|Jumlah guru kelas per sekolah|,
|guru_matematika|integer|Jumlah guru matematika per sekolah|,
|guru_bahasa_indonesia|integer|Jumlah guru Bahasa Indonesia per sekolah|,
|guru_bahasa_inggris|integer|Jumlah guru Bahasa Inggris per sekolah|,
|guru_sejarah_indonesia|integer|Jumlah guru sejarah per sekolah|,
|guru_pkn|integer|Jumlah guru pendidikan kewarganegaraan per sekolah|,
|guru_penjaskes|integer|Jumlah guru pendidikan jasmani, olahraga, dan kesehatan per sekolah|,
|guru_agama_budi_pekerti|integer|Jumlah guru agama dan budi pekerti per sekolah|,
|guru_seni_budaya|integer|Jumlah guru seni budaya per sekolah|,
|ptk_laki|integer|Jumlah pendidik dan tenaga kependidikan berjenis kelamin laki-laki per sekolah|,
|ptk_perempuan|integer|Jumlah pendidik dan tenaga kependidikan berjenis kelamin perempuan per sekolah|,
|pegawai_laki|integer|Jumlah pegawai per sekolah|,
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
