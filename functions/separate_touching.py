# Work in progress: separate parts that touch each other so each one is counted.
# Connected component counting sees touching parts as a single blob.
#
# Idea to explore:
#   1. Distance transform: distance from each white pixel to the nearest black pixel
#   2. Threshold the distance map so each part keeps only its center (one marker per part)
#   3. Watershed: grow the markers back out until they meet, which splits the blob


def separate_touching_parts(cleaned_img):
    raise NotImplementedError("Separating touching parts is not implemented yet")
