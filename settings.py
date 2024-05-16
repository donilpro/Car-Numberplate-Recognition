from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QLabel
from PyQt5.QtGui import QPixmap, QImage
import PyQt5.QtGui
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal, QByteArray, QBuffer, QIODevice
from design.ui.settingsUI import Ui_Dialog
import configparser


class SettingsDialog(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        config = configparser.ConfigParser()
        config.read('settings.ini')
        self._set_cls_model(config['PATHS']['ClsModel'])
        self._set_det_model(config['PATHS']['DetModel'])

    def get_cls_model(self):
        return self._clsModel

    def get_det_model(self):
        return self._detModel

    def _set_cls_model(self, model):
        self._clsModel = model
        self.labelClsModel.setText(model)

    def _set_det_model(self, model):
        self._detModel = model
        self.labelDetModel.setText(model)
