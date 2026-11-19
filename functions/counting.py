import cv2


def count_objects(cleaned_img, min_area=300):
    # TODO: I want to implement connected component labeling (8-connectivity)
    # by myself instead of using cv2.connectedComponentsWithStats.
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        cleaned_img,
        connectivity=8
    )

    count = 0

    for i in range(1, num_labels):  # Skip background
        area = stats[i, cv2.CC_STAT_AREA]

        if area >= min_area:  # Adjust min_area for your image resolution
            count += 1

    return count
