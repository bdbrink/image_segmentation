import matplotlib as mpl
import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans

# Read and display the original image
image = mpl.image.imread("pancakes.jpeg")
plt.imshow(image)

# Print the shape of the original image
print(image.shape)

# Reshape the image to have one dimension for clustering
x = image.reshape(-1, 3)
print(x.shape)

# Perform K-means clustering with 10 clusters
kmeans = KMeans(n_clusters=10,  n_init=10)
kmeans.fit(x)

# Retrieve the cluster centers and assign each pixel to its nearest cluster center
segmented_img = kmeans.cluster_centers_[kmeans.labels_]

# Reshape the segmented image to match the shape of the original image
segmented_img = segmented_img.reshape(image.shape)

# Display the segmented image
plt.imshow(segmented_img / 255)

# Save the original image in the BGR format
cv2.imwrite("image1.png", cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR))

# Save the segmented image in the BGR format
cv2.imwrite("image1.png", cv2.cvtColor(segmented_img.astype("uint8"), cv2.COLOR_BAYER_BG2BGR))
