

# Input nilai pengukuran dari pengguna
p1 = float(input("Masukkan hasil pengukuran 1 (kg): "))
p2 = float(input("Masukkan hasil pengukuran 2 (kg): "))
p3 = float(input("Masukkan hasil pengukuran 3 (kg): "))


# Nilai standar sebenarnya
nilai_riil = 10.00


# Hitung rata-rata
rata_rata = (p1 + p2 + p3) / 3


# Hitung galat absolut
galat = abs(rata_rata - nilai_riil)


# Tampilkan hasil
print("\nRata-rata pengukuran: {:.2f} kg".format(rata_rata))
print("Galat absolut terhadap 10.00 kg: {:.2f} kg".format(galat))