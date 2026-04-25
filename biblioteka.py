boks = [
    {"title": "W pustyni i w puszczy", "author": "Henryk Sienkiewicz", "quantity": 3},
    {"title": "Lalka", "author": "Bolesław Prus", "quantity": 2},
    {"title": "Pan Tadeusz", "author": "Adam Mickiewicz", "quantity": 1},
    {"title": "Ferdydurke", "author": "Witold Gombrowicz", "quantity": 4},
    {"title": "Wiedźmin: Ostatnie życzenie", "author": "Andrzej Sapkowski", "quantity": 5},
]

users = [
    {"login": "kacper", "password": "kacper123", "role": "czytelnik"},
    {"login": "marcin", "password": "marcin123", "role": "czytelnik"},
    {"login": "monika", "password": "monika123", "role": "czytelnik"},
]

borrowings = {
    "kacper": [],
    "marcin": [],
    "monika": [],
}

MAX_LOGIN_ATTEMPTS = 3

def find_user(login, password):
    for user in users:
        if user["login"] == login and user["password"] == password:
            return user
    return None

def login():
    attempts = 0

    while attempts < MAX_LOGIN_ATTEMPTS:
        print("\n--- LOGOWANIE ---")
        login_input = input("Login: ")
        password_input = input("Hasło: ")

        user = find_user(login_input, password_input)

        if user is not None:
            print(f"\nWitaj, {user['login']}!")
            return user["login"]
        else:
            attempts += 1
            remaining = MAX_LOGIN_ATTEMPTS - attempts
            print(f"Błędny login lub hasło. Pozostało prób: {remaining}")

    print("\nPrzekroczono maksymalną liczbę prób logowania. Program zostanie zamknięty.")
    return None

def show_menu():
    print("\n--- MENU ---")
    print("1. Wyświetl dostępne książki")
    print("2. Wypożycz książkę")
    print("3. Pokaż moje wypożyczenia")
    print("4. Wyloguj się")
    choice = input("Wybierz opcję (1-4): ")
    return choice

def show_catalog():
    print("\n--- KATALOG KSIĄŻEK ---")
    print(f"{'Lp.':<5} {'Tytuł':<35} {'Autor':<25} {'Dostępne'}")
    print("-" * 70)

    for i, book in enumerate(boks, start=1):
        print(f"{i:<5} {book['title']:<35} {book['author']:<25} {book['quantity']}")

    print()

def find_book(title):
    for book in boks:
        if book["title"].lower() == title.lower():
            return book
    return None

def borrow_book(current_user):
    print("\n--- WYPOŻYCZANIE KSIĄŻKI ---")
    title = input("Podaj tytuł książki do wypożyczenia: ")

    book = find_book(title)

    if book is None:
        print(f"Nie znaleziono książki o tytule: \"{title}\".")
        return

    if book["quantity"] <= 0:
        print(f"Brak dostępnych sztuk książki: \"{book['title']}\".")
        return

    book["quantity"] -= 1
    borrowings[current_user].append(book["title"])
    print(f"Wypożyczono: \"{book['title']}\". Pozostało sztuk: {book['quantity']}.")

def show_borrowings(current_user):
    print("\n--- MOJE WYPOŻYCZENIA ---")
    user_books = borrowings[current_user]

    if len(user_books) == 0:
        print("Nie masz żadnych wypożyczonych książek.")
        return

    for i, title in enumerate(user_books, start=1):
        print(f"  {i}. {title}")

    print(f"Łącznie wypożyczonych: {len(user_books)}")

def main_loop(current_user):
    while True:
        choice = show_menu()

        if choice == "1":
            show_catalog()
        elif choice == "2":
            borrow_book(current_user)
        elif choice == "3":
            show_borrowings(current_user)
        elif choice == "4":
            print(f"Do widzenia, {current_user}!")
            break
        else:
            print("Nieprawidłowy wybór. Wybierz opcję 1-4.")

def main():
    print("+" * 20)
    print("WITAJ W BIBLIOTECE!")
    print("+" * 20)

    current_user = login()

    if current_user is not None:
        main_loop(current_user)

main()