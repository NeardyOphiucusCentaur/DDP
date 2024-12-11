from animal import animal

class Amphibi(animal):
    def __init__(self, name, makanan, hidup, berkembangbiak, jenisair, bernapas):
        super().__init__(name, makanan, hidup, berkembangbiak)
        self.jenisair = jenisair
        self.bernapas = bernapas

    def info_amphibi(self):
        super().info_animal()
        print("==========Ciri Khas Amphibi==========")
        print(f"Jenis air \t\t\t: {self.jenisair}")
        print(f"Bernapas dengan \t\t: {self.bernapas}")
        print("--------------------------------------------------------------") 

hewan = Amphibi("Salamander", "Moluska", "Darat dan air", "Bertelur", "Air tawar", "Paru-paru dan insang")
hewan.info_amphibi()