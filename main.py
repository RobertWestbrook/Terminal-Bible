import sys
from PyQt5 import QtGui, uic, QtWidgets
from Bible import *

# ----------------------UI Logic------------------------#


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(Ui, self).__init__()
        uic.loadUi('Terminal Bible.ui', self)  # Load the .ui file
        self.show()  # Show the GUI

        # versions
        self.version = NIV
        self.NKJV_box = self.findChild(QtWidgets.QCheckBox, 'NKJVbox')
        self.nkjv = self.NKJV_box
        self.NIV_box = self.findChild(QtWidgets.QCheckBox, 'NIVbox')
        self.niv = self.NIV_box
        self.ESV_box = self.findChild(QtWidgets.QCheckBox, 'ESVbox')
        self.esv = self.ESV_box

        # Update version
        self.nkjv.stateChanged.connect(self.version_update)
        self.niv.stateChanged.connect(self.version_update)
        self.esv.stateChanged.connect(self.version_update)

        # Book Combo
        self.comboBook = self.findChild(QtWidgets.QComboBox, 'comboBook')
        self.comboBook.addItems(Bible(self.version, "John", 1).bookNames)
        self.comboBook.currentTextChanged.connect(self.update_chapter)
        self.comboBook.currentTextChanged.connect(self.update_display)
        self.update_chapter()
        self.update_display()

        # chapter Combo
        self.comboChapter = self.findChild(QtWidgets.QComboBox, 'comboChapter')
        self.comboChapter.activated.connect(self.update_display)

        # Display
        self.display = self.findChild(QtWidgets.QTextBrowser, 'display')
        self.display.moveCursor(QtGui.QTextCursor.Start)
        self.address = self.findChild(QtWidgets.QLabel, 'address')

    # ----------------------Functionality------------------------#

    def update_chapter(self):
        '''
        When Book or chapter are changed this function will update the
        combo boxs.
        '''
        self.comboChapter.clear()
        self.chapterNums = Bible(
            self.version, self.comboBook.currentText(), 1).chapterTotal
        for c in range(1, self.chapterNums + 1):
            self.comboChapter.addItem(f'{c}')
        self.comboChapter.setCurrentIndex(0)

    def update_address(self):
        '''Displays proper verse address above text.'''
        self.address.clear()
        verseNums = (Bible(self.version, self.comboBook.currentText(),
                           self.comboChapter.currentIndex()+1).verseTotal)
        self.address.setText(f'-~ {self.comboBook.currentText()} '
                             f'{self.comboChapter.currentIndex()+1} : 1 - '
                             f'{verseNums}'
                             f'({Bible(self.version, "John", 1).getVersion()}) ~-')

    def update_display(self):
        '''Updates desplay to reflect the Book -> Chapter selected'''
        self.display.clear()
        text = (Bible(self.version, self.comboBook.currentText(),
                      self.comboChapter.currentIndex()+1).readChapter())
        self.display.append(text)
        self.update_address()
        self.display.moveCursor(QtGui.QTextCursor.Start)

    def version_update(self):
        '''
        Updates Text based on version selected.
        TO DO: Make versions capable of parallel display.
        '''
        if self.nkjv.isChecked() is True:
            self.version = NKJV
        elif self.esv.isChecked() is True:
            self.version = ESV
        elif self.niv.isChecked() is True:
            self.version = NIV
        else:
            self.version = Bible.NIV

        self.update_display()

    # ---------------------- Execution ------------------------#


if __name__ == '__main__':
    # Create an instance of QtWidgets.QApplication
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()  # Create an instance of our class
    app.exec_()  # Start the applications

    # ---------------------- To Do List ------------------------#

# Create a notes secton that auto saves as a texteditor for each passage that. Each
# chapter that open has a notes tab the can be opened to with any notes previously
# saved in it!
# Fix the navigation buttons
# Finish the search function.
