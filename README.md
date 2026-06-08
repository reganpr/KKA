# LAPORAN PRAKTIKUM ANALISIS DATA PENJUALAN

## 1. Business Question

Perusahaan ingin menjawab beberapa pertanyaan bisnis berikut:

1. Bagaimana tren penjualan dari bulan ke bulan?
2. Apakah anggaran iklan (Ad Budget) memiliki hubungan dengan total penjualan (Total Sales)?
3. Siapa pelanggan yang paling bernilai berdasarkan analisis RFM (Recency, Frequency, Monetary)?
4. Seberapa baik anggaran iklan dapat digunakan untuk memprediksi penjualan?

---

## 2. Data Wrangling

Tahapan pembersihan dan persiapan data yang dilakukan:

* Mengimpor dataset menggunakan Pandas.
* Memeriksa struktur data menggunakan `df.info()`.
* Mengecek nilai kosong menggunakan `df.isnull().sum()`.
* Mengubah kolom `Order_Date` menjadi format datetime.
* Membuat kolom baru `Month` untuk analisis penjualan bulanan.
* Menghapus data yang memiliki nilai kosong pada kolom `Total_Sales` sebelum proses pemodelan regresi.
* Melakukan agregasi data berdasarkan bulan untuk mendapatkan total penjualan bulanan.

---

## 3. Insights

### A. Tren Penjualan Bulanan (Bar Chart / Line Chart)

Visualisasi tren penjualan bulanan menunjukkan perubahan total penjualan dari waktu ke waktu. Grafik ini membantu perusahaan mengidentifikasi periode dengan penjualan tertinggi maupun terendah.

Interpretasi:

* Jika grafik menunjukkan kenaikan, berarti performa penjualan semakin baik.
* Jika terjadi penurunan pada bulan tertentu, perusahaan perlu mencari penyebabnya seperti berkurangnya promosi atau faktor musiman.

### B. Korelasi Anggaran Iklan dan Penjualan (Heatmap)

Heatmap korelasi digunakan untuk melihat hubungan antara variabel `Ad_Budget` dan `Total_Sales`.

Interpretasi:

* Nilai korelasi mendekati +1 menunjukkan hubungan positif yang kuat.
* Artinya, semakin besar anggaran iklan yang dikeluarkan, semakin tinggi potensi penjualan yang diperoleh.
* Jika korelasi rendah, faktor lain selain iklan kemungkinan lebih berpengaruh terhadap penjualan.

### C. Analisis Pelanggan (RFM)

Analisis RFM digunakan untuk mengelompokkan pelanggan berdasarkan:

* Recency (seberapa baru pelanggan bertransaksi)
* Frequency (seberapa sering pelanggan bertransaksi)
* Monetary (berapa besar nilai transaksi pelanggan)

Pelanggan dengan skor RFM tinggi merupakan pelanggan terbaik yang perlu dipertahankan.

---

## 4. Recommendation

Berdasarkan hasil analisis:

1. Tingkatkan investasi iklan pada periode yang terbukti menghasilkan penjualan tinggi.
2. Evaluasi strategi pemasaran pada bulan dengan performa penjualan rendah.
3. Berikan program loyalitas kepada pelanggan dengan skor RFM tertinggi untuk meningkatkan retensi pelanggan.
4. Gunakan model regresi linear sebagai alat bantu prediksi penjualan berdasarkan anggaran iklan.
5. Lakukan pemantauan data secara berkala agar keputusan bisnis dapat dibuat berdasarkan data terbaru.

## Kesimpulan

Analisis menunjukkan bahwa data penjualan dapat dimanfaatkan untuk memahami tren bisnis, mengukur efektivitas iklan, mengidentifikasi pelanggan terbaik, dan memprediksi penjualan di masa mendatang. Hasil ini dapat menjadi dasar dalam pengambilan keputusan strategis perusahaan.
