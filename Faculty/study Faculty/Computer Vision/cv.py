from matplotlib import pyplot as plt
import numpy as np
import cv2
from scipy.ndimage import rotate

OR_img = cv2.imread(
    'C:\\VS code Clone\\p\\study Faculty\\image.jpg')
print(OR_img.shape)
img = cv2.resize(OR_img, (600, 400))
image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
image_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite('C:\\VS code Clone\\p\\study Faculty\\image_gray.jpg', image_gray)
cv2.imwrite('C:\\VS code Clone\\p\\study Faculty\\image_HSV.jpg', image_HSV)
# cropping
cropped_image = img[50:250, 100:400]


cv2.imshow('Image', image_gray)
cv2.imshow('HSV', image_HSV)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey()
cv2.destroyAllWindows()

print(img.shape)

# rotation

roated_image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
roated_image1 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
roated_image2 = cv2.rotate(img, cv2.ROTATE_180)
roated_image3 = rotate(img, 45)
cv2.imshow('Rotated Image', roated_image)
cv2.imshow('Rotated Image1', roated_image1)
cv2.imshow('Rotated Image2', roated_image2)
cv2.imshow('Rotated Image3', roated_image3)
cv2.waitKey()
cv2.destroyAllWindows()

# flipping

flipped_image_hor = cv2.flip(img, 1)  # horizontal flip
flipped_image_var = cv2.flip(img, 0)  # vertical flip
cv2.imshow('Flipped Image hor', flipped_image_hor)
cv2.imshow('Flipped Image var', flipped_image_var)
cv2.waitKey()
cv2.destroyAllWindows()

# pixel manipulation

pixel = img[100, 100]
print('Original Pixel Value at (100, 100):', pixel)

cv2.imshow('Modified Image', img)
img[100:200, 100:200] = [255, 255, 0]  # Changing pixel to green
cv2.imshow('Modified Image', img)
cv2.waitKey()
cv2.destroyAllWindows()


# detection of face using haarcascade

# 1️⃣ Image Acquisition
# Read the image (make sure the image file is in the same folder as this code)
img = cv2.imread("C:\\VS code Clone\\p\\study Faculty\\download.jpg")
cv2.imshow("Original Image", img)

# 2️⃣ Preprocessing
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Preprocessed Image", blur)

# 3️⃣ Feature Extraction
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(blur, scaleFactor=1.1, minNeighbors=100)

# 4️⃣ Classification / Recognition
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 5️⃣ Output / Visualization
cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# video capture using haarcascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Video Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Draw

new_img_line = cv2.line(img.copy(), (0, 0), (300, 300), (255, 0, 0), 5)
new_img_line = cv2.arrowedLine(img.copy(), (0, 0), (300, 300), (255, 0, 0), 5)
new_img_rectangle = cv2.rectangle(
    img.copy(), (50, 50), (200, 200), (0, 255, 0), 3)
new_img_circle = cv2.circle(img.copy(), (300, 200), 50, (0, 0, 255), -1)

cv2.imshow('Line', new_img_line)
cv2.imshow('Rectangle', new_img_rectangle)
cv2.imshow('Circle', new_img_circle)
cv2.waitKey()
cv2.destroyAllWindows()


# Drow a polyline
# Polyline pointes

shape_info = np.array([(50, 50), (200, 50), (200, 200), (50, 200)])
drow_poly = cv2.polylines(img, [shape_info],
                          True, color=(255, 0, 255), thickness=3)
cv2.fillPoly(img, [shape_info], color=(0, 255, 255))

drow_circle = cv2.circle(img, (300, 200), 50, color=(255, 0, 255), thickness=3)

cv2.imshow('Polyline', drow_poly)
cv2.imshow('Circle', drow_circle)
cv2.waitKey()
cv2.destroyAllWindows()

ww = cv2.FONT_HERSHEY_COMPLEX
image_with_text = cv2.putText(
    img.copy(), "my name", (50, 50), 4, 1, (0, 255, 0), 2)
cv2.imshow('Circle', image_with_text)
cv2.waitKey()
cv2.destroyAllWindows()

# move imge

rows, colc, dim = img.shape
move = np.float32([
    [1, 0, 50],
    [0, 1, 100],
    [0, 0, 1]
])

imge_translated = cv2.warpPerspective(img, move, (colc, rows))

cv2.imshow('Translated Image', imge_translated)


rotat1e = cv2.getRotationMatrix2D((colc/2, rows/2), 15, 1)
to_retated_image = cv2.warpAffine(img, rotat1e, (colc, rows))

cv2.imshow('Rotated Image', to_retated_image)
cv2.waitKey()
cv2.destroyAllWindows()


