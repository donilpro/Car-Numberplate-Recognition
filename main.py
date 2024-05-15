from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QLabel
from PyQt5.QtGui import QPixmap, QImage
import PyQt5.QtGui
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal, QByteArray, QBuffer, QIODevice
from design.ui.application import Ui_MainWindow
import sys
from detector.loader import ImageLoader


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.imageContainer = None

        self.actionOpen.triggered.connect(self.open_image)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'JPEG File (*.jpg);;PNG File (*.png)')
        print(file_path)
        if not file_path:
            return
        self.imageContainer = ImageLoader(file_path)
        self.update_image_data()

    def update_image_data(self):
        self.display_main_image()
        self.display_cropped_image()
        self.display_number_label()

    def display_main_image(self):
        self.mainView.setPixmap(self.imageContainer.get_image())

    def display_cropped_image(self):
        self.plateView.setPixmap(self.imageContainer.get_cropped_image())

    def display_number_label(self):
        self.plateDecodedLabel.setText(self.imageContainer.get_symbols())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
