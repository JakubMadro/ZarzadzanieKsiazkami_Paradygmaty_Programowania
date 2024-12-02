import tkinter as tk
from tkinter import messagebox, ttk
from book import Book
from book_import import import_books_from_csv
from book_export import export_books_to_csv

class BookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zarządzanie Biblioteką")
        self.books = import_books_from_csv()

        # Lista książek
        self.tree = ttk.Treeview(root, columns=("Tytuł", "Autor", "Rok", "Dostępność"), show="headings")
        self.tree.heading("Tytuł", text="Tytuł")
        self.tree.heading("Autor", text="Autor")
        self.tree.heading("Rok", text="Rok")
        self.tree.heading("Dostępność", text="Dostępność")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Przyciski
        btn_frame = tk.Frame(root)
        btn_frame.pack(fill=tk.X, pady=5)

        tk.Button(btn_frame, text="Dodaj Książkę", command=self.add_book).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Usuń Książkę", command=self.remove_book).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Zapisz do CSV", command=self.save_books).pack(side=tk.RIGHT, padx=5)

        # Załaduj książki do listy
        self.load_books()

    def load_books(self):
        """Wczytuje książki do widoku"""
        for book in self.books:
            self.tree.insert("", tk.END, values=(book.title, book.author, book.year, book.is_available))

    def add_book(self):
        """Dodaje nową książkę"""
        def save_new_book():
            title = title_entry.get()
            author = author_entry.get()
            year = year_entry.get()
            is_available = available_var.get()
            try:
                year = int(year)
                new_book = Book(title, author, year, is_available)
                self.books.append(new_book)
                self.tree.insert("", tk.END, values=(title, author, year, is_available))
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Błąd", "Rok musi być liczbą!")

        add_window = tk.Toplevel(self.root)
        add_window.title("Dodaj Książkę")

        tk.Label(add_window, text="Tytuł:").grid(row=0, column=0, padx=5, pady=5)
        title_entry = tk.Entry(add_window)
        title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Autor:").grid(row=1, column=0, padx=5, pady=5)
        author_entry = tk.Entry(add_window)
        author_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Rok:").grid(row=2, column=0, padx=5, pady=5)
        year_entry = tk.Entry(add_window)
        year_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Dostępność:").grid(row=3, column=0, padx=5, pady=5)
        available_var = tk.BooleanVar(value=True)
        tk.Checkbutton(add_window, text="Dostępna", variable=available_var).grid(row=3, column=1, padx=5, pady=5)

        tk.Button(add_window, text="Zapisz", command=save_new_book).grid(row=4, column=0, columnspan=2, pady=10)

    def remove_book(self):
        """Usuwa zaznaczoną książkę"""
        selected_item = self.tree.selection()
        if selected_item:
            for item in selected_item:
                values = self.tree.item(item, "values")
                self.tree.delete(item)
                self.books = [book for book in self.books if not (book.title == values[0] and book.author == values[1])]
        else:
            messagebox.showwarning("Uwaga", "Wybierz książkę do usunięcia!")

    def save_books(self):
        """Zapisuje książki do pliku CSV"""
        export_books_to_csv(self.books)
        messagebox.showinfo("Sukces", "Dane zapisane do pliku!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()