img = cv2.imread("C:\\VS code Clone\\p\\study Faculty\\image.jpg")
img = cv2.resize(img, (600, 400))

# ----------------------------------------------------------

# section 3

# Edge Detection
laplacian = cv2.Laplacian(img, cv2.CV_64F)
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.subplot(122)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian Image')
plt.show()

# sobel edge detection
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobel = cv2.add(sobelx, sobely)
plt.subplot(121)
plt.imshow(img, cmap='gray')  # org
plt.title('org')
plt.subplot(122)
plt.imshow(sobel, cmap='gray')  # NEW
plt.title('edged')
plt.show()

# canny edge detection
canny = cv2.Canny(img, 100, 200)
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('org')
plt.subplot(122)
plt.imshow(canny, cmap='gray')
plt.title('edged')
plt.show()


# image Blurring

# average blurring
blur = cv2.blur(img, (15, 15))
plt.subplot(121)
plt.imshow(img)
plt.title('org')
plt.subplot(122)
plt.imshow(blur)
plt.title('blurred')
plt.show()

# gaussian blurring
gauss = cv2.GaussianBlur(img, (5, 5), 0)
plt.subplot(121)
plt.imshow(img)
plt.title('org')
plt.subplot(122)
plt.imshow(gauss)
plt.title('blurred')
plt.show()

# median blurring
blur = cv2.medianBlur(img, 15)
plt.subplot(121)
plt.imshow(img)
plt.title('org')
plt.subplot(122)
plt.imshow(blur)
plt.title('blurred')
plt.show()

# ----------------------------------------------------------

# Section 4
# Harris corner detection

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("org", img)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)  # الناتج هنا نقطه صغيره
dst = cv2.dilate(dst, None)  # بيكبر النقطه الصغيرهه

img[dst > 0.01*dst.max()] = [255, 0, 0]

cv2.imshow("harris", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Fast Feature Detector
fast = cv2.FastFeatureDetector_create()
kp = fast.detect(img, None)
img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0))


cv2.imshow("1", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ----------------------------------------------------------
# Section 5  المقارنه (نقط مميزه) feature sift
# sift create

print("--- تشغيل SIFT ---")
# 1. قراءة الصورة
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. إنشاء كائن SIFT
sift = cv2.SIFT_create()

# 3. اكتشاف النقاط (Keypoints) وحساب البصمات (Descriptors)
keypoints, descriptors = sift.detectAndCompute(gray, None)

print(f"عدد النقاط المكتشفة بواسطة SIFT: {len(keypoints)}")

# 4. رسم النقاط على الصورة
# flags=4 (cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) ترسم دوائر بحجم المفتاح واتجاهه
image_with_keypoints = cv2.drawKeypoints(img, keypoints, None, flags=4)

# العرض باستخدام Matplotlib
plt.imshow(cv2.cvtColor(image_with_keypoints, cv2.COLOR_BGR2RGB))
plt.title('SIFT Keypoints')
plt.show()


# Fast
# 2. Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
fast = cv2.FastFeatureDetector_create()
keypoints = fast.detect(gray, None)
image_with_keypoints = cv2.drawKeypoints(img, keypoints, None, flags=4)

plt.imshow(cv2.cvtColor(image_with_keypoints, cv2.COLOR_BGR2RGB))
plt.title('FAST Keypoints')
plt.show()

# ----------------------------------------------------------
# Section 6

# بنقرأ الصورتين أبيض وأسود (Grayscale) لأن الألوان مش هتفيدنا في مطابقة الأشكال
img1 = cv2.imread('box.png', 0)   # الصورة اللي بندور عليها (Query)
img2 = cv2.imread('scene.png', 0)  # الصورة اللي بندور جواها (Train)

# بنشغل SIFT
sift = cv2.SIFT_create()

# بنقوله طلع النقط (kp) والبصمات (des) من الصورتين
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# بنجيب الـ BFMatcher
bf = cv2.BFMatcher()

# بنقوله قارن البصمات ببعض وهات لي أقرب "نقطتين" لكل نقطة (k=2)
matches = bf.knnMatch(des1, des2, k=2)

good_matches = []
for m, n in matches:
    # m: أقرب تطابق
    # n: تاني أقرب تطابق

    # لو المسافة بتاعت m أقل بكتير من n (أقل من 75%)
    if m.distance < 0.75 * n.distance:
        good_matches.append([m])

# بنرسم الخطوط بين النقط المتطابقة
img_final = cv2.drawMatchesKnn(
    img1, kp1, img2, kp2, good_matches, None, flags=2)
plt.imshow(img_final)
plt.show()
