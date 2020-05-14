'''
7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.
Christopher Reesman
5/9/20
'''

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"\nThe number {number} is not a multiple of 10.")