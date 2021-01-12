import pyttsx3
import PyPDF2
#import os

# book = open('api.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages
# print(pages)
engine = pyttsx3.init('sapi5')

# for num in range(6, pages):
#     page = pdfReader.getPage(6)
#     text = page.extractText()
#     engine.say(text)
#     engine.runAndWait()

# engine.say('Hello World')
# engine.runAndWait()
# engine.say('isnt this cool')
# engine.runAndWait()
engine.say('Pretty cool, a')
engine.runAndWait()
#print(1)

# cwd = os.getcwd()
# files = os.listdir(cwd)
# print('Files in %r: %s' %(cwd, files))

exit()
