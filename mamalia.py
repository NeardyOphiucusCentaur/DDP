from animal import animal
class Mamalia(animal):
    def __init__(self, name, makanan, hidup, berkembangbiak, fiturtubuh, darah):
        super().__init__(name, makanan, hidup, berkembangbiak)
        self.fiturtubuh = fiturtubuh
        self.darah = darah

    def info_mamalia(self):
        super().info_animal()
        print("==========Ciri Khas Mamalia==========")
        print(f"Fitur tubuh \t\t\t: {self.fiturtubuh}")
        print(f"Berdarah \t\t: {self.darah}")
        print("--------------------------------------------------------------")

hewan = Mamalia("Paus biru", "Plankton", "Laut", "Melahirkan", "Kelenjar air susu", "Panas")
hewan.info_mamalia()