# library_management.py

class LibraryManagement:
    """
    Library Management System

    This module uses lists, sets, tuples, and dictionaries to manage library data. It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

    Data Structures:

    1. Lists: To store collections of books, members, and loans.
    2. Tuples: To store immutable book and member details.
    3. Sets: To manage unique genres and authors.
    4. Dictionaries: To map book IDs and member IDs to their details and manage loan records.

    List of books with details (Book ID, Title, Author, Genre, Availability):
    books = [
        (1, "1984", "George Orwell", "Dystopian", True),
        (2, "To Kill a Mockingbird", "Harper Lee", "Fiction", True),
        (3, "The Great Gatsby", "F. Scott Fitzgerald", "Classic", False),
        (4, "Moby Dick", "Herman Melville", "Adventure", True),
        (5, "War and Peace", "Leo Tolstoy", "Historical", False)
    ]

    List of members with details (Member ID, Name, Age, Membership Type):
    members = [
        (101, "Alice", 30, "Premium"),
        (102, "Bob", 25, "Standard"),
        (103, "Charlie", 28, "Premium"),
        (104, "Diana", 35, "Standard"),
        (105, "Eve", 40, "Premium")
    ]

    List of loans (Loan ID, Book ID, Member ID, Loan Date, Return Date):
    loans = [
        (1001, 1, 101, "2023-01-01", "2023-01-15"),
        (1002, 3, 102, "2023-01-10", None),
        (1003, 5, 103, "2023-01-12", None)
    ]

    Set of unique genres:
    genres = set()

    Adding genres from books:
    for book in books:
        genres.add(book[3])

    Set of unique authors:
    authors = set()

    Adding authors from books:
    for book in books:
        authors.add(book[2])

    Dictionary to map book IDs to their details:
    book_catalog = {book[0]: book for book in books}

    Dictionary to map member IDs to their details:
    member_catalog = {member[0]: member for member in members}

    Dictionary to manage loan records:
    loan_records = {loan[0]: loan for loan in loans}

    Functions:

    List-Related Methods:
    1. find_book_index(book_id): Finds the index of a book in the list.
    2. find_member_index(member_id): Finds the index of a member in the list.
    3. sort_books_by_title(): Sorts books by title.
    4. sort_members_by_age(): Sorts members by age.
    5. reverse_loans(): Reverses the list of loans.
    6. append_loan(loan): Appends a new loan to the list.
    7. remove_loan(loan_id): Removes a loan from the list.

    Tuple-Related Methods:
    1. find_max_min_age_members(): Finds the maximum and minimum age of members.
    2. count_genre_occurrences(genre): Counts the occurrences of a specific genre.

    Set-Related Methods:
    1. add_genre(genre): Adds a new genre.
    2. remove_genre(genre): Removes a genre.
    3. list_all_genres(): Lists all genres.
    4. add_author(author): Adds a new author.
    5. remove_author(author): Removes an author.
    6. list_all_authors(): Lists all authors.
    7. find_common_genres(other_genres): Finds common genres between two sets.
    8. find_unique_genres(): Finds unique genres in the library.
    9. clear_genres(): Clears all genres.

    Dictionary-Related Methods:
    1. add_book(book_id, title, author, genre, availability): Adds a new book to the library.
    2. remove_book(book_id): Removes a book from the library.
    3. get_book_details(book_id): Gets book details.
    4. list_books_by_genre(genre): Lists all books by genre.
    5. count_books_by_genre(genre): Counts books by genre.
    6. add_member(member_id, name, age, membership_type): Adds a new member to the library.
    7. remove_member(member_id): Removes a member from the library.
    8. get_member_details(member_id): Gets member details.
    9. list_members_by_membership_type(membership_type): Lists all members by membership type.
    10. count_members_by_membership_type(membership_type): Counts members by membership type.
    11. update_book_details(book_id, new_details): Updates book details.
    12. update_member_details(member_id, new_details): Updates member details.
    13. merge_book_catalogs(other_catalog): Merges two book catalogs.
    14. merge_member_catalogs(other_catalog): Merges two member catalogs.
    15. get_all_book_ids(): Gets all book IDs.
    16. get_all_member_ids(): Gets all member IDs.
    17. clear_book_catalog(): Clears the book catalog.
    18. clear_member_catalog(): Clears the member catalog.
    """

    def __init__(self):
        # List of books in the library with genres
        self.books = [
            ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"),
            ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
            ("1984", "George Orwell", 1949, "Science Fiction"),
            ("Pride and Prejudice", "Jane Austen", 1813, "Classic"),
            ("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction"),
            ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy"),
            ("Fahrenheit 451", "Ray Bradbury", 1953, "Science Fiction"),
            ("Jane Eyre", "Charlotte Brontë", 1847, "Classic"),
            ("Wuthering Heights", "Emily Brontë", 1847, "Classic"),
            ("The Road", "Cormac McCarthy", 2006, "Fiction"),
            ("Beloved", "Toni Morrison", 1987, "Fiction"),
            ("The Goldfinch", "Donna Tartt", 2013, "Fiction"),
            ("The Underground Railroad", "Colson Whitehead", 2016, "Fiction")
        ]

        # List of users
        self.users = ["Alice", "Bob", "Charlie", "Diana"]

        # Set of unique genres
        self.genres = set()

        # Adding genres from books
        for book in self.books:
            self.genres.add(book[3])

        # Dictionary to map book titles to their details
        self.library_catalog = {title: (author, year, genre) for title, author, year, genre in self.books}

        # Dictionary to manage user checkouts
        self.user_checkouts = {user: [] for user in self.users}

    # List-Related Methods
    def find_book_index(self, title):
        """Finds the index of a book in the list."""
        for index, book in enumerate(self.books):
            if book[0] == title:
                return index
        return -1

    def sort_books_by_year(self):
        """Sorts books by year."""
        return sorted(self.books, key=lambda book: book[2])

    def reverse_users(self):
        """Reverses the list of users."""
        return self.users[::-1]

    def append_user(self, user):
        """Appends a new user to the list."""
        self.users.append(user)
        print(f"User '{user}' added.")

    def remove_user(self, user):
        """Removes a user from the list."""
        self.users.remove(user)
        print(f"User '{user}' removed.")

    # Tuple-Related Methods
    def find_max_min_year(self):
        """Finds the maximum and minimum year of books."""
        years = [book[2] for book in self.books]
        return max(years), min(years)

    # Set-Related Methods
    def add_genre(self, genre):
        """Adds a new genre."""
        self.genres.add(genre)
        print(f"Genre '{genre}' added.")

    def remove_genre(self, genre):
        """Removes a genre."""
        self.genres.discard(genre)
        print(f"Genre '{genre}' removed.")

    def list_all_genres(self):
        """Lists all genres."""
        return self.genres

    def find_common_genres(self, other_genres):
        """Finds common genres between two sets."""
        return self.genres.intersection(other_genres)

    def find_unique_genres(self):
        """Finds unique genres in the library."""
        return self.genres.difference({"Fiction", "Classic"})

    def clear_genres(self):
        """Clears all genres."""
        self.genres.clear()
        print("All genres cleared.")

    # Dictionary-Related Methods
    def add_book(self, title, author, year, genre):
        """Adds a new book to the library."""
        if title not in self.library_catalog:
            self.library_catalog[title] = (author, year, genre)
            self.genres.add(genre)
            print(f"Book '{title}' added.")
        else:
            print(f"Book '{title}' already exists.")

    def remove_book(self, title):
        """Removes a book from the library."""
        if title in self.library_catalog:
            book_details = self.library_catalog.pop(title)
            print(f"Book '{title}' removed.")
        else:
            print(f"Book '{title}' not found.")

    def get_book_details(self, title):
        """Gets book details."""
        return self.library_catalog.get(title, "Book not found.")

    def list_books_by_author(self, author):
        """Lists all books by an author."""
        return [title for title, details in self.library_catalog.items() if details[0] == author]

    def list_books_by_genre(self, genre):
        """Lists all books in a genre."""
        return [title for title, details in self.library_catalog.items() if details[2] == genre]

    def count_books_by_author(self, author):
        """Counts books by an author."""
        return sum(1 for title, details in self.library_catalog.items() if details[0] == author)

    def checkout_book(self, user, book_title):
        """Checks out a book to a user."""
        if book_title in self.library_catalog and user in self.user_checkouts:
            self.user_checkouts[user].append(book_title)
            print(f"{user} checked out {book_title}.")
        else:
            print(f"Book or user not found.")

    def return_book(self, user, book_title):
        """Returns a book from a user."""
        if user in self.user_checkouts and book_title in self.user_checkouts[user]:
            self.user_checkouts[user].remove(book_title)
            print(f"{user} returned {book_title}.")
        else:
            print(f"Book or user not found.")

    def update_book_details(self, title, new_details):
        """Updates book details."""
        if title in self.library_catalog:
            self.library_catalog[title] = new_details
            print(f"Updated details for book '{title}'.")
        else:
            print(f"Book '{title}' not found.")

    def merge_library_catalogs(self, other_catalog):
        """Merges two library catalogs."""
        for title, details in other_catalog.items():
            if title not in self.library_catalog:
                self.library_catalog[title] = details
                self.genres.add(details[2])
        print("Library catalogs merged.")

    def get_all_book_titles(self):
        """Gets all book titles."""
        return list(self.library_catalog.keys())

    def clear_library_catalog(self):
        """Clears the library catalog."""
        self.library_catalog.clear()
        print("Library catalog cleared.")

