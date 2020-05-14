'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
Christopher Reesman
5/11/20
'''

def make_shirt(size='large', text='I love Python'):
  print(f"The shirt size is {size}")
  print(f"\nThe message should read '{text}'")

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'We will rock you!')