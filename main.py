import matplotlib as mpl
import matplotlib.pyplot as plt
import cv2

from sklearn.cluster import KMeans

image = mpl.image.imread("pancakes.jpeg")
plt.imshow(image)

print(image.shape)

# condense first two coordinates into one dimension
x = image.reshape(-1, 3)
print(x.shape)

# More clusters, more detail
# Performance is downgraded though
kmeans = KMeans(n_clusters=10,  n_init=10)
kmeans.fit(x)

segmented_img = kmeans.cluster_centers_[kmeans.labels_]
segmented_img = segmented_img.reshape(image.shape)
plt.imshow(segmented_img / 255)

cv2.imwrite("image1.png", cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR))
cv2.imwrite("image1.png", cv2.cvtColor(segmented_img.astype("uint8"), cv2.COLOR_BAYER_BG2BGR))