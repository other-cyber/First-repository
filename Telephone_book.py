person = {}


def add_contact(*, person: dict, name: str ):
    if person.get(name) is None:
        phone = int(input("Введите номер: "))
        person[name] = phone
        print("Контакт успешно добавлен!")
        return 
    else:
        yes_or_no = input("Хотите перезаписать номер? ").lower()
        if yes_or_no == "да":
            phone = int(input("Введите номер: "))
            person[name] = phone
        elif yes_or_no == "нет":
            return 

def delete_contact(*, person: dict, name: str):
    if person.get(name) is None:
        print("Такого человека нет в книге")
        return 
    else:
        del person[name]
        print("Контакт успешно удален!")

def find_number_by_name(*, person: dict, name: str): 
    if person.get(name) is None:
        print("Такого человека нет в книге")
        return 
    else:
        print(person[name])


def all_print(person):
    if person:
        for item in person.items():
            keys, value = item
            print(keys, value)
    else:
        print("Словарь пуст")
        return 

def quit():
    return 1


def interface():
    while True:
        print("========================")
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Найти номер по имени")
        print("4. Показать все контакты")
        print("5. Выйти")
        choice = int(input("Введите число: "))
        if choice == 1:
            name = input("Введите имя: ")
            add_contact(person=person, name=name)
        elif choice == 2:
            name = input("Введите имя: ")
            delete_contact(person=person, name=name)
        elif choice == 3:
            name = input("Введите имя: ")
            find_number_by_name(person=person, name=name)
        elif choice == 4:
            all_print(person=person)
        elif choice == 5:
            quit()
            print("Вы вышли")
            return 
            
        

def main():
    interface()

main()