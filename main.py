import sys
from PyQt5 import QtGui, uic, QtWidgets
from Bible import Bible

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('Terminal Bible.ui', self) # Load the .ui file
        self.show() # Show the GUI

        #versions
        self.version = Bible.NIV
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
        self.update_chapter()

        # chapter Combo
        self.comboChapter = self.findChild(QtWidgets.QComboBox, 'comboChapter')
        print (self.comboChapter.currentIndex())
        # self.comboChapter.currentIndexChanged.connect(self.update_verse)
        self.comboChapter.activated.connect(self.update_verse)
        # self.comboChapter.activated.connect(self.navigation_update)
            # wouldn't work on Index Change???
        
        # verse combo
        self.comboVerse = self.findChild(QtWidgets.QComboBox, 'comboVerse')
        self.comboVerse.activated.connect(self.single_verse)

        # Display
        self.display = self.findChild(QtWidgets.QTextBrowser, 'display')
        self.display.moveCursor(QtGui.QTextCursor.Start)
        self.address = self.findChild(QtWidgets.QLabel, 'address')

        #-------------This section needs work---------------------#
        # # Navigation Buttons -- 
        self.next_button = self.findChild(QtWidgets.QPushButton, 'next')
        self.next_button.setEnabled(False)
        # # self.next_button.clicked.connect(self.navigation_update)
        # self.next_button.clicked.connect(self.next_item)
        self.previous_button = self.findChild(QtWidgets.QPushButton, 'previous')
        self.previous_button.setEnabled(False)
        # self.previous_button.clicked.connect(self.previous_item)
        # # self.comboChapter.currentIndexChanged.connect(self.navigation_update)
        # self.navigation_update()
        
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
        self.comboChapter.setCurrentIndex(0)
        self.update_verse()
        # self.update_display()


    def update_verse(self):
        '''updates with verse combobox'''
        self.comboVerse.clear()
        verseNums = (Bible(self.version, self.comboBook.currentText(),
                           self.comboChapter.currentIndex()+1).verseTotal)
        if self.comboChapter.currentIndex()+1 < 1:    
            self.comboChapter.setCurrentIndex(1)
        for v in range(1, verseNums +1):
            self.comboVerse.addItem(f'{v}')

        self.comboVerse.setCurrentIndex(-1)
        self.update_display()


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


    def single_verse(self):
        ''' Updates display when verse is selected to just have one verse displayed. '''
        self.display.clear()
        self.address.clear()
        text = (Bible(self.version, self.comboBook.currentText(), self.comboChapter
                      .currentIndex()+1).singleVerse(self.comboVerse.currentIndex()+1))
        self.display.append(text)
        self.address.setText(f'-~ {self.comboBook.currentText()} '
                             f'{self.comboChapter.currentIndex()+1}:'
                             f'{self.comboVerse.currentIndex()+1} '
                             f'({Bible(self.version, "John", 1).getVersion()}) ~-')


    def version_update(self):
        '''
        Updates Text based on version selected.
        TO DO: Make versions capable of parallel display.
        '''
        if self.nkjv.isChecked() is True:
            self.version = Bible.NKJV
        elif self.esv.isChecked() is True:
            self.version = Bible.ESV
        elif self.niv.isChecked() is True:
            self.version = Bible.NIV
        else:
            self.version = Bible.NIV

        if self.comboVerse.currentIndex() != -1:
            self.single_verse()
        else:
            self.update_display()


# ----------------This Section needs work!---------------------#
    # def next_item(self):
    #     '''On Button click, this changes the the combobox position of the chapter.
    #        to "next" chapter
    #     '''
    #     print ("next clicked")


    # def previous_item(self): # 
    #     '''On Button click, this changes the the combobox position of the chapter.
    #        to "previous" chapter
    #     '''
    #     print ("Previous Clicked" + f"{self.comboChapter.currentIndex()}")
    #     if self.comboChapter.currentIndex() > 0:
    #         indx = self.comboChapter.currentIndex()-1
    #     else:
    #         indx = self.comboChapter.currentIndex()
    #     self.comboChapter.setCurrentIndex(indx)


    # def navigation_update(self):
    #     ''' sets parameters on the buttons to activate and deactivate
    #     when index reaches limit'''
    #     if self.comboChapter.currentIndex()+1 != int(Bible(self.version, self.comboBook.currentText(), 
    #                                             self.comboChapter.currentIndex()+1).chapterTotal):
    #         self.next_button.setEnabled(True)
    #     else:
    #         self.next_button.setEnabled(False)
        
    #     if self.comboChapter.currentIndex() <= 0:
    #         self.previous_button.setEnabled(False)
    #     else:
    #         self.previous_button.setEnabled(True) 

    # def search(self):
    #     '''Need to create a function in bible app class to search through scripture for certain phrases
    #     then connect link a search bar to this.'''
    #     pass
#------------------------------------------------------------------


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = Ui() # Create an instance of our class
    app.exec_() # Start the applications



# Todo: 
# Create a notes secton that auto saves as a texteditor for each passage that. Each 
# chapter that open has a notes tab the can be opened to with any notes previously 
# saved in it!
# Fix the navigation buttons
# Finish the search function.