import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

image = mpl.image.imread("pancakes.jpeg")
plt.imshow(image)

print(image.shape)

# condense first two coordinates into one dimension
x = image.reshape(-1, 3)
print(x.shape)

# find 2 clusters in image
kmeans = KMeans(n_clusters=2,  n_init=10)
kmeans.fit(x)

segmented_img = kmeans.cluster_centers_[kmeans.labels_]
segmented_img = segmented_img.reshape(image.shape)
plt.imshow(segmented_img / 255)