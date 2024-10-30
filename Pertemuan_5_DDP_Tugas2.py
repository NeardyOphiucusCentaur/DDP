print("Ini adalah program sederhana untuk menghitung luas bangun datar")
print("pilih salah satu menu angka: \n1. Persegi \n2. Lingkaran \n3. Segitiga")
rumus = int(input("Masukan Rumus Yang ingin di lihat "))
match rumus:
    case 1:
        print("Luas Persegi = sisi*sisi")
        sisi= int(input("Masukan Angka "))
        Luas= sisi*sisi
        print(int(Luas))
    case 2:
        print("Luas Lingkaran = phi*r*r*")
        r= int(input("Masukan Angka "))
        phi= 3.14
        Luas= phi*r*r
        print(int(Luas))
    case 3:
        print("Luas Segitiga = 1/2*alas*tinggi")
        alas= int(input("Masukan Angka alas "))
        tinggi= int(input("Masukan Angka tinggi "))
        Luas= 1/2*alas*tinggi
        print(int(Luas))
    case _:
        print("Salah Pilih")