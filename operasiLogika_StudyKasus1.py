

# Input 3 hasil pengukuran
p1 = float(input("Pengukuran 1 (mm): "))
p2 = float(input("Pengukuran 2 (mm): "))
p3 = float(input("Pengukuran 3 (mm): "))


# Hitung rata-rata
rata2 = (p1 + p2 + p3) / 3


# Hitung nilai maksimum dan minimum
maks = max(p1, p2, p3)
minim = min(p1, p2, p3)


# Hitung rentang (range)
range_ukur = maks - minim


# Evaluasi stabilitas
stabil = range_ukur <= 0.02


# Tampilkan hasil
print("\nRata-rata: ", round(rata2, 3), "mm")
print("Nilai maksimum: ", maks, "mm")
print("Nilai minimum: ", minim, "mm")

print("Range: ", round(range_ukur, 3), "mm")
print("Apakah alat stabil?", stabil)
