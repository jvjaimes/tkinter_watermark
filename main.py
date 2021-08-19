from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageTk

''' Version: j21.08.00001
    Create by: jose V. Jaimes.
    Date: Aug 17, 2021
    GUI application to upload a image an add a watermark
    then save it with the following format nam_watermark.ext, 
    then it will open another  screen with the file watermarked in the right low corner'''

def open_image(image):
    root = tk.Toplevel()
    img = Image.open(image)
    w, h = img.size
    w = int(w / 6)
    h = int(h / 6)
    print(w, h)
    img = img.resize((w, h))
    tkimage = ImageTk.PhotoImage(img)
    tk.Label(root, image=tkimage).grid()
    root.mainloop()


def addwatermark(file,newfile):
    photo = Image.open(file)
    # Store image width and height
    w, h = photo.size
    print(w, h)
    # make the image editable
    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype("Roboto-Black.ttf", 68)
    # get text width and height
    text = "© Jose V. Jaimes."
    text_w, text_h = drawing.textsize(text, font)
    position_watermark = w - text_w, (h - text_h) - 50
    w = int(w / 6)
    h = int(h / 6)
    print(w, h)
    c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
    drawing = ImageDraw.Draw(c_text)
    drawing.text((0,0), text, fill="#ffffff", font=font)
    c_text.putalpha(100)
    photo.paste(c_text, position_watermark, c_text)
    photo.save(newfile)
    open_image(newfile)

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    filename_list = filename.split('/')[-1:][0].split('.')
    new_filename = filename_list[0] + '_watermark.' + filename_list[1]
    print(new_filename)
    addwatermark(filename,new_filename)




ws = Tk()
ws.title('Watermark image')
ws.geometry('200x200')
ws.config(padx=20, pady=20, bg="white")
Lebel1 = Label(ws,  text='Choose a jpg image ')
Lebel1.grid(row=0, column=0, padx=10)
upld = Button(ws, text='Upload File', command=UploadAction)
upld.grid(row=3, columnspan=3, pady=10)
ws.mainloop()