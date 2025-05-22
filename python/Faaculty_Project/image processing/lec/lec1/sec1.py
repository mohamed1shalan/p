import cv2
my_image = cv2.imread('python\image processing\lec\lec1\image.jpg')
new_image = my_image.copy()
cv2.imshow('Image', my_image)
cv2.waitKey(500)

to_gray = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image', to_gray)
cv2.waitKey(500)

to_change_size = cv2.resize(my_image, (200, 200))
cv2.imshow('Image', to_change_size)
cv2.waitKey(500)

rotated_90 = cv2.rotate(my_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('Image', rotated_90)
cv2.waitKey(500)

rotated_180 = cv2.rotate(my_image, cv2.ROTATE_180)
cv2.imshow('Image', rotated_180)
cv2.waitKey(500)

rotated_90_clockwise = cv2.rotate(my_image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Image', rotated_90_clockwise)
cv2.waitKey(500)

# الرسم على الصورة
# رسم مستطيل حول الوجه (مثال)
rectange1 = cv2.rectangle(my_image, (500, 500), (700, 700),
                          (0, 0, 255), 2)  # (B, G, R), thickness
cv2.imshow('Image', rectange1)
cv2.waitKey(500)

text_ = cv2.putText(new_image, "Your Name", (500, 500),
                    # (B, G, R)  # (B, G, R)
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
cv2.imshow('Image', text_)
cv2.waitKey(500)
cv2.destroyAllWindows()

# processing in image
gaussian = cv2.GaussianBlur(new_image, (5, 5), 0)
median = cv2.medianBlur(new_image, 5)
bilateral = cv2.bilateralFilter(new_image, 9, 75, 75)

# عرض النتائج
cv2.imshow('Original', new_image)
cv2.imshow('Gaussian Blur', gaussian)
cv2.imshow('Median Blur', median)
cv2.imshow('Bilateral Filter', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
