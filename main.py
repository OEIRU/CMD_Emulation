import tkinter as tk
from ui import create_ui
from commands import execute
import os

def execute_command():
    """Функция для обработки ввода команды."""
    command = command_entry.get()  # Получение введённой команды
    current_dir = os.getcwd()  # Получение текущей директории

    if command.strip():
        output_text.insert(tk.END, f"{current_dir}> {command}\n")  # Печать текущей директории и команды в область вывода
        command_entry.delete(0, tk.END)  # Очистка строки ввода
        
        # Выполнение команды
        result = execute(command)

        if result == "CLEAR_SCREEN":
            output_text.delete(1.0, tk.END)  # Очистка экрана
        elif result == "EXIT":
            root.quit()  # Завершение программы
        else:
            output_text.insert(tk.END, f"{result}\n")
    else:
        output_text.insert(tk.END, f"{current_dir}> Введите команду.\n")

    output_text.see(tk.END)  # Прокрутка вниз

# Создание основного окна
root = tk.Tk()
root.title("Эмулятор командного процессора Windows")
root.geometry("800x600")

# Создание интерфейса
output_text, command_entry = create_ui(root, execute_command)

# Фокус на поле ввода при запуске
command_entry.focus_set()

# Запуск основного цикла программы
root.mainloop()
