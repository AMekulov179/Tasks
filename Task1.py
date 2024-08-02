import tkinter as tk
import customtkinter as CTk
from PIL import Image
import json
import os
from tkinter import simpledialog

# Пользователи
def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return []

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)

def load_projects():
    if os.path.exists("projects.json"):
        with open("projects.json", "r") as f:
            return json.load(f)
    return []

def save_projects(projects):
    with open("projects.json", "w") as f:
        json.dump(projects, f, indent=4)

users = load_users()
projects = load_projects()

class Window1(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("960x540")
        self.title("Система управления задачами")
        self.configure(bg="white")

        self.label0 = CTk.CTkLabel(master=self, text="", height=self.winfo_screenheight(),
                                   width=self.winfo_screenwidth(), bg_color="white")
        self.label0.place(x=0, y=0)

        button_width = 200
        button_height = 50
        button_spacing = 20

        self.image = CTk.CTkImage(Image.open("4360835.png"), size=(150, 150))
        self.image_label = CTk.CTkLabel(master=self, image=self.image, text="", bg_color="white")
        self.image_label.place(relx=0.5, rely=0.5, anchor='center', y=-110)

        self.Button = CTk.CTkButton(master=self, text="  Авторизоваться  ", height=button_height, width=button_width,
                                    fg_color="transparent", font=("GOST type B", 24), bg_color="white", border_width=2,
                                    border_color="black", text_color="black", corner_radius=20,
                                    command=self.open_window2)
        self.Button.place(relx=0.5, rely=0.5, anchor='center')

        self.Button2 = CTk.CTkButton(master=self, text="Зарегистрироваться", height=button_height, width=button_width,
                                     fg_color="transparent", font=("GOST type B", 24), bg_color="white", border_width=2,
                                     border_color="black", text_color="black", corner_radius=20,
                                     command=self.open_window3)
        self.Button2.place(relx=0.5, rely=0.5, anchor='center', y=button_height + button_spacing)

        def login(self):
            username = self.username_var.get()
            password = self.password_var.get()
            for user in users:
                if user["login"] == username and user["password"] == password:
                    self.destroy()
                    window4 = Window4(username)
                    window4.mainloop()
                    return
            CTk.CTkLabel(self, text="Неправильный логин или пароль", text_color="red", bg_color="white").pack(pady=10)

    def open_window2(self):
        self.destroy()
        window2 = Window2()
        window2.mainloop()

    def open_window3(self):
        self.destroy()
        window3 = Window3()
        window3.mainloop()

class Window2(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("960x540")
        self.title("Авторизация")

        button_width = 200
        button_height = 50
        button_spacing = 20

        self.label = CTk.CTkLabel(self, text="Авторизация", font=("GOST type B", 24))
        self.label.pack(pady=10)

        self.label0 = CTk.CTkLabel(master=self, text="", height=self.winfo_screenheight(),
                                   width=self.winfo_screenwidth(), bg_color="white")
        self.label0.place(x=0, y=0)

        self.label1 = CTk.CTkLabel(self, text="Имя пользователя", height=30, width=button_width,
                                   font=("GOST type B", 24), bg_color="white", text_color="black")
        self.label1.pack(pady=10)

        self.username_var = tk.StringVar()
        self.username_entry = CTk.CTkEntry(self, textvariable=self.username_var, width=300,font=("GOST type B", 20))
        self.username_entry.insert(0, "")
        self.username_entry.pack(pady=10)

        self.label2 = CTk.CTkLabel(self, text="Пароль", height=30, width=button_width,
                                   font=("GOST type B", 24), bg_color="white", text_color="black")
        self.label2.pack(pady=10)

        self.password_var = tk.StringVar()
        self.password_entry = CTk.CTkEntry(self, textvariable=self.password_var, width=300, show='*',font=("GOST type B", 20))
        self.password_entry.insert(0, "")
        self.password_entry.pack(pady=10)

        self.login_button = CTk.CTkButton(self, text="Войти", command=self.login, height=40,
                                         width=300 , fg_color="transparent", font=("GOST type B", 20),
                                         bg_color="white", border_width=2, border_color="black", text_color="black",
                                         corner_radius=10)
        self.login_button.pack(pady=10)

        self.back_button = CTk.CTkButton(self, text="Назад", command=self.back_to_window1,height=40,
                                         width=300 , fg_color="transparent", font=("GOST type B", 20),
                                         bg_color="white", border_width=2, border_color="black", text_color="black",
                                         corner_radius=10)
        self.back_button.pack(pady=10)

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()
        for user in users:
            if user["login"] == username and user["password"] == password:
                self.destroy()
                window4 = Window4(username)
                window4.mainloop()
                return
        CTk.CTkLabel(self, text="Неправильный логин или пароль", text_color="red",bg_color="white").pack(pady=10)

    def back_to_window1(self):
        self.destroy()
        window1 = Window1()
        window1.mainloop()

class Window3(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("960x540")
        self.title("Регистрация")

        self.label0 = CTk.CTkLabel(master=self, text="", height=self.winfo_screenheight(),
                                   width=self.winfo_screenwidth(), bg_color="white")
        self.label0.place(x=0, y=0)


        self.label1 = CTk.CTkLabel(self, text="Имя пользователя", height=30, width=300,
                                   font=("GOST type B", 24), bg_color="white", text_color="black")
        self.label1.pack(pady=10)

        self.username_var = tk.StringVar()
        self.username_entry = CTk.CTkEntry(self, textvariable=self.username_var, width=300)
        self.username_entry.insert(0, "")
        self.username_entry.pack(pady=10)

        self.label2 = CTk.CTkLabel(self, text="Пароль", height=30, width=300,
                                   font=("GOST type B", 24), bg_color="white", text_color="black")
        self.label2.pack(pady=10)

        self.password_var = tk.StringVar()
        self.password_entry = CTk.CTkEntry(self, textvariable=self.password_var, width=300)
        self.password_entry.insert(0, "")
        self.password_entry.pack(pady=10)

        self.label3 = CTk.CTkLabel(self, text="Должность", height=30, width=300,
                                   font=("GOST type B", 24), bg_color="white", text_color="black")
        self.label3.pack(pady=10)

        self.job_var = tk.StringVar()
        self.job_combobox = CTk.CTkComboBox(self, values=["руководитель", "работник"], height=30, width=300,
                                            font=("GOST type B", 20))
        self.job_combobox.pack(pady=10)

        self.register_button = CTk.CTkButton(self, text="Зарегистрироваться", command=self.register,height=40,
                                         width=300 , fg_color="transparent", font=("GOST type B", 20),
                                         bg_color="white", border_width=2, border_color="black", text_color="black",
                                         corner_radius=10)
        self.register_button.pack(pady=10)

        self.back_button = CTk.CTkButton(self, text="Назад", command=self.back_to_window1,height=40,
                                         width=300 , fg_color="transparent", font=("GOST type B", 20),
                                         bg_color="white", border_width=2, border_color="black", text_color="black",
                                         corner_radius=10)
        self.back_button.pack(pady=10)

    def register(self):
        username = self.username_var.get()
        password = self.password_var.get()
        job = self.job_combobox.get()
        if username and password and job:
            users.append({"login": username, "password": password, "job": job})
            save_users(users)
            self.destroy()
            window1 = Window1()
            window1.mainloop()
        else:
            CTk.CTkLabel(self, text="Заполните все поля", text_color="red").pack(pady=10)

    def back_to_window1(self):
        self.destroy()
        window1 = Window1()
        window1.mainloop()

class Window4(CTk.CTk):
    def __init__(self, username):
        super().__init__()

        self.geometry("960x540")
        self.title(f"Проекты пользователя {username}")

        self.label0 = CTk.CTkLabel(master=self, text="", height=self.winfo_screenheight(),
                                   width=self.winfo_screenwidth(), bg_color="white")
        self.label0.place(x=0, y=0)

        self.username = username
        self.label = CTk.CTkLabel(self, text=f"Добро пожаловать, {username}", font=("GOST type B", 24), bg_color="white")
        self.label.grid(row=0, column=1, columnspan=2, padx=180, pady=5)

        self.search_label = CTk.CTkLabel(self, text="Поиск проекта", font=("GOST type B", 20), bg_color="white")
        self.search_label.grid(row=1, column=1, columnspan=2, padx=0, pady=5)
        self.search_entry = CTk.CTkEntry(self, width=300, font=("GOST type B", 20))
        self.search_entry.grid(row=2, column=1, columnspan=2, padx=0, pady=5)
        self.search_entry.bind("<Return>", self.search_project)

        self.project_listbox = tk.Listbox(self, selectmode=tk.SINGLE, height=12, width=50, font=("GOST type B", 20))
        self.project_listbox.grid(row=3, column=1, columnspan=2, padx=0, pady=20)

        self.update_project_list()

        self.project_listbox.bind("<Double-1>", self.select_project)

        self.select_button4 = CTk.CTkButton(self, text="   Открыть проект   ", command=self.open_windowtask, height=40,
                                            width=200, fg_color="transparent", font=("GOST type B", 18),
                                            bg_color="white", border_width=2, border_color="black", text_color="black",
                                            corner_radius=10)
        self.select_button4.grid(row=4, column=0, padx=10, pady=20)

        self.add_button = CTk.CTkButton(self, text="Добавить проект", command=self.add_project, height=40,
                                        width=200, fg_color="transparent", font=("GOST type B", 20),
                                        bg_color="white", border_width=2, border_color="black", text_color="black",
                                        corner_radius=10)
        self.add_button.grid(row=4, column=1, padx=0, pady=20)

        self.delete_button = CTk.CTkButton(self, text="Удалить проект", command=self.delete_project, height=40,
                                           width=200, fg_color="transparent", font=("GOST type B", 20),
                                           bg_color="white", border_width=2, border_color="black", text_color="black",
                                           corner_radius=10)
        self.delete_button.grid(row=4, column=2, padx=0, pady=20)

        self.back_button = CTk.CTkButton(self, text="Назад", command=self.back_to_window2, height=40,
                                         width=140, fg_color="transparent", font=("GOST type B", 20),
                                         bg_color="white", border_width=2, border_color="black", text_color="black",
                                         corner_radius=10)
        self.back_button.grid(row=4, column=3, padx=20, pady=20)

        for user in users:
            if user["login"] == self.username and user["job"] == "работник":
                self.add_button.grid_remove()
                self.delete_button.grid_remove()
                break

    def update_project_list(self):
        self.project_listbox.delete(0, tk.END)
        for project in projects:
            self.project_listbox.insert(tk.END, project["name"])

    def select_project(self, event):
        selected_index = self.project_listbox.curselection()
        if selected_index:
            project_name = self.project_listbox.get(selected_index)


    def search_project(self, event):
        search_query = self.search_entry.get().strip().lower()
        self.project_listbox.delete(0, tk.END)
        for project in projects:
            if search_query in project["name"].lower():
                self.project_listbox.insert(tk.END, project["name"])

    def load_projects(self):
        self.project_listbox.delete(0, tk.END)
        for project in projects:
            self.project_listbox.insert(tk.END, project["name"])

    def open_windowtask(self):
        selected_project = self.project_listbox.get(tk.ACTIVE)
        if selected_project:
            self.destroy()
            windowtask = WindowTask(self.username, selected_project)
            windowtask.mainloop()

    def add_project(self):
        project_name = simpledialog.askstring("Название проекта", "Введите название нового проекта:")
        if project_name:
            projects.append({"name": project_name, "tasks": []})
            save_projects(projects)
            self.load_projects()

    def delete_project(self):
        selected_project_name = self.project_listbox.get(tk.ACTIVE)
        if selected_project_name:
            global projects
            projects = [project for project in projects if project["name"] != selected_project_name]
            save_projects(projects)
            self.load_projects()

    def back_to_window2(self):
        self.destroy()
        window2 = Window2()
        window2.mainloop()



class WindowDeleteProject(CTk.CTk):
    def __init__(self, x, y, username):
        super().__init__()

        self.username = username

        self.geometry(f"960x540+{x}+{y}")
        self.title("Удаление проекта")

        self.label0 = CTk.CTkLabel(master=self, text="", height=self.winfo_screenheight(),
                                   width=self.winfo_screenwidth(), fg_color="white")
        self.label0.place(x=0, y=0)

        self.label1 = CTk.CTkLabel(self, text="Выберите проект для удаления", height=30, width=400,
                                   font=("GOST type B", 24), fg_color="white", text_color="black")
        self.label1.pack(pady=10)

        self.projects_combobox = CTk.CTkComboBox(self, values=[project['name'] for project in projects], height=40, width=300)
        self.projects_combobox.pack(pady=10)

        self.delete_button = CTk.CTkButton(self, text="Удалить", height=50, width=200,
                                           fg_color="transparent", font=("GOST type B", 24), bg_color="white",
                                           border_width=2, border_color="black", text_color="black", corner_radius=20,
                                           command=self.delete_project)
        self.delete_button.pack(pady=20)

        self.back_button = CTk.CTkButton(self, text="Назад", height=50, width=200,
                                         fg_color="transparent", font=("GOST type B", 24), bg_color="white",
                                         border_width=2, border_color="black", text_color="black", corner_radius=20,
                                         command=self.back_to_window4)
        self.back_button.pack(pady=20)

    def delete_project(self):
        selected_project = self.projects_combobox.get()
        if selected_project:
            global projects
            projects = [project for project in projects if project["name"] != selected_project]
            save_projects(projects)
            self.label1.configure(text="Проект удален", text_color="red")
            self.after(2000, self.destroy)

    def back_to_window4(self):
        self.destroy()
        window4 = Window4(self.username)
        window4.geometry(f"960x540+{self.winfo_x()}+{self.winfo_y()}")
        window4.mainloop()

class WindowTask(CTk.CTk):
    def __init__(self, username, project_name):
        super().__init__()

        self.geometry("960x540")
        self.title(f"Задачи проекта {project_name}")

        self.label0 = CTk.CTkLabel(master=self, text="", height=self.winfo_screenheight(),
                                   width=self.winfo_screenwidth(), bg_color="white")
        self.label0.place(x=0, y=0)

        self.username = username
        self.project_name = project_name

        self.label = CTk.CTkLabel(self, text=f"Задачи проекта {project_name}:", font=("GOST type B", 24),bg_color="white")
        self.label.grid(row=0, column=1,columnspan=2,padx=0,pady=20)

        self.task_listbox = tk.Listbox(self,height=12, width=50, font=("GOST type B", 24))
        self.task_listbox.grid(row=1, column=1,columnspan=2,padx=0,pady=20)

        self.load_tasks()

        self.add_task_button = CTk.CTkButton(self, text="Добавить задачу", command=self.add_task,height=40,
                                         width=100 , fg_color="transparent", font=("GOST type B", 18),
                                         bg_color="white", border_width=2, border_color="black", text_color="black",
                                         corner_radius=10)
        self.add_task_button.grid(row=2, column=0,padx=20,pady=20)

        self.edit_task_button = CTk.CTkButton(self, text="Редактировать задачу", command=self.edit_task,height=40,
                                         width=100 , fg_color="transparent", font=("GOST type B", 18),
                                         bg_color="white", border_width=2, border_color="black", text_color="black",
                                         corner_radius=10)
        self.edit_task_button.grid(row=2, column=1,padx=0,pady=20)

        self.delete_task_button = CTk.CTkButton(self, text="Удалить задачу", command=self.delete_task,height=40,
                                         width=100 , fg_color="transparent", font=("GOST type B", 18),
                                         bg_color="white", border_width=2, border_color="black", text_color="black",
                                         corner_radius=10)
        self.delete_task_button.grid(row=2, column=2,padx=0,pady=20)

        self.back_button = CTk.CTkButton(self, text="Назад", command=self.back_to_window4,height=40,
                                         width=120 , fg_color="transparent", font=("GOST type B", 18),
                                         bg_color="white", border_width=2, border_color="black", text_color="black",
                                         corner_radius=10)
        self.back_button.grid(row=2, column=3,padx=20,pady=20)

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for project in projects:
            if project["name"] == self.project_name:
                for task in project.get("tasks", []):
                    task_info = f"{task['name']} - статус: {task['status']}, приоритет: {task['priority']}"
                    self.task_listbox.insert(tk.END, task_info)

    def add_task(self):
        self.open_task_window()

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_info = self.task_listbox.get(selected_task_index[0])
            task_name = task_info.split(' - ')[0]
            for project in projects:
                if project["name"] == self.project_name:
                    task = next((task for task in project.get("tasks", []) if task["name"] == task_name), None)
                    if task:
                        self.open_task_window(task)

    def open_task_window(self, task=None):
        add_task_window = CTk.CTkToplevel(self)
        add_task_window.geometry("500x340+1300+0")
        add_task_window.title("Добавить задачу" if task is None else "Редактировать задачу")


        CTk.CTkLabel(add_task_window, text="Название задачи:",font=("GOST type B", 18)).pack(pady=5)
        task_name_entry = CTk.CTkEntry(add_task_window)
        task_name_entry.pack(pady=5)
        if task:
            task_name_entry.insert(0, task["name"])
            task_name_entry.configure(state='disabled')

        CTk.CTkLabel(add_task_window, text="Статус задачи:",font=("GOST type B", 18)).pack(pady=5)
        status_combobox = CTk.CTkComboBox(add_task_window, values=["Готово", "В работе"],font=("GOST type B", 18))
        status_combobox.pack(pady=5)
        if task:
            status_combobox.set(task["status"])

        CTk.CTkLabel(add_task_window, text="Приоритет задачи:").pack(pady=5)
        priority_combobox = CTk.CTkComboBox(add_task_window, values=["Первый", "Второй"],font=("GOST type B", 18))
        priority_combobox.pack(pady=5)
        if task:
            priority_combobox.set(task["priority"])

        def save_task():
            task_name = task_name_entry.get()
            status = status_combobox.get()
            priority = priority_combobox.get()

            if task_name and status and priority:
                for project in projects:
                    if project["name"] == self.project_name:
                        if task:
                            task["status"] = status
                            task["priority"] = priority
                        else:
                            project["tasks"].append({"name": task_name, "status": status, "priority": priority})
                        save_projects(projects)
                        self.load_tasks()
                        add_task_window.destroy()
                        return

        CTk.CTkButton(add_task_window, text="Сохранить", command=save_task,font=("GOST type B", 18)).pack(pady=10)
        CTk.CTkButton(add_task_window, text="Отмена", command=add_task_window.destroy,font=("GOST type B", 18)).pack(pady=10)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_info = self.task_listbox.get(selected_task_index[0])
            task_name = task_info.split(' - ')[0]

            for project in projects:
                if project["name"] == self.project_name:
                    project["tasks"] = [task for task in project.get("tasks", []) if task["name"] != task_name]
                    save_projects(projects)
                    self.load_tasks()
                    return

    def back_to_window4(self):
        self.destroy()
        window4 = Window4(self.username)
        window4.mainloop()




if __name__ == "__main__":
    window1 = Window1()
    window1.mainloop()
