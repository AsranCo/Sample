##پیشنهاد موسیقی


all_users = {}
all_albums = {}


def add_user(username, age, city, albums, all_users, all_albums):
    all_users[username] = age, city, albums


def add_album(album_name, artist_name, genre, tracks, all_users, all_albums):
    all_albums[album_name] = genre, artist_name, tracks


def query_user_artist(username, artist_name, all_users, all_albums):
    counter = 0
    albums_name = []
    if username in all_users.keys():
        for album_index in all_users[username][2]:
            albums_name.append(album_index)
    for albums in albums_name:
        for a in all_albums[albums]:
            if a == artist_name:
                counter = counter + all_albums[albums][2]
    return (counter)


def query_user_genre(username, genre, all_users, all_albums):
    counter = 0
    albums_name = []
    if username in all_users.keys():
        for album_index in all_users[username][2]:
            albums_name.append(album_index)
    for albums in albums_name:
        for a in all_albums[albums]:
            if a == genre:
                counter = counter + all_albums[albums][2]
    return (counter)


def query_age_artist(age, artist_name, all_users, all_albums):
    counter = 0
    albums_name = []
    for a in all_users.values():
        if age in a:
            albums_name = (a[2])

    for albums in albums_name:
        for a in all_albums[albums]:

            if a == artist_name:
                counter = counter + all_albums[albums][2]
    return (counter)


def query_age_genre(age, genre, all_users, all_albums):
    counter = 0
    albums_name = []
    for a in all_users.values():
        if age in a:
            albums_name = (a[2])

    for albums in albums_name:
        for a in all_albums[albums]:
            if a == genre:
                counter = counter + all_albums[albums][2]
    return (counter)


def query_city_artist(city, artist_name, all_users, all_albums):
    counter = 0
    albums_name = []
    for a in all_users.values():
        if city in a:
            albums_name = (a[2])

    for albums in albums_name:
        for a in all_albums[albums]:
            if a == artist_name:
                counter = counter + all_albums[albums][2]
    return (counter)


def query_city_genre(city, genre, all_users, all_albums):
    counter = 0
    albums_name = []
    for a in all_users.values():
        if city in a:
            albums_name = (a[2])

    for albums in albums_name:
        for a in all_albums[albums]:
            if a == genre:
                counter = counter + all_albums[albums][2]
    return (counter)


add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], all_users, all_albums)
add_user("Saeid", 22, "Esfehan", ["eclipse", "barf", "gavazn"], all_users, all_albums)
add_album("eclipse", "malmsteen", "classic", 10, all_users, all_albums)
add_album("barf", "beeptunes", "pop", 22, all_users, all_albums)
add_album("tekunbede", "beeptunes", "pop", 14, all_users, all_albums)
add_album("gavazn", "sorena", "persian", 18, all_users, all_albums)
add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], all_users, all_albums)
add_album("bidad", "shajarian", "classic", 10, all_users, all_albums)
add_album("blaze", "ghorbani", "pop", 9, all_users, all_albums)

# query_user_artist("SAliB", "beeptunes", all_users, all_albums)
# query_user_artist("Ali", "ghorbani", all_users, all_albums)
# query_user_genre("Ali", "classic", all_users, all_albums)
# query_age_artist(12, "shajarian", all_users, all_albums)
# query_age_artist(22, "malmsteen", all_users, all_albums)
# query_age_genre(19, "pop", all_users, all_albums)
# query_age_genre(12, "pop", all_users, all_albums)
# query_city_artist("Bushehr", "ghorbani", all_users, all_albums)
# query_city_artist("Tehran", "sorena", all_users, all_albums)
query_city_genre("Tehran", "pop", all_users, all_albums)
