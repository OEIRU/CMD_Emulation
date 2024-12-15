import tkinter as tk
from tkinter import scrolledtext

def create_ui(root, execute_command):
    """Создаёт интерфейс командного процессора."""
    # Область вывода текста
    output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.NORMAL, font=("Courier", 12))
    output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Поле ввода команды
    command_entry = tk.Entry(root, font=("Courier", 12))
    command_entry.pack(fill=tk.X, padx=10, pady=(0, 10))
    command_entry.bind("<Return>", lambda event: execute_command())  # Обработка Enter

    # Возвращаем элементы для работы
    return output_text, command_entry
