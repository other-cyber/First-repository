class Book:
    def __init__(self, title, author, year, genre, is_available=True):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.is_available = is_available
        
    def __str__(self):
        return f"Название {self.title}, автор {self.author}, год {self.year}, жанр {self.genre}, доступна она ли {'да' if self.is_available else 'нет'}"
    
    def borrow(self):
        if self.is_available:
            self.is_available = False
            
    def return_book(self):
        self.is_available = True
                
class Library:
    @property
    def book(self):
        return self.__books
    @property
    def name(self):
            return self.__name
    def __init__(self, name):
        self.__name = name
        self.__books = []
    
    def add_book(self, book):
        self.__books.append(book)  
        
    def remove_book(self, title):
        for i in self.__books:
            if title in i.title:
                self.__books.remove(i)
        
    
    def find_by_author(self, author):
        result = []
        for i in self.__books:
            if author in i.author:
                result.append(i.title)
        return result
    
    def find_by_genre(self, genre):
        result = []
        for i in self.__books:
            if genre in i.genre:
                result.append(i.title)
        return result
    
    def get_available_books(self):
        result = []
        for i in self.__books:
            if i.is_available:
                result.append(i.title)
        return result
    
    def get_books_info(self):
        for b in self.book:
            print(b)
            
    def borrow_book(self, title):
        for i in self.__books:
            if title in i.title:
                if i.is_available:
                    i.is_available = False
    def return_book(self, title):
        for i in self.__books:
            if title in i.title:
                if not i.is_available:
                    i.is_available = True
            
def main():
    # работа с классом Book
    book = Book("Война и мир", "Толстой", 1869, "роман")
    book1 = Book("Преступление и наказание", "Достоевский", 1866, "роман", is_available=False)
    print(book)
    book.borrow()
    print(book)
    book.return_book()
    print(book)
    library = Library("Городская библиотека")
    print(library.name)
    library.add_book(book)
    library.add_book(book1)
    print(library.find_by_author("Толстой"))
    print(library.find_by_genre("роман"))
    print(library.get_available_books())
    library.get_books_info()
    library.borrow_book("Война и мир")
    library.get_books_info()
    library.return_book("Война и мир")
    library.remove_book("Война и мир")
    library.get_books_info()
if __name__ == "__main__":
    main()