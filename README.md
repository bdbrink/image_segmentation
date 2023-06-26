# Image Segmentation with K-means Clustering

This script performs image segmentation using K-means clustering. It uses the `matplotlib` and `cv2` libraries for image processing and visualization, and the `KMeans` class from `sklearn.cluster` for clustering.

## Prerequisites

Before running the script, ensure that you have the following:

- Python 3.x installed
- Required packages: `matplotlib`, `cv2`, `scikit-learn`

## Usage

1. Clone the repository or download the script `image_segmentation.py`.

2. Place the image file you want to segment in the same directory as the script.

3. Open the script in a Python IDE or text editor.

4. Modify the script if needed (e.g., change the filename or number of clusters).

5. Run the script.

## Script Explanation

1. Import the required libraries:

    ```python
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import cv2
    from sklearn.cluster import KMeans
    ```

2. Read and store the image:

    ```python
    image = mpl.image.imread("pancakes.jpeg")
    ```

3. Display the original image:

    ```python
    plt.imshow(image)
    ```

4. Print the shape of the original image:

    ```python
    print(image.shape)
    ```

5. Reshape the image to have one dimension for clustering:

    ```python
    x = image.reshape(-1, 3)
    ```

6. Print the shape of the reshaped image:

    ```python
    print(x.shape)
    ```

7. Perform K-means clustering with a specified number of clusters:

    ```python
    kmeans = KMeans(n_clusters=10,  n_init=10)
    kmeans.fit(x)
    ```

8. Retrieve the cluster centers and assign each pixel to its nearest cluster center:

    ```python
    segmented_img = kmeans.cluster_centers_[kmeans.labels_]
    ```

9. Reshape the segmented image to match the shape of the original image:

    ```python
    segmented_img = segmented_img.reshape(image.shape)
    ```

10. Display the segmented image:

    ```python
    plt.imshow(segmented_img / 255)
    ```

11. Save the original image in the BGR format:

    ```python
    cv2.imwrite("image1.png", cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR))
    ```

12. Save the segmented image in the BGR format:

    ```python
    cv2.imwrite("image1.png", cv2.cvtColor(segmented_img.astype("uint8"), cv2.COLOR_BAYER_BG2BGR))
    ```

## Customization

You can customize the script according to your needs:

- Change the input image file name:

    ```python
    image = mpl.image.imread("your_image.jpg")
    ```

- Adjust the number of clusters for K-means clustering:

    ```python
    kmeans = KMeans(n_clusters=K, n_init=10)
    ```

- Modify the output image file name:

    ```python
    cv2.imwrite("output_image.png", cv2.cvtColor(segmented_img.astype("uint8"), cv2.COLOR_BAYER_BG2BGR))
    ```

