import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

image = mpl.image.imread("pancakes.jpeg")
plt.imshow(image)

print(image.shape)