# Pembukaan
Assalamualaikum warahmatullahi wabarakatuh. Mohon ijin pimpinan. Dengan ini saya sampaikan data mengenai persekolahan di Indonesia, wabil khusus perbandingan antara kondisi nasional dan Papua (Provinsi Papua dan Provinsi Papua Barat). Data diperoleh dari situs Data Pokok Pendidikan Dasar dan Menengah (https://dapo.dikdasmen.kemdikbud.go.id/). Maksud dan tujuan dari ini adalah untuk belajar apa yang sekiranya terjadi di Papua, setidaknya dari segi pendidikan 🙏🏽.

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

# Keluar dari virtual environment
Ketik `deactivate` di terminal.

# Penutup
Demikian saya ucapkan wabillahi taufiq wal hidayah, wassalamualikum warahmatullahi wabarakatuh. 🙏🏽.
