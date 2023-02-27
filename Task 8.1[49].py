#8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. 
#Доделать задание вебинара и реализовать Update, Delete

def menu():
    phone_book = []
    while True:
        choice = show_menu()
        if choice == "":
            print("до новых встреч")
            break
        elif choice == "1":
            entry = create_entry(*new_entry(mode = "new"))
            phone_book.append(entry)
        elif choice == "2":
            surname = surname()
            entries = select(phone_book, surname)
            show_entries(entries)
        elif choice == "3":
            surname = surname()
            entries = select(phone_book, surname)
            if entries:
                idx = phone_book.index(entries[0])
                entry = create_entry(*new_entry(mode = "update"))
                entry = merge(entry, entries[0])
                phone_book[idx] = entry
        elif choice == "4":
            surname = surname()
            recs = select(phone_book, surname)
            if entries:
                idx = phone_book.index(entries[0])
                phone_book.pop(idx)
        elif choice == "5":
            filename = file_name()
            entries = import_file(filename)
            phone_book.extend(entries)
        elif choice == "6":
            filename = file_name()
            export_file(filename, phone_book)
        elif choice == "7":
            show_all_entries(phone_book)
        else:
            print("Недопустимый пункт меню")

def show_menu() -> str:
    print("*"*20)
    print("МЕНЮ:")
    print("\t1 - Ввод новой записи")
    print("\t2   - Поиск записи по фамилии")
    print("\t3  - Изменение записи по фамилии")
    print("\t4 - Удаление записи по фамилии")
    print("\t5 - Импорт из файла")
    print("\t6 - Экспорт в файл")
    print("\t7   - Вывод на экран содержимого справочника")

    return input("Выберите нужный пункт")

def create_entry(surname, name, tel, desc) -> dict:
    return {'surname': surname, 'name': name, 'tel': tel, 'desc': desc}

def surname():
    return input("Введите фамилию:")

def select(phone_book: list, template: str, ) -> list:
    return [rec for rec in phone_book if rec['surname'].lower().startswith(template.lower())]

def new_entry(mode = "new") -> tuple:
    if mode == "new":
        print("Режим ввода новой записи")
    elif mode == "update":
        print("Ввод новых данных для записи {surname}")
        print("Пустая строка означает оставить данные без изменения")
    else:
        raise ValueError(f"Недоустимый флаг mode: {mode}")
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    tel = input("Введите номер телефона: ")
    desc = input("Введите Описание: ")
    return surname, name, tel, desc

def show_entries(entries: list):
    for entry in entries:
        show_entry(entry)

def show_entry(entry: dict):
    for val in entry.values():
        print(val, end=" ")
    print("")

def merge(new_rec: dict, old_rec: dict) -> dict:
    tmp_entry = new_entry.fromkeys(new_entry.keys())
    for key in new_entry.keys():
        tmp_entry[key] = new_entry[key] if new_entry[key] != "" else old_entry[key]
    return tmp_entry

def file_name() -> str:
    return input("Введите имя файла:")

def import_file(filename: str, delimiter="#") -> list:
    rez = []
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            surname, name, tel, desc = line.strip().split(delimiter)
            rez.append({'surname': surname, 'name': name, 'tel': tel, 'desc': desc})
    return rez

def export_file(filename: str, phone_book: list, delimiter="#"):
    with open(filename, mode="w", encoding="utf-8") as file:
        for rec in phone_book:
            file.write(",".join(rec.values()))
            file.write(f"\n")

def show_all_entries(phone_book: list):
    print("Записи в справочнике:")
    for entry in phone_book:
        show_entry(entry)

menu()
