def make_album(artist_name, album_title):
    """ Catalogue """
    album = {'artist': artist_name, 'album': album_title}
    return album


info = []

while True:
    artist_name = input("\nEnter Name: ").title()
    album_title = input("Enter Album: ").title()

    info.append(make_album(artist_name, album_title))

    repeat = input("\nDo you want to enter more names? (yes/no): ").lower()

    if repeat != 'yes':
        break

print("\n--- Catalogue ---")
for catalogue in info:
    print(f"\n{catalogue}")
