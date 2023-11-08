import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QStackedWidget,QTableWidgetItem
from pymongo import MongoClient
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal

client = MongoClient('mongodb://localhost:27017/')
db = client['autonomen_chirurgischen_Robotern']
collection = db['BA23']

data = collection.find()



# Get the number of databases

class AllInfo(QMainWindow):
    show_prev_signal = pyqtSignal()
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        # Use a QPushButton for the central widget
        self.first_page = None
        loadUi("Allinfoform.ui", self)
        self.pushButton_backLast.clicked.connect(self.go_back)
        self.pushButton_delete.clicked.connect(self.delete_selected_row)
       # Set the number of rows and columns in the table

        # Add headers

        self.m_finalTableWidget.setColumnCount(17)

        headers = [
            "_id","Name","Surname","Gender","DOB","OperationDate","InsuranceID","EmergencyContact",
            "Notes","NeedleTip","NeedleLength","NeedleDiameter","NeedleDepth","WoundLocation","WoundDepth",
            "WoundSize","Number of Stitches"
        ]
        self.m_finalTableWidget.setHorizontalHeaderLabels(headers)
        self.m_finalTableWidget.hideColumn(0)

    def delete_selected_row(self):
        selected_row = self.m_finalTableWidget.currentRow()
        if selected_row >= 0:
            document_id = self.m_finalTableWidget.item(selected_row, 0).text()
            # Convert the ObjectId string to a valid ObjectId object
            from bson import ObjectId
            doc_id = ObjectId(document_id)
            # Use the ObjectId to delete the corresponding MongoDB document
            collection.delete_one({'_id': doc_id})
            # Remove the selected row from the table widget
            self.m_finalTableWidget.removeRow(selected_row)

    def go_back(self):
        self.hide()
        self.show_prev_signal.emit()

    def loadData(self):
        data = collection.find()
        num_documents = collection.count_documents({})
        self.m_finalTableWidget.setRowCount(num_documents)
        for row_idx, document in enumerate(data):
            # Retrieve field values from the document
            values = [
                str(document['_id']),
                document['Name'],
                document['Surname'],
                document['Gender'],
                document['DOB'],
                document['OperationDate'],
                document['InsuranceID'],
                document['EmergencyContact'],
                document['Notes'],
                document['NeedleTip'],
                document['NeedleLength'],
                document['NeedleDiameter'],
                document['NeedleDepth'],
                document['WoundLocation'],
                document['WoundDepth'],
                document['WoundSize'],
                document['Number of Stitches']

            ]

            # Set values in the table
            for col_idx, value in enumerate(values):
                item = QTableWidgetItem(value)
                self.m_finalTableWidget.setItem(row_idx, col_idx, item)


