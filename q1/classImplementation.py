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
        if duration < 0:
            
    