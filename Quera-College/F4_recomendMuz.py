##پیشنهاد موسیقی


all_users = {}
all_albums = {}


def add_user(username, age, city, albums, all_users, all_albums):
    all_users[username, age, city] = albums


def add_album(album_name, artist_name, genre, tracks, all_users, all_albums):
    all_albums[album_name, artist_name, genre] = tracks


def query_user_artist(username, artist_name, all_users, all_albums):
    counter = 0
    albums_name = []

    for use in all_users.keys():
        if username in use:
            albums_name.append(all_users[use])

    for alb in range(len(albums_name)):
        for albums in albums_name[alb]:
            for use in all_albums.keys():
                if artist_name in use and albums in use:
                    counter = counter + all_albums[use]
    return counter


def query_user_genre(username, genre, all_users, all_albums):
    counter = 0
    albums_name = []

    for use in all_users.keys():
        if username in use:
            albums_name.append(all_users[use])

    for alb in range(len(albums_name)):
        for albums in albums_name[alb]:
            for use in all_albums.keys():
                if genre in use and albums in use:
                    counter = counter + all_albums[use]
    return counter


def query_age_artist(age, artist_name, all_users, all_albums):
    counter = 0
    albums_name = []

    for use in all_users.keys():
        if age in use:
            albums_name.append(all_users[use])

    for alb in range(len(albums_name)):
        for albums in albums_name[alb]:
            for use in all_albums.keys():
                if artist_name in use and albums in use:
                    counter = counter + all_albums[use]
    return counter


def query_age_genre(age, genre, all_users, all_albums):
    counter = 0
    albums_name = []
    for use in all_users.keys():
        if age in use:
            albums_name.append(all_users[use])

    for alb in range(len(albums_name)):
        for albums in albums_name[alb]:
            for use in all_albums.keys():
                if genre in use and albums in use:
                    counter = counter + all_albums[use]
    return counter


def query_city_artist(city, artist_name, all_users, all_albums):
    counter = 0
    albums_name = []
    for use in all_users.keys():
        if city in use:
            albums_name.append(all_users[use])

    for alb in range(len(albums_name)):
        for albums in albums_name[alb]:
            for use in all_albums.keys():
                if artist_name in use and albums in use:
                    counter = counter + all_albums[use]
    return counter


def query_city_genre(city, genre, all_users, all_albums):
    counter = 0
    albums_name = []
    for use in all_users.keys():
        if city in use:
            albums_name.append(all_users[use])

    for alb in range(len(albums_name)):
        for albums in albums_name[alb]:
            for use in all_albums.keys():
                if genre in use and albums in use:
                    counter = counter + all_albums[use]
    return counter


##------------------------------------------------------ todo پاسخ دیگران
# all_users = dict()
# all_albums = dict()
#
#
# def add_user(username, age, city, albums, all_users, all_albums):
#     all_users[username] = {"age" : age , "city" : city , "albums" : albums}
#
#
# def add_album(album_name, artist_name, genre, tracks, all_users, all_albums):
#     all_albums[album_name] = {"artist_name" : artist_name , "genre" : genre , "tracks" : tracks}
#
#
# def query_user_artist(username, artist_name, all_users, all_albums):
#     numberOfTracks = 0
#     for i in all_users[username]["albums"]:
#         if all_albums[i]["artist_name"] == artist_name :
#             numberOfTracks += all_albums[i]["tracks"]
#     return numberOfTracks
#
#
# def query_user_genre(username, genre, all_users, all_albums):
#     numberOfTracks = 0
#     for i in all_users[username]["albums"]:
#         if all_albums[i]["genre"] == genre :
#             numberOfTracks += all_albums[i]["tracks"]
#     return numberOfTracks
#
#
# def query_age_artist(age, artist_name, all_users, all_albums):
#     numberOfTracks = 0
#     for i in all_users :
#         if all_users[i]["age"] == age :
#             numberOfTracks += query_user_artist(i, artist_name, all_users, all_albums)
#     return numberOfTracks
#
# def query_age_genre(age, genre, all_users, all_albums):
#     numberOfTracks = 0
#     for i in all_users :
#         if all_users[i]["age"] == age :
#             numberOfTracks += query_user_genre(i, genre, all_users, all_albums)
#     return numberOfTracks
#
#
# def query_city_artist(city, artist_name, all_users, all_albums):
#     numberOfTracks = 0
#     for i in all_users :
#         if all_users[i]["city"] == city :
#             numberOfTracks += query_user_artist(i, artist_name, all_users, all_albums)
#     return numberOfTracks
#
# def query_city_genre(city, genre, all_users, all_albums):
#     numberOfTracks = 0
#     for i in all_users :
#         if all_users[i]["city"] == city :
#             numberOfTracks += query_user_genre(i, genre, all_users, all_albums)
#     return numberOfTracks

add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], all_users, all_albums)
add_user("Saeid", 22, "Esfehan", ["eclipse", "barf", "gavazn"], all_users, all_albums)
add_user("reza", 22, "Esfehan", ["eclipse", "barf", "gavazn"], all_users, all_albums)
add_album("eclipse", "malmsteen", "classic", 10, all_users, all_albums)
add_album("barf", "beeptunes", "pop", 22, all_users, all_albums)
add_album("tekunbede", "beeptunes", "pop", 14, all_users, all_albums)
add_album("gavazn", "sorena", "persian", 18, all_users, all_albums)
add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], all_users, all_albums)
add_album("bidad", "shajarian", "classic", 10, all_users, all_albums)
add_album("blaze", "ghorbani", "pop", 9, all_users, all_albums)
add_album("bidad", "ghorbani", "pop", 9, all_users, all_albums)
# query_user_artist("Ali", "ghorbani", all_users, all_albums)
# print(query_user_artist("SAliB", "sorena", all_users, all_albums))
# print(query_user_artist("SAliB", "beeptunes", all_users, all_albums))
# print(query_user_genre("SAliB", "pop", all_users, all_albums))
print(query_age_artist(22, "malmsteen", all_users, all_albums))
# print(query_age_genre(19, "pop", all_users, all_albums))
# print(query_city_artist("Tehran", "sorena", all_users, all_albums))
# print(query_city_genre("Tehran", "pop", all_users, all_albums))
# print(query_age_artist(22, "malmsteen", all_users, all_albums))
# print(query_age_artist(12, "shajarian", all_users, all_albums))
# print(query_age_artist(12, "ghorbani", all_users, all_albums))
