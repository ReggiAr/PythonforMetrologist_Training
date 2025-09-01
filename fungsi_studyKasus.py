

# Fungsi untuk mengubah Celcius ke Kelvin
def to_kelvin(c):
    return c + 273.15


# Fungsi untuk mengubah Celcius ke Fahrenheit
def to_fahrenheit(c):
    return (c * 9/5) + 32


# Fungsi utama untuk mengembalikan keduanya dalam bentuk 
tuple
def konversi_suhu(c):
    k = to_kelvin(c)
    f = to_fahrenheit(c)
    return (k, f)


# Uji fungsi dengan suhu 25 derajat Celcius

celcius = 25
kelvin, fahrenheit = konversi_suhu(celcius)


# Cetak hasil
print(f"Suhu: {celcius}°C")
print(f"Dalam Kelvin: {kelvin} K")
print(f"Dalam Fahrenheit: {fahrenheit} °F")

