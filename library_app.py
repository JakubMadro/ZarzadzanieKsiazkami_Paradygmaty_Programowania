from library_manager import LibraryManager


class LibraryApp:
    def __init__(self):
        self.manager = LibraryManager()

    def print_menu(self):
        print("\nZarządzanie biblioteką:")
        options = [
            "1. Dodaj książkę",
            "2. Wyświetl listę książek",
            "3. Usuń książkę",
            "4. Zmień dostępność książki",
            "5. Eksportuj do CSV",
            "6. Importuj z CSV",
            "7. Wyjście"
        ]
        print('\n'.join(options))
        choice = input("Wybierz opcję (1-7): ")
        return int(choice) if choice.isdigit() else 0

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                self.manager.add_book()
            elif choice == 2:
                self.manager.view_books()
            elif choice == 3:
                self.manager.remove_book()
            elif choice == 4:
                self.manager.update_availability()
            elif choice == 5:
                self.manager.export_to_csv()
            elif choice == 6:
                self.manager.import_from_csv()
            elif choice == 7:
                print("Zamykanie aplikacji...")
                break
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")
