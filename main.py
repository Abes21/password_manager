# from getpass import getpass
# from auth import check_master_password
# from storage import load_data, save_data, add_entry
# from crypto import encrypt, decrypt

entries = []

def add_entry():
    service = input("Podaj serwis: ")
    login = input("Podaj login/email: ")
    password = input("Podaj hasło: ")

    entry = {
        "service": service,
        "login": login,
        "password": password
    }

    entries.append(entry)
    print("Dodano pomyślnie.")



def show_entries():
    print("Wyświetlanie haseł")

def search_entry():
    print("Wyszukiwanie")

def delete_entry():
    print("Usuwanie")


while True:
    print("""
        1.Dodaj hasło
        2.Pokaż hasła
        3.Wyszukaj
        4.Usuń
        5.Wyjście
    """)
    menu = input("Co chcesz zrobić: ")
    if menu == "1":
        add_entry()
    elif menu == "2":
        show_entries()
    elif menu == "3":
        search_entry()
    elif menu == "4":
        delete_entry()
    elif menu == "5":
        print("Zamykanie programu...")
        break
    else:
        print("Brak takiej opcji.")