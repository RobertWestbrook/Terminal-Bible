# Terminal-Bible
 Python based Bible that can be viewed in the Terminal **OR** the optional GUI.

## Install 
Just download the file and directory in terminal:
`python Bible.py` This program was designed with Python 3.8.2 and therefore should be run in this version or later. I cannot guarantee full functionality in earlier versions.

## Instructions
When run in terminal make sure that you enter a valid bible book and chapter and the text of the chapter should be displayed. If invalid input you will recieve an error and will need to rerun. 

### To Run GUI Version:
`cd` to the `Terminal-Bible` directory and run:
`python main.py`

### Example:
In terminal: 
`cd` to the file directory `Terminal-Bible`.
Open Python Shell and import the following:
`from Bible import Bible`
For searches you can use the following format:
`Bible(<version>, <book>, <chapter>).readChapter()`
`Bible(NIV, "John", 15).readChapter()`

*Current bible versions available are*
- **NIV**(New International Version), 
- **ESV**(English Standard Version), 
- **NKJV**(New King James Version)

*This should display the chapter, if done correctly, directly in your terminal.*



## Known Issues
This is still in its very beginning beta stage so it here are the following known issues:
* Input must be accurate - capitalization and all with no trailing spaces, else user will recieve an error and will need to rerun.
* Cannot search anything but **book** and **chapter**. 

## TO DO
- Create function that checks to see if user input is accurate.
- Create a feature that allows to do specific word or phrase searches.
- Create a way to search specific verse via address book - chapter: verse/
  sections of verses.
  Create a way to log what user has read and save progress.