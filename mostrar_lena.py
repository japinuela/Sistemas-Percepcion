from PIL import Image
import matplotlib.pyplot as plt


img_color = Image.open("./lena_color.tiff")
plt.imshow(img_color)
plt.axis('off')
plt.show()

