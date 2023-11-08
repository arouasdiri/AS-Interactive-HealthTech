import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QStackedWidget, QMessageBox,QTableWidget, QTableWidgetItem
from pymongo import MongoClient
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox

client = MongoClient('mongodb://localhost:27017/')
db = client['autonomen_chirurgischen_Robotern']
collection = db['BA23']

class FinalPage(QMainWindow):
    show_next_signal = pyqtSignal()
    show_all_signal = pyqtSignal()
    show_prev_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("final_form.ui", self)
        self.pushButton_finalback.clicked.connect(self.go_back)
        self.pushButton_newpatient.clicked.connect(self.go_first)
        self.pushButton_exit.clicked.connect(self.exit_program)
        self.pushButton_info.clicked.connect(self.go_AllInfoPage)
        self.pushButton_saveAllinfo.clicked.connect(self.saveAllDataInfo)


    def set_patient_infoall(self, firstPageData, secondPageData, thirdPageData):
        self.fdata = {
            "Name": firstPageData.get("Name", ""),
            "Surname": firstPageData.get("Surname", ""),
            "Gender": firstPageData.get("Gender", ""),
            "DOB": firstPageData.get("DOB", ""),
            "OperationDate": firstPageData.get("OperationDate", ""),
            "InsuranceID": firstPageData.get("InsuranceID", ""),
            "EmergencyContact": firstPageData.get("EmergencyContact", ""),
            "Notes": firstPageData.get("Notes", ""),

            "NeedleTip": secondPageData.get("NeedleTip", ""),
            "NeedleLength": secondPageData.get("NeedleLength", ""),
            "NeedleDiameter": secondPageData.get("NeedleDiameter", ""),
            "NeedleDepth": secondPageData.get("NeedleDepth", ""),
            "WoundLocation": secondPageData.get("WoundLocation", ""),
            "WoundDepth": secondPageData.get("WoundDepth", ""),
            "WoundSize" : secondPageData.get("WoundSize", ""),
            "Number of Stitches" : secondPageData.get("Number of Stitches", ""),

            "points": thirdPageData        }

        self.fcomboBox_gender.setCurrentText(self.fdata["Gender"])
        self.flineEdit_firstname.setText(self.fdata["Name"])
        self.fdateEdit_birthdate.setDate(QtCore.QDate.fromString(self.fdata["DOB"], "dd-MM-yyyy"))
        self.flineEdit_lastname.setText(self.fdata["Surname"])
        self.fdateEdit_scheduledate.setDate(QtCore.QDate.fromString(self.fdata["OperationDate"], "dd-MM-yyyy"))
        self.flineEdit_patientid.setText(self.fdata["InsuranceID"])
        self.flineEdit_emergency.setText(self.fdata["EmergencyContact"])
        self.flineEdit_notes.setText(self.fdata["Notes"])
        self.fcomboBox_nTip.setCurrentText(self.fdata["NeedleTip"])
        self.fcomboBox_nLength.setCurrentText(self.fdata["NeedleLength"])
        self.fcomboBox_nDiameter.setCurrentText(self.fdata["NeedleDiameter"])
        self.flineEdit_nPatientDepth.setText(self.fdata["NeedleDepth"])
        self.fcomboBox_wLocation.setCurrentText(self.fdata["WoundLocation"])
        self.flineEdit_wDepth.setText(self.fdata["WoundDepth"])
        self.flineEdit_wSize.setText(self.fdata["WoundSize"])
        self.flineEdit_nStitches.setText(self.fdata["Number of Stitches"])
        self.co_tableWidget.setRowCount(int(self.fdata["Number of Stitches"]))
        for row, item in enumerate(thirdPageData):
            for col, value in enumerate(item):
                table_item = QTableWidgetItem(str(value))
                self.co_tableWidget.setItem(row, col, table_item)
        print(thirdPageData)

    def go_back(self):
        self.hide()
        self.show_prev_signal.emit()

    def go_first(self):
        self.hide()
        self.show_next_signal.emit()

    def saveAllDataInfo(self):
        result = collection.insert_one(self.fdata)
        QMessageBox.about(self, "Glückwunsch!", "Du hast alle Daten erfolgreich gesichert!")
        if result.acknowledged:
            print("Daten erfolgreich gespeichert.")
        else:
            print("Fehler beim Speichern der Daten.")
    def exit_program(self):
        reply = QMessageBox.question(self, 'Programm beenden', 'Möchten Sie das Programm wirklich beenden?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.quit()

    def go_AllInfoPage(self):
        self.hide()
        self.show_all_signal.emit()