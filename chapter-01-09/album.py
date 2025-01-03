def make_album(artist, title, tracks=None):
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album


albums = [
    make_album("the beatles", "abbey road"),
    make_album("pink floyd", "dark side of the moon"),
    make_album("led zeppelin", "led zeppelin iv"),
    make_album("the rolling stones", "let it bleed"),
    make_album("the who", "who's next"),
    make_album("metallica", "master of puppets"),
    make_album("nirvana", "nevermind"),
    make_album("pearl jam", "ten"),
    make_album("soundgarden", "superunknown"),
    make_album("alice in chains", "dirt"),
    make_album("tool", "lateralus", 13),
    make_album("rage against the machine", "rage against the machine", 10),
    make_album("system of a down", "toxicity", 14),
    make_album("audioslave", "audioslave", 12),
    make_album("stone temple pilots", "core", 12),
]

for album in albums:
    print(album)

while True:
    artist = input("\nArtist: ")
    if artist == "q":
        break

    title = input("Title: ")
    if title == "q":
        break

    tracks = input("Tracks: ")
    if tracks == "q":
        break

    album = make_album(artist, title, tracks)
    print(album)
