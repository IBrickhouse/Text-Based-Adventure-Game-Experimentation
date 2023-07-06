#Player always starts with 100 health and stamina
#maybe have health stamina based on age?
#stamina goes down with each move
#when stamina gets too low, they must rest for a time
#stamina regenerates by 1 evey event taken while sitting

class Player:
  def __init__(self, name, age):
    self.name = name
    self.age = age

    if age <=25 and age > 5:
        self.health = 100
        self.energy = 100

    elif age > 25 and age < 50:
        self.health = 75
        self.energy = 75

    elif age > 50:
        self.health = 50
        self.energy = 50
    
    self.weapon = "none"
      
p1 = Player("Jack", 26)

print(p1.weapon)