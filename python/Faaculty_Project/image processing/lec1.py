import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"D:\ddr\My Drive\p\python\image processing\image.jpg")

plt.imshow(img)
plt.show()
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
