#tugas nomor 1 
print(" ## Nomor 1 ##")
def celcius_ke_farenheit(celcius):
    farenheit=(celcius*9/5)+32
    return farenheit

suhu_celcius1 = 0
suhu_celcius2 = 100
suhu_farenheit1 = celcius_ke_farenheit(suhu_celcius1)
suhu_farenheit2 = celcius_ke_farenheit(suhu_celcius2)
print("Suhu celcius", suhu_celcius1, "sama dengan", suhu_farenheit1)
print("Suhu celcius", suhu_celcius2, "sama dengan", suhu_farenheit2)
print()

#tugas nomor 2
print(" ## Nomor 2 ##")
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0 #menentukan ganjil atau genap
    return hitung #mengembalikan nilai hitung

angka1 = 4
hasil1 = genap_ganjil(angka1)
print(f"Bilangan {angka1} bernilai {hasil1}")

angka2 = 7
hasil2 = genap_ganjil(angka2)
print(f"Bilangan {angka2} bernilai {hasil2}")
print()

#tugas nomor 3
print(" ## Nomor 3 ##")
def cek_kelulusan(nilai):
    if nilai >= 60:
        return "Lulus"
    else:
        return "gagal"
    
nilai_kamu = 80
status = cek_kelulusan(nilai_kamu)
print(f"Nilai: {nilai_kamu} Status: {status}")