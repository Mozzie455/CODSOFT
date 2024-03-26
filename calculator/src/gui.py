#!/usr/bin/python3

# gui.py

""" Simple calculator with basic arithmetic operations. """


from configparser import ConfigParser
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

constants = ConfigParser()
constants.read("./src/constants.ini")


class CalcWindow(QMainWindow):
    """ Calculator's main window. """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        window_size = constants.get("CONSTANTS", "WINDOW_SIZE")
        window_height = constants.get("CONSTANTS", "WINDOW_SIZE")
        width, height = int(window_size), int(window_height)
        self.setFixedSize(width, height)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        window_height = constants.get("CONSTANTS", "DISPLAY_HEIGHT")
        self.display.setFixedHeight(int(window_height))
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                button_width = constants.get("CONSTANTS", "BUTTON_SIZE")
                button_height = constants.get("CONSTANTS", "BUTTON_SIZE")
                width, height = int(button_width), int(button_height)
                self.buttonMap[key].setFixedSize(width, height)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set the display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get the display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")
