from ultralytics import YOLO
import cv2 as cv


def detect(img: cv.typing.MatLike, model: YOLO):
    im = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = model(im)
    time = 0
    for task_speed in results[0].speed.values():
        time += task_speed

    for result in results:
        cords = result.boxes.xyxy
        cords = cords[0].int()
        image = im[cords[1]:cords[3], cords[0]:cords[2], :]
        return image, cords, result.boxes.conf, time
