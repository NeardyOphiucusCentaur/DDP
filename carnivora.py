from animal import animal
class Carnivora(animal):
    def __init__(self, name, makanan, hidup, berkembangbiak, jenismakanan, rantaimakanan):
        super().__init__(name, makanan, hidup, berkembangbiak)
        self.jenismakanan = jenismakanan
        self.rantaimakanan = rantaimakanan

    def info_carnivora(self):
        super().info_animal()
        print("==========Ciri Khas Carnivora==========")
        print(f"Jenis makanan \t\t\t: {self.jenismakanan}")
        print(f"Posisi rantai makanan \t\t: {self.rantaimakanan}")
        print("--------------------------------------------------------------")

hewan = Carnivora("Paus orca", "Hewan laut besar", "Laut", "Melahirkan", "Daging", "Predator")
hewan.info_carnivora()