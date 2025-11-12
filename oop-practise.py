class SuperHero:
    name = ''
    height = ''
    city = ''
    
    def get_name(self):
        print(self.name)
    

first_super_hero = SuperHero()
first_super_hero.name = 'Batman'

first_super_hero.get_name()
print(first_super_hero.city)