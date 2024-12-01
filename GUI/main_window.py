from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from GUI.style.style_Qt import CONST_MAIN_WINDOW
from Logics.download_video import download_video_youtube_dl

def popup_window(title : str, text : str):
    window = QMessageBox()
    window.setWindowTitle(title)
    window.setText(text)
    window.exec()

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Скачивание видео с ютуб")
        self.setFixedSize(350, 250)
        self.setWindowIcon(QIcon(r"image\icon.webp"))
        self.setStyleSheet(CONST_MAIN_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Через ';' без пробелов введите ссылку на видео")
        self.url = QLineEdit()
        self.url.setFixedHeight(60)
        download = QPushButton(text="Начать скачивание")
        download.clicked.connect(self.download_and_save_selection)
        
        control_UI.addWidget(instructions, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.url)
        control_UI.addWidget(download)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
        
    def download_and_save_selection(self):
        try:
            url_list = self.url.text().split(";")
            path = QFileDialog().getExistingDirectory(self, "Выбирите куда сохранить видео(папку)")
            for i in range(len(url_list) - 1):
                print(url_list[i])
                if "https" not in url_list[i] or "youtube" not in url_list[i]:
                    raise ValueError("Вы неправильно указали ссылку")

                download_video_youtube_dl(url_list[i], path)
                
            popup_window("Успех", "Все видео скачаны")
            
        except ValueError:
            popup_window("Ошибка", "Скорее всего проблема ввода, обратитесь к вашему программисту")
            
