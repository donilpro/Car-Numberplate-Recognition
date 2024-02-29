import sys

from design.main_design import Ui_MainWindow

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QImage

from ultralytics import YOLO
import cv2 as cv


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.image = None
        self.tableDict = {}
        self.model = YOLO('yolov8n.pt')
        self.path = ''

        self.openFileBtn.clicked.connect(self.open_image)
        self.tableWidget.cellChanged.connect(self.cell_changed)
        self.detectBtn.clicked.connect(self.detect_objects)

    def cell_changed(self, row, column):
        print('cell changed')
        print(column, row)

    def open_image(self) -> None:
        """
        Метод открывает диалоговое окно с выбором файла и записывает изображение в атрибут класса
        :return:
        """
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'JPEG File (*.jpg);;PNG File (*.png)')
        self.path = file_path
        if not file_path:
            return
        self.image = cv.imread(file_path)
        self.set_image(self.image)

    def set_image(self, image) -> None:
        """
        Метод отображает изображение во фрейме
        :param view:
        :param image:
        :return:
        """
        frame = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.imageLabel.setPixmap(QPixmap.fromImage(image))

    def read_table(self):
        self.tableDict.clear()
        for row in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row, 0) is not None:
                key = self.tableWidget.item(row, 0).text()
                if self.tableDict.get(key) is None:
                    if self.tableWidget.item(row, 1) is not None:
                        value = self.tableWidget.item(row, 1).text()
                        try:
                            self.tableDict[key] = float(value)
                        except ValueError:
                            self.tableDict[key] = 0
                            self.tableWidget.setItem(row, 1, QTableWidgetItem())
                    else:
                        self.tableDict[key] = 0
                else:
                    self.tableWidget.setItem(row, 0, QTableWidgetItem())
                    self.tableWidget.setItem(row, 1, QTableWidgetItem())
            elif self.tableWidget.item(row, 1) is not None:
                self.tableWidget.setItem(row, 1, QTableWidgetItem())
        print(self.tableDict)

    def detect_objects(self) -> None:
        self.read_table()
        reversed_classes = dict(zip(self.model.names.values(), self.model.names.keys()))
        classes_list = []
        for key in self.tableDict.keys():
            try:
                classes_list.append(reversed_classes[key])
            except KeyError:
                continue

        results = self.model(self.path, classes=classes_list)

        for result in results:
            print(result.boxes.conf)
            print(result.boxes.cls)
            self.set_image(result.plot())

            for box in result.boxes:
                cls_id = int(box.cls)
                cls_conf = float(box.conf)
                cls_name = self.model.names[cls_id]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    win = Window()
    win.show()
    sys.exit(app.exec())
