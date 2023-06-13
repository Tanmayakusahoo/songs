recent_playlist = []  # Initialize an empty playlist
capacity = 3  # Set the initial capacity of the playlist

while True:
    song = input("Please enter a song or 'END' to finish: ")

    if song == "END":
        print("You have ended the task")
        break

    if song in recent_playlist:
        recent_playlist.remove(song)  # Remove the song if it already exists in the playlist

    recent_playlist.append(song)  # Add the new song to the playlist

    if len(recent_playlist) > capacity:
        recent_playlist.pop(0)  # Remove the oldest song if the playlist exceeds the capacity

    print(recent_playlist)