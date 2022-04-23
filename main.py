import pyttsx3
from PyPDF2 import PdfFileReader

pdf = PdfFileReader("sample.pdf")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[28].id)
engine.setProperty('rate', 200)

for page in pdf.pages:
    print(page.extractText())
    engine.say(page.extractText())
    engine.runAndWait()
