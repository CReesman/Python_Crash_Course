'''
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
Christopher Reesman
5/9/20
'''

sandwich_orders = ['tuna','italian','roast beef','turkey','ham','pastrami','pastrami','pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
  current_sandwich = sandwich_orders.pop()

  print(f"\nI made your {current_sandwich.title()}")
  finished_sandwiches.append(current_sandwich)

# Display all confirmed users.
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
  print(finished_sandwich.title())