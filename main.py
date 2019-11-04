from classes import Artist, Album, Song
# import classes as clx

if __name__ == "__main__":
    art1 = Artist("Mettalica", "USA")
    alb1 = Album('Death magnetic', 2008, 'Thrash metal', art1)
    song1 = Song('That Was Just Your Life', 2008, 426, art1, alb1)
    song2 = Song('The End of the Line', 2008, 470,  art1, alb1)
    alb2 = Album('St. Anger', 2003, 'Thrash metal', art1)
    song3 = Song('Frantic', 2003, 348,  art1, alb2)
    art2 = Artist('Motorhead', "USA")
    song4 = Song('Enter Sandman', 1991, 330, art1)
    song4.add_artist(art2)

    print(art1.songs_number, alb1.duration,
          alb1.songs_number, art1.album_number,
          song4.features, art2.album_number)


