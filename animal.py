# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

#buat minimal 3 class child (Amphibi,  Mamalia, Carnivora, dll) setiap class child itu memiliki 2 properti dan method  
#buat 3 objek dari masing masing class child. 

class animal:
    def __init__(self, name, makanan, hidup, berkembangbiak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak

    def info_animal(self):
        print("--------------------------------------------------------------")
        print(f"Nama hewan \t\t\t: {self.name}")
        print(f"Makanan \t\t\t: {self.makanan}")
        print(f"Hidup \t\t\t\t: {self.hidup}")
        print(f"Berkembang biak dengan cara \t: {self.berkembangbiak}")
        print("--------------------------------------------------------------")

hewan = animal("Ular python", "Hewan kecil, sedang dan besar", "Darat", "Bertelur beranak")
hewan.info_animal()

