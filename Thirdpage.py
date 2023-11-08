import sys
import pyrealsense2 as rs
import numpy as np
import cv2
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtGui import QImage, QPixmap


class CameraPage(QMainWindow):
    show_next_signal = pyqtSignal()
    show_prev_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("coordinationform.ui", self)

        self.final_page = None
        self.image_label.setScaledContents(True)
        self.pushButton_thirdnext.clicked.connect(self.save_points)
        self.pushButton_thirdback.clicked.connect(self.go_back)
        self.pushButton_reset.clicked.connect(self.reset)
        
        self.initValues()
        self.initCamera()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(30)  # Update the image every 30 milliseconds

    def initValues(self):
        self.maxPointCnt = 0
        self.points = []
        self.dataInfo = []
        self.number = 0
        self.co_listWidget.clear()

    def initCamera(self):
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        self.pipeline.start(self.config)

    def save_points(self):
        self.show_next_signal.emit()
        self.hide()

    def setPointCount(self, n):
        self.maxPointCnt = n

    def getThirdPageData(self):
        return self.dataInfo
        

    def go_back(self):
        self.hide()
        self.show_prev_signal.emit()

    def reset(self):
        self.points = []
        self.dataInfo = []
        self.co_listWidget.clear()
        self.number = 0

    def update_image(self):
        # Warten auf neue Frames
        frames = self.pipeline.wait_for_frames()

        # Zugriff auf Farb- und Tiefenframe
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        # Überprüfen, ob Frames vorhanden sind
        if not color_frame or not depth_frame:
            return

        # Konvertierung der Frames in numpy-Arrays
        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())

        # Liste von Farben für die Punkte
        point_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255),
                        (0, 255, 255), (255, 165, 0), (255, 255, 255), (255, 192, 203), (255, 215, 0)]

        # Iteration über die Punkte
        for i, point in enumerate(self.points):
            x_image, y_image = point[:2]
            # Festlegen der Farbe für den Punkt
            point_color = point_colors[i % len(point_colors)]

            # Zeichnen eines Markers und Texts auf dem Farbbild
            cv2.drawMarker(color_image, (x_image, y_image), point_color, markerType=cv2.MARKER_CROSS, markerSize=10, thickness=2)
            cv2.putText(color_image, "P" + str(i), (x_image + 10, y_image + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, point_color, 1, cv2.LINE_AA)

        # Konvertierung des Farbarrays in ein QPixmap-Objekt
        pixmap = QPixmap.fromImage(QImage(color_image.data, color_image.shape[1], color_image.shape[0], color_image.strides[0], QImage.Format_RGB888))

        # Setzen des Pixmaps auf das Image-Label
        self.image_label.setPixmap(pixmap)



    def mousePressEvent(self, event):
        pos = self.image_label.mapFromParent(event.pos())
        x = pos.x()
        y = pos.y()

        if 0 <= x < self.image_label.width() and 0 <= y < self.image_label.height() and self.number < self.maxPointCnt:
            x_normalized = x / self.image_label.width()
            y_normalized = y / self.image_label.height()

            x_image = int(x_normalized * 640)
            y_image = int(y_normalized * 480)

            depth_frame = self.pipeline.wait_for_frames().get_depth_frame()
            depth_intrin = depth_frame.profile.as_video_stream_profile().intrinsics
            depth = depth_frame.get_distance(x_image, y_image)
            point = rs.rs2_deproject_pixel_to_point(depth_intrin, [x_image, y_image], depth)

            if point[0] == 0 and point[1] == 0 and point[2] == 0:
                self.show_warning_message("Warning!", "Remove interference element")
                return
            
                #if self.points[i] is None
            self.points.append((x_image, y_image, point[2]))
            self.dataInfo.append((round(point[0] * 1000, 2), round(point[1] * 1000, 2), round(point[2] * 1000, 2)))
            #self.points.append((round(point[0],2), round(point[1],2), round(point[2],2)))
            textbox_item = ["Point" + str(self.number) + ": (" + str(round(point[0] * 1000, 2)) + " mm, " + str(round(point[1] * 1000, 2)) + " mm, " + str(round(point[2] * 1000, 2)) + " mm)"]
            self.co_listWidget.addItems(textbox_item)
            self.number = self.number + 1


    def show_warning_message(self, title, message):
        QMessageBox.information(self, title, message)



    def show_main_window(self):
        self.final_page.hide()
        self.show()
