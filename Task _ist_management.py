def add_task(tasks, name):
    task = (name, "Не выполнено")
    tasks.append(task)
    return tasks


def complete_task(tasks, index):
    if index > len(tasks) or index < 1:
        print("Вы вышли за пределы списка")
        main()
    else:
        task = tasks[index-1][0], "выполнено"
        tasks[index-1] = task
        return tasks


def delete_tasks(tasks, index):
    if index > len(tasks) or index < 1:
        print("Вы вышли за пределы списка")
        return tasks
    else:
        tasks.pop(index-1)


def show_tasks(tasks):
    if len(tasks) == 0:
        print("У вас нет задач")
        return tasks
    num = 1
    for i in tasks:
        print(f"{num} {i}")
        num += 1

def show_stats(tasks):
    completed_tasks = 0
    uncompleted_tasks = 0
    for task in tasks:
        if task[1] == "выполнено":
            completed_tasks += 1
        else:
            uncompleted_tasks += 1

    print(f"Всего задач - {len(tasks)}")
    print(f"Выполнено - {completed_tasks}")
    print(f"Невыполнено - {uncompleted_tasks}")

 
def main():
    tasks = []
    while True:
        print(" ")
        print("1. Показать все задачи")    
        print("2. Добавить задачу")  
        print("3. Выполнить задачу")
        print("4. Удалить задачу")
        print("5. Показать статистику")
        choice = int(input("Введите число: "))
        if choice == 1:
            show_tasks(tasks)
        elif choice == 2:
            name = input("Введите название задачи: ")
            add_task(tasks, name)
            print("Задача добавлена")
        elif choice == 3:
            show_tasks(tasks)
            index = int(input("Введите номер задачи: "))
            complete_task(tasks, index)
        elif choice == 4:
            index = int(input("Введите номер задачи: "))
            delete_tasks(tasks, index)
        elif choice == 5:
            show_stats(tasks)
main()