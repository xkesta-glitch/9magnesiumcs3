class Publication: #Creates a class
  def __init__(self, title: str, author: str): #Creates a constructor that takes title and author as attributes
    self.__title = title #Asigns the title attribute to private
    self.__author = author #Asings the author attribute to private

  @property #Turns the function into an attribute
  def get_title(self): 
    return self.__title #Returns the title

  @property #Turns the function into an attribute
  def get_author(self):
    return self.__author #Returns the author

  @get_title.setter #Allows the title to be set
  def set_title(self, title):
    self.__title = title #Returns the new title

  @get_author.setter #Allows the author to be set
  def set_author(self, author):
    self.__author = author #Returns the new author

  def display_info(self): #Displays the title and author
    print(f"Title: {self.__title}") #Prints the title
    print(f"Author: {self.__author}") #Prints the author

class Book(Publication): #Creates a class that inherits from Publication
  def __init__(self, title: str, author: str, number_pages: int): #Creates a constructor that takes title, author, and number_pages as attributes
    super().__init__(title, author) #Calls the constructor of the parent class
    self.__number_pages = number_pages #Assigns the number_pages attribute to private

  @property #Turns the function into an attribute
  def get_number_pages(self):
    return self.__number_pages #Returns the number of pages

  @get_number_pages.setter #Allows the number of pages to be set
  def set_number_pages(self, number_pages):
    if number_pages > 0: #Checks if the pages is greater than 0
        self.__number_pages = number_pages #Returns the new number of pages

class Magazine(Publication): #Creates a class that inherits from Publication
  def __init__(self, title: str, author: str, issue_number: int): #Creates a constructor that takes title, author, and issue_number as attributes
    super().__init__(title, author) #Calls the constructor of the parent class
    self.__issue_number = issue_number #Assigns the issue_number attribute to private

  @property #Turns the function into an attribute
  def get_issue_number(self):
    return self.__issue_number #Returns the issue number

  @get_issue_number.setter #Allows the issue number to be set
  def set_issue_number(self, issue_number):
    self.__issue_number = issue_number #Returns the new issue number

publication1 = Publication("The Great Gatsby", "F. Scott Fitzgerald") #Creates an object for Publication
book1 = Book("To Kill a Mockingbird", "Harper Lee", 281) #Creates an object for Book
magazine1 = Magazine("National Geographic", "Various Authors", 202) #Creates an object for Magazine

print("Publication Info:") #Prints the publication info
publication1.display_info() #Prints the title and author of the publication

print("\nBook Info:") #Prints the book info
book1.set_number_pages = -300 #Sets an invalid number of pages
book1.display_info() #Prints the title and author of the book
print(f"Number of Pages: {book1.get_number_pages}") #Prints the number of pages

print("\nMagazine Info:") #Prints the magazine info
magazine1.display_info() #Prints the title and author of the magazine
print(f"Issue Number: {magazine1.get_issue_number}") #Prints the issue number