# Example usage
if __name__ == "__main__":
    library = LibraryManagement()

    print("Library Catalog:")
    for title, details in library.library_catalog.items():
        print(f"{title}: {details}")

    print("\nGenres Available:")
    print(library.genres)

    print("\nUser Checkouts:")
    for user, checkouts in library.user_checkouts.items():
        print(f"{user}: {checkouts}")

    # Add and remove books
    library.add_book("The Alchemist", "Paulo Coelho", 1988, "Fiction")
    library.remove_book("1984")

    print("\nLibrary Catalog After Changes:")
    for title, details in library.library_catalog.items():
        print(f"{title}: {details}")

    # Get book details
    print("\nBook Details for 'The Great Gatsby':")
    print(library.get_book_details("The Great Gatsby"))

    # List books by author
    print("\nBooks by George Orwell:")
    print(library.list_books_by_author("George Orwell"))

    # Count books by author
    print("\nCount of Books by George Orwell:")
    print(library.count_books_by_author("George Orwell"))

    # Find book index
    print("\nIndex of 'The Great Gatsby':")
    print(library.find_book_index("The Great Gatsby"))

    # Add and remove genres
    library.add_genre("Mystery")
    library.remove_genre("Romance")

    # List all genres
    print("\nAll Genres:")
    print(library.list_all_genres())

    # Checkout and return books
    library.checkout_book("Alice", "The Great Gatsby")
    library.return_book("Alice", "The Great Gatsby")

    print("\nUser Checkouts After Transactions:")
    for user, checkouts in library.user_checkouts.items():
        print(f"{user}: {checkouts}")

    # Sort books by year
    print("\nBooks Sorted by Year:")
    for book in library.sort_books_by_year():
        print(book)

    # Reverse the list of users
    print("\nReversed List of Users:")
    print(library.reverse_users())

    # Find the maximum and minimum year of books
    max_year, min_year = library.find_max_min_year()
    print(f"\nMaximum Year: {max_year}, Minimum Year: {min_year}")

    # Count the occurrences of a specific author
    print(f"\nOccurrences of 'George Orwell': {library.count_books_by_author('George Orwell')}")

    # Find common genres between two sets
    other_genres = {"Fiction", "Mystery", "Adventure"}
    print(f"\nCommon Genres: {library.find_common_genres(other_genres)}")

    # Find unique genres in the library
    print(f"\nUnique Genres: {library.find_unique_genres()}")

    # Update book details
    library.update_book_details("The Great Gatsby", ("F. Scott Fitzgerald", 1925, "Classic"))
    print(f"\nUpdated Book Details for 'The Great Gatsby': {library.get_book_details('The Great Gatsby')}")

    # Merge two library catalogs
    other_catalog = {
        "Brave New World": ("Aldous Huxley", 1932, "Dystopian"),
        "The Handmaid's Tale": ("Margaret Atwood", 1985, "Dystopian")
    }
    library.merge_library_catalogs(other_catalog)
    print("\nMerged Library Catalog:")
    for title, details in library.library_catalog.items():
        print(f"{title}: {details}")

    # Append a new user to the list
    library.append_user("Eve")
    print("\nUpdated List of Users:")
    print(library.users)

    # Remove a user from the list
    library.remove_user("Charlie")
    print("\nUpdated List of Users After Removal:")
    print(library.users)

    # Clear all genres
    library.clear_genres()
    print("\nGenres After Clearing:")
    print(library.genres)

    # Get all book titles
    print("\nAll Book Titles:")
    print(library.get_all_book_titles())

    # Clear the library catalog
    library.clear_library_catalog()
    print("\nLibrary Catalog After Clearing:")
    print(library.library_catalog)