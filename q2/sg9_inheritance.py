class Publication:
  def __init__(self, title: str, author: str):
    self.title(title)
    self.author(author)

  def get_title(self, title: str):
    self.__title = str(title)

  def get_author(self, author: str):
    self.__author = str(author)

  def set_title(self, title: str):
    self.__title(title)
    x1.set_title("To Kill a Mockingbird")

  def set_author(self, author: str):
    self.__author(author)
    
