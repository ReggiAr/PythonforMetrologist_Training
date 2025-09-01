

# Input dua hasil pengukuran
m1 = float(input("Pengukuran 1 (gram): "))
m2 = float(input("Pengukuran 2 (gram): "))


# Hitung rata-rata
rata_rata = (m1 + m2) / 2


# Hitung selisih absolut
selisih = abs(m1 - m2)


# Evaluasi konsistensi
konsisten = selisih <= 0.005


# Tampilkan hasil
print("\nRata-rata massa: ", round(rata_rata, 5), "gram")
print("Selisih pengukuran: ", round(selisih, 5), "gram")
print("Apakah timbangan konsisten?", konsisten)
