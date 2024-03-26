#!/usr/bin/python3

# __main__.py

import sys
from PyQt6.QtWidgets import QApplication
from src.gui import CalcWindow
from src.controller import Calc, evaluateExpression

"""Calculator's main execution file"""


def main():
    """Calculator's main function"""
    # Create an instance of QApplication
    app = QApplication([])
    # show application's Graphic User Interface
    window = CalcWindow()
    window.show()
    Calc(model=evaluateExpression, view=window)
    # Run the calculator application's event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
