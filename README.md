<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/5772edc5-e181-4c1f-afdf-1e6932dc78d3" /># Smart Infantometer Cloud System (AWS Cloud Ecosystem)

Aplikasi ini merupakan prototipe ekosistem *cloud computing* berbasis **Amazon Web Services (AWS)** untuk mendeteksi dini indikasi gangguan tumbuh kembang (*stunting*/*underweight*) pada balita secara otomatis dan *real-time*. Sistem ini mengintegrasikan pengiriman data sensor dari perangkat perangkat keras menuju infrastruktur komputasi awan hingga lapisan presentasi antarmuka web.

---

## 🚀 Fitur Utama

- **Real-time Data Pipeline:** Transmisi log otomatis dari perangkat IoT menggunakan protokol MQTT yang aman ke AWS IoT Core.
- **Serverless Computing:** Pemrosesan logika data dan perutean (*routing*) dinamis tanpa manajemen server menggunakan AWS Lambda.
- **Relational Data Tracking:** Penyimpanan rekam medis terstruktur, konsisten, dan berdurabilitas tinggi pada Amazon RDS MySQL.
- **Automated Early Warning System:** Pemicu alarm otomatis asinkron melalui Amazon SNS ke surel tenaga kesehatan ketika mendeteksi parameter kritis.
- **Modern Minimalist UI Dashboard:** Tampilan visualisasi dasbor web interaktif yang di-*hosting* pada Amazon EC2 untuk memantau akumulasi data aktivitas dan jumlah anak terdata.

---

## 📐 Arsitektur & Diagram Sistem

### 1. Use Case Diagram
Menggambarkan interaksi fungsional antara perangkat keras (*Node IoT*) yang bertugas mengirimkan metrik dengan tenaga medis sebagai pengguna akhir sistem.

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/56258c99-5ec0-48db-a116-bdc81717f9e6" />


### 2. Sequence Diagram
Menjelaskan siklus hidup perjalanan data (*data lifecycle*) secara kronologis dari lapisan fisik, lapisan logika *cloud*, hingga lapisan visualisasi web.

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/2a2b1526-8368-451d-a39b-ab60b0c7f835" />
