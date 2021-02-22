class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvBooks(self):
        print("Books present in library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(f"You have been issue {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry , This Book is already issued by someone else")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book ! i hope yoy enjoing it")


class Student:
    def requestBook(self):
        self.book = input("Enter the book you want: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book you return: ")
        return self.book


if __name__ == '__main__':
    centeraLibary = Library(["Alogoritham", "Django", "Python notes", "clrs"])
    # centeraLibary.displayAvBooks()
    student = Student()
    while (True):
        welcomeMsg = '''\n =====Welcome to central Library=====
        please choose an option:
        1 . List all the books
        2. Request a book
        3. Return a book
        4. exit the library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centeraLibary.displayAvBooks()
        elif a == 2:
            centeraLibary.borrowBooks(student.requestBook())
        elif a == 3:
            centeraLibary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for using")
            exit()
        else:
            print("Invalid Choice!!")
