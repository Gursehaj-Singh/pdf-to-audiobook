from PyPDF2 import PdfReader
from gtts import gTTS
import os

filename = "file_to_convert.pdf"
reader = PdfReader(filename)
page = reader.pages[0]
text = page.extract_text()

my_text = text
my_language = "en"

file = gTTS(text=my_text, lang=my_language, slow=False)

file.save("newaudiofile.mp3")
os.system("newaudiofile.mp3")
