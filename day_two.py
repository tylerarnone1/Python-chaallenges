#1--------------------------------------------

student = ['Kyle','Don','drew']
print(students[1])
print(students[2])

#2--------------------------------------------

foods = ('pasta','pizza', 'meatloaf')
for food in foods:
    print(f'{food} is dope')
    
for food in foods[1:]:
    print(food)
#3-------------------------------------------------------

home_town = {
    'city':'Phoenix',
    'state': 'Arizona',
    'population': 1626000
}
print(f"I am from {home_town['city']}, {home_town['state']}. It has a population
      of {home_town['population']}")
 #4----------------------------------------------------------     
      for key, value in home_town.items():
  print(f"{key} = {value}")

#5----------------------------------------------------------


  cohort = {
    'students': ('Jim','Bell','Bob'),
    'fav-food': ('pizza', 'cocopuffs','fruit')
    
}
for key,value in cohort.items():
  print(f'{key} = {value}')

#6------------------------------------------------------

awesome_students = ['is awesome']


for student in awesome_students:
  print(f'student{key} {awesome_students}')

#7-------------------------------------------------------------

for food in [food for food in foods if 'a' in food]:
  print(food)