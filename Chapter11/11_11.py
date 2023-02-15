from Tombola import Tombola

class Fake(Tombola):
    def pick(self):
        return 13

print(Fake)
f = Fake()