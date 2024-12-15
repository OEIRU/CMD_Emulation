import os

COMMANDS = {
    "help": "Вывод списка доступных команд.",
    "dir": "Вывод содержимого текущей директории.",
    "cd": "Смена текущей директории.",
    "mkdir": "Создание новой директории.",
    "echo": "Вывод текста на экран.",
    "cls": "Очистка экрана.",
    "exit": "Завершение работы программы.",
    "rmdir": "Удаление пустой директории.",
    "type": "Вывод содержимого файла."
}

def execute(command):
    """Обработка команд."""
    args = command.split()
    if not args:
        return "Ошибка: команда не указана."

    cmd = args[0].lower()

    if cmd == "help":
        return "\n".join([f"{cmd}: {desc}" for cmd, desc in COMMANDS.items()])

    elif cmd == "dir":
        return "\n".join(os.listdir(os.getcwd()))

    elif cmd == "cd":
        if len(args) > 1:
            try:
                os.chdir(args[1])
                return f"Текущая директория: {os.getcwd()}"
            except FileNotFoundError:
                return "Ошибка: директория не найдена."
            except PermissionError:
                return "Ошибка: отказано в доступе."
        return "Ошибка: путь не указан."

    elif cmd == "mkdir":
        if len(args) > 1:
            try:
                os.mkdir(args[1])
                return f"Директория {args[1]} создана."
            except FileExistsError:
                return "Ошибка: директория уже существует."
            except PermissionError:
                return "Ошибка: отказано в доступе."
        return "Ошибка: имя директории не указано."

    elif cmd == "echo":
        return " ".join(args[1:])

    elif cmd == "cls":
        return "CLEAR_SCREEN"

    elif cmd == "exit":
        return "EXIT"

    elif cmd == "rmdir":
        if len(args) > 1:
            try:
                os.rmdir(args[1])
                return f"Директория {args[1]} удалена."
            except FileNotFoundError:
                return "Ошибка: директория не найдена."
            except OSError:
                return "Ошибка: директория не пуста или используется."
            except PermissionError:
                return "Ошибка: отказано в доступе."
        return "Ошибка: имя директории не указано."

    elif cmd == "type":
        if len(args) > 1:
            try:
                with open(args[1], "r") as file:
                    return file.read()
            except FileNotFoundError:
                return "Ошибка: файл не найден."
            except PermissionError:
                return "Ошибка: отказано в доступе."
        return "Ошибка: имя файла не указано."

    return f"Ошибка: команда '{cmd}' не распознана."
