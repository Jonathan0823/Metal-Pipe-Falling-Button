import sys
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rip my ears")
        self.setWindowIcon(QIcon("assets/images.jpeg"))
        self.setFixedSize(400, 300)
        self.labelimage = QLabel(self)
        self.button = QPushButton("Drop", self)       
        self.image = QPixmap("assets/image.jpeg") 

        self.initUI()

    def initUI(self):
        self.labelimage.setPixmap(QPixmap("assets/images.jpeg"))
        self.labelimage.setScaledContents(True)
        self.labelimage.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.labelimage)
        layout.addWidget(self.button)

        self.labelimage.setObjectName("labelimage")
        self.button.setObjectName("button")

        self.setLayout(layout)

        self.setStyleSheet("""

        QWidget#labelimage {
            background-color: #FFFFFF;
            border-radius: 10px;
            padding: 10px;
        }
                           
        QPushButton#button {
            background-color: #FFFFFF;
            border: 2px solid #000000;
            border-radius: 10px;
            padding: 10px;
        }
                           
        QPushButton#button:hover {
            background-color: #d1d1d1;
            color: #FFFFFF;
        }

        """)

        self.button.clicked.connect(self.playsound)

    def playsound(self):
        sound = "assets/sound.mp3"
        pygame.mixer.init()
        pygame.mixer.Sound(sound).play()
        pass

def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
