def make_album(artist_name, album_title, number_of_songs=None):
    """ Catalogue """
    artist = {'name': artist_name, 'album': album_title}
    if number_of_songs:
        artist['numder_of_songs'] = number_of_songs
    return artist


info = []

while True:
    artist_name = input("\nEnter Name: ").title()
    album_title = input("Enter Album: ").title()
    number_of_songs = input("Enter Number of Songs: ")

    info.append(make_album(artist_name, album_title, number_of_songs))

    repeat = input("\nDo you want to enter more names? (yes/no): ").lower()

    if repeat != 'yes':
        break

print("\n--- Catalogue ---")
for name in info:
    print(f"\n{name}")
