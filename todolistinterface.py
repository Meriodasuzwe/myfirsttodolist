import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

filename = "tasks.json"
tasks = {}
task_id = 1

# Загрузка задач
try:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        tasks = {int(k): v for k, v in data.items()}
        if tasks:
            task_id = max(tasks.keys()) + 1
except FileNotFoundError:
    pass
except json.JSONDecodeError:
    pass

# Функции
def refresh_listbox():
    listbox.delete(0, tk.END)
    for id, info in tasks.items():
        status = "✅" if info["done"] else "❌"
        listbox.insert(tk.END, f"{id}. {info['text']} | {status} | {info['created']}")

def add_task():
    global task_id
    text = entry.get().strip()
    if text:
        tasks[task_id] = {
            "text": text,
            "done": False,
            "created": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        task_id += 1
        entry.delete(0, tk.END)
        refresh_listbox()
    else:
        messagebox.showwarning("Ошибка", "Введите текст задачи")

def mark_done():
    try:
        selected = listbox.get(listbox.curselection())
        id = int(selected.split(".")[0])
        tasks[id]["done"] = True
        refresh_listbox()
    except:
        messagebox.showwarning("Ошибка", "Выберите задачу для отметки")

def delete_task():
    try:
        selected = listbox.get(listbox.curselection())
        id = int(selected.split(".")[0])
        tasks.pop(id)
        refresh_listbox()
    except:
        messagebox.showwarning("Ошибка", "Выберите задачу для удаления")

def save_and_exit():
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)
    root.destroy()

# GUI
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x400")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

btn_add = tk.Button(root, text="Добавить задачу", command=add_task)
btn_add.pack(pady=5)

listbox = tk.Listbox(root, width=80)
listbox.pack(pady=10, expand=True, fill=tk.BOTH)

btn_done = tk.Button(root, text="Отметить выполненной", command=mark_done)
btn_done.pack(pady=5)

btn_delete = tk.Button(root, text="Удалить задачу", command=delete_task)
btn_delete.pack(pady=5)

btn_save = tk.Button(root, text="Сохранить и выйти", command=save_and_exit)
btn_save.pack(pady=5)

refresh_listbox()
root.mainloop()
