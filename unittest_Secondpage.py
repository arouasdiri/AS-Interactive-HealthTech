import sys
import unittest
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from unittest.mock import patch
from Secondpage import SurgicalDataForm

app = QApplication([])

class TestSurgicalDataForm(unittest.TestCase):

    def setUp(self):
        self.form = SurgicalDataForm()

    def test_initValues(self):
        self.form.initValues()
        self.assertEqual(self.form.comboBox_nTip.currentIndex(), 0)
        self.assertEqual(self.form.spinBox_nLengh.value(), 20)
        self.assertEqual(self.form.comboBox_nDiameter.currentIndex(), 0)
        self.assertEqual(self.form.spinBox_nPatientDepth.value(), 0)
        self.assertEqual(self.form.comboBox_wLocation.currentIndex(), 0)
        self.assertEqual(self.form.spinBox_wDepth.value(), 0)
        self.assertEqual(self.form.spinBox_wSize.value(), 0)
        self.assertEqual(self.form.spinBox_nStitches.value(), 1)

    def test_clicksave_with_missing_data(self):
        with patch.object(QMessageBox, 'warning') as mock_warning:
            self.form.pushButton_next.click()  # Trigger the click event
            QApplication.processEvents()  # Process pending events

            # The save should not proceed and a message box should be shown
            self.assertTrue(mock_warning.called)
            self.assertEqual(mock_warning.call_count, 1)
            self.assertFalse(self.form.isVisible())

    def test_clicksave_with_valid_data(self):
        self.form.comboBox_nTip.setCurrentIndex(1)
        self.form.spinBox_nLengh.setValue(50)
        self.form.comboBox_nDiameter.setCurrentIndex(1)
        self.form.spinBox_nPatientDepth.setValue(25)
        self.form.comboBox_wLocation.setCurrentIndex(1)
        self.form.spinBox_wDepth.setValue(10)
        self.form.spinBox_wSize.setValue(20)
        self.form.spinBox_nStitches.setValue(3)

        self.form.pushButton_next.click()  # Trigger the click event

        # The form should be hidden
        self.assertFalse(self.form.isVisible())

    def tearDown(self):
        self.form.close()


if __name__ == "__main__":
    unittest.main()
