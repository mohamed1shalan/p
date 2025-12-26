import multiprocessing
import time
import os

# ==============================================================================
# دالة مساعدة عشان نعرف إحنا في أنهي عملية (توضيح فقط)
# ==============================================================================


def print_process_info(msg):
    print(f"[{msg}] Executed by PID: {os.getpid()}")

# ==============================================================================
# الجزء الأول: Queue (الطابور الآمن للعمليات)
# السبب: العمليات (Processes) ذاكرتها منفصلة. لو استخدمت list عادية، كل عملية هتاخد
# نسخة منها وأي تعديل مش هيسمع عند التانية. الـ Queue هو الحل للربط بينهم.
# ==============================================================================


def producer_func(q):
    print_process_info("Producer")
    for i in range(3):
        item = f"Data_{i}"
        q.put(item)  # وضع البيانات في الطابور
        print(f"   -> Producer sent: {item}")
        time.sleep(0.5)


def consumer_func(q):
    print_process_info("Consumer")
    for i in range(3):
        # get() هيوقف العملية لحد ما يلاقي بيانات (Blocking)
        item = q.get()
        print(f"   <- Consumer received: {item}")


def run_queue_demo():
    print("\n--- 1. Multiprocessing Queue Demo ---")
    # نستخدم multiprocessing.Queue وليس queue.Queue (بتاعة الـ Threads)
    # لأن دي بتستخدم Pickle عشان تنقل البيانات بين الذاكرة المنفصلة
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=producer_func, args=(q,))
    p2 = multiprocessing.Process(target=consumer_func, args=(q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()


# ==============================================================================
# الجزء الثاني: Pipe (الماسورة السريعة)
# السبب: الـ Queue بطيئة شوية لأنها بتعمل locking عشان الأمان.
# لو عندك عمليتين بس بيكلموا بعض، الـ Pipe أسرع بكتير لأنها اتصال مباشر (Full Duplex).
# ==============================================================================
def sender_pipe(conn):
    print_process_info("Sender-Pipe")
    msg = "Hello from the other side!"
    conn.send(msg)  # إرسال مباشر
    conn.close()   # لازم نقفل الاتصال


def receiver_pipe(conn):
    print_process_info("Receiver-Pipe")
    if conn.poll():  # (اختياري) نتأكد إن فيه داتا قبل ما نعمل recv
        print("   Checking pipe... Data found.")

    msg = conn.recv()  # استقبال (Blocking)
    print(f"   Received via Pipe: {msg}")


def run_pipe_demo():
    print("\n--- 2. Multiprocessing Pipe Demo ---")
    # بترجع طرفين: parent_conn و child_conn
    parent_conn, child_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=sender_pipe, args=(child_conn,))
    p.start()

    # العملية الرئيسية (Parent) هتستقبل
    receiver_pipe(parent_conn)
    p.join()


# ==============================================================================
# الجزء الثالث: Pool (Map & Async) - أهم جزء للامتحان
# السبب: لو عندنا 1000 رقم، مينفعش نفتح 1000 عملية (الجهاز هيموت).
# الـ Pool بيفتح عدد ثابت (4 مثلاً) ويوزع عليهم الـ 1000 مهمة بذكاء.
# ==============================================================================

# دالة حسابية بسيطة (تربيع الرقم)
def square_task(n):
    # time.sleep(0.1) # محاكاة لعملية بتاخد وقت
    return n * n


def run_pool_demo():
    print("\n--- 3. Process Pool Demo ---")
    data = [1, 2, 3, 4, 5, 6, 7, 8]

    # نفتح Pool فيه 3 عمال (Processes)
    with multiprocessing.Pool(processes=3) as pool:

        # أ) الطريقة المتزامنة (Synchronous Map)
        # السبب: بنستخدمها لما نكون محتاجين النتائج ومترتبة عشان نكمل شغل حالاً.
        # البرنامج هيقف هنا لحد ما كل الأرقام تتحسب.
        print("   [Map] Starting sync map (Blocking)...")
        results = pool.map(square_task, data)
        print(f"   [Map] Results: {results}")

        # ب) الطريقة غير المتزامنة (Asynchronous Map)
        # السبب: بنستخدمها لما نكون عايزين نرمي الشغل للعمال ونكمل إحنا شغل تاني
        # (زي واجهة رسومية GUI مش عايزينها تهنج).
        print("   [Map_Async] Starting async map (Non-Blocking)...")
        async_result = pool.map_async(square_task, data)

        print("   [Main] I can do other work while Pool is working...")

        # لما نعوز النتيجة، بنعمل get()
        # لو خلصوا هتيجي فوراً، لو مخلصوش هنستنى هنا
        print(f"   [Map_Async] Final Results: {async_result.get()}")

        # ج) تحسين الأداء (Chunksize)
        # السبب: بدل ما نبعت للعمال رقم رقم (تضييع وقت في المواصلات)،
        # بنبعتلهم "حزم". كل عامل ياخد حزمة فيها رقمين مثلاً يحسبهم ويرجع.
        # ده بيقلل الـ Overhead جداً في الداتا الكبيرة.
        print("   [Chunksize] Optimizing with chunks...")
        res_chunk = pool.map(square_task, data, chunksize=2)
        print(f"   [Chunksize] Results: {res_chunk}")


# ==============================================================================
# التشغيل الرئيسي (إجباري في الويندوز)
# ==============================================================================
if __name__ == "__main__":
    run_queue_demo()
    time.sleep(1)
    run_pipe_demo()
    time.sleep(1)
    run_pool_demo()
