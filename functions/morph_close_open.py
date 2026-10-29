import numpy as np
import cv2


kernel = np.ones((2, 2), dtype=np.uint8)


def morph_operation(binary_frame):

    # Fill small black gaps inside
    closed_img = cv2.morphologyEx(
        binary_frame,
        cv2.MORPH_CLOSE,
        kernel
    )

    # Remove small isolated white noise
    cleaned_img = cv2.morphologyEx(
        closed_img,
        cv2.MORPH_OPEN,
        kernel
    )

    return cleaned_img
