def make_album(artist_name, album_title, number_of_songs=None):
    
    album = {'Artist name': artist_name.title(), 'Album title': album_title.title()}
    
    if number_of_songs:
        album['Number of songs'] = number_of_songs
        
    return album

album_info = make_album("David Foster", "Single", number_of_songs=4)
print(album_info)

album_info = make_album("Coldplay", "Ghost Stories", number_of_songs=8)
print(album_info)

album_info =  make_album("Earth, Wind & Fire", "That's the Way of the World")
print(album_info)