import xml.etree.ElementTree as ET
bible = ET.parse("NIV.xml").getroot()

# Creates the dictionary with <Book>:<Books Parsed Element>#
titleElement = [b for b in bible.findall('b')]
title=[b.get('n') for b in bible.findall('b')]
book = dict(zip(title, titleElement))


# ___________________BIBLE SEARCH:_______________________#
def chapterSearch(name, chapter):
    '''Allows you to see whole text of a single chapter of the bible.'''
    nameChoice = str(name)
    chapterChoice = str(chapter)
    bookOfChoice = book[nameChoice]
    chapterElements = bookOfChoice.findall('c')
    chapterList = [c.get('n') for c in chapterElements]
    chaptersToChooseFrom = dict(zip(chapterList, chapterElements))
    chapterOfChoice = chaptersToChooseFrom[chapterChoice]
    verseElement = [v for v in chapterOfChoice.findall('v')]
    print ("\n-~|" + bookOfChoice.get('n') + " " + chapterOfChoice.get('n') + "|~-\n")
    textList = []
    for v in verseElement:
        text = v.get('n') + "| " + v.text +"\n"
        textList.append(text)
    return textList


def chapterQuantity(name):
    '''Get the chapters that are availble in a user selected book'''
    chNum = len(book[name].findall('c'))
    return chNum


def verseQuantity():
    '''Get the number of verses to pick from in user selected chapter.'''
    vNum = len(chapterSearch(name, chapter))
    return vNum


def textFormat():
    textList = chapterSearch(name, chapter)
    for t in textList:
        formattedText = print (t)
    return formattedText


def getBook():
    for t in title:
        bookList = print (t)
    name = str(input(f"Here is a list of all of the books: {bookList}\nWhat Book Would you like to Read? >> "))
    if name in book:
        return name
    else:
        print ("Invalid book")
        getBook()


def getChapter(name): #still need to work out bugs on validation
    num = chapterQuantity(name)
    chapter = input(f"There are {num} chapters in that book...\n"
                "What chapter would you like to read? >> ")
    return chapter


# def getVerse(name, chapter):
#     fullChapter = chapterSearch(name, chapter)
#     verseInput = print(input(f'There are {verseQuantity()} verses in {name} {chapter}'))
#     pass


# ___________________USER INPUT____________________#
# Asks for user input to search a particular chapter of the bible
name = getBook()
chapter = getChapter(name)


#  Testing Purpose!!!
# name = "John"
# chapter = "14"


#__________________EXECUTION:_________________#
# getVerse(name, chapter)
# print(chapterSearch(name, chapter))
# getVerse()
# verseQuantity()
# chapterQuantity(name)
textFormat()


# ___________________TO DO:_______________________#
# - Create function that checks to see if user input is accurate.
# - Create a feature that allows to do specific word or phrase searches.
# - Create a way to search specific verse via address book - chapter: verse/
#   sections of verses.
#   Create a way to log what user has read and save progress.
# - Create an Optional GUI that allows.

