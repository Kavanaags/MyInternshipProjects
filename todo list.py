import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime, timedelta

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []
        self.completed_tasks = []

        # Task input
        tk.Label(root, text="Task Description:").grid(row=0, column=0, padx=10, pady=10)
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)

        # Due date input using spinboxes
        tk.Label(root, text="Due Date:").grid(row=1, column=0, padx=10, pady=10)
        self.day_spinbox = tk.Spinbox(root, from_=1, to=31, width=3)
        self.month_spinbox = tk.Spinbox(root, from_=1, to=12, width=3)
        self.year_spinbox = tk.Spinbox(root, from_=datetime.now().year, to=2050, width=5)
        self.day_spinbox.grid(row=1, column=1, padx=5, pady=10)
        self.month_spinbox.grid(row=1, column=2, padx=5, pady=10)
        self.year_spinbox.grid(row=1, column=3, padx=5, pady=10)

        # Priority input
        tk.Label(root, text="Priority:").grid(row=2, column=0, padx=10, pady=10)
        priority_options = ["High", "Medium", "Low"]
        self.priority_var = tk.StringVar(root)
        self.priority_var.set(priority_options[1])  # default to Medium
        priority_menu = tk.OptionMenu(root, self.priority_var, *priority_options)
        priority_menu.grid(row=2, column=1, padx=10, pady=10)

        # Add Task button
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=4, rowspan=3, padx=10, pady=10)

        # Task List
        self.task_listbox = tk.Listbox(root, width=60, height=10)
        self.task_listbox.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        # Buttons for actions
        update_button = tk.Button(root, text="Update Task", command=self.update_task)
        update_button.grid(row=4, column=0, padx=10, pady=10)

        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=4, column=1, padx=10, pady=10)

        complete_button = tk.Button(root, text="Mark Completed", command=self.complete_task)
        complete_button.grid(row=4, column=2, padx=10, pady=10)

        # Display Completed Tasks
        tk.Label(root, text="Completed Tasks:").grid(row=5, column=0, columnspan=5, pady=10)
        self.completed_listbox = tk.Listbox(root, width=60, height=5)
        self.completed_listbox.grid(row=6, column=0, columnspan=5, padx=10, pady=10)

    def add_task(self):
        task_description = self.task_entry.get()
        day = int(self.day_spinbox.get())
        month = int(self.month_spinbox.get())
        year = int(self.year_spinbox.get())
        priority = self.priority_var.get()

        try:
            due_date = datetime(year, month, day)
            current_date = datetime.now()

            if current_date <= due_date:
                task = {"description": task_description, "due_date": due_date.strftime("%Y-%m-%d"), "priority": priority, "completed": False}
                self.tasks.append(task)
                self.update_task_list()
                self.task_entry.delete(0, tk.END)
                self.clear_spinboxes()
            else:
                messagebox.showwarning("Warning", "Due date should be today or in the future.")
        except ValueError:
            messagebox.showwarning("Warning", "Invalid date.")

    def clear_spinboxes(self):
        self.day_spinbox.delete(0, tk.END)
        self.month_spinbox.delete(0, tk.END)
        self.year_spinbox.delete(0, tk.END)

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = " [Completed]" if task["completed"] else ""
            self.task_listbox.insert(tk.END, f"{task['description']} - Due: {task['due_date']}, Priority: {task['priority']}{status}")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_description = simpledialog.askstring("Input", "Enter new task description:")
            if new_description:
                self.tasks[selected_task_index[0]]["description"] = new_description
                self.update_task_list()

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["completed"] = True
            completed_task = self.tasks.pop(selected_task_index[0])
            self.completed_tasks.append(completed_task)
            self.update_task_list()
            self.update_completed_list()

    def update_completed_list(self):
        self.completed_listbox.delete(0, tk.END)
        for task in self.completed_tasks:
            self.completed_listbox.insert(tk.END, f"{task['description']} - Due: {task['due_date']}, Priority: {task['priority']} [Completed]")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
