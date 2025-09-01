# Langkah 1: Nested Dictionary awal
alat_ukur = {
    "T001": {
        "nama": "Termometer Digital",
        "pengukuran": [36.5, 36.7, 36.6]
    },
    "T002": {
        "nama": "Termometer Raksa",
        "pengukuran": [36.3, 36.4, 36.5]
    }
}

# Langkah 2: Tambahkan alat baru
alat_ukur["T003"] = {
    "nama": "Termometer Inframerah",
    "pengukuran": [36.8, 36.9, 37.0]
}

# Langkah 3: Cetak rata-rata pengukuran dari masing-masing alat
for id_alat, data in alat_ukur.items():
    nama = data["nama"]
    pengukuran = data["pengukuran"]
    rata_rata = sum(pengukuran) / len(pengukuran)
    print(f"{nama} - Rata-rata: {rata_rata:.2f}")

# Langkah 4: Hitung total jumlah seluruh pengukuran
total_pengukuran = 0
for data in alat_ukur.values():
    total_pengukuran += len(data["pengukuran"])

print(f"Total seluruh pengukuran: {total_pengukuran} data")

