'''
8-6
City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:

"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values that are returned.

Christopher Reesman
5/11/20
'''

def city_country(city, country):
  output = f"{city.title()}, {country.title()}"
  return output

print(city_country('Santiago','Chile'))
print(city_country('Barcelona','Spain'))
print(city_country('Austin','The United States of America'))
