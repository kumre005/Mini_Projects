class Library:
    def __init__(self):
        self.noBooks = 0
        self.Books = []

    def addBooks(self, Book):
        self.Books.append(Book)
        self.noBooks = len(self.Books)

    def showInfo(self):
        print(f"The library has {self.noBooks}")

        print("The Books are :- ")

        for Book in self.Books:
            print(f"* {Book}")

l1 = Library()
l1.addBooks("Harry Potter")
l1.addBooks("Commando")
l1.addBooks("Nothing matters...!")
l1.showInfo()
