import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication

from Firstpage import Window
from Secondpage import SurgicalDataForm
from Thirdpage import CameraPage
from Lastpage import FinalPage
from AllinfoPage import AllInfo


class CameraApplication(QObject):
    def __init__(self):
        super().__init__()

        # the widgets
        self.firstPage = Window()
        self.secondPage = SurgicalDataForm()
        self.thirdPage = CameraPage()
        self.lastPage = FinalPage()
        self.InfoPage = AllInfo()

        # signals connection
        self.firstPage.show_next_signal.connect(self.showSecondPage)
        self.secondPage.show_next_signal.connect(self.showThirdPage)
        self.thirdPage.show_next_signal.connect(self.showLastPage)
        self.lastPage.show_next_signal.connect(self.showFirstPageNew)
        self.lastPage.show_all_signal.connect(self.showAllInfoPage)

        self.secondPage.show_prev_signal.connect(self.showFirstPage)
        self.thirdPage.show_prev_signal.connect(self.showSecondPage)
        self.lastPage.show_prev_signal.connect(self.showThirdPage)
        self.InfoPage.show_prev_signal.connect(self.showLastPage)

        # show the first page
        self.firstPage.show()

    def showFirstPageNew(self):
        self.firstPage.initValues()
        self.secondPage.initValues()
        self.thirdPage.initValues()

        self.firstPage.show()

    def showFirstPage(self):
        self.firstPage.show()

    def showSecondPage(self):
        self.secondPage.show()

    def showThirdPage(self):
        count = self.secondPage.getPointNumber()
        print(count)
        self.thirdPage.setPointCount(count)
        self.thirdPage.show()

    def showLastPage(self):
        firstPageData = self.firstPage.getFirstPageData()
        secondPageData = self.secondPage.getSecondPageData()
        thirdPageData = self.thirdPage.getThirdPageData()

        self.lastPage.set_patient_infoall(firstPageData, secondPageData, thirdPageData)
        self.lastPage.show()

    def showAllInfoPage(self):
        self.InfoPage.loadData()
        self.InfoPage.show()


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    # Run the application's main loop

    cApp = CameraApplication()

    sys.exit(app.exec())