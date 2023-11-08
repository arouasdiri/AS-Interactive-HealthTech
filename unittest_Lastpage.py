import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from Lastpage import FinalPage

class TestFinalPage(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.page = FinalPage()

    def tearDown(self):
        self.app.quit()

    def test_set_patient_infoall(self):
        firstPageData = {
            "Name": "John",
            "Surname": "Doe",
            "Gender": "Male",
            "DOB": "01-01-1990",
            "OperationDate": "01-02-2023",
            "InsuranceID": "123456789",
            "EmergencyContact": "Jane Doe",
            "Notes": "Test notes"
        }
        secondPageData = {
            "NeedleTip": "Straight Needle",
            "NeedleLength": "10",
            "NeedleDiameter": "FineNeedle: Gauge 30-33",
            "NeedleDepth": "5",
            "WoundLocation": "Head/Neck",
            "WoundDepth": "10",
            "WoundSize": "50",
            "Number of Stitches": "3"
        }
        thirdPageData = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

        self.page.set_patient_infoall(firstPageData, secondPageData, thirdPageData)

        self.assertEqual(self.page.fcomboBox_gender.currentText(), "Männlich")
        self.assertEqual(self.page.flineEdit_firstname.text(), "John")
        self.assertEqual(self.page.fdateEdit_birthdate.date().toString("dd-MM-yyyy"), "01-01-1990")
        self.assertEqual(self.page.flineEdit_lastname.text(), "Doe")
        self.assertEqual(self.page.fdateEdit_scheduledate.date().toString("dd-MM-yyyy"), "01-02-2023")
        self.assertEqual(self.page.flineEdit_patientid.text(), "123456789")
        self.assertEqual(self.page.flineEdit_emergency.text(), "Jane Doe")
        self.assertEqual(self.page.flineEdit_notes.text(), "Test notes")
        self.assertEqual(self.page.fcomboBox_nTip.currentText(), "Straight Needle")
        self.assertEqual(self.page.fcomboBox_nLength.currentText(), "10")
        self.assertEqual(self.page.fcomboBox_nDiameter.currentText(), "FineNeedle: Gauge 30-33")
        self.assertEqual(self.page.flineEdit_nPatientDepth.text(), "5")
        self.assertEqual(self.page.fcomboBox_wLocation.currentText(), "Head/Neck")
        self.assertEqual(self.page.flineEdit_wDepth.text(), "10")
        self.assertEqual(self.page.flineEdit_wSize.text(), "50")
        self.assertEqual(self.page.flineEdit_nStitches.text(), "3")
        self.assertEqual(self.page.co_tableWidget.rowCount(), 3)
        for row in range(3):
            for col in range(3):
                item = self.page.co_tableWidget.item(row, col)
                self.assertEqual(item.text(), thirdPageData[row][col])

if __name__ == "__main__":
    unittest.main()
