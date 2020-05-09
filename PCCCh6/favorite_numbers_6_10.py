'''
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.
Christopher Reesman
5/8/20
'''

favorite_numbers = {
  'Chris': [7,30,22],
  'Laurie': [10,44,78],
  'Luke': [3,1,6],
  'Jan': [15,91,33],
  'Brad': [20,2,64],
  }

for name, numbers in favorite_numbers.items():
  print(f"\n{name.title()}'s favorite numbers are:")
  for number in numbers:
    print(f"\t{number}")