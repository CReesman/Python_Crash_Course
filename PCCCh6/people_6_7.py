'''
6-7. 
People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
Christopher Reesman
5/8/20
'''

person1 = {'first_name': 'Christopher','last_name': 'Reesman','age': 38,'city': 'Hummelstown'}
person2 = {'first_name': 'Laurie','last_name': 'Reesman','age': 40,'city': 'Hummelstown'}
person3 = {'first_name': 'Donna','last_name': 'Reesman','age': 68, 'city': 'Lebanon'}

people = [person1, person2, person3]

for person in people:
  print(person)