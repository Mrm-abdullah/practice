import pyttsx3
import PyPDF2
book = open('py111.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
friend = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extract_text()
    friend.say(text)
    friend.runAndWait()