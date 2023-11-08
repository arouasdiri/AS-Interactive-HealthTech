import unittest
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QApplication
from Thirdpage import CameraPage

class TestCameraPage(unittest.TestCase):

    def setUp(self):
        # Setup code
        self.app = QApplication([])
        self.camera_page = CameraPage()

    def tearDown(self):
        # Teardown code
        self.camera_page.close()

    def test_initValues(self):
        self.camera_page.initValues()
        self.assertEqual(self.camera_page.maxPointCnt, 0)
        self.assertEqual(self.camera_page.points, [])
        self.assertEqual(self.camera_page.dataInfo, [])
        self.assertEqual(self.camera_page.number, 0)
        self.assertEqual(self.camera_page.co_listWidget.count(), 0)

    def test_setPointCount(self):
        self.camera_page.setPointCount(5)
        self.assertEqual(self.camera_page.maxPointCnt, 5)

    def test_getThirdPageData(self):
        data = self.camera_page.getThirdPageData()
        self.assertEqual(data, self.camera_page.dataInfo)

    def test_reset(self):
        self.camera_page.points = [(10, 20, 30), (40, 50, 60)]
        self.camera_page.dataInfo = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)]
        self.camera_page.number = 2
        self.camera_page.co_listWidget.addItem("Point 1")
        self.camera_page.co_listWidget.addItem("Point 2")

        self.camera_page.reset()

        self.assertEqual(self.camera_page.points, [])
        self.assertEqual(self.camera_page.dataInfo, [])
        self.assertEqual(self.camera_page.number, 0)
        self.assertEqual(self.camera_page.co_listWidget.count(), 0)

    def test_mousePressEvent(self):
        # Simulate a mouse press event at coordinates (100, 100)
        event = QMouseEvent(
            QMouseEvent.MouseButtonPress,
            QPoint(100, 100),
            Qt.LeftButton,
            Qt.LeftButton,
            Qt.NoModifier
        )
        self.camera_page.mousePressEvent(event)
        # Add your assertions here to test the behavior of the method

    def test_save_points(self):
        # Simulate emitting the show_next_signal
        self.camera_page.show_next_signal.emit()
        # Check if the camera page is hidden after emitting the signal
        self.assertFalse(self.camera_page.isVisible())

    def test_go_back(self):
        # Simulate emitting the show_prev_signal
        self.camera_page.show_prev_signal.emit()
        # Check if the camera page is hidden after emitting the signal
        self.assertFalse(self.camera_page.isVisible())

    def test_go_next(self):
        self.camera_page.show_next_signal.emit()
        self.assertFalse(self.camera_page.isVisible())
        

if __name__ == '__main__':
    unittest.main()
