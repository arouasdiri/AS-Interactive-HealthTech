import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFormLayout, QRadioButton
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal, QDate, QTime, QDateTime
from PyQt5.QtWidgets import QMessageBox

class Window(QMainWindow):
    show_next_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.surgical_data_form = None
        loadUi("firstform.ui", self)
        self.pushButton_firstsave.clicked.connect(self.clicksave)
        self.initValues()

        # Set tab order for input fields
        self.setTabOrder(self.radioButton_male, self.radioButton_female)
        self.setTabOrder(self.radioButton_female, self.radioButton_divers)
        self.setTabOrder(self.radioButton_divers, self.dateEdit_birthdate)
        self.setTabOrder(self.dateEdit_birthdate, self.lineEdit_firstname)
        self.setTabOrder(self.lineEdit_firstname, self.lineEdit_lastname)
        self.setTabOrder(self.lineEdit_lastname, self.dateEdit_scheduledate)
        self.setTabOrder(self.dateEdit_scheduledate, self.lineEdit_patientid)
        self.setTabOrder(self.lineEdit_patientid, self.lineEdit_emergency)
        self.setTabOrder(self.lineEdit_emergency, self.lineEdit_notes)
        self.setTabOrder(self.lineEdit_notes, self.pushButton_firstsave)

    def initValues(self):
        self.lineEdit_firstname.setText("")
        self.lineEdit_lastname.setText("")
        self.dateEdit_birthdate.setDate(QDate(1940, 1, 1))
        self.dateEdit_scheduledate.setDate(QDate.currentDate())
        self.lineEdit_patientid.setText("")
        self.lineEdit_emergency.setText("")
        self.lineEdit_notes.setText("")

        self.dateEdit_birthdate.setDisplayFormat("dd-MM-yyyy")
        self.dateEdit_scheduledate.setDisplayFormat("dd-MM-yyyy")

        # Hier aktivieren wir die QLineEdit-Felder nach dem Zurücksetzen
        self.lineEdit_firstname.setEnabled(True)
        self.lineEdit_lastname.setEnabled(True)
        self.lineEdit_patientid.setEnabled(True)
        self.lineEdit_emergency.setEnabled(True)
        self.lineEdit_notes.setEnabled(True)

        # Geschlechtsauswahl auf "Männlich" setzen (Index 0)
        self.radioButton_male.setChecked(True)

    def clicksave(self):
        if self.lineEdit_firstname.text() == '' or self.lineEdit_lastname.text() == '' or self.lineEdit_patientid.text() == '' or self.lineEdit_emergency.text() == '':
            QMessageBox.about(self, "Achtung!", "Du musst alle erforderlichen Daten eingeben.")
            return

        operation_date = self.dateEdit_scheduledate.date()
        current_date = QDate.currentDate()
        if operation_date < current_date:
            QMessageBox.about(self, "Achtung!", "Das Datum der Operation darf nicht in der Vergangenheit liegen.")
            return

        self.show_next_signal.emit()
        self.hide()

    def getFirstPageData(self):
        return {
            "Name": self.lineEdit_firstname.text(),
            "Surname": self.lineEdit_lastname.text(),
            "Gender": self.get_selected_gender(),
            "DOB": self.dateEdit_birthdate.date().toString("dd-MM-yyyy"),
            "OperationDate": self.dateEdit_scheduledate.date().toString("dd-MM-yyyy"),
            "InsuranceID": self.lineEdit_patientid.text(),
            "EmergencyContact": self.lineEdit_emergency.text(),
            "Notes": self.lineEdit_notes.text()
        }

    def get_selected_gender(self):
        if self.radioButton_male.isChecked():
            return "Männlich"
        elif self.radioButton_female.isChecked():
            return "Weiblich"
        elif self.radioButton_divers.isChecked():
            return "Divers"
        else:
            return ""

    def show_main_window(self):
        self.surgical_data_form.hide()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
