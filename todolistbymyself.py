import json
from datetime import datetime

filename="tasks.json"
tasks={}
task_id=1

try:
    with open(filename,"r",encoding="utf-8") as f:
        tasks=json.load(f)
        tasks={int(k):v for k,v in tasks.items()}
        if tasks:
            task_id=max(tasks.keys())+1
except FileNotFoundError:
    pass


while True:
    print("\n=== Список дел ===")
    print("1. Ввести задачу")
    print("2. Просмотреть задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    print("5. Выход")
    
    choice=input("Введите число от 1 до 5:")
    
    if choice=="1":
        text = input("Введите задачу: ")
        tasks[task_id]={
            "text":text,
            "done":False,
            "created":datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        print(f"Задача '{text}' добавлена под номером {task_id}")
        task_id+=1
    
    elif choice =="2":
        if not tasks:
            print("Нет задач для просмотра")
        else:
            print("\nСписок задач:")
            for id,info in tasks.items():
                status="✅"if info["done"]else"❌"
                print(f"{id}. {info['text']} | {status} | создана: {info['created']}")
    elif choice=="4":
        if not tasks:
            print("Нет задач для удаления")
        else:
            delete_id = input("Введите ID задачи для удаления: ")
            if delete_id.isdigit() and int(delete_id)in tasks:
                removed=tasks.pop(int(delete_id))
                print(f"Задача '{removed['text']}' удалена ❌")
            else:
                print("Неверный ID")
    elif choice=="3":
        if not tasks:
            print("Нет задач для отметки")
        else:
            done_id = input("Введите ID задачи для отметки как выполненной: ")
            if done_id.isdigit() and int(done_id) in tasks:
                tasks[int(done_id)]["done"]=True
                print(f"Задача '{tasks[int(done_id)]['text']}' отмечена как выполненная ✅")
            else:
                print("Неверный ID")
    
    elif choice=="5":
        print("Сохраняю и выхожу...")
        break
    else:
        print("Неверное значение!")
        
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)
        

                
