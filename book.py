class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def get_info(self):
        return (f"Książka: '{self.title}' \t"
                f"Autor: {self.author} \t"
                f"Rok: {self.year} \t"
                f"Dostępność: {'Tak' if self.available else 'Nie'}")