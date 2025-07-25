import time


class illness:
   def __init__(self, pet):
      self.pet = pet
      pass
   
class ick(illness):
  def __init__(self, pet):
      self.pet = pet 
      pet.sicknessname = "ick"
      alive = True
      while alive == True: 
        self.attack(pet)
        time.sleep(5)
      pass
  
  def attack(pet):
    pet.health -= 15
    pet.issick = True
    pet.metabolism -= 25

    pass

  def treated(pet):
     global alive
     pet.issick = False
     alive = False
     if pet.metabolism > 100:
       pet.metabolism = 100