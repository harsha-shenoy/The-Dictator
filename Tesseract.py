import cv2
import pytesseract as tes
tes.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import PyPDF2
from win32com.client import Dispatch
import time

def PdfToBeRead(PdfFile):
    pdf = open(PdfFile,'rb')
    try:
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        pdf_n_pages = pdf_reader.numPages
        file = open(r'E:\PyCharmProjects\Try\text.txt','w')
        for page in range(pdf_n_pages):
            page_select = pdf_reader.getPage(page)
            text = page_select.extractText()
            file.write(text)
        file.close()
        pdf.close()
    except Exception:
        speak('Unknown Characters found')
    file = open(r'E:\PyCharmProjects\Try\text.txt', 'r')
    ret_text = file.read()
    return ret_text


def speak(text):
    speak = Dispatch("SAPI.SPVoice")
    speak.Speak(text)


def ImageToBeRead(image):
    String = tes.image_to_string(Image.open(image),lang='eng')
    return String

def start():
    print("Welcome to THE DICTATOR!")
    speak("Welcome to THE DICTATOR!")
    time.sleep(0.25)
    print('Press ESC to exit')
    speak('Press ESC to exit')
    k = cv2.waitKey(1) &  0xFF
    while(True):
        speak("Enter the file to be read")
        File = input("Enter the file to be read\n")
        if k == 27:
            pass
        else:
            try:
                if File.endswith('.pdf'):
                    pdfread = PdfToBeRead(File)
                    print(pdfread)
                    speak(pdfread)
                elif File.endswith('.jpg') or File.endswith('.png'):
                    imageread = ImageToBeRead(File)
                    print(imageread)
                    speak(imageread)
                elif File.endswith('.txt'):
                    with open(File,'r') as FileRead:
                        for line in FileRead:
                            speak(line)
                else:
                    speak('Unknown File')

            except FileNotFoundError:
                speak('File Does not exist...PLease Check Again...Sorry')

if __name__ == '__main__':
    start()
