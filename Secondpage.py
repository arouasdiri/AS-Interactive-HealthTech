import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QStackedWidget, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal, Qt


class SurgicalDataForm(QMainWindow):
    show_next_signal = pyqtSignal()
    show_prev_signal = pyqtSignal()

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.camera_page = None
        # Use a QPushButton for the central widget
        loadUi("needleform.ui", self)
        self.pushButton_next.clicked.connect(self.clicksave)
        self.pushButton_backfirst.clicked.connect(self.go_back)
        self.initValues()
        self.setTabOrder(self.comboBox_nTip, self.spinBox_nLengh)
        self.setTabOrder(self.spinBox_nLengh, self.comboBox_nDiameter)
        self.setTabOrder(self.comboBox_nDiameter, self.spinBox_nPatientDepth)
        self.setTabOrder(self.spinBox_nPatientDepth, self.comboBox_wLocation)
        self.setTabOrder(self.comboBox_wLocation, self.spinBox_wDepth)
        self.setTabOrder(self.spinBox_wDepth, self.spinBox_wSize)
        self.setTabOrder(self.spinBox_wSize, self.spinBox_nStitches)

    def initValues(self):
        self.comboBox_nTip.setCurrentIndex(0)
        self.spinBox_nLengh.setValue(20)
        self.comboBox_nDiameter.setCurrentIndex(0)
        self.spinBox_nPatientDepth.setValue(0)
        self.comboBox_wLocation.setCurrentIndex(0)
        self.spinBox_wDepth.setValue(0)
        self.spinBox_wSize.setValue(0)
        self.spinBox_nStitches.setValue(1)

    def clicksave(self):
        needle_length = self.spinBox_nLengh.value()
        needle_depth = self.spinBox_nPatientDepth.value()
        wound_depth = self.spinBox_wDepth.value()
        wound_size = self.spinBox_wSize.value()
        num_stitches = self.spinBox_nStitches.value()

        if needle_length == "" or needle_depth == "" or wound_depth == "" or wound_size == "" or num_stitches == "":
            QMessageBox.warning(self, "Achtung!", "Bitte füllen Sie alle erforderlichen Felder aus.")
            return

        needle_length = float(needle_length)
        needle_depth = float(needle_depth)
        wound_depth = float(wound_depth)
        wound_size = float(wound_size)
        num_stitches = float(num_stitches)

        if needle_length <= 0:
            QMessageBox.warning(self, "Achtung!", "Die Nadel Länge muss größer als Null sein.")
            return

        if needle_depth <= 0:
            QMessageBox.warning(self, "Achtung!", "Die Nadel-Tiefe muss größer als Null sein.")
            return

        if needle_depth > needle_length:
            QMessageBox.warning(self, "Achtung!", "Die Nadel-Tiefe darf nicht größer sein als die Nadel-Länge.")
            return

        if not (10 <= needle_length <= 70):
            QMessageBox.warning(self, "Achtung!", "Die Nadel-Länge muss zwischen 10 und 70 mm liegen.")
            return

        if wound_depth <= 0:
            QMessageBox.warning(self, "Achtung!", "Die Wundtiefe muss größer als Null sein.")
            return

        if wound_size <= 0:
            QMessageBox.warning(self, "Achtung!", "Die Wundgröße muss größer als Null sein.")
            return

        if num_stitches <= 0:
            QMessageBox.warning(self, "Achtung!", "Die Anzahl der Stiche muss größer als Null sein.")
            return

        needle_tip = self.comboBox_nTip.currentText()
        needle_diameter = self.comboBox_nDiameter.currentText()

        print("Operationsdaten gespeichert!")

        # Zeige die Kamera-Seite an
        self.show_next_signal.emit()
        self.hide()

    def show_main_window(self):
        self.camera_page.hide()
        self.show()

    def getSecondPageData(self):
        return {
            "NeedleTip": self.comboBox_nTip.currentText(),
            "NeedleLength": str(self.spinBox_nLengh.value()),
            "NeedleDiameter": self.comboBox_nDiameter.currentText(),
            "NeedleDepth": str(self.spinBox_nPatientDepth.value()),
            "WoundLocation": self.comboBox_wLocation.currentText(),
            "WoundDepth": str(self.spinBox_wDepth.value()),
            "WoundSize": str(self.spinBox_wSize.value()),
            "Number of Stitches": str(self.spinBox_nStitches.value()),
        }
    
    def getPointNumber(self):
        return self.spinBox_nStitches.value()

    def go_back(self):
        self.hide()
        self.show_prev_signal.emit()

    


class CameraPage(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("camerapage.ui", self)
        self.pushButton_back.clicked.connect(self.go_back)

    def go_back(self):
        self.hide()
        self.parent().show_main_window()
