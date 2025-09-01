

# Fungsi placeholder untuk simpan hasil (belum diimplementasikan)


def simpan_hasil():
    pass  # fitur ini akan dibuat kemudian


# Inisialisasi list untuk menyimpan hasil semua batch
semua_hasil = []


# Loop untuk 3 batch pengukuran
for batch in range(1, 4):
    print(f"\nBatch {batch}:")
    data_batch = []
    # Input 3 nilai valid (positif) untuk tiap batch
    i = 0
    while i < 3:
        try:
             nilai = float(input(f"  Pengukuran ke-{i+1}: "))
        except ValueError:
                print("  ❌ Masukkan angka yang  valid!")
                continue          
        if nilai < 0:
            print("  ❌ Nilai negatif tidak valid,diabaikan.")
            continue
        data_batch.append(nilai)
        i += 1


    # Simpan data batch
    semua_hasil.append(data_batch)


    # Evaluasi stabilitas batch
    maks = max(data_batch)
    minim = min(data_batch)
    selisih = maks - minim


    # Penilaian
    if selisih <= 0.002:
        status = "Sangat Stabil"
    elif selisih <= 0.005:
        status = "Stabil"
    else:
        status = "Tidak Stabil"


    # Tampilkan hasil
    print(f"  Data: {[f'{d:.3f}' for d in data_batch]}")
    print(f"  Status: {status}")


# Fungsi penyimpanan belum diimplementasikan
simpan_hasil()