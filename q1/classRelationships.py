class Ppop:
    def __init__(self, name: str, created: str):
        self.name = name
        self.created = created
        self.Ppop_list =[]
    def play(self) -> None:
        print(f"Playing: {self.name} by {self.author}")
    def pause(self) -> None:
        return(f"Paused: {self.name} by {self.author}")
    def fast_forward(self, seconds: int) -> None:
        return(f"Fast forwarding {seconds} seconds in {self.name} by {self.author}")
    def get_duration(self) -> int:
        return self.__private_duration
    def set_duration(self, duration: int) -> None:
        if duration.strip():
            self.__private_duration = duration
            print(f"Duration set to {duration} seconds for {self.name} by {self.author}")
        else:
            print("Invalid duration. Please provide a valid duration.")

if __name__ == "__main__":
    song = Ppop("Lifetime", "Ben&Ben", "", 277, "06-04-2020")
    song2 = Ppop("Kalapastangan", "fitterkarma", "", 276, "11-24-2023")
    print("--- BEFORE ---") 
    song.play()
    print(song.pause())
    print(song.fast_forward(30))
    print(f"Duration: {song.get_duration()} seconds")
    song.set_duration("200")
    print(f"Updated Duration: {song.get_duration()} seconds")
    song2.play()
    print(song2.pause())
    print(song2.fast_forward(50))
    print(f"Duration: {song2.get_duration()} seconds")
    song2.set_duration("250")
    print(f"Updated Duration: {song2.get_duration()} seconds")

    print("--- AFTER ---")
    print(f"Object 1: {song.name}, {song.author}, {song.get_duration()} seconds, {song._Ppop__private_release_date}")
    print(f"Object 2: {song2.name}, {song2.author}, {song2.get_duration()} seconds, {song2._Ppop__private_release_date}")

#New Class
class Album:
    def __init__(self, name: str, created: str):
        self.name = name
        self.created = created
        self.pop_list = []

    def add_pop(self, ppop: Ppop) -> None:
        self.pop_list.append(ppop)
        print(f"Added '{ppop.name}' to '{self.name}' album.")

    def display_album(self) -> None:
        print(f"Album: {self.name} (Created: {self.created})")
        if not self.pop_list:
            print("Album is empty.")
            return

        for ppop in self.pop_list:
            print(f"- {ppop.name} by {ppop.author}, {ppop.get_duration()} seconds")


if __name__ == "__main__":
    print("--- BEFORE ---")
    song = Ppop("Lifetime", "", "Ben&Ben", 277, "06-04-2020")
    song2 = Ppop("Kalapastangan", "", "fitterkarma", 276, "11-24-2023")

    song.play()
    print(song.pause())
    print(song.fast_forward(30))
    print(f"Duration: {song.get_duration()} seconds")
    song.set_duration("200")
    print(f"Updated Duration: {song.get_duration()} seconds")

    song2.play()
    print(song2.pause())
    print(song2.fast_forward(50))
    print(f"Duration: {song2.get_duration()} seconds")
    song2.set_duration("250")
    print(f"Updated Duration: {song2.get_duration()} seconds")

    print("--- AFTER ---")
    print(f"Object 1: {song.name}, {song.author}, {song.get_duration()} seconds, {song._Ppop__private_release_date}")
    print(f"Object 2: {song2.name}, {song2.author}, {song2.get_duration()} seconds, {song2._Ppop__private_release_date}")

    print("=== I. BEFORE RELATIONSHIP ===")
    album = Album("P-pop Album", "09-21-2011")

    print(f"Album created: '{album.name}' with no songs.")
    print(f"Object 1: {song.name}, {song.author}, {song.get_duration()} seconds, {song._Ppop__private_release_date}")
    print(f"Object 2: {song2.name}, {song2.author}, {song2.get_duration()} seconds, {song2._Ppop__private_release_date}")

    print("=== II. BUILDING RELATIONSHIP ===")
    album.add_pop(song)
    album.add_pop(song2)

    print("=== III. AFTER RELATIONSHIP ===")
    album.display_album()


    
