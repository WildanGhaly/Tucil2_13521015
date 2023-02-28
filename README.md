
# Tugas Kecil II - Mencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer

## Deskripsi Tugas
Mencari sepasang titik terdekat dengan Algoritma Divide and Conquer sudah dijelaskan di 
dalam kuliah. Persoalan tersebut dirumuskan untuk titik pada bidang datar (2D). Pada Tucil 2
kali ini Anda diminta mengembangkan algoritma mencari sepasang titik terdekat pada bidang 
3D. Misalkan terdapat n buah titik pada ruang 3D. Setiap titik P di dalam ruang dinyatakan 
dengan koordinat P = (x, y, z). Carilah sepasang titik yang mempunyai jarak terdekat satu 
sama lain. Jarak dua buah titk P1 = (x1, y1, z1) dan P2 = (x2, y2, z2).

Buatlah program dalam dalam Bahasa C/C++/Java/Python/Golang/Ruby/Perl (pilih salah 
satu) untuk mencari sepasang titik yang jaraknya terdekat datu sama lain dengan menerapkan 
algoritma divide and conquer untuk penyelesaiannya, dan perbandingannya dengan 
Algoritma Brute Force.




## Implementasi Algoritma

Algoritma Divide and Conquer dilakukan dengan cara membagi permasalahan titik terdekat dengan membagi dua list titik yang sudah ada secara rekursif sampai hanya tersisa dua atau tiga titik. Setelah tersisa 2 atau 3 titik maka program akan melakukan perhitungan euclidian dan membandingkan hasilnya dengan perhitungan euclidian dari proses lainnya.
## Requirement dan Cara Menjalankan Program

Program ini menggunakan bahasa Python sehingga hanya akan bisa dijalankan apabila sistem telah memiliki instalasi Python. Program juga memanfaatkan library matplotlib yang bisa diinstall dengan kode berikut atau melakukan instalasi dari MSYS2 MINGW:

```bash
  python -m pip install -U pip
  python -m pip install -U matplotlib
```

Setelah itu program akan bisa dijalankan dengan cara menjalankan kode berikut:

```bash
  py src/main.py
```
## Authors

- 13521015 [Hidayatullah Wildan Ghaly Buchary](https://github.com/WildanGhaly)

