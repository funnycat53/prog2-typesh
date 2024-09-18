class kaste():
    def __init__(self, nosaukums, pielietojums, izmers):
        self.nosaukums = nosaukums
        self.pielietojums = pielietojums
        self.izmers = izmers

k1 = kaste("Rando", "Bulciņas", "Liela")
print(k1.nosaukums, k1.pielietojums, k1.izmers)