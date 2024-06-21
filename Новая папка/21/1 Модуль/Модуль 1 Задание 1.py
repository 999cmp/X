import tkinter as tk
from tkinter import messagebox

class DriverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Приложение для водителя")
        
        # Метка приветствия
        self.label = tk.Label(self.root, text="Добро пожаловать, водитель!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Кнопка для просмотра нарушений
        self.violation_button = tk.Button(self.root, text="Просмотреть нарушения", command=self.view_violations)
        self.violation_button.pack(pady=5)

        # Кнопка для редактирования профиля
        self.profile_button = tk.Button(self.root, text="Редактировать профиль", command=self.edit_profile)
        self.profile_button.pack(pady=5)

    def view_violations(self):
        # просто выводим сообщение
        messagebox.showinfo("Просмотр нарушений", "Здесь будут отображаться ваши нарушения")

    def edit_profile(self):
        # просто выводим сообщение
        messagebox.showinfo("Редактирование профиля", "Здесь будет возможность редактировать профиль")

root = tk.Tk()
app = DriverApp(root)
root.mainloop()
