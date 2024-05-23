from ultralytics import YOLO
import cv2 as cv
import numpy as np

from skimage.util import img_as_ubyte, img_as_bool, img_as_float
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb

import matplotlib.pyplot as plt


def classify(img: cv.typing.MatLike, model: YOLO, threshold: float = 100):
    threshold = int(threshold)

    image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # image = cv.medianBlur(image, 2)
    bw = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
                               cv.THRESH_BINARY, 11, 2)
    bw = cv.bitwise_not(bw)
    # bw = closing(image < threshold, square(3))
    cleared = clear_border(bw)
    label_image = label(cleared)
    image_label_overlay = label2rgb(label_image, image=image, bg_label=0)
    cords = []

    regions = regionprops(label_image)
    if len(regions) == 0:
        return 'No regions', [], cleared, image

    for region in regions:
        image_area = image.shape[0] * image.shape[1]
        letter_width = region.bbox[3] - region.bbox[1] < image.shape[1] / 5
        if region.area >= image_area / 256 and image_area / 20 and letter_width:
            image = cv.rectangle(image, (region.bbox[1], region.bbox[0]), (region.bbox[3], region.bbox[2]), color=(0,255,0), thickness=1)
            cords.append(region.bbox)

    plt.imshow(image, cmap='gray')

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
    conf = []
    for result in results:
        conf.append(round(float(result.probs.top1conf), 2))
        predicted.append(result.names[result.probs.top1])

    plt.show()

    return ''.join(predicted), conf, cleared, image
