import time

tasks = []


def add_task():
    name = input("أدخل اسم المهمة: ")
    duration = int(input("كم دقيقة تحتاج لتنفيذها؟ "))
    tasks.append({"name": name, "duration": duration})
    print(f"✅ تم إضافة المهمة: {name} ({duration} دقيقة)")


def show_tasks():
    if not tasks:
        print("📭 لا توجد مهام حالياً.")
        return
    print("\n📋 قائمة المهام:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']} - {task['duration']} دقيقة")


def start_task():
    if not tasks:
        print("📭 لا توجد مهام لبدء تنفيذها.")
        return
    show_tasks()
    choice = int(input("اختر رقم المهمة لبدء تنفيذها: ")) - 1
    if 0 <= choice < len(tasks):
        task = tasks[choice]
        print(f"🚀 بدء المهمة: {task['name']} ({task['duration']} دقيقة)")
        for i in range(task['duration'], 0, -1):
            print(f"⏳ متبقي: {i} دقيقة", end="\r")
            time.sleep(60)  # 60 ثانية لكل دقيقة
        print(f"\n✅ تم الانتهاء من المهمة: {task['name']}")
        tasks.pop(choice)
    else:
        print("❌ رقم غير صحيح.")


def main():
    while True:
        print("\n--- منظم الوقت ---")
        print("1. إضافة مهمة")
        print("2. عرض المهام")
        print("3. بدء تنفيذ مهمة")
        print("4. خروج")
        choice = input("اختر رقم: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            start_task()
        elif choice == "4":
            print("👋 إلى اللقاء!")
            break
        else:
            print("❌ خيار غير صحيح.")


if __name__ == "__main__":
    main()
