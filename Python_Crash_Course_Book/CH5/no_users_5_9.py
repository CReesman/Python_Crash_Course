'''
5-9
No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.

If the list is empty, print the message We need to find some users!
Remove all of the usernames from your list, and make sure the correct message is printed.
Christopher Reesman
5/7/20
'''

usernames = []

if usernames:
  for name in usernames:
    if name == 'admin':
      print("Hello admin, would you like to see a status report?")
    else:
      print("Hello Jaden, thank you for logging in again.")
else:
  print("We need to find some users!")