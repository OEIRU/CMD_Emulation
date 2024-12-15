import tkinter as tk
from ui import create_ui
from commands import execute
import os

def execute_command():
    """Функция для обработки ввода команды."""
    command = command_entry.get()  # Получение введённой команды
    current_dir = os.getcwd()  # Получение текущей директории

    if command.strip():
        # Добавление текста с цветом для текущей директории и команды
        output_text.insert(tk.END, f"{current_dir}> ", 'directory')  # Печать текущей директории
        output_text.insert(tk.END, f"{command}\n", 'command')  # Печать команды

        command_entry.delete(0, tk.END)  # Очистка строки ввода
        
        # Выполнение команды
        result = execute(command)

        if result == "CLEAR_SCREEN":
            output_text.delete(1.0, tk.END)  # Очистка экрана
        elif result == "EXIT":
            root.quit()  # Завершение программы
        else:
            output_text.insert(tk.END, f"{result}\n", 'output')  # Печать результата
    else:
        output_text.insert(tk.END, f"{current_dir}> Введите команду.\n", 'error')

    output_text.see(tk.END)  # Прокрутка вниз

# Создание основного окна
root = tk.Tk()
root.title("Эмулятор командного процессора Windows")
root.geometry("800x600")

# Создание интерфейса
output_text, command_entry = create_ui(root, execute_command)

# Настройка стилей для различных типов текста
output_text.tag_configure('directory', foreground='blue')  # Цвет для директории
output_text.tag_configure('command', foreground='green')  # Цвет для команды
output_text.tag_configure('output', foreground='black')  # Цвет для вывода
output_text.tag_configure('error', foreground='red')  # Цвет для ошибок

# Фокус на поле ввода при запуске
command_entry.focus_set()

# Запуск основного цикла программы
root.mainloop()
