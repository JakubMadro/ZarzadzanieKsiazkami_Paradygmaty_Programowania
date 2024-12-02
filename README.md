# Zarządzanie Książkami

Projekt aplikacji do zarządzania kolekcją książek, który umożliwia dodawanie, wyświetlanie, usuwanie i aktualizowanie danych książek. Aplikacja korzysta z pliku CSV jako bazy danych do przechowywania informacji o książkach.

## Spis Treści

- [Opis projektu](#opis-projektu)
- [Technologie](#technologie)
- [Wymagania]()
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Struktura projektu](#struktura-projektu)

## Opis projektu

Aplikacja umożliwia zarządzanie kolekcją książek poprzez prosty interfejs w terminalu. Użytkownik może:

- Dodawać nowe książki do bazy danych.
- Wyświetlać wszystkie książki w kolekcji.
- Usuwać książki z bazy na podstawie wieku (rok wydania).
- Aktualizować informacje o wynagrodzeniu (np. status dostępności).

Dane są przechowywane w pliku CSV, co pozwala na łatwe importowanie i eksportowanie danych.

## Technologie

- Python 3.x
- CSV do przechowywania danych
- Obsługa błędów i walidacja danych

## Wymagania

Python w wersji 3.x 

Aby sprawdzic czy posiadasz pythona na swoim komputerze, użyj polecenia 

   ```bash
   python --version
   ```

## Instalacja

1. Sklonuj repozytorium na swój komputer:
   ```bash
   git clone https://github.com/JakubMadro/ZarzadzanieKsiazkami_Paradygmaty_Programowania.git

   cd ZarzadzanieKsiazkami_Paradygmaty_Programowania

   python main.py
   ```

