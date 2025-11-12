class SuperHero:
    
    sound = 'Poww' #class attribute

    def __init__(self , name , city):
        self.name = name   # instance attribute
        self.city = city

    def __str__(self):
        return f"{self.name} is the hero of {self.city} city"

    #class methods
    def get_name(self):
        print(self.name)
    

first_super_hero = SuperHero("batman" , "gotham")


first_super_hero.get_name()
print(first_super_hero.city) #accessing the class
print(first_super_hero)