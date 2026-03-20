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
            update_task()
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
    task_id = len(tasks) + 12
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
    global tasks
    print("\n--- รายการงานทั้งหมด ---")
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "เสร็จแล้ว" if task["completed"] else "ยังไม่เสร็จ"
        print(f"{idx}. {task['title']} | วันครบกำหนด: {task['due_date']} | สถานะ: {status}")

def update_task():
    global tasks
    print("\n--- แก้ไขงาน ---")
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return
    view_tasks()
    try:
        index = int(input("เลือกงานที่จะแก้ไข (ลำดับ): "))
    except ValueError:
        print("กรุณาป้อนตัวเลขลำดับให้ถูกต้อง")
        return
    if index < 1 or index > len(tasks):
        print("ลำดับไม่ถูกต้อง")
        return
    task = tasks[index - 1]
    print(f"งานเดิม: {task['title']}, {task['description']}, วันครบกำหนด: {task['due_date']}, สถานะ: {'เสร็จแล้ว' if task['completed'] else 'ยังไม่เสร็จ'}")
    new_title = input(f"ชื่อเรื่องใหม่ (Enter เพื่อข้าม): ")
    new_description = input(f"รายละเอียดใหม่ (Enter เพื่อข้าม): ")
    new_completed = input(f"สถานะเสร็จแล้ว? (y/n, Enter เพื่อข้าม): ")
    if new_title:
        task['title'] = new_title
    if new_description:
        task['description'] = new_description
    if new_completed.lower() == 'y':
        task['completed'] = True
    elif new_completed.lower() == 'n':
        task['completed'] = False
    print("แก้ไขงานสำเร็จ!")

def edit_task():
    pass

def delete_task():
    global tasks
    print("\n--- ลบงาน ---")
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return
    view_tasks()
    try:
        index = int(input("เลือกงานที่ต้องการลบ (ลำดับ): "))
    except ValueError:
        print("กรุณาป้อนตัวเลขลำดับให้ถูกต้อง")
        return
    if index < 1 or index > len(tasks):
        print("ลำดับไม่ถูกต้อง")
        return
    task = tasks[index - 1]
    confirm = input(f"ต้องการลบงานนี้จริงหรือไม่ (y/n): {task['title']} ")
    if confirm.lower() == 'y':
        tasks.pop(index - 1)
        print("ลบงานสำเร็จ!")
    else:
        print("ยกเลิกการลบงาน")

if __name__ == "__main__":
    main()