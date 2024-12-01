from PyQt6.QtWidgets import QApplication
from GUI.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    
    start = MainWindow()
    
    app.exec()
