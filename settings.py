from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QLabel
from PyQt5.QtGui import QPixmap, QImage
import PyQt5.QtGui
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal, QByteArray, QBuffer, QIODevice
from design.ui.settingsUI import Ui_Dialog


class SettingsDialog(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
