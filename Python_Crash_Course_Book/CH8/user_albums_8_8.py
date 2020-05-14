'''
8-8
User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
Christopher Reesman
5/12/20
'''

def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

while True:
  print("\nPlease tell me the artist:")
  print("(enter 'q' at any time to quit)")

  artist = input("Artist: ")
  if artist == 'q':
    break

  title = input("Album Title: ")
  if title == 'q':
    break

  formatted_make_album = make_album(artist, title)
  print(f"\n{formatted_make_album}!")