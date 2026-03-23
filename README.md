🐍 SNAKE ARCADE: EVOLVED PUZZLE
Snake Arcade adalah sebuah permainan klasik yang dikembangkan menggunakan Python dan Pygame dengan penambahan mekanik gameplay modern. Pemain tidak hanya dituntut untuk memakan apel agar tumbuh panjang, tetapi juga harus menghindari racun dan memanfaatkan kemunculan apel emas (Golden Apple) untuk memenangkan rekor tertinggi.

🎮 FITUR UTAMA & MEKANIK
Aplikasi ini mengintegrasikan berbagai logika permainan yang dinamis untuk menciptakan pengalaman yang menantang:

🍎 MULTI-FOOD SYSTEM: * Apel Merah: Makanan standar untuk menambah panjang badan (+1).

Apel Emas (Bonus): Muncul setiap 30 detik dengan durasi terbatas (+5 skor & panjang).

Racun Hijau: Muncul secara periodik; jika dimakan akan mengurangi skor dan panjang badan secara drastis (-3).

⏲️ ACCURATE TIME TRACKING: Sistem penghitung waktu yang cerdas, mampu mendeteksi durasi pause sehingga waktu bermain tetap akurat.

⏸️ INTERACTIVE PAUSE MENU: Antarmuka jeda yang memungkinkan pemain untuk melanjutkan, mengulang (restart), atau kembali ke menu utama tanpa menutup aplikasi.

🏆 PERSISTENT HIGH SCORES: Skor tertinggi disimpan berdasarkan tingkat kesulitan (Mudah, Normal, Sulit) menggunakan sistem I/O file.

🎨 DYNAMIC VISUALS: Render grid latar belakang untuk presisi gerakan dan desain kepala ular yang memiliki detail mata.

🧪 ARSITEKTUR PROYEK (MODULAR STRUCTURE)
Proyek ini dibangun dengan struktur modular untuk memastikan setiap komponen memiliki tanggung jawab yang terpisah:

📜 main.py: Pusat kendali permainan, menangani game loop, input pemain, dan logika tabrakan.

🧠 high_score.py: Mengelola sistem penyimpanan data (Save/Load) rekor pemain.

⚙️ config.py: Berisi seluruh konstanta global seperti kecepatan, warna, dan ukuran blok ular.

🛠️ utils.py: Menyediakan fungsi pembantu untuk render teks, tombol interaktif, dan HUD (Heads-Up Display).

🖥️ keluar.py & setting.py: Menangani antarmuka menu Game Over dan konfigurasi kesulitan.

🛠️ TECH STACK
Language: Python 3.x

Library: Pygame (Graphics, Sound, & Input Handling)

Logic: Coordinate-based collision & Time-based spawn management.

📂 STRUKTUR PROYEK
Plaintext
/Snake-Arcade
  ├── main.py          <-- Logic Utama & Spawn Manager
  ├── config.py        <-- Konstanta Game & Warna
  ├── high_score.py    <-- Data Persistence (Rekor)
  ├── utils.py         <-- UI Components & HUD
  ├── setting.py       <-- Konfigurasi Kesulitan
  ├── keluar.py        <-- Menu Evaluasi Akhir
  └── README.md        <-- Dokumentasi Proyek
🚀 PANDUAN INSTALASI
Persiapan: Pastikan library Pygame sudah terpasang. Jika belum, instal melalui terminal:
pip install pygame

Jalankan Game: Eksekusi file utama untuk mulai bermain:
python main.py
