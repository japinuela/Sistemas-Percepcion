from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

img_color = Image.open("./lena_color.tiff")
""" plt.imshow(img_color)
plt.axis('off')
plt.show()
 """
#Convertur la imagen a n-d array
a = np.array(img_color)
print(type(a))
print("shape: ", a.shape)
print("dtype: ", a.dtype) #uint8 . Cada canal tiene un valor de pixel 0 a 255


#Acceder a un pixel concreto
y = 13
x = 70
print("Valor pixel: ", a[y,x])

#Extraer canales
R = a[:,:,0]
G = a[:,:,1]
B = a[...,2]

""" fig, ax = plt.subplots(1,4,figsize=(10,3))
ax[0].imshow(a)
ax[1].imshow(R, cmap="gray"); ax[1].set_title("R")
ax[2].imshow(G, cmap="gray"); ax[2].set_title("G")
ax[3].imshow(B, cmap="gray"); ax[3].set_title("B")
for x in ax:
    x.axis('off')
plt.show()
 """

counts, bins = np.histogram(R, bins=256, range=(0,255))
plt.figure()
plt.plot(counts)
plt.title("Histograma Numpy")
plt.xlim([0,255])
plt.xlabel("Intesidad")
plt.ylabel("Frecuencia")
plt.show()

#Seaborn
plt.figure(figsize=(6,4))
for ch, col, name in [(R,"r","Red"), (G,"g","Green"), (B,"b","Blue")]:
    sns.histplot(ch.ravel(), bins=256, binrange=(0,255), stat="density", element="step", fill=True, alpha=0.3, color=col, label=name)
plt.legend()
plt.show()

