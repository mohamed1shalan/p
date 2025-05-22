from skimage import io  # << cat image
from skimage import data  # << with camira


cat = io.imread('python\image processing\lec\lec1\image.jpg')
io.imshow(cat)
io.show()
print(cat.shape)  # width , hight
print(cat.size)  # width * hight
print(cat.min())  # hight value bix
print(cat.max())  # min >>
print(cat.mean())  # mean >>

# get value of pix
print(cat[0, 0])  # get value of pix
cat[0, 0] = [255, 255, 255]  # change value
cat[:10] = [255, 255, 255]  # change value all clu

# filter value of pixel

mask = cat > 78  # select some pixel
cat[mask] = 225
io.imshow(cat)
cat[:10, :10] = [255, 255, 255]  # change value all clu
io.imshow(cat)

io.show()
