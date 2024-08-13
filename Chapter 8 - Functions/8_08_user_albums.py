def make_album(artist_name, album_title, number_of_songs=None):
    
    album = {'Artist name': artist_name.title(), 
             'Album title': album_title.title()}
    
    if number_of_songs:
        album['Number of songs'] = number_of_songs
        
    return album


while True:
    
    print("Enter the album information.")
    print("(Enter 'q' at any time to quit):\n")
    
    artist_name = input("Enter the artist name: ")
    if artist_name == 'q':
        break
    
    album_title = input("Enter the album title: ")
    if album_title == 'q':
        break
    
    number_of_songs = input("Enter the number of songs (digit '0' if none): ")
    
    if number_of_songs == 'q':
        break
    
    number_of_songs = int(number_of_songs)
    
    while number_of_songs < 0:
        number_of_songs = input("\n-> Invalid number! Enter the number of"
                                " songs again (digit '0' if none): ")
            
        if number_of_songs == 'q':
            break
        
        number_of_songs = int(number_of_songs)
    
    album_info = make_album(artist_name, album_title, number_of_songs)
    print(f"\n{album_info}\n\n")