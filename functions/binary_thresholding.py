import numpy as np

def binary_threshold(gray_frame):

    binary_img = np.zeros(gray_frame.shape, dtype=np.uint8)


    binary_img = (gray_frame > 200).astype(np.uint8) * 255
    
    # for i in range(gray_frame.shape[0]):
    #     for j in range(gray_frame.shape[1]):

    #         if gray_frame[i,j] > 200:

    #             binary_img[i,j] = 255
    #         else:
    #             binary_img[i,j] = 0

    return binary_img