'''
6-8 
Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
Christopher Reesman
5/8/20
'''

alex = {'anmial': 'cat','owner': 'Chris'}
opal = {'anmial': 'cat','owner': 'Laurie'}
chloe = {'animal': 'dog','owner': 'Amber'}
tocket = {'animal': 'dog','owner': 'Brad'}

pets = [alex, opal, chloe, tocket]

for name, languages in favorite_languages.items():
       print(f"\n{name.title()}'s favorite languages are:")
➌     for language in languages:
           print(f"\t{language.title()}")

