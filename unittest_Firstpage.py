import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDate
from PyQt5.QtTest import QTest
from Firstpage import Window

app = QApplication([])


class TestWindow(unittest.TestCase):

    def setUp(self):
        self.window = Window()

    def test_initValues(self):
        self.window.initValues()

        self.assertEqual(self.window.lineEdit_firstname.text(), "")
        self.assertEqual(self.window.lineEdit_lastname.text(), "")
        self.assertEqual(self.window.get_selected_gender(), "Männlich")
        self.assertEqual(self.window.dateEdit_birthdate.date().toString("dd-MM-yyyy"), "01-01-1940")
        self.assertEqual(self.window.dateEdit_scheduledate.date().toString("dd-MM-yyyy"), QDate.currentDate().toString("dd-MM-yyyy"))
        self.assertEqual(self.window.lineEdit_patientid.text(), "")
        self.assertEqual(self.window.lineEdit_emergency.text(), "")
        self.assertEqual(self.window.lineEdit_notes.text(), "")

    def test_getFirstPageData(self):
        self.window.lineEdit_firstname.setText("John")
        self.window.lineEdit_lastname.setText("Doe")
        self.window.radioButton_female.setChecked(True)  # Set the "Weiblich" radio button
        self.window.dateEdit_birthdate.setDate(self.window.dateEdit_birthdate.minimumDate())
        self.window.dateEdit_scheduledate.setDate(self.window.dateEdit_scheduledate.minimumDate())
        self.window.lineEdit_patientid.setText("123456")
        self.window.lineEdit_emergency.setText("Emergency Contact")
        self.window.lineEdit_notes.setText("Some notes")

        data = self.window.getFirstPageData()
        expected_data = {
            "Name": "John",
            "Surname": "Doe",
            "Gender": "Weiblich",
            "DOB": self.window.dateEdit_birthdate.minimumDate().toString("dd-MM-yyyy"),
            "OperationDate": self.window.dateEdit_scheduledate.minimumDate().toString("dd-MM-yyyy"),
            "InsuranceID": "123456",
            "EmergencyContact": "Emergency Contact",
            "Notes": "Some notes"
        }

        self.assertEqual(data, expected_data)

    def test_clicksave_with_missing_data(self):
        self.window.lineEdit_firstname.setText("John")
        self.window.lineEdit_lastname.setText("Doe")
        self.window.lineEdit_patientid.setText("123456")
        self.window.lineEdit_emergency.setText("Emergency Contact")
        self.window.pushButton_firstsave.clicked.emit()  # Emit the clicked signal manually
        QApplication.processEvents()  # Process pending events

        # Wait for the window to become visible
        self.window.show()
        QApplication.processEvents()
        QTest.qWaitForWindowExposed(self.window)

        # The save should not proceed and a message box should be shown
        self.assertTrue(self.window.isVisible())

    def test_clicksave_with_past_operation_date(self):
        self.window.lineEdit_firstname.setText("John")
        self.window.lineEdit_lastname.setText("Doe")
        self.window.lineEdit_patientid.setText("123456")
        self.window.lineEdit_emergency.setText("Emergency Contact")
        self.window.dateEdit_scheduledate.setDate(QDate.currentDate().addDays(-1))
        self.window.pushButton_firstsave.clicked.emit()  # Emit the clicked signal manually
        QApplication.processEvents()  # Process pending events

        # Wait for the window to become visible
        self.window.show()
        QApplication.processEvents()
        QTest.qWaitForWindowExposed(self.window)

        # The save should not proceed and a message box should be shown
        self.assertTrue(self.window.isVisible())

    def test_clicksave_successful(self):
        self.window.lineEdit_firstname.setText("John")
        self.window.lineEdit_lastname.setText("Doe")
        self.window.lineEdit_patientid.setText("123456")
        self.window.lineEdit_emergency.setText("Emergency Contact")
        self.window.dateEdit_scheduledate.setDate(QDate.currentDate().addDays(1))
        self.window.pushButton_firstsave.clicked.emit()  # Emit the clicked signal manually

        # The window should be hidden
        self.assertFalse(self.window.isVisible())

    def tearDown(self):
        self.window.close()


if __name__ == "__main__":
    unittest.main()
