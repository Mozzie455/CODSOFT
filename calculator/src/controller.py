#!/usr/bin/python3

# controller.py

from configparser import ConfigParser
from functools import partial

constants = ConfigParser()
constants.read("./src/constants.ini")


class Calc:
    """Calculator controller class."""

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        error_message = constants.get("CONSTANTS", "ERROR_MSG")
        if self._view.displayText() == error_message:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)


def evaluateExpression(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = constants.get("CONSTANTS", "ERROR_MSG")
    return result
