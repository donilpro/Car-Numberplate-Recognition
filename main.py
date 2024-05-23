from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
import PyQt5.QtGui
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal, QByteArray, QBuffer, QIODevice, Qt
from design.ui.application import Ui_MainWindow
import sys
from detector.loader import ImageLoader
from settings import SettingsDialog


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.debugBtnTextNormal = 'Origin'
        self.debugBtnTextDefault = self.debugBtn.text()
        self.isDebug = False

        self.imageContainer = None
        self.thresh = None

        self.actionOpen.triggered.connect(self.open_image)
        self.actionSettings.triggered.connect(self.open_settings)
        self.debugBtn.clicked.connect(self.display_bw)
        self.detectBtn.clicked.connect(self.update_image_data)

        self.dialog = SettingsDialog()
        self.thresh = self.dialog.get_thresh()
        # self.dialog.setAttribute(Qt.WA_DeleteOnClose)

        self.update_model_info(cls_model=self.dialog.get_short_cls_model(), det_model=self.dialog.get_short_det_model())

    def display_bw(self):
        if self.imageContainer is not None:
            if not self.isDebug:
                self.plateView.setPixmap(self.imageContainer.get_bw_image())
                self.mainView.setPixmap(self.imageContainer.get_bbox_image())
                self.isDebug = True
                self.debugBtn.setText(self.debugBtnTextNormal)
            else:
                self.display_main_image()
                self.display_cropped_image()
                self.isDebug = False
                self.debugBtn.setText(self.debugBtnTextDefault)

    def open_settings(self):
        self.dialog.exec_()
        self.thresh = self.dialog.get_thresh()

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'JPEG File (*.jpg);;PNG File (*.png)')
        print(file_path)
        if not file_path:
            return
        if self.thresh is not None:
            self.imageContainer = ImageLoader(file_path, cls_model=self.dialog.get_cls_model(),
                                              det_model=self.dialog.get_det_model(), thresh=self.thresh)
        else:
            self.imageContainer = ImageLoader(file_path, cls_model=self.dialog.get_cls_model(),
                                              det_model=self.dialog.get_det_model())
        if self.thresh is not None:
            self.imageContainer.set_threshold(self.thresh)
        self.update_image_data()

    def update_image_data(self):
        if self.imageContainer:
            self.display_main_image()
            self.display_cropped_image()
            self.display_number_label()

            det_conf = str(round(float(self.imageContainer.get_det_conf()) * 100, 2)) + ' %'
            cls_conf = ''

            for sym, conf in self.imageContainer.get_cls_conf():
                cls_conf += f'\n{sym} - {conf}%'

            time = str(round(self.imageContainer.get_time())) + ' ms'
            self.update_model_info(cls_acc=cls_conf, det_acc=det_conf, elapsed_time=time)
        else:
            QMessageBox.warning(self, "Error", "Image's not set")

    def display_main_image(self):
        self.mainView.setPixmap(self.imageContainer.get_image())

    def display_cropped_image(self):
        self.plateView.setPixmap(self.imageContainer.get_cropped_image())

    def display_number_label(self):
        self.plateDecodedLabel.setText(self.imageContainer.get_symbols())

    def update_model_info(self, cls_model=None, det_model=None, elapsed_time=None, cls_acc=None, det_acc=None):
        if cls_model is not None:
            self.labelClsModel.setText('Classification model: ' + cls_model)
        if det_model is not None:
            self.labelDetModel.setText('Detector model: ' + det_model)
        if elapsed_time is not None:
            self.labelTime.setText('Elapsed time: ' + str(elapsed_time))
        if cls_acc is not None:
            self.labelClsAcc.setText('Classification accuracy: ' + str(cls_acc))
        if det_acc is not None:
            self.labelDetAcc.setText('Detector accuracy: ' + str(det_acc))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
