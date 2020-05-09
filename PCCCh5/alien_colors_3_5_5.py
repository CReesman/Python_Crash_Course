'''
5-5. 
Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

*If the alien is green, print a message that the player earned 5 points.
*If the alien is yellow, print a message that the player earned 10 points.
*If the alien is red, print a message that the player earned 15 points.
*Write three versions of this program, making sure each message is printed for the appropriate color alien.
Christopher Reesman
5/7/20
'''

alien_color = ['green']

if 'green' in alien_color:
  print("Player 1 just earned 5 points")
elif 'yellow' in alien_color:
  print("Player 1 just earned 10 points")
else:
  print("Player 1 earned 15 points.")

alien_color = ['yellow']

if 'green' in alien_color:
  print("Player 1 just earned 5 points")
elif 'yellow' in alien_color:
  print("Player 1 just earned 10 points")
else:
  print("Player 1 earned 15 points.")

alien_color = ['red']

if 'green' in alien_color:
  print("Player 1 just earned 5 points")
elif 'yellow' in alien_color:
  print("Player 1 just earned 10 points")
else:
  print("Player 1 earned 15 points.")