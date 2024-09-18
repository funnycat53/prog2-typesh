class Cilveks:
    def __init__(self, vards, dzimums, vecums):
        self.name= vards
        self.sex= dzimums
        self.age= vecums
    def dzimsanasdiena(self):
           self.age +=1
           self.BazarsParSevi()

    def mainit_vardu(self, jaunais_vards):
            self.name = jaunais_vards
            self.BazarsParSevi()

    def mainit_dzimumu(self, jaunais_dzimums = ""):
            if jaunais_dzimums == "":
                if self.sex == "s":
                    self.sex = "v"
                else:
                 self.sex = "s"
            else:
                self.dzimums = jaunais_dzimums


    def BazarsParSevi(self):
        if self.sex == "s":
            dzimums = "sieviete"
        elif self.sex == "v":
             dzimums = "vīrietis"
        else:
             dzimums = self.sex
             
        if self.name == "P":
             vards = "Patriks"
        else:
             vards = self.name     
              
        print("Sveiki, mani sauc {}, man ir {} gadi. Es esmu {}.".format(vards, self.age, dzimums))


class Sieviete(Cilveks):
     def __init__(self, vards, hair_color, vecums):
          super().__init__(vards, "s", vecums)
          self.matu_krasa = hair_color
          self.BazarsParSevi()

def BazarsParSevi(self):
     super().BazarsParSevi()
     print("Mana matu krāsa ir", )

persona = Cilveks("Patriks", "V", 18)

persona.BazarsParSevi()
