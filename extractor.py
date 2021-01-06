import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))  # users/user
print(BASE_DIR)
picture = os.path.join(BASE_DIR, 'pictures/Mirabukky/id.jpg')
text_dir = os.path.join(BASE_DIR, 'pictures/img2text')

text = pytesseract.image_to_string(picture)
save = True
print(text)


def writeToFile(name):
    file_path = os.path.join(text_dir, f'{name}.txt')
    newFile = open(file_path, 'w+')
    newFile.write(text)
    newFile.close()


if save:
    print('enter new file name')
    name = input('>>>')
    if name != '':
        writeToFile(name)
    else:
        print('new file name cannot be empty')


# print(text)
