tasks = []

def show_menu():
    print("\n== MENU ==")
    print("1. Dodaj zadanie")
    print("2. Wyświetl zadania")
    print("3. Usuń zadanie")
    print("4. Zakończ")

def add_task():
    task = input("Wpisz treść zadania: ")
    tasks.append(task)
    print("Zadanie dodane!")

def show_tasks():
    if not tasks:
        print("Brak zadań.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    show_tasks()
    try:
        num = int(input("Podaj numer zadania do usunięcia: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Usunięto: {removed}")
        else:
            print("Nieprawidłowy numer.")
    except ValueError:
        print("Wprowadź liczbę.")

while True:
    show_menu()
    choice = input("Wybierz opcję (1-4): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Do zobaczenia!")
        break
    else:
        print("Nieprawidłowy wybór.")

