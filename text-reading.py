import os
import io
from gtts import gTTS
from playsound import playsound
f = io.open(r'''C:\Users\ACER\Desktop\pythonprojects\malayalam reading\novel.txt''',encoding='utf-8')
book_content = f.read()
ob = gTTS(book_content,lang='ml')
ob.save("novel.mp3")
playsound("novel.mp3")
os.remove("novel.mp3")
f.close()