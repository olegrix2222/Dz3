class Person:
  height = 139
  name = "name"
  is_sad = True
  def __init__(self, name, height):
    self.name = name
    self.height = height

class Cat:
  name = "Murzik"
  
  def __init__(self, name):
   self.name = name

  def play_w_human(self, human):
    human.is_sad = False


me = Person("Oleg", 11)
my_pet = Cat("Murzik") 
my_friend =Person("Makar", 11)
my_friend2 =Person("Zakhar", 12)
my_friend3 =Person("Dima", 15)

print(me.is_sad)
my_pet.play_w_human(me)
print("Sad - ", me.is_sad)

print(my_friend.is_sad)
my_pet.play_w_human(my_friend)
print("Sad - ", my_friend.is_sad)

print(my_friend2.is_sad)
my_pet.play_w_human(my_friend2)
print("Sad - ", my_friend2.is_sad)

print(my_friend3.is_sad)
my_pet.play_w_human(my_friend3)
print("Sad - ", my_friend3.is_sad)