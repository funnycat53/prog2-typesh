class kaste():
    def __init__(self, nosaukums, pielietojums, izmers):
        self.nosaukums = nosaukums
        self.pielietojums = pielietojums
        self.izmers = izmers

    def mainit_nosaukums(self, jaunais_nosaukums):
        self.nosaukums = jaunais_nosaukums

    def mainit_izmeru(self, jaunais_izmers):
        if jaunais_izmers == "L":
            jaunais_izmers = "Liela"
        elif jaunais_izmers == "M":
            jaunais_izmers = "Vidēja"
        elif jaunais_izmers == "S":
            jaunais_izmers = "Maza"
        else:
            self.izmers = jaunais_izmers

    def info(self, jaunais_pielietojums):
        if jaunais_pielietojums == "b":
            jaunais_pielietojums = "Bulciņas"
        elif jaunais_pielietojums == "k":
            jaunais_pielietojums = "Kūciņas"
        elif jaunais_pielietojums == "s":
            jaunais_pielietojums = "Suliņas"
        else:
            self.pielietojums = jaunais_pielietojums

        return f"Kastes nosaukums ir {self.nosaukums}. Ta tiek pielietota, lai pārvadātu {self.pielietojums}. Tās izmērs ir {self.izmers}"