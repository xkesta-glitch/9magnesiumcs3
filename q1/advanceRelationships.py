class PpopGroups(Ppop):
    def __init__(self, name: str, author: str, duration: int, release_date: str, group: str):
        super().__init__(name, "", author, duration, release_date)
        self.group = group

    def get_name(self) -> str:
        return f"{self.name} [{self.group}]"

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
    album = Album("P-pop Album", "09-21-2011")

    album.add_pop(song)
    album.add_pop(song2)

    album.display_album()
