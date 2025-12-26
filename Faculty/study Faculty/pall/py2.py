import threading
import time
import concurrent.futures

# ==============================================================================
# الجزء الأول: الإدارة الحديثة للـ Threads (ThreadPoolExecutor)
# السبب: الطريقة اليدوية (إنشاء قائمة threads وعمل start ثم join) مرهقة وعرضة للأخطاء.
# الـ Executor بيدير "مسبح" من العمال (Workers) وينظم العمل بينهم أوتوماتيكياً.
# ==============================================================================


def worker_task(name, duration):
    print(f"   [Worker-{name}] Started (will take {duration}s)")
    time.sleep(duration)
    print(f"   [Worker-{name}] Finished")


def run_executor_demo():
    print("\n--- 1. ThreadPoolExecutor Demo ---")

    # max_workers=2: يعني شغل 2 threads بس في نفس اللحظة، والباقي يقف طابور
    # with: عشان يضمن إن الـ Pool يتقفل صح لما نخلص (Context Manager)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        print("   Submitting tasks...")
        # submit: بتبعت المهمة للمدير، وهو بيقرر امتى يشغلها حسب العمال المتاحين
        executor.submit(worker_task, "A", 2)
        executor.submit(worker_task, "B", 1)
        executor.submit(worker_task, "C", 1)  # دي هتستنى لما حد من A أو B يخلص

    print("   All tasks completed by Executor.")


# ==============================================================================
# الجزء الثاني: إنشاء Thread عن طريق الوراثة (Subclassing)
# السبب: تنظيم الكود (OOP). لو الـ Thread ليه بيانات خاصة بيه وخصائص كتير،
# الأفضل نعمله كلاس مستقل بدل ما نكتب دالة عادية.
# ==============================================================================

# 1. الوراثة من threading.Thread
class MyCustomThread(threading.Thread):
    def __init__(self, thread_id):
        # 2. لازم ننادي الـ init بتاع الأب عشان الـ thread يتبني صح في الذاكرة
        threading.Thread.__init__(self)
        self.my_id = thread_id

    # 3. دالة run هي المكان الوحيد اللي الكود بتاعه بيشتغل في الخلفية
    def run(self):
        print(f"   [Class-Thread {self.my_id}] Running custom logic...")
        time.sleep(1)
        print(f"   [Class-Thread {self.my_id}] Done.")


def run_subclass_demo():
    print("\n--- 2. Subclassing Thread Demo ---")
    t1 = MyCustomThread(101)
    t2 = MyCustomThread(102)

    t1.start()  # بايثون هتروح تنادي دالة run() لوحدها
    t2.start()

    t1.join()
    t2.join()


# ==============================================================================
# الجزء الثالث: المشكلة والحل (Race Condition vs Locks)
# السبب: لما كذا thread يعدلوا متغير واحد، القراءات بتدخل في بعضها (Interleaving).
# الحل: الـ Lock بيخلي العملية "ذرية" (Atomic)، يعني محدش يقاطعها.
# ==============================================================================

shared_data = 0
lock = threading.Lock()  # القفل المشترك


def unsafe_function():
    global shared_data
    for _ in range(100000):
        # مشكلة: قراءة وتعديل وكتابة بدون حماية
        # ممكن thread تاني يقطعنا في النص ويغير القيمة
        shared_data += 1


def safe_function_with_lock():
    global shared_data
    for _ in range(100000):
        # الحل: استخدام with lock
        # بيعمل acquire() في البداية و release() في النهاية أوتوماتيك
        with lock:
            shared_data += 1


def run_race_condition_demo():
    global shared_data
    print("\n--- 3. Race Condition & Lock Demo ---")

    # 1. تجربة الفشل (بدون Lock)
    shared_data = 0
    t1 = threading.Thread(target=unsafe_function)
    t2 = threading.Thread(target=unsafe_function)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # النتيجة المتوقعة: رقم عشوائي أقل من 200,000
    print(f"   Without Lock Result: {shared_data} (Expected 200000) -> ERROR")

    # 2. تجربة النجاح (مع Lock)
    shared_data = 0
    t1 = threading.Thread(target=safe_function_with_lock)
    t2 = threading.Thread(target=safe_function_with_lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # النتيجة المتوقعة: 200,000 بالظبط
    print(
        f"   With Lock Result:    {shared_data} (Expected 200000) -> SUCCESS")


if __name__ == "__main__":
    run_executor_demo()      # الجزء الأول: الإدارة الحديثة
    run_subclass_demo()      # الجزء الثاني: الوراثة
    run_race_condition_demo()  # الجزء الثالث: القفل وحماية البيانات


# . لماذا نستخدم ThreadPoolExecutor بدلاً من Thread العادي؟
# المشكلة: في الطريقة القديمة، كنا بنعمل list ونحط فيها الـ threads ونعمل loop للـ start و loop للـ join. ولو نسينا join واحد، البرنامج ممكن يضرب.

# الحل: الـ Executor بيشيل عنك الهم ده.

# في الكود: استخدمنا max_workers=2. هتلاحظ في الـ Output إن المهمة C مابدأتش غير لما B خلصت، لأن الـ Pool كان مليان. ده بيحميك إنك تفتح 1000 thread وتهنج الجهاز .

# 2. لماذا نستخدم الوراثة (Subclassing)؟
# السبب: التنظيم (OOP). لو بتعمل برنامج شات مثلاً، هتعمل كلاس اسمه ClientThread، وتخزن فيه اسم المستخدم والـ IP جوه self. ده صعب تعمله بالدوال العادية.

# الشرط: لازم تعرف دالة run(). دي الدالة "المقدسة" اللي start() بتدور عليها عشان تشغلها .

# 3. ما هي مشكلة الـ Race Condition بالضبط؟
# السيناريو: تخيل shared = 10.

# Thread A قرأ 10. (لسه مزودش).

# Thread B قرأ 10. (لسه مزودش).

# Thread A زود وبقت 11 وحفظها.

# Thread B زود (على الـ 10 اللي قرأها) وبقت 11 وحفظها.


# الكارثة: العمليتين حصلوا، بس القيمة زادت 1 بس بدل 2. ده اسمه Lost Update .

# 4. لماذا with lock هي الحل الأمثل؟
# الحماية: بتعمل منطقة عازلة (Critical Section). مستحيل Thread B يدخل يقرأ المتغير طول ما Thread A لسه بيعدل فيه.

# الأمان (Context Manager): أهم ميزة في with إنها بتضمن فتح القفل (release) حتى لو الكود ضرب Error. لو كنت بتستخدم الطريقة اليدوية (acquire/release) وحصل Error قبل الـ release، البرنامج كله هيدخل في Deadlock ويقف للأبد .
