import unittest
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QStackedWidget, QTableWidgetItem
from pymongo import MongoClient
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal

# Importieren der zu testenden Klasse
from AllinfoPage import AllInfo

# Beispieltests für die AllInfo-Klasse
class TestAllInfo(unittest.TestCase):
    def test_delete_selected_row(self):
        # Vorbereitung des Tests
        app = QApplication([])
        main_window = QMainWindow()
        all_info = AllInfo(parent=main_window)
        all_info.m_finalTableWidget.setRowCount(3)
        item = QTableWidgetItem("60f4e1c43fa8c93ebc9d4b0c")  # Gültiger ObjectId-Wert
        all_info.m_finalTableWidget.setItem(0, 0, item)

        # Ausführung des Tests
        all_info.m_finalTableWidget.setCurrentCell(0, 0)
        all_info.delete_selected_row()

        # Überprüfung des Ergebnisses
        self.assertEqual(all_info.m_finalTableWidget.rowCount(), 2)


    def test_go_back(self):
        # Vorbereitung des Tests
        app = QApplication([])
        main_window = QMainWindow()
        all_info = AllInfo(parent=main_window)
        signal_received = False

        def on_show_prev_signal():
            nonlocal signal_received
            signal_received = True

        all_info.show_prev_signal.connect(on_show_prev_signal)

        # Ausführung des Tests
        all_info.go_back()

        # Überprüfung des Ergebnisses
        self.assertTrue(signal_received)

if __name__ == '__main__':
    unittest.main()
