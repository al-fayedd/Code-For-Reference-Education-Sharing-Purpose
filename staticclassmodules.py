class Book:
    total_books = 0

    def __init__(self, title, author):
        if not self.is_valid_title(title):
            raise ValueError("Title must be a non-empty string")
        self.title = title
        self.author = author
        Book.total_books += 1

    def get_info(self):
        return f"{self.title} by {self.author}"

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and title.strip() != ""
    @classmethod
    def get_total_books(cls):
        """Returns the total number of Book instances created."""
        return cls.total_books
    
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")
book4 = Book("Pride and Prejudice", "Jane Austen")
book5 = Book("The Catcher in the Rye", "J. D. Salinger")
book6 = Book("The Hobbit", "J. R. R. Tolkien")
book7 = Book("The Lord of the Rings", "J. R. R. Tolkien")
book8 = Book("The Catcher in the Rye", "J. D. Salinger")
book9 = Book("The Great Gatsby", "F. Scott Fitzgerald")


print(book3.get_info())
print(book7.get_info())

print(Book.is_valid_title("The Illiad"))
print(Book.get_total_books())
    
    
