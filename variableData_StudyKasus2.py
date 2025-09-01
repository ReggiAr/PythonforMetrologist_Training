

# Input suhu dari alat dalam Fahrenheit
f = float(input("Masukkan hasil pengukuran suhu (°F): "))


# Konversi ke Celsius
c = (5 / 9) * (f - 32)


# Nilai referensi standar suhu
standar = 25.0


# Hitung galat absolut
galat = abs(c - standar)


# Tampilkan hasil
print("\nSuhu dalam Celsius: {:.2f} °C".format(c))
print("Galat terhadap standar 25.0 °C: {:.2f} °C".format(galat))
