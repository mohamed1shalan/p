import cv2
import numpy as np
import matplotlib.pyplot as plt

# ============== Q1: نماذج الضوضاء في الصور ==============


def add_gaussian_noise(image, mean=0, sigma=25):
    """إضافة ضوضاء غوسية للصورة"""
    row, col = image.shape
    gauss = np.random.normal(mean, sigma, (row, col))
    noisy = image + gauss
    return np.clip(noisy, 0, 255).astype(np.uint8)


def add_salt_pepper_noise(image, prob=0.05):
    """إضافة ضوضاء الملح والفلفل للصورة"""
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = np.random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def add_exponential_noise(image, scale=10.0):
    """إضافة ضوضاء أسية للصورة"""
    row, col = image.shape
    noise = np.random.exponential(scale, (row, col))
    noisy = image + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

# ============== Q2: معالجة الصورة الملونة ==============


# 1. قراءة الصورة الأصلية
img = cv2.imread('python/image processing/lec/lec1/image.jpg')

# 2. عرض الصورة الأصلية
cv2.imshow('original Cai image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. التحويل إلى التدرج الرمادي
img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4. عرض الصورة الرمادية
cv2.imshow('Grey Cai image', img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. تطبيق التحويل اللوغاريتمي
c = 255 / np.log(1 + np.max(img_1))
log_transformed = c * np.log(1 + img_1)
log_transformed = np.array(log_transformed, dtype=np.uint8)

# 6. عرض الصورة بعد التحويل اللوغاريتمي
cv2.imshow('Image Cai after applying Log Train', log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. تدوير الصورة بمقدار 60 درجة
rows, cols = img_1.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 60, 1)
rotated = cv2.warpAffine(img_1, M, (cols, rows))

# 8. تغيير حجم الصورة
resized = cv2.resize(img_1, (780, 540))

# 9. فصل ودمج القنوات اللونية
b, g, r = cv2.split(img)
merged = cv2.merge((b, g, r))

# 10. تطبيق تحويل فورييه
dft = np.fft.fft2(img_1)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(np.abs(dft_shift))

# 11. عرض نتيجة تحويل فورييه
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Figure 7'), plt.xticks([]), plt.yticks([])
plt.show()

# ============== عرض نماذج الضوضاء كمثال إضافي ==============

# إنشاء صورة رمادية مثالبة
sample_image = np.zeros((300, 300), dtype=np.uint8)
sample_image[100:200, 100:200] = 128

# تطبيق نماذج الضوضاء
gaussian_noisy = add_gaussian_noise(sample_image, sigma=30)
salt_pepper_noisy = add_salt_pepper_noise(sample_image, prob=0.1)
exponential_noisy = add_exponential_noise(sample_image, scale=15.0)

# عرض النتائج
cv2.imshow('Gaussian Noise', gaussian_noisy)
cv2.imshow('Salt and Pepper Noise', salt_pepper_noisy)
cv2.imshow('Exponential Noise', exponential_noisy)
cv2.waitKey(0)
cv2.destroyAllWindows()
