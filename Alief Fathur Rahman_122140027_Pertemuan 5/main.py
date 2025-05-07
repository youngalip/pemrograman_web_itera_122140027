from abc import ABC, abstractmethod

# Abstract Base Class (ABC) for LibraryItem
class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self._title = title
        self._item_id = item_id

    @abstractmethod
    def display_details(self):
        pass

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if len(new_title) > 0:
            self._title = new_title
        else:
            print("Title tidak boleh kosong!")

# Subclass Book
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self._author = author

    def display_details(self):
        return f"Book Title: {self.title}, Author: {self._author}, ID: {self._item_id}"

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if len(new_author) > 0:
            self._author = new_author
        else:
            print("Author tidak boleh kosong!")

# Subclass Magazine
class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self._issue_number = issue_number

    def display_details(self):
        return f"Magazine Title: {self.title}, Issue: {self._issue_number}, ID: {self._item_id}"

# Subclass Newspaper
class Newspaper(LibraryItem):
    def __init__(self, title, item_id, publication_date):
        super().__init__(title, item_id)
        self._publication_date = publication_date

    def display_details(self):
        return f"Newspaper Title: {self.title}, Date: {self._publication_date}, ID: {self._item_id}"

    @property
    def publication_date(self):
        return self._publication_date

    @publication_date.setter
    def publication_date(self, new_date):
        if len(new_date) > 0:
            self._publication_date = new_date
        else:
            print("Tanggal publikasi tidak boleh kosong!")

# Library Class
class Library:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        if isinstance(item, LibraryItem):
            self._items.append(item)
        else:
            print("Item harus berupa turunan LibraryItem.")

    def display_all_items(self):
        for item in self._items:
            print(item.display_details())

    def find_item_by_title(self, title):
        for item in self._items:
            if item.title.lower() == title.lower():
                return item.display_details()
        return "Item tidak ditemukan."

    def find_item_by_id(self, item_id):
        for item in self._items:
            if item._item_id == item_id:
                return item.display_details()
        return "Item tidak ditemukan."

# Membuat instance Library
library = Library()

# Buku tentang Marvel
book1 = Book("Marvel Encyclopedia", "B001", "Stephen Wiacek")
book2 = Book("The Marvel Book", "B002", "DK Publishing")
book3 = Book("Marvel Comics: The Untold Story", "B003", "Sean Howe")
book4 = Book("Marvel 5-Minute Stories", "B004", "Marvel Press")

# Majalah
magazine1 = Magazine("Indonesian Foods", "M001", 2018)
magazine2 = Magazine("Art of Fashion", "M002", 2023)
magazine3 = Magazine("Supercars", "M003", 2024)
magazine4 = Magazine("Minimalis", "M004", 2025)

# Koran
newspaper1 = Newspaper("Kompas", "N001", "2025-05-01")
newspaper2 = Newspaper("Republika", "N002", "2025-05-02")

# Tambahkan semua item ke perpustakaan
library.add_item(book1)
library.add_item(book2)
library.add_item(book3)
library.add_item(book4)

library.add_item(magazine1)
library.add_item(magazine2)
library.add_item(magazine3)
library.add_item(magazine4)

library.add_item(newspaper1)
library.add_item(newspaper2)

# Tampilkan semua item
print("Daftar Item Perpustakaan:")
library.display_all_items()

# Contoh pencarian
print("\nMencari item berdasarkan judul 'Marvel Encyclopedia':")
print(library.find_item_by_title("Marvel Encyclopedia"))

print("\nMencari item berdasarkan ID 'M001':")
print(library.find_item_by_id("M001"))
