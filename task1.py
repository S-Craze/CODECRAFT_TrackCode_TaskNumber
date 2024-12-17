#To Do List

import tkinter as tk
from tkinter import messagebox
import json

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        task = Task(data['title'], data['description'])
        task.completed = data['completed']
        return task

class ToDoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task):
        self.tasks.remove(task)
        self.save_tasks()

    def get_tasks(self):
        return self.tasks

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                tasks_data = json.load(f)
                return [Task.from_dict(task) for task in tasks_data]
        except FileNotFoundError:
            return []

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.todo_list = ToDoList()

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.title_label = tk.Label(self.frame, text="Task Title")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.frame)
        self.title_entry.pack()

        self.desc_label = tk.Label(self.frame, text="Task Description")
        self.desc_label.pack()
        self.desc_entry = tk.Entry(self.frame)
        self.desc_entry.pack()

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(self.frame)
        self.tasks_listbox.pack()

        self.complete_button = tk.Button(self.frame, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack()

        self.remove_button = tk.Button(self.frame, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.load_tasks()

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()
        if title and description:
            task = Task(title, description)
            self.todo_list.add_task(task)
            self.update_tasks_listbox()
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both title and description")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.todo_list.get_tasks():
            status = "Completed" if task.completed else "Pending"
            self.tasks_listbox.insert(tk.END, f"{task.title} - {task.description} [{status}]")

    def mark_complete(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task = self.todo_list.get_tasks()[selected_task_index[0]]
            task.mark_complete()
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark complete")

    def remove_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task = self.todo_list.get_tasks()[selected_task_index[0]]
            self.todo_list.remove_task(task)
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to remove")

    def load_tasks(self):
        self.update_tasks_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
