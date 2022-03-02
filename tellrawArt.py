from PIL import Image
import numpy
import pyperclip
from tkinter import filedialog

command = "/tellraw @a ["

print("CHOOSE A .JPEG PLS")
def rgbtohex(rgb):
    converted_hex = ""
    for colour in rgb:
        if len(hex(colour)[2::]) != 1:
            converted_hex += hex(colour)[2::].upper()
        else:
            converted_hex += "0" + hex(colour)[2::].upper()
    return converted_hex


with Image.open(filedialog.askopenfilename()) as image:
    if image.size != (20, 20):
        pic = numpy.asarray(image.resize((20,20)))
    else:
        pic = numpy.asarray(image)

for line in pic:
    for pixel in line:
        command += '{"text":"⬛","color":"#' + rgbtohex(pixel) + '"},'
    command += r'{"text":"\n"},'

pyperclip.copy(command[:-15] + "]")