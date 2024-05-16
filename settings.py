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
        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')
        self._set_cls_model(self.config['PATHS']['ClsModel'])
        self._set_det_model(self.config['PATHS']['DetModel'])
        self._set_thresh(self.config['PARAMS']['Thresh'])

        self.selectClsModel.clicked.connect(self._cls_model_selector)
        self.selectDetModel.clicked.connect(self._det_model_selector)

    def _cls_model_selector(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Weight File (*.pt)')
        if not file_path:
            return
        self._set_cls_model(file_path)
        self._save_ini(cls_model=file_path)

    def _det_model_selector(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Weight File (*.pt)')
        if not file_path:
            return
        self._set_det_model(file_path)
        self._save_ini(det_model=file_path)

    def get_cls_model(self):
        return self._clsModel

    def get_det_model(self):
        return self._detModel

    def get_short_cls_model(self):
        return self._clsModel.replace('\\', '/').split('/')[-1]

    def get_short_det_model(self):
        return self._detModel.replace('\\', '/').split('/')[-1]

    def _set_cls_model(self, model):
        self._clsModel = model
        self.labelClsModel.setText(model)

    def _set_det_model(self, model):
        self._detModel = model
        self.labelDetModel.setText(model)

    def _set_thresh(self, thresh):
        self._thresh = thresh

    def _save_ini(self, cls_model=None, det_model=None, thresh=None):
        if cls_model is not None:
            # self.config['PATHS']['ClsModel'] = cls_model
            self.config.set('PATHS', 'ClsModel', cls_model)
        if det_model is not None:
            # self.config['PATHS']['DetModel'] = det_model
            self.config.set('PATHS', 'DetModel', det_model)
        if thresh is not None:
            # self.config['PARAMS']['Thresh'] = thresh
            self.config.set('PARAMS', 'Thresh', thresh)
        with open('settings.ini', 'w') as configfile:
            self.config.write(configfile)
