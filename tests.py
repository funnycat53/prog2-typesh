class Cilveks:
    def __init__(self, vards, dzimums, vecums):
        self.name= vards
        self.sex= dzimums
        self.age= vecums
    def dzimsanasdiena(self):
            self.age +=1
    def BazarsParSevi(self):
        if self.sex == "S":
            dzimums = "sieviete"
        elif self.sex == "V":
            dzimums = "vīrietis"
        else:
             dzimums = self.sex
        
        if self.name == "P":
             vards = "Patriks"
        else:
             vards = self.name     
        print("Sveiki, mani sauc {}, man ir {} gadi. Es esmu {}.".format(vards, self.age, dzimums))

persona = Cilveks("P", "V", 18)
persona1 = Cilveks("Anna", "S", 23)


persona.BazarsParSevi()

