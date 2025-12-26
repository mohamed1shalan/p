import threading
import multiprocessing
import time

# ==============================================================================
# الجزء الأول: I/O Bound Tasks (Threading is Good)
# السبب: المهام التي تعتمد على الانتظار (مثل تحميل الملفات) لا تتأثر بالـ GIL.
# لأن الـ Thread يسلم الـ CPU لغيره أثناء الانتظار.
# ==============================================================================


def download_file(file_number):
    print(f"   [Thread-{file_number}] Starting download...")
    time.sleep(1)  # محاكاة للانتظار (I/O Operation)
    print(f"   [Thread-{file_number}] Finished download.")


def run_io_demo():
    print("\n--- 1. I/O Bound Task (Threading Demo) ---")
    start_time = time.time()

    threads = []
    # سنقوم بإنشاء 5 خيوط (Threads) تعمل معاً
    for i in range(5):
        # target: اسم الدالة بدون أقواس
        # args: المعاملات داخل tuple. ملاحظة: الفاصلة (i,) ضرورية جداً!
        t = threading.Thread(target=download_file, args=(i,))
        threads.append(t)
        t.start()  # تشغيل الخيط في الخلفية

    # join: تجعل البرنامج الرئيسي ينتظر انتهاء الخيوط قبل الاستمرار
    for t in threads:
        t.join()

    end_time = time.time()
    # النتيجة المتوقعة: حوالي ثانية واحدة لأنهم عملوا بالتوازي أثناء الانتظار
    print(f"Total Time (Threading): {end_time - start_time:.2f} seconds.")


# ==============================================================================
# الجزء الثاني: CPU Bound Tasks & The GIL (Threading is BAD here)
# السبب: بايثون تسمح لـ Thread واحد فقط بالعمل فعلياً بسبب الـ GIL.
# في العمليات الحسابية، الـ Threads تتنافس على CPU واحد، مما يبطئ العمل.
# الحل: استخدام Multiprocessing.
# ==============================================================================

def cpu_heavy_task():
    # عملية حسابية ثقيلة تستهلك المعالج
    count = 50_000_000
    while count > 0:
        count -= 1


def run_cpu_demo():
    print("\n--- 2. CPU Bound Task (Threading vs Multiprocessing) ---")

    # 1. تجربة الـ Threading (ستكون بطيئة)
    print("   Starting Threading test (Wait...)...")
    start_thread = time.time()
    t1 = threading.Thread(target=cpu_heavy_task)
    t2 = threading.Thread(target=cpu_heavy_task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(
        f"   Threading Time (Affected by GIL): {time.time() - start_thread:.2f}s")

    # 2. تجربة الـ Multiprocessing (توازي حقيقي)
    # كل Process لها Memory و GIL خاص بها، لذا تعمل على Cores مختلفة.
    print("   Starting Multiprocessing test...")
    start_process = time.time()
    p1 = multiprocessing.Process(target=cpu_heavy_task)
    p2 = multiprocessing.Process(target=cpu_heavy_task)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(
        f"   Multiprocessing Time (True Parallel): {time.time() - start_process:.2f}s")


# ==============================================================================
# الجزء الثالث: Race Conditions & Locks
# السبب: الـ Threads تتشارك الذاكرة. لو عدلوا نفس المتغير في نفس الوقت، القيمة بتخرب.
# الحل: استخدام Lock لحماية المنطقة الحرجة (Critical Section).
# ==============================================================================

shared_counter = 0
lock = threading.Lock()  # إنشاء القفل


def unsafe_update():
    global shared_counter
    for _ in range(100000):
        # هنا يحدث تداخل (Race Condition)
        shared_counter += 1


def safe_update():
    global shared_counter
    for _ in range(100000):
        # with lock: تضمن أن خيطاً واحداً فقط يدخل هذا البلوك في المرة الواحدة
        with lock:
            shared_counter += 1


def run_race_condition_demo():
    global shared_counter
    print("\n--- 3. Race Condition & Locks ---")

    # 1. التجربة بدون قفل (نتيجة خاطئة)
    shared_counter = 0
    t1 = threading.Thread(target=unsafe_update)
    t2 = threading.Thread(target=unsafe_update)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(
        f"   Unsafe Counter Result (Should be 200000): {shared_counter} (BUG!)")

    # 2. التجربة مع القفل (نتيجة صحيحة)
    shared_counter = 0
    t1 = threading.Thread(target=safe_update)
    t2 = threading.Thread(target=safe_update)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"   Safe Counter Result (With Lock): {shared_counter} (Correct!)")


# ==============================================================================
# التشغيل الرئيسي
# شرط if __name__ == "__main__" ضروري جداً عند استخدام Multiprocessing
# لمنع تكرار تشغيل الكود بشكل لا نهائي (Infinite Loop) على ويندوز.
# ==============================================================================
if __name__ == "__main__":
    run_io_demo()            # Lab 1: Part 1 (I/O Threading)
    run_cpu_demo()           # Lab 1: Part 2 (GIL & Multiprocessing)
    run_race_condition_demo()  # Lab 1: Part 3 (Locks)


# شرح تفصيلي للأسباب (Why?) بناءً على محتوى السكشن:
# 1. ليه استخدمنا threading في الجزء الأول (Download)؟

# النوع: المهمة هنا I/O Bound (تحميل، انتظار).

# السبب: عندما يتوقف الـ Thread بسبب time.sleep أو انتظار الشبكة، يقوم الـ GIL بالسماح لـ Thread آخر بالعمل.


# النتيجة: نحصل على سرعة عالية وكأننا نعمل بالتوازي.

# 2. ليه الـ threading كان بطيء في الجزء الثاني (CPU)؟

# النوع: المهمة CPU Bound (حسابات كثيرة).


# المشكلة (The GIL): في بايثون، الـ GIL (Global Interpreter Lock) يمنع تشغيل أكثر من Thread واحد في نفس اللحظة لتنفيذ كود بايثون .

# النتيجة: الـ Threads ستعمل بالتناوب (Concurrency) وليس بالتوازي (Parallelism)، ومع تكلفة التبديل بينهم (Context Switching)، قد يكون الأداء أبطأ من التسلسلي!

# 3. ليه استخدمنا multiprocessing لحل مشكلة الـ CPU؟

# الحل: الـ Process هي عملية مستقلة تماماً، لها الذاكرة الخاصة بها ولها الـ GIL الخاص بها .


# النتيجة: يمكن تشغيل العمليتين على نواتين (Cores) مختلفتين في المعالج في نفس اللحظة (True Parallelism).

# 4. ليه النتيجة طلعت غلط في unsafe_update؟
# السبب (Race Condition): عملية counter += 1 ليست خطوة واحدة، بل هي ثلاث خطوات (قراءة القيمة، تزويدها، حفظها).

# عندما يعمل خيطان في نفس الوقت، قد يقرأ الاثنان نفس القيمة (مثلاً 5) ويزودانها لتصبح 6. النتيجة المحفوظة ستكون 6 بدلاً من 7. ضاعت عملية جمع!.
# +1

# 5. ليه with lock صلحت المشكلة؟
# السبب: الـ Lock يجبر الـ Threads على "الاصطفاف". لا يمكن لأي Thread الدخول لتعديل المتغير إلا إذا كان يحمل المفتاح. هذا يحول المنطقة الحرجة (Critical Section) إلى عملية ذرية (Atomic) لا يمكن مقاطعتها
