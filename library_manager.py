import csv
from book import Book


class LibraryManager:
    def __init__(self, filename="booksDB.csv"):
        self.books = []
        self.filename = filename
        self.import_from_csv()

    def add_book_manual(self, title, author, year, available):
        book = Book(title, author, year, available)
        return book


    def import_from_csv(self):
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.books = [
                    Book(row["Tytuł"], row["Autor"], int(row["Rok"]), row["Dostępność"] == 'True')
                    for row in reader
                ]
            print(f"Dane zostały zaimportowane z pliku '{self.filename}'.")
        except FileNotFoundError:
            print(f"Plik '{self.filename}' nie istnieje.")
        except Exception as e:
            print(f"Wystąpił błąd podczas importu: {e}")

    def export_to_csv(self):
        """Eksportuje dane książek do pliku CSV."""
        try:
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["Tytuł", "Autor", "Rok", "Dostępność"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for book in self.books:
                    writer.writerow({
                        "Tytuł": book.title,
                        "Autor": book.author,
                        "Rok": book.year,
                        "Dostępność": str(book.available)
                    })
            print(f"Dane zostały zapisane do pliku '{self.filename}'.")
        except Exception as e:
            print(f"Wystąpił błąd podczas eksportu: {e}")

