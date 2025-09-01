import copy


# 1. Nested list hasil pengukuran 3 batch × 3 data
hasil_asli = [
    [100.001, 100.000, 100.002],
    [99.998, 100.000, 99.999],
    [100.003, 100.002, 100.001]
]


# 2. Copy list
salinan1 = hasil_asli.copy()               # Shallow copy
salinan2 = copy.deepcopy(hasil_asli)       # Deep copy


# 3. Ubah nilai pada salinan1 dan salinan2
salinan1[0][0] = 999.999  # Akan memengaruhi hasil_asli!


salinan2[1][1] = 123.456  # Tidak memengaruhi hasil_asli


# Tampilkan hasil_asli setelah perubahan
print("Isi hasil_asli setelah modifikasi salinan:")
for batch in hasil_asli:
    print(batch)


# Penjelasan:
print("\nPenjelasan:")
print("- Shallow copy (`copy()`): hanya menyalin referensi list luar. Elemen dalamnya (list batch) masih sama dengan aslinya.")
print("- Deep copy (`copy.deepcopy()`): membuat salinan sepenuhnya, termasuk isi di dalam nested list.")


# 4. Tampilkan isi hasil_asli dengan loop dan enumerate
print("\n📊 Data Hasil Asli:")
for i, batch in enumerate(hasil_asli):
    print(f"Batch {i+1}:")
    for j, nilai in enumerate(batch):
        print(f"  Pengukuran ke-{j+1}: {nilai:.3f}")


    # 5. Evaluasi stabilitas batch
    selisih = max(batch) - min(batch)
    if selisih <= 0.002:
        status = "Stabil"
    else:
        status = "Tidak Stabil"
    print(f"  Status: {status}\n")