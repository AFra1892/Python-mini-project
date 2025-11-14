class SuperHero:
    
    sound = 'Poww' #class attribute

    def __init__(self , name , city , power):
        self.name = name   # instance attribute
        self.power = power
        self.city = city

    def __str__(self):
        return f"{self.name} is the hero of {self.city} city"

    #class methods
    def get_name(self):
        print(self.name)
    
class SideKick(SuperHero):
    def get_power(self):
        return self.power


first_super_hero = SuperHero("batman" , "gotham" , 'being-rich')
first_sideKick = SideKick('robin' , 'gotham' , 'no-power')
first_super_hero.get_name()
print(first_super_hero.city) #accessing the class
print(first_super_hero)
print(first_sideKick.get_power())