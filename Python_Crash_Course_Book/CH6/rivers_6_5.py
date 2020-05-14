'''
6-5
Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
Use a loop to print the name of each river included in the dictionary.
Use a loop to print the name of each country included in the dictionary.
Christohper Reesman
5/7/20
'''

rivers = {
    'amazon': 'brazil',
    'mississippi': 'united states of america',
    'nile': 'egypt',
    }

for key, value in rivers.items():
  print(f"The {key.title()} runs through {value.title()}")

for name in rivers.keys():
  print(name.title())

for name in rivers.values():
  print(name.title())