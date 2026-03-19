# This script prints 'Hello World' to the console

def main():

    global tasks
    tasks = []
    while True:
        print("\n===== ToDo List Menu =====")
        print("1. เพิ่มงานใหม่")
        print("2. ดูงานทั้งหมด")
        print("3. แก้ไขงาน")
        print("4. ลบงาน")
        print("5. ออกจากโปรแกรม")
        choice = input("เลือกเมนู (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("ออกจากโปรแกรม")
            break
        else:
            print("กรุณาเลือกเมนู 1-5 เท่านั้น")

def add_task():
    global tasks
    print("\n--- เพิ่มงานใหม่ ---")
    title = input("ชื่อเรื่อง: ")
    description = input("รายละเอียด: ")
    due_date = input("วันครบกำหนด (YYYY-MM-DD): ")
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("เพิ่มงานสำเร็จ!")

def view_tasks():
    pass

def edit_task():
    pass

def delete_task():
    pass

if __name__ == "__main__":
    main()