import tkinter as tk
from tkinter import ttk, messagebox
from library_manager import LibraryManager



class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zarządzanie Biblioteką")
        self.manager = LibraryManager(filename="booksDB.csv")  # Użycie istniejącej klasy LibraryManager

        # Lista książek (Treeview)
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
        tk.Button(btn_frame, text="Zmień Dostępność", command=self.update_availability).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Eksportuj do CSV", command=self.export_books).pack(side=tk.RIGHT, padx=5)
        tk.Button(btn_frame, text="Importuj z CSV", command=self.import_books).pack(side=tk.RIGHT, padx=5)

        # Załaduj istniejące książki
        self.load_books()

    def load_books(self):
        for book in self.manager.books:
            self.tree.insert("", tk.END,
                             values=(book.title, book.author, book.year, "Tak" if book.available else "Nie"))

    def add_book(self):
        """Dodaje nową książkę"""

        def save_new_book():
            title = title_entry.get()
            author = author_entry.get()
            year = year_entry.get()
            available = available_var.get()

            if not title or not author or not year:
                messagebox.showerror("Błąd", "Wszystkie pola są wymagane!")
                return

            try:
                year = int(year)
                self.manager.books.append(self.manager.add_book_manual(title, author, year, available))
                self.tree.insert("", tk.END, values=(title, author, year, "Tak" if available else "Nie"))
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
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Uwaga", "Wybierz książkę do usunięcia!")
            return

        for item in selected_item:
            values = self.tree.item(item, "values")
            self.manager.books = [book for book in self.manager.books if book.title != values[0]]
            self.tree.delete(item)

    def update_availability(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Uwaga", "Wybierz książkę do zmiany dostępności!")
            return

        for item in selected_item:
            values = self.tree.item(item, "values")
            for book in self.manager.books:
                if book.title == values[0]:
                    book.available = not book.available
                    self.tree.item(item,
                                   values=(book.title, book.author, book.year, "Tak" if book.available else "Nie"))
                    break

    def export_books(self):
        """Eksportuje książki do CSV"""
        self.manager.export_to_csv()
        messagebox.showinfo("Sukces", "Dane zostały zapisane do pliku CSV!")

    def import_books(self):
        """Importuje książki z CSV"""
        self.manager.import_from_csv()
        self.tree.delete(*self.tree.get_children())
        self.load_books()


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()