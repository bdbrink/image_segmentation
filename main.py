import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

image = mpl.image.imread("pancakes.jpeg")
plt.imshow(image)

print(image.shape)

x = image.reshape(-1, 3)
print(x.shape)