import numpy as np

weights = [.114,.587,.299]

def gray_scale_frame(frame):

    grayscale_frame = np.dot(frame, weights).astype(np.uint8)

    return grayscale_frame