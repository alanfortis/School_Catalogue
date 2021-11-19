class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  def get_Name(self):
    return self.name
  def get_Level(self):
    return self.level
  def get_NumberOfStudents(self):
    return self.numberOfStudents
  def set_NumberOfStudents(self, new_NumberOfStudents):
    self.numberOfStudents = new_NumberOfStudents
  def __repr__(self):
    return "A {level} school named {name} with {numberOfStudents} students".format(level = self.level, name = self.name, numberOfStudents = self.numberOfStudents)
mySchool = School("Mystery", "High", 97)
print(mySchool)
print(mySchool.get_Name())
print(mySchool.get_Level())
mySchool.set_NumberOfStudents(200)
print(mySchool.get_NumberOfStudents())
class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy
  def get_pickupPolicy(self):
    return self.pickupPolicy
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + " The pickup polity is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)
primarando = PrimarySchool("Shkola", 300, "Pickup Allowed")
print(primarando.get_pickupPolicy())
print(primarando)
class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams
  def get_sportTeams(self):
    return self.sportsTeams
  def __repr__(self):
    partentClass = super().__repr__()
    return partentClass + " SportsTeam here is {sportsTeams}".format(sportsTeams = self.sportsTeams)
objecto_morale = HighSchool("High Morale", 999, ["Footbal", "ValleyBall"])
print(objecto_morale.get_sportTeams)
print(objecto_morale)
