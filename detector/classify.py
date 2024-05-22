from ultralytics import YOLO
import cv2 as cv
import numpy as np

from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb

import matplotlib.pyplot as plt


def classify(img: cv.typing.MatLike, model: YOLO, threshold: float = 100):
    threshold = int(threshold)
    image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    bw = closing(image < threshold, square(3))
    cleared = clear_border(bw)
    label_image = label(cleared)
    image_label_overlay = label2rgb(label_image, image=image, bg_label=0)
    plt.imshow(cleared, cmap='gray')
    plt.show()
    cords = []

    regions = regionprops(label_image)
    if len(regions) == 0:
        return 'No regions', bw

    for region in regions:
        if region.area >= image.shape[0] / 16 * image.shape[1] / 16:
            cords.append(region.bbox)

    letters_boxes = np.array(cords)
    letters_boxes = letters_boxes[letters_boxes[:, 1].argsort()]
    letters_boxes = letters_boxes[:6, :]
    i = 1
    numbers = []
    for box in letters_boxes:
        letter = image[box[0]:box[2], box[1]:box[3]]
        numbers.append(letter)
        i += 1

    results = model(numbers)
    predicted = []
    for result in results:
        # print(result.conf)
        predicted.append(result.names[result.probs.top1])

    return ''.join(predicted), cleared
