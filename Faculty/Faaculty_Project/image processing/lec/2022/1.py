import cv2
import numpy as np
import matplotlib.pyplot as plt

# ============== Q1: تحويلات الصورة الأساسية ==============


def apply_image_negative(image):
    """السكشن 1: تحويل الصورة إلى سالبها"""
    return 255 - image


def apply_log_transform(image):
    """السكشن 6: التحويل اللوغاريتمي"""
    c = 255 / np.log(1 + np.max(image))
    log_transformed = c * np.log(1 + image)
    return np.array(log_transformed, dtype=np.uint8)


def apply_gamma_transform(image, c=1, gamma=0.9):
    """السكشن 6: تحويل قانون القوة (جاما)"""
    gamma_corrected = c * np.power(image/255.0, gamma)
    return np.uint8(gamma_corrected * 255)


def apply_histogram_equalization(image):
    """السكشن 1: معادلة الهيستوجرام"""
    return cv2.equalizeHist(image)

# ============== Q2: تحويل فورييه ==============


def apply_fourier_transform(image):
    """السكشن 6: تحويل فورييه"""
    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * np.log(np.abs(dft_shift))
    return magnitude_spectrum

# ============== التنفيذ الرئيسي ==============


def main():
    # تحميل الصورة الأصلية (افترض أن img_1 موجودة بالفعل)
    img_1 = cv2.imread('cai.jpg', cv2.IMREAD_GRAYSCALE)

    if img_1 is None:
        print("خطأ: لم يتم العثور على الصورة 'cai.jpg'")
        return

    # Q1.1: تحويل الصورة إلى سالبها
    negative_img = apply_image_negative(img_1)

    # Q1.2: عرض الصورة السالبة
    cv2.imshow('Figure 5: Image Negative', negative_img)
    cv2.waitKey(0)

    # Q1.3: التحويل اللوغاريتمي
    log_img = apply_log_transform(img_1)

    # Q1.4: عرض التحويل اللوغاريتمي
    cv2.imshow('Figure 6: Log Transform', log_img)
    cv2.waitKey(0)

    # Q1.5: تحويل جاما (c=1, gamma=0.9)
    gamma_img = apply_gamma_transform(img_1, c=1, gamma=0.9)

    # Q1.6: عرض تحويل جاما
    cv2.imshow('Figure 7: Gamma Transform (c=1, γ=0.9)', gamma_img)
    cv2.waitKey(0)

    # Q1.7: معادلة الهيستوجرام
    equalized_img = apply_histogram_equalization(img_1)

    # Q1.8: عرض الصورة المعادلة
    cv2.imshow('Figure 8: Histogram Equalization', equalized_img)
    cv2.waitKey(0)

    # Q2: تحويل فورييه
    fourier_img = apply_fourier_transform(img_1)

    # عرض تحويل فورييه
    plt.imshow(fourier_img, cmap='gray')
    plt.title('Figure 4: Fourier Transform')
    plt.xticks([]), plt.yticks([])
    plt.show()

    # إغلاق جميع النوافذ
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
