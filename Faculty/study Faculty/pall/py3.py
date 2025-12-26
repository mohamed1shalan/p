import threading
import time
import random

# ==============================================================================
# الجزء الأول: مشكلة الـ Deadlock والحل بـ RLock
# السبب: الـ Lock العادي "غبي"؛ لا يعرف من يملكه. لو دالة معاها القفل نادت دالة تانية
# محتاجة نفس القفل، البرنامج هيقف (Deadlock).
# الحل: RLock (Reentrant Lock) بيسمح لنفس الـ Thread ياخد القفل كذا مرة.
# ==============================================================================

# نستخدم RLock هنا. لو غيرتها لـ Lock() عادي، البرنامج سيتجمد (Deadlock)!
my_rlock = threading.RLock()


def inner_operation():
    print("   [Inner] Trying to acquire lock...")
    my_rlock.acquire()  # المرة الثانية: RLock سيوافق لأننا نفس الـ Thread
    print("   [Inner] Acquired! Working...")
    my_rlock.release()  # تنقيص العداد
    print("   [Inner] Released lock.")


def outer_operation():
    print("   [Outer] Trying to acquire lock...")
    my_rlock.acquire()  # المرة الأولى
    print("   [Outer] Acquired! Calling inner function...")

    inner_operation()  # استدعاء دالة تطلب نفس القفل

    my_rlock.release()
    print("   [Outer] Released lock.")


def run_rlock_demo():
    print("\n--- 1. RLock Demo (Nested Calls) ---")
    t = threading.Thread(target=outer_operation)
    t.start()
    t.join()


# ==============================================================================
# الجزء الثاني: Semaphore (كإشارة مرور / Signal)
# السبب: في نمط المنتج والمستهلك، المستهلك محتاج يعرف "امتى" الداتا تجهز.
# لو استخدمنا Lock عادي، المستهلك هيقعد يلف (Busy Waiting) ويحرق CPU.
# الحل: Semaphore يبدأ بـ 0. المستهلك يعمل acquire (ينام) والمنتج يعمل release (يصحيه).
# ==============================================================================

# العداد يبدأ بـ 0، يعني "ممنوع المرور" لأي حد يعمل acquire
signal_semaphore = threading.Semaphore(0)
shared_item = None


def producer_sem():
    global shared_item
    print("   [Producer-Sem] Working hard to produce item...")
    time.sleep(1)
    shared_item = "Data_Package_1"
    print("   [Producer-Sem] Item Ready! Signaling consumer...")
    signal_semaphore.release()  # تزويد العداد 1 (إشارة خضراء)


def consumer_sem():
    print("   [Consumer-Sem] Waiting for item...")
    signal_semaphore.acquire()  # العداد 0، فالخيط هينام هنا لحد ما الإشارة تيجي
    print(f"   [Consumer-Sem] Woke up! Consumed: {shared_item}")


def run_semaphore_demo():
    print("\n--- 2. Semaphore Demo (Signaling) ---")
    t1 = threading.Thread(target=producer_sem)
    t2 = threading.Thread(target=consumer_sem)
    t2.start()  # نبدأ المستهلك الأول عشان نشوفه وهو بينتظر
    t1.start()
    t1.join()
    t2.join()


# ==============================================================================
# الجزء الثالث: Condition (غرفة الانتظار الذكية)
# السبب: أحياناً بنحتاج شروط معقدة (مثلاً: استنى لما الليستة يبقى فيها 5 عناصر).
# الـ Semaphore بسيط (عداد بس).
# الحل: الـ Condition بيخليك تعمل wait() (تنام وتسيب القفل) و notify() (تصحي النايمين).
# ==============================================================================

cond_var = threading.Condition()
shared_buffer = []


def producer_cond():
    print("   [Producer-Cond] Starting...")
    with cond_var:  # لازم نمسك القفل الأول
        print("   [Producer-Cond] Adding items to buffer...")
        time.sleep(1)
        shared_buffer.append("Item_A")
        shared_buffer.append("Item_B")

        print("   [Producer-Cond] Buffer ready. Notifying all...")
        cond_var.notify_all()  # صحي كل اللي نايمين مستنيين الشرط ده


def consumer_cond():
    with cond_var:  # لازم نمسك القفل
        # while: حماية من "الاستيقاظ الخاطئ". لازم نتأكد إن الشرط اتحقق فعلاً
        while len(shared_buffer) == 0:
            print("   [Consumer-Cond] Buffer empty. Going to sleep (wait)...")
            cond_var.wait()  # سيب القفل ونام في غرفة الانتظار

        print(f"   [Consumer-Cond] Woke up! Buffer has: {shared_buffer}")


def run_condition_demo():
    print("\n--- 3. Condition Demo (Wait/Notify) ---")
    t1 = threading.Thread(target=producer_cond)
    t2 = threading.Thread(target=consumer_cond)
    t2.start()  # المستهلك ينام الأول
    t1.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    run_rlock_demo()      # الجزء الأول: مشكلة التداخل
    run_semaphore_demo()  # الجزء الثاني: الإشارة البسيطة
    run_condition_demo()  # الجزء الثالث: التحكم المتقدم


# لماذا RLock وليس Lock؟
# المشكلة: انظر لدالة outer_operation في الكود. هي أخذت القفل، ثم نادت inner_operation التي تحاول أخذ نفس القفل.


# لو كان Lock عادي: سيظن أن هناك شخصاً غريباً يمسك القفل (رغم أنه هو نفسه!) وسيمنعه، مما يؤدي لتعليق البرنامج للأبد (Deadlock) .

# الحل: RLock يسجل "اسم المالك" و "عدد مرات الدخول". طالما أنت المالك، يسمح لك بالدخول، فقط يزود العداد. ولن يفتح الباب لغيرك إلا عندما تعمل release بنفس عدد مرات الـ acquire .

# 2. لماذا Semaphore أفضل من متغير عادي للإشارة؟
# المشكلة: لو استخدمت متغير flag = True، المستهلك سيحتاج لعمل حلقة while flag is False: pass. هذا يسمى Busy Waiting ويستهلك المعالج بنسبة 100% بلا فائدة.


# الحل: semaphore.acquire() تجعل نظام التشغيل يضع الـ Thread في حالة "نوم" (Sleep)، فلا يستهلك أي موارد حتى يوقظه المنتج بـ release() .

# 3. لماذا Condition هو الأقوى؟
# الميزة: يدمج بين القفل (لحماية البيانات) والانتظار (للتوفير).

# في الكود: لاحظ cond_var.wait(). هذا الأمر سحري؛ فهو يقوم بخطوتين:

# يحرر القفل (ليسمح للمنتج بالدخول وتعديل البيانات).

# ينام فوراً.

# عندما يصحو (بعد notify)، يقوم أوتوماتيكياً باستعادة القفل قبل إكمال الكود. هذا يضمن أمان تام للبيانات وكفاءة عالية .
