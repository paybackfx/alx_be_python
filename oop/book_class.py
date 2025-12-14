class Book:
    """A class representing a book with title, author, and publication year."""

    def __init__(self, title: str, author: str, year: int):
        """Initialize the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor method that prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
