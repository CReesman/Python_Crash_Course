'''
4-10
Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

*Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
*Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
*Print the message The last three items in the list are:. Use a slice to print the last three items in the list.
Christopher Reesman
5/5/20
'''

pizza = ['pepperoni', 'mushroom', 'green pepper','ham','pineapple']
for topping in pizza:
  print(f"I like {topping} pizza")

print("I really love pizza!")
print(f"The first three items in the list are: {pizza[:3]}")
print(f"Three items from the middle of the list are: {pizza[1:4]}")
print(f"The last three items in the list are: {pizza[-3:]}")