playlist = {
    "playlist" : "chill",
    "songs" :
    [
        {"title" : "number 41", "artist" : "dave matthews band", "duration" : 4.55, "album": "Crash"},
        {"title" : "crash", "artist" : "dave matthews band", "duration" : 2.32, "album" : "ants marching"}
    ]

}

for val in playlist["songs"]:
    total_length = val["duration"]
    print(total_length)
