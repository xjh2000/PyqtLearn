import typing

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QWidget

from view.MainWindow import Ui_MainWindow


class MainControl(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainControl, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print('收益_min:')
