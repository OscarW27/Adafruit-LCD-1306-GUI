import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import main as main

import subprocess

import tkinter


def startscript():
    text = entry.get("1.0",'end-1c')
    RST = None

    dc = 23
    SPI_PORT = 0 
    SPI_DEVICE = 0

    disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

    disp.begin()
    disp.clear()
    disp.display()

    width = disp.width
    height = disp.height

    image = Image.new('1' , (width, height))

    draw = ImageDraw.Draw(image)

    draw.rectangle((1,1,width,height), outline=0, fill=0)
    padding = -2
    top = padding
    bottom = height-padding

    x = 0
    font = ImageFont.load_default()

    while True:
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        draw.text((x,top+8), text , font=font, fill=255)

        disp.image(image)
        disp.display()
        time.sleep(.1)


window = tkinter.Tk()

## window and bg settings
window.geometry("330x200")
window.configure(bg='#848C8E')
window.title("Adafruit LCD text printer")
window.iconbitmap(default='raspberryicon.ico')

## start the window
text = tkinter.Label(window, text="Type the text for the LCD underneath", font="Ariel 14", bg="#848C8E")    
entry = tkinter.Text(window, width=30, height=4, font="Ariel 12")
button = tkinter.Button(window, text="Send", bd=4, width=10, command= startscript)
text.grid(row=0, column=0, pady=10)
entry.grid(row=1, column=0, pady=10)
button.grid(row=2, column=0, pady=10)

window.mainloop()