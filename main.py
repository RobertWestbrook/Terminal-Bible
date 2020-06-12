from PyQt5 import QtCore, QtGui, uic, QtWidgets
import sys
from Bible import Bible

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('Terminal Bible.ui', self) # Load the .ui file
        self.show() # Show the GUI
        
        # Book Combo 
        self.comboBook = self.findChild(QtWidgets.QComboBox, 'comboBook')
        self.comboBook.addItems(Bible.bookNames)
        self.comboBook.setCurrentIndex(0)
        self.comboBook.currentTextChanged.connect(self.update_chapter)
        self.update_chapter()
        
        # chapter Combo
        self.comboChapter = self.findChild(QtWidgets.QComboBox, 'comboChapter')
        self.comboChapter.setCurrentIndex(0)
        self.comboChapter.activated.connect(self.update_verse) # wouldn't work on Index Change???
        
        # verse combo
        self.comboVerse = self.findChild(QtWidgets.QComboBox, 'comboVerse')

        # Display
        self.display = self.findChild(QtWidgets.QTextEdit, 'display')
        self.display.setReadOnly(True)
        self.update_display()
        
    # Functionality

    def update_chapter(self):
        '''
        When Book or chapter are changed this function will update the 
        combo boxs.
        '''   
        self.comboChapter.clear()
        self.chapterNums = Bible(self.comboBook.currentText(), 1).chapterTotal
        for c in range(1, self.chapterNums +1):
            self.comboChapter.addItem(f'{c}')
        self.update_verse()
        self.update_display()


    def update_verse(self):
        '''updates when verse combo box'''
        self.comboVerse.clear()
        self.verseNums = Bible(self.comboBook.currentText(), self.comboChapter.currentIndex()+1).verseTotal
        for v in range(1, self.verseNums +1):
            self.comboVerse.addItem(f'{v}')
            self.update_display()
        

    def update_display(self):
        self.display.clear()
        self.display.moveCursor(QtGui.QTextCursor.Start)
        self.text = Bible(self.comboBook.currentText(), self.comboChapter.currentIndex()+1).readChapter()
        self.display.append(self.text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = Ui() # Create an instance of our class
    app.exec_() # Start the application