class Hrac:
    #constructor
    def __init__(self, name, age, elo):
        self.name = name  
        self.age = age
        self.elo = elo
    
class Password_generator:
    def create_basic_pass(self, hodnotnejHrac):
        pass_basic = hodnotnejHrac.name + str(hodnotnejHrac.age)
        return pass_basic

h1 = Hrac("Jakub",25,1400)
passw = Password_generator().create_basic_pass(h1)
print(passw)




