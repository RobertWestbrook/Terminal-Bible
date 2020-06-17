from PyQt5 import QtCore, QtGui, uic, QtWidgets
import sys
from Bible import Bible

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('Terminal Bible.ui', self) # Load the .ui file
        self.show() # Show the GUI
        
        #versions
        self.version = Bible.NIV
        self.NKJVbox = self.findChild(QtWidgets.QCheckBox, 'NKJVbox')
        self.nkjv = self.NKJVbox
        self.NIVbox = self.findChild(QtWidgets.QCheckBox, 'NIVbox')
        self.niv = self.NIVbox
        self.ESVbox = self.findChild(QtWidgets.QCheckBox, 'ESVbox')
        self.esv = self.ESVbox
        # self.versionUpdate()
        self.nkjv.stateChanged.connect(self.versionUpdate)
        self.niv.stateChanged.connect(self.versionUpdate)
        self.esv.stateChanged.connect(self.versionUpdate)
        
        # Book Combo 
        self.comboBook = self.findChild(QtWidgets.QComboBox, 'comboBook')
        self.comboBook.addItems(Bible(self.version, "John", 1).bookNames)
        self.comboBook.setCurrentIndex(0)
        self.comboBook.currentTextChanged.connect(self.update_chapter)
        self.update_chapter()
        
        # chapter Combo
        self.comboChapter = self.findChild(QtWidgets.QComboBox, 'comboChapter')
        self.comboChapter.setCurrentIndex(0)
        self.comboChapter.activated.connect(self.update_verse) # wouldn't work on Index Change???
        
        # verse combo
        self.comboVerse = self.findChild(QtWidgets.QComboBox, 'comboVerse')
        self.comboVerse.activated.connect(self.single_verse)
        
        # Display
        self.display = self.findChild(QtWidgets.QTextBrowser, 'display')
        self.display.moveCursor(QtGui.QTextCursor.Start)
        self.address = self.findChild(QtWidgets.QLabel, 'address')
        self.update_display()
        self.update_address()


    # Functionality
    def update_chapter(self):
        '''
        When Book or chapter are changed this function will update the 
        combo boxs.
        '''   
        self.comboChapter.clear()
        self.chapterNums = Bible(self.version, self.comboBook.currentText(), 1).chapterTotal
        for c in range(1, self.chapterNums +1):
            self.comboChapter.addItem(f'{c}')
        self.update_verse()
        self.update_display()
        print ('chapter update:')

    def update_verse(self):
        '''updates with verse combobox'''
        self.comboVerse.clear()
        self.verseNums = Bible(self.version, self.comboBook.currentText(), self.comboChapter.currentIndex()+1).verseTotal
        for v in range(1, self.verseNums +1):
            self.comboVerse.addItem(f'{v}')
            self.update_display()
        print ('verse update:')

    def update_address(self):
        self.address.clear()
        self.verseNums = Bible(self.version, self.comboBook.currentText(), self.comboChapter.currentIndex()+1).verseTotal
        self.address.setText(f'-~ {self.comboBook.currentText()} {self.comboChapter.currentIndex()+1} : 1 - '
                               f'{self.verseNums} ({Bible(self.version, "John", 1).getVersion()}) ~-')
        print ('address update:')

    def update_display(self):
        self.display.clear()
        self.text = Bible(self.version, self.comboBook.currentText(), self.comboChapter.currentIndex()+1).readChapter()
        self.display.append(self.text)
        self.update_address()
        self.display.moveCursor(QtGui.QTextCursor.Start)
        print ('display update:')


    def single_verse(self):
        self.display.clear()
        self.address.clear()
        self.text = (Bible(self.version, self.comboBook.currentText(), self.comboChapter
                    .currentIndex()+1).singleVerse(self.comboVerse.currentIndex()+1))
        self.display.append(self.text)
        self.address.setText(f'-~ {self.comboBook.currentText()} {self.comboChapter.currentIndex()+1}:'
                            f'{self.comboVerse.currentIndex()+1} ({Bible(self.version, "John", 1).getVersion()}) ~-')
        print ('single verse')

    def versionUpdate(self):
        '''
        Updates Text based on version selected.
        TO DO: -There is a bug in the single verse change that only allows
               doesn't allow version to be updated single verse if verse 
               selected is "1". 
               - Make versions capable of parallel display.
        '''
        print("version changed")
        if self.nkjv.isChecked() == True:
            self.version = Bible.NKJV
            print("NKJV")
        elif self.esv.isChecked() == True:
            self.version = Bible.ESV
            print("esv")
        elif self.niv.isChecked()==True:
            self.version = Bible.NIV
            print("NIV")
        else:
            self.version = Bible.NIV
        if self.comboVerse.currentIndex() != 0:
            self.single_verse()
        else:
            self.update_display()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = Ui() # Create an instance of our class
    app.exec_() # Start the applications



