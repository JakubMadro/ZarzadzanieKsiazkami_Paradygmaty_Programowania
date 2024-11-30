import csv
from book import Book


class LibraryManager:
    def __init__(self):
        self.books = []

    def add_book(self):
        print("Dodaj nową książkę:")
        title = input("Podaj tytuł: ")
        author = input("Podaj autora: ")
        year = int(input("Podaj rok wydania: "))
        self.books.append(Book(title, author, year))
        print(f"Książka '{title}' została dodana do biblioteki.")

    def view_books(self):
        if not self.books:
            print("\nBrak książek w bibliotece.")
        else:
            print("\nLista książek:")
            for book in self.books:
                print(book.get_info())

    def remove_book(self):
        title = input("Podaj tytuł książki do usunięcia: ")
        book_to_remove = next((book for book in self.books if book.title == title), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Książka '{title}' została usunięta.")
        else:
            print(f"Nie znaleziono książki o tytule '{title}'.")

    def update_availability(self):
        title = input("Podaj tytuł książki do aktualizacji dostępności: ")
        book = next((book for book in self.books if book.title == title), None)
        if book:
            book.available = not book.available
            print(f"Dostępność książki '{title}' została zmieniona na: {'Dostępna' if book.available else 'Niedostępna'}.")
        else:
            print(f"Nie znaleziono książki o tytule '{title}'.")

    def export_to_csv(self, filename="books.csv"):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Tytuł", "Autor", "Rok", "Dostępność"])
            for book in self.books:
                writer.writerow([book.title, book.author, book.year, book.available])
        print(f"Dane zostały wyeksportowane do pliku '{filename}'.")

    def import_from_csv(self, filename="books_import.csv"):
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.books = [
                    Book(row["Tytuł"], row["Autor"], int(row["Rok"]), row["Dostępność"] == 'True')
                    for row in reader
                ]
            print(f"Dane zostały zaimportowane z pliku '{filename}'.")
        except FileNotFoundError:
            print(f"Plik '{filename}' nie istnieje.")
        except Exception as e:
            print(f"Wystąpił błąd podczas importu: {e}")
