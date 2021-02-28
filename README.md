# OTW LULUS !
> Tugas Kecil II Mata Kuliah IF2211 Strategi Algoritma Tahun Akademik 20

## Table of contents
* [General info](#general-info)
* [Documentation](#documentation)
* [Requirements](#requirements)
* [Setup](#setup)
* [How To Run](#how-to-run)
* [Author](#author)

## General info
OTW LULUS! adalah program penyusunan rencana kuliah menggunakan pendekatan algoritma decrease and conquer melalui topological sorting.

Penerapan algoritma decrease and conquer dalam topological sort penyusunan rencana kuliah merupakan varian algoritma decrease and conquer versi decrease by a variable size. Ukuran instans persoalan akan direduksi bervariasi pada setiap iterasi algoritma berdasarkan banyaknya mata kuliah yang memiliki derajat masuk 0.

Adapun tahap algoritma decrease and conquer dalam tahapan topological sort
Tahap Decrease 
Algoritma akan mereduksi persoalan dengan menghilangkan simpul beserta semua busur yang keluar dari simpul tersebut pada graf, dan kurangi derajat simpul yang berhubungan dengan simpul tersebut dengan 1. 
Tahap Conquer
Memproses upa-persoalan berupa directed acyclic graph yang telah melalui tahap decrease. Kemudian, secara rekursif akan memproses directed acyclic graph sampai semua simpul pada graph diurutkan.

## Documentation
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/63598464/109429466-6d8d6780-7a2e-11eb-8bf6-cce2c398827e.gif)
![tasdasd](https://user-images.githubusercontent.com/63598464/109429565-de348400-7a2e-11eb-8f2b-1e2b694af048.png)

## Requirements
1. Python 3.9
2. Library Roman
    ```
    pip install roman
    ```
## Setup
```
git clone https://github.com/isabellahandayani/topological-sort
```

## How To Run
### Alternatif 1
```
cd Tucil2_13519081/bin
```
Jalankan 13519081.exe pada folder bin
### Alternatif 2
Jika komputer mendeteksi file .exe sebagai virus, 
```
cd Tucil2_13519081/src
python 13519081.py
```

## Author
Isabella Handayani Sumantri - 13519081