# 15-Puzzle
Tugas seleksi Ca-IRK 2019

## Algoritma
Algoritma yang digunakan dalam program 15-Puzzle-Solver adalah Branch and Bound, yaitu seperti algoritma BFS (breadth-first-search) yang juga melakukan pembentukan pohon ruang status dinamis untuk mencari solusi persoalan dengan pencarian melebar, namun dengan prinsip least cost search. Pada algoritma Branch and Bound, setiap simpul diberi nilai cost c(i), dan simpul berikutnya yang akan diekspan tidak berdasarkan urutan pembangkitan, tetapi simpul yang memiliki cost yang paling kecil (least cost search) maka dari itu digunakan priority queue sebagai penyimpanan simpul ekspan. <br>
Pada permainan 15-Puzzle, goal state adalah matriks 4x4 dengan angka 1-15 yang terurut lalu di pojok kanan bawah ada sel kosong.
Cara kerja algoritma 15-Puzzle-Solver secara umum adalah pertama dicek terlebih dahulu apakah goal state dapat dicapai dari initial state, yaitu dengan melihat apakah sigma fungsi kurang(i) + X bernilai genap, jika ya maka goal tersebut reachable. <br>
Lalu, dibentuk pohon ruang status dengan setiap simpul terdiri atas susunan puzzle, langkah (moves) yang dilakukan untuk mencapai simpul tersebut, serta c(i), f(i), dan g(i), di mana ketiga fungsi tersebut menyatakan:
- c(i) = f(i) + g(i), yaitu ongkos untuk simpul i
- f(i), yaitu ongkos untuk mencapai simpul i dari akar. Pada persoalan ini, f(i)-nya yaitu jumlah langkah untuk mencapai simpul tersebut. 
- g(i), yaitu ongkos mencapai simpul tujuan dari simpul i. Pada program ini, g(i) yang saya ambil berupa jumlah manhattan distance (jarak antara posisi saat itu dengan posisi seharusnya) ubin tidak kosong yang tidak terdapat pada susunan akhir. Alternatif lainnya bisa menggunakan jumlah ubin tidak kosong yang tidak terdapat pada susunan akhir, namun ini kurang akurat karena tidak memperhitungkan jarak antara susunan saat itu dengan susunan target.

## Cara penggunaan program
1. Jalankan program dengan mengetikkan pada terminal:
```
python3 app.py
```
2. Masukkan susunan puzzle yang ingin diselesaikan. Jika ingin memasukkan tile kosong, dapat menginput angka 0 atau mengosongkan field.
3. Klik tombol `Solve` untuk menyelesaikan susunan puzzle yang telah diinput.

## Author
13519040 - Shafira Naya Aprisadianti