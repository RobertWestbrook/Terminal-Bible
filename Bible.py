import xml.etree.ElementTree as ET

NIV = "assets/bible-versions/NIV.xml"
ESV = "assets/bible-versions/ESV.xml"
NKJV = "assets/bible-versions/NKJV.xml"

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

    # ---------------------- init ------------------------#

    def __init__(self, version= NIV, title="Genesis", chapter=1):
        '''This is where the address is passed in the args.
            to be run as Bible(NIV,"John", 15).'''

        self.bible = ET.parse(version).getroot()
        self.bookElem = [b for b in self.bible.findall('b')]
        self.bookNames = [t.get('n') for t in self.bible.findall('b')]
        self.contents = dict(zip(self.bookNames, self.bookElem))
        self.title = title
        self.chapter = chapter
        self.chapterNums = [int(c.get('n')) for c in self.contents[title]]
        self.chapterTotal = len(self.chapterNums)
        self.chapterElem = [c for c in self.contents[title]]
        self.chContents = dict(zip(self.chapterNums, self.chapterElem))
        self.verseNums = [int(v.get('n')) for v in self.chContents[chapter]]
        self.verseTotal = len(self.verseNums)
        self.verseText = [v.text for v in self.chContents[chapter]]
        self.verseContent = dict(zip(self.verseNums, self.verseText))

    # ---------------------- Functionality ------------------------#

    def getVersion(self):
        return self.bible.get('n')

    def singleVerse(self, verse):
        '''returns a single verse'''
        v = f"{verse}: {self.verseContent[verse]}"
        return v

    def readChapter(self):
        '''Basic search that returns the entire chapter at once.'''
        text = []
        for i in self.verseContent:
            text.append(f"{i}. {self.verseContent[i]}")
        wholeText = "\n".join(text)
        return wholeText

    def printChapter(self):
        '''Basic search that prints out the entire chapter at once.'''
        print(f"\n--<| {self.title}:{self.chapter} |>--\n")
        text = []
        for i in self.verseContent:
            text.append(f"{i}. {self.verseContent[i]}")
        wholeText = "\n".join(text)
        print(wholeText)

