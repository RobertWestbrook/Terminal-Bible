from PyQt5 import QtCore, QtGui, uic, QtWidgets
import sys
from Bible import Bible



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('Terminal Bible.ui', self) # Load the .ui file
        self.show() # Show the GUI

        self.comboBook = self.findChild(QtWidgets.QComboBox, 'comboBook')
        self.comboBook.addItems(Bible.bookNames)
        self.comboBook.activated.connect(self.on_combo_change)

        self.comboChapter = self.findChild(QtWidgets.QComboBox, 'comboChapter')
        self.comboChapter.addItems(['test'])

        self.comboVerse = self.findChild(QtWidgets.QComboBox, 'comboVerse')
        self.comboVerse.addItems(['test'])

        self.dislay = self.findChild(QtWidgets.QTextBrowser, 'display')
        self.display.append("test")

    def on_combo_change(self):
        print(self.comboBook.currentText())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = Ui() # Create an instance of our class
    app.exec_() # Start the application