# OOPACT-PartII
class Ppop:
    def __init__(self, name: str, age: str, author: str, __private_duration: int, __private_release_date: str):
        self.name = name
        self.author = author
        self.__private_duration = __private_duration
        self.__private_release_date = __private_release_date
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
