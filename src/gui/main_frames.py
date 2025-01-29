from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QApplication
from PyQt6.QtCore import Qt
import sys

class InazumaElevenWindow(QMainWindow):
    def __init__(self, menu_window):
        super().__init__()
        self.menu_window = menu_window
        self.setWindowTitle("Inazuma Eleven")
        self.setGeometry(150, 150, 400, 300)

        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        back_button = QPushButton("Back to Menu")
        back_button.clicked.connect(self.back_to_menu)
        layout.addWidget(back_button)

    def back_to_menu(self):
        self.menu_window.show()
        self.close()

class InazumaEleven2Window(QMainWindow):
    def __init__(self, menu_window):
        super().__init__()
        self.menu_window = menu_window
        self.setWindowTitle("Inazuma Eleven 2")
        self.setGeometry(150, 150, 400, 300)

        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        back_button = QPushButton("Back to Menu")
        back_button.clicked.connect(self.back_to_menu)
        layout.addWidget(back_button)

    def back_to_menu(self):
        self.menu_window.show()
        self.close()

class InazumaEleven3Window(QMainWindow):
    def __init__(self, menu_window):
        super().__init__()
        self.menu_window = menu_window
        self.setWindowTitle("Inazuma Eleven 3")
        self.setGeometry(150, 150, 400, 300)

        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        back_button = QPushButton("Back to Menu")
        back_button.clicked.connect(self.back_to_menu)
        layout.addWidget(back_button)

    def back_to_menu(self):
        self.menu_window.show()
        self.close()

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inazuma Eleven Scouting Toolkit")
        self.setGeometry(100, 100, 600, 400)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Título centrado
        self.label = QLabel("Select a videogame")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Botones de navegación
        self.button_ie = QPushButton("Inazuma Eleven")
        self.button_ie2 = QPushButton("Inazuma Eleven 2")
        self.button_ie3 = QPushButton("Inazuma Eleven 3")
        self.button_exit = QPushButton("Exit")

        # Conectar botones con eventos
        self.button_ie.clicked.connect(self.open_ie_window)
        self.button_ie2.clicked.connect(self.open_ie2_window)
        self.button_ie3.clicked.connect(self.open_ie3_window)
        self.button_exit.clicked.connect(self.close)

        # Agregar elementos al layout
        layout.addWidget(self.label)
        layout.addWidget(self.button_ie)
        layout.addWidget(self.button_ie2)
        layout.addWidget(self.button_ie3)
        layout.addWidget(self.button_exit)

        # Ventanas secundarias
        self.ie_window = None
        self.ie2_window = None
        self.ie3_window = None

    def open_ie_window(self):
        self.ie_window = InazumaElevenWindow(self)
        self.ie_window.show()
        self.hide()

    def open_ie2_window(self):
        self.ie2_window = InazumaEleven2Window(self)
        self.ie2_window.show()
        self.hide()

    def open_ie3_window(self):
        self.ie3_window = InazumaEleven3Window(self)
        self.ie3_window.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec())
