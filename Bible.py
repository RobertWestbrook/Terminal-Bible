import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import StringProperty
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
    print ("-~|" + bookOfChoice.get('n') + " " + chapterOfChoice.get('n') + "|~-")
    textList = []
    for v in verseElement:
        text = v.get('n') + "| " + v.text
        textList.append(text)
    return '\n'.join(textList)


# ___________________USER INPUT____________________#
# Asks for user input to search a particular chapter of the bible
# name = str(input("What Book >> ")) 
# chapter = str(input("What chapter >> "))

#  Testing Purpose!!!
# name = "John"
# chapter = "14"

# ___________________GUI____________________#

class BibleUI(App):
    address =StringProperty("\n-~|" + "name" + " " + "chapter" + "|~-\n")
    read = StringProperty(chapterSearch("John", "14"))

#__________________EXECUTION:_________________#
# print (chapterSearch(name, chapter))
if __name__ == '__main__':
    BibleUI().run()

# ___________________TO DO:_______________________#
# - Create function that checks to see if user input is accurate.
# - Create a feature that allows to do specific word or phrase searches.
# - Create a way to search specific verse via address book - chapter: verse/
#   sections of verses.
#   Create a way to log what user has read and save progress.
# - Create an Optional GUI that allows 

