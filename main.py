import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

image = mpl.image.imread("pancakes.jpeg")
plt.imshow(image)

print(image.shape)

# condense first two coordinates into one dimension
x = image.reshape(-1, 3)
print(x.shape)

kmeans = KMeans(n_clusters=2,  n_init=10)
kmeans.fit(x)
