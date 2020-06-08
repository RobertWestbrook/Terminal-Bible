from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QComboBox
import xml.etree.ElementTree as ET

class Bible:
    '''Allows to search the entire bible and utilize elements for personal research.
    call using: Bible("name_of_Book", chapter#_in_book)
    .title - gets the title of the book you searched.
    .chapter - gets chapter searched
    .chapterNums - gets a list of the chapter numbers in the book.
    .chapterElem - gets the raw chapter element parsed from XML tree.
    .chContents - dictionary of {chapter Numbers : chapter Elements}
    .verseNums - returns list of verses in selected chapter.
    .verseText - returns all of the text for the chapter as a list.
    .verseContent - this is a dictionary of {verse# : verse text} 
                    verses can be called using the keys of this dict.
    .bookElem - gets a list of element from each book
    .bookNames - returns a list of all book names in bible.
    .contents - is dictionary of {book name : book element}
    .readChapter() - prints a fromatted full text display of selected
                    book chapter. 
    .singleVerse(<verse_num>) - returns a single verse.
    '''

    # ____inital Parsing from and main dictionary setup_____#
    bible = ET.parse("NIV.xml").getroot()
    bookElem = [b for b in bible.findall('b')]
    bookNames = [t.get('n') for t in bible.findall('b')]
    contents = dict(zip(bookNames, bookElem)) 


    # ____traits and methods_____#
    def __init__(self, title, chapter):
        '''This is where the address is passed in the args.
            to be run as Bible("John", 15).'''
        self.title = title
        self.chapter = chapter
        self.chapterNums = [int(c.get('n')) for c in Bible.contents[title]]
        self.chapterElem = [c for c in Bible.contents[title]]
        self.chContents = dict(zip(self.chapterNums, self.chapterElem))
        self.verseNums = [int(v.get('n')) for v in self.chContents[chapter]]
        self.verseText = [v.text for v in self.chContents[chapter]]
        self.verseContent = dict(zip(self.verseNums, self.verseText))
        

    def singleVerse(self, verse):
        '''returns a single verse'''
        v = f"{verse}: {self.verseContent[verse]}"
        return v 


    def readChapter(self):
        '''Basic search that outputs the entire chapter at once.'''
        print (f"\n--<| {self.title}:{self.chapter} |>--\n")
        for i in self.verseContent:
            print (f"{i}) {self.verseContent[i]}")

    
# def callGui():
#     '''Just runs GUI to for the app.'''
#     Form, Window = uic.loadUiType("Terminal Bible.ui")
#     app = QApplication([])
#     window = Window()
#     form = Form()
#     form.setupUi(window)
#     window.show()
#     app.exec_()

#     combo = QComboBox()
#     combo.addItem("Apple")
#     combo.addItem("Pear")
#     combo.addItem("Lemon")


# if __name__ == '__main__':
#     callGui()