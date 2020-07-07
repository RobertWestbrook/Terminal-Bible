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
    NIV = "NIV.xml"
    ESV = "ESV.xml"
    NKJV= "NKJV.xml"


    # ____traits and methods_____#
    def __init__(self, version, title, chapter):
        '''This is where the address is passed in the args.
            to be run as Bible("John", 15).'''
        # ____inital Parsing from and main dictionary setup_____#
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
        # verseElem = [v for v in self.chContents[chapter]]
        # self.verseElems = dict(zip(self.verseNums, verseElem))

    def getVersion(self):
        # print (self.bible.get('n'))
        return self.bible.get('n')


    def singleVerse(self, verse):
        '''returns a single verse'''
        v = f"{verse}: {self.verseContent[verse]}"
        return v 


    def readChapter(self):
        '''Basic search that outputs the entire chapter at once.'''
        text = []
        for i in self.verseContent:
            text.append(f"{i}. {self.verseContent[i]}")
        wholeText = "\n".join(text)
        return wholeText


    def printChapter(self):
        '''Basic search that outputs the entire chapter at once.'''
        print (f"\n--<| {self.title}:{self.chapter} |>--\n")
        text = []
        for i in self.verseContent:
            text.append(f"{i}. {self.verseContent[i]}")
        wholeText = "\n".join(text)
        print (wholeText)


# text = Bible(Bible.NIV, "John", 1).contents
# full = {}
# for b in text:
#     chapter = Bible(Bible.NIV, b, 1).chContents
#     for c in chapter:
#         verse = Bible(Bible.NIV, b, c).verseContent
#         full.update({b:{c:verse}})
# print (full['Genesis'].keys())
# # print (full['Genesis'][20])
# # print (text)