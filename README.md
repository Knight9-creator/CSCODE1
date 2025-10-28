playlist = ["Love", "Like", "Subscribe"]

while True:
    print("\nPlaylist:", playlist)
    print("(a)dd (i)nsert (r)emove (p)op (s)ort (v)iew (q)uit")
    choice = input("Choose: ").strip().lower()
    if choice == "q":
        print("Goodbye!")
        break
    elif choice == "a":
        playlist.append(input("Name of song to add: "))
    elif choice == "i":
        playlist.append(input("Name of song to input: "))
    elif choice == "r":
        playlist.remove(input("Name of song to Remove: "))
    elif choice == "p":
        inp = input("Name of song to Delete(pop): ")

        for i in range(len(playlist)):
            x = playlist[i]
            if x == inp:
                y=i
                break

        playlist.pop(y)
    elif choice == "s":
        playlist.sort()
        print("Sorted Playlist!")
    elif choice == "v":
        print(playlist)
    else:
        print("Enter a valid character based on the prompt...")
