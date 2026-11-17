import numpy as np
import cv2


kernel = np.ones((3, 3), dtype=np.uint8)


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

def dilate(binary_frame):

    original_height = binary_frame.shape[0]
    original_width = binary_frame.shape[1]

    pad_width = (kernel.shape[0] - 1) // 2
    binary_frame = np.pad(binary_frame, pad_width, mode='constant', constant_values=0)

    out = np.copy(binary_frame)

    for i in range(pad_width, binary_frame.shape[0] - pad_width):
        for j in range(pad_width, binary_frame.shape[1] - pad_width):

            window = binary_frame[i - pad_width:i + pad_width + 1,
                                  j - pad_width:j + pad_width + 1]

            if np.any(window == 1):
                out[i, j] = 1

    closed_img = out[pad_width:pad_width + original_height, pad_width:pad_width + original_width]

    return closed_img

def erode(binary_frame):

    original_height = binary_frame.shape[0]
    original_width = binary_frame.shape[1]

    pad_width = (kernel.shape[0] - 1) // 2
    binary_frame = np.pad(binary_frame, pad_width, mode='constant', constant_values=0)

    out = np.copy(binary_frame)

    for i in range(pad_width, binary_frame.shape[0] - pad_width):
        for j in range(pad_width, binary_frame.shape[1] - pad_width):

            window = binary_frame[i - pad_width:i + pad_width + 1,
                                  j - pad_width:j + pad_width + 1]

            if np.any(window == 0):
                out[i, j] = 0

    opened_img = out[pad_width:pad_width + original_height, pad_width:pad_width + original_width]

    return opened_img
