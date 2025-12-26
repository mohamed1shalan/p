import threading
import multiprocessing
import time
import random
from queue import Queue

# ==============================================================================
# الجزء الأول: الإشارات باستخدام Event
# السبب: أحياناً نحتاج خيط يقول لخيط تاني "ابدأ دلوقت".
# لو استخدمنا متغير عادي (Flag)، الخيط المنتظر هيعمل Busy Waiting (يفضل يلف ويسأل).
# الحل: Event. الخيط المنتظر ينام بـ wait()، والخيط التاني يصحيه بـ set().
# ==============================================================================

event_signal = threading.Event()
shared_data_event = None


def producer_event():
    global shared_data_event
    print("   [Producer-Event] Preparing data...")
    time.sleep(1)
    shared_data_event = random.randint(100, 999)
    print("   [Producer-Event] Data Ready. Setting Event flag.")

    # 1. ارفع العلم (set): أي حد عامل wait() هيصحى فوراً
    event_signal.set()


def consumer_event():
    print("   [Consumer-Event] Waiting for signal...")

    # 2. نام واستنى الإشارة (wait): لا يستهلك CPU
    event_signal.wait()

    print(f"   [Consumer-Event] Woke up! Data is: {shared_data_event}")

    # 3. نزل العلم (clear): عشان نستعد للمرة الجاية (لو فيه loop)
    event_signal.clear()


def run_event_demo():
    print("\n--- 1. Event Demo (Signaling) ---")
    t1 = threading.Thread(target=producer_event)
    t2 = threading.Thread(target=consumer_event)
    t2.start()  # شغل المستهلك الأول عشان ينام
    t1.start()
    t1.join()
    t2.join()


# ==============================================================================
# الجزء الثاني: الطابور الآمن Queue (أهم جزء)
# السبب: الـ Event ينفع للإشارة بس، لكن لو عايز تنقل بيانات كتير بسرعة، البيانات ممكن تضيع
# أو تتداخل (Race Condition) لو استخدمنا متغير shared عادي.
# الحل: Queue. هي Thread-Safe، بتنظم الدور، ولو فاضية المستهلك بينام لوحده.
# ==============================================================================

safe_queue = Queue()


def producer_queue():
    for i in range(3):
        item = f"Pack_{i}"
        print(f"   [Producer-Queue] Putting {item}...")
        # put: حط في الطابور. لو مليان، هينتظر.
        safe_queue.put(item)
        time.sleep(0.5)


def consumer_queue():
    for i in range(3):
        # get: هات من الطابور. لو فاضي، هينام أوتوماتيك (Blocking).
        item = safe_queue.get()
        print(f"   [Consumer-Queue] Got {item}")

        # task_done: قول للطابور إني خلصت معالجة العنصر ده
        safe_queue.task_done()


def run_queue_demo():
    print("\n--- 2. Queue Demo (Safe Data Transfer) ---")
    t1 = threading.Thread(target=producer_queue)
    t2 = threading.Thread(target=consumer_queue)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# ==============================================================================
# الجزء الثالث: Process Pool (مسبح العمليات)
# السبب: إنشاء Process عملية مكلفة (Heavyweight). لو عندك 1000 مهمة، مينفعش تفتح 1000 Process.
# الحل: Pool. بتفتح عدد ثابت (مثلاً 4 عمال) وتديهم الـ 1000 مهمة يخلصوها بالدور.
# ==============================================================================

# دالة العملية (لازم تكون global عشان الـ multiprocessing في ويندوز يشوفها)
def worker_function(task_id):
    pid = multiprocessing.current_process().pid
    print(f"   [Pool-Worker] Task {task_id} running on Process PID: {pid}")
    time.sleep(0.5)
    return task_id * 2


def run_pool_demo():
    print("\n--- 3. Process Pool Demo ---")
    # عدد العمال = عدد الأنوية في جهازك (أو حدده بـ processes=4)
    with multiprocessing.Pool() as pool:
        print("   Pool started. Distributing tasks...")

        # apply: بتبعت مهمة وتستنى نتيجتها (Blocking) - زي ما في السكشن
        # (في الواقع العملي بنستخدم map للسرعة، بس apply بتوضح الترتيب)
        for i in range(5):
            pool.apply(worker_function, args=(i,))

    print("   Pool closed.")


# ==============================================================================
# الجزء الرابع: Custom Process (الوراثة)
# السبب: لتنظيم الكود. بدل ما ترمي الكود كله في دالة، بتعمل Class يمثل العملية،
# وتقدر تضيف له خصائص (Attributes) ودوال مساعدة.
# ==============================================================================

class MyProcess(multiprocessing.Process):
    def __init__(self, name):
        multiprocessing.Process.__init__(self)  # لازم init للأب
        self.proc_name = name

    def run(self):
        print(f"   [Subclass-Proc] {self.proc_name} is running...")
        time.sleep(1)
        print(f"   [Subclass-Proc] {self.proc_name} finished.")


def run_subclass_demo():
    print("\n--- 4. Process Subclass Demo ---")
    procs = []
    for i in range(2):
        p = MyProcess(f"Worker_{i}")
        procs.append(p)
        p.start()  # بتنادي run() في عملية منفصلة

    for p in procs:
        p.join()


if __name__ == "__main__":
    run_event_demo()     # 1. الإشارة
    run_queue_demo()     # 2. الطابور الآمن
    run_pool_demo()      # 3. إدارة العمليات
    run_subclass_demo()  # 4. الوراثة في العمليات

# الشرح التفصيلي للأسباب (Why & How):
# 1. لماذا Event وليس While Loop؟
# المشكلة: لو المستهلك عمل while item is None: pass، المعالج هيفضل شغال 100% يلف في الفاضي.

# الحل: event.wait() بتفصل الخيط تماماً (Sleep) لحد ما الـ OS يصحيه لما الإشارة تيجي event.set(). ده بيوفر موارد الجهاز لعمليات تانية .

# 2. لماذا Queue هي "الملك" في الـ Threading؟
# المشكلة: التعامل مع الـ Lists العادية بين الـ Threads بيحتاج Lock ووجع دماغي عشان الـ Race Conditions.

# الحل: الـ Queue مصممة خصيصاً للتزامن. هي Thread-Safe (فيها Lock داخلي) وبتدير الانتظار (Blocking) لوحدها. يعني لو الطابور فاضي، الكود بيقف لوحده من غير ما تكتب if ولا wait .

# 3. لماذا Process Pool وليس Process لكل مهمة؟
# المشكلة: كل Process بتاخد مساحة من الرامات ووقت عشان تتعمل (Overhead). لو شغلت 1000 عملية، الجهاز هيهنج.

# الحل: الـ Pool بيفتح عدد قليل (مثلاً 4) ويفضل مشغلهم. لما واحد يخلص مهمة، يدخل على اللي بعدها. ده بيخلي الأداء أسرع وأخف على الذاكرة .

# 4. لماذا نستخدم apply في السكشن رغم أنها بطيئة؟
# السبب: في السكشن (صفحة 12)، تم استخدام pool.apply لتوضيح الفكرة خطوة بخطوة (Sequential execution inside Pool). هي بتشغل المهمة وتستنى تخلص قبل ما تروح للسطر اللي بعده.

# معلومة إضافية: عشان التوازي الحقيقي، بنستخدم pool.map أو pool.apply_async (هنشوفهم في Lab 5).
