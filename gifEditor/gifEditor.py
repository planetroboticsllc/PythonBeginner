import tkinter
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image, ImageEnhance, ImageFilter, ImageSequence, ImageDraw2
import tempfile
import os

images = []
gif = None
tempDir = None
stopAnimation = False


# Function to load gif file and get all frames as images
def loadgif(gifFilePath):
    global images
    global gif
    global tempDir
    # reset old values
    images = []
    gif = None
    if tempDir:
        tempDir.cleanup()
    if not tempDir:
        tempDir = tempfile.TemporaryDirectory()

    tempDirName = tempDir.name
    print(tempDirName)

    fileName = os.path.basename(gifFilePath)
    fileName = os.path.splitext(fileName)[0]
    # print(fileName)

    gif = Image.open(gifFilePath)
    i = 0
    for frame in ImageSequence.Iterator(gif):
        i += 1
        filePath = tempDirName
        filePath = os.path.join(filePath, f"{fileName}{i}.png")
        # print(filePath)
        frame.save(filePath, lossless=True)
        img = Image.open(filePath)
        images.append(img)


def animateGIF(indx):
    global stopAnimation
    if stopAnimation:
        indx = 0
    if indx >= 0 and indx < len(images):
        img = images[indx]
        width, height = img.size
        gifImageLabel.configure(True, image=ctk.CTkImage(images[indx], size=(width, height)))
        indx += 1
    else:
        indx = 0

    if stopAnimation == False:
        app.after(30, animateGIF, indx)


def cropImages(left, top, right, bottom):
    global stopAnimation
    global images
    stopAnimation = True
    imgCopy = []
    for img in images:
        imgCopy.append(img.crop((left, top, right, bottom)))

    images = imgCopy
    img = images[0]
    width, height = img.size
    gifImageLabel.configure(True, image=ctk.CTkImage(img, size=(width, height)))

def cropLeft():
    global stopAnimation
    stopAnimation = True
    img = images[0]
    width, height = img.size
    cropImages(left=15, top=0, right=width, bottom=height)

def cropRight():
    global stopAnimation
    stopAnimation = True
    img = images[0]
    width, height = img.size
    cropImages(left=0, top=0, right=width-15, bottom=height)

def cropTop():
    global stopAnimation
    stopAnimation = True
    img = images[0]
    width, height = img.size
    cropImages(left=0, top=15, right=width, bottom=height)

def cropBottom():
    global stopAnimation
    stopAnimation = True
    img = images[0]
    width, height = img.size
    cropImages(left=0, top=0, right=width, bottom=height-15)

def brighten(factor):
    global stopAnimation
    global images
    stopAnimation = True

    imgCopy = []
    for img in images:
        img = img.convert(mode="RGB")
        imgEnhancer = ImageEnhance.Brightness(img)
        imgCopy.append(imgEnhancer.enhance(factor))

    images = imgCopy
    img = images[0]
    width, height = img.size
    gifImageLabel.configure(True, image=ctk.CTkImage(img, size=(width, height)))

def contrast(factor):
    global stopAnimation
    global images
    stopAnimation = True

    imgCopy = []
    for img in images:
        img = img.convert(mode="RGB")
        imgEnhancer = ImageEnhance.Contrast(img)
        imgCopy.append(imgEnhancer.enhance(factor))

    images = imgCopy
    img = images[0]
    width, height = img.size
    gifImageLabel.configure(True, image=ctk.CTkImage(img, size=(width, height)))

def brightenUp():
    brighten(1.1)

def brightenDown():
    brighten(0.9)

def constUp():
    contrast(1.1)

def constDown():
    contrast(0.9)

def enhanceGIF(enhancer, factor):
    ImageEnhance.Contrast(self.enhancedImage)
def stopGIF():
    global stopAnimation
    stopAnimation = True

def startGIF():
    global stopAnimation
    stopAnimation = False
    app.after(30, animateGIF, 0)

if __name__ == '__main__':
    app = ctk.CTk()
    app.geometry('1200x500')
    app.title("GIF Editor")
    icon = tkinter.PhotoImage(file='appIcon.png')
    app.iconphoto(False, icon)

    # grid layout
    app.grid_rowconfigure(0, weight=0)
    app.grid_columnconfigure(1, weight=1)

    gifFrame = ctk.CTkFrame(app, corner_radius=5)
    gifFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    gifFrame.grid_rowconfigure(0, weight=1)
    gifFrame.grid_columnconfigure(0, weight=1)

    editFrame = ctk.CTkFrame(app, corner_radius=5)
    editFrame.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
    editFrame.grid_rowconfigure(3, weight=0)
    editFrame.grid_columnconfigure(4, weight=0)

    imgUp = Image.open('up.png')
    imgDown = Image.open('down.png')
    upImage = ctk.CTkImage(imgUp, size=(24, 24))
    downImage = ctk.CTkImage(imgDown, size=(24, 24))

    loadgif("messi.gif")
    if len(images) > 1:
        img = images[0]
        width, height = img.size
        gifImageLabel = ctk.CTkLabel(gifFrame, text='', image=ctk.CTkImage(images[0], size=(width, height)))
        gifImageLabel.grid(row=0, column=0, padx=5, pady=5)

        stopAnimationBtn = ctk.CTkButton(editFrame, text='stop', hover_color=("gray70", "gray30"), anchor="w",
                                         command=stopGIF)
        stopAnimationBtn.grid(row=0, column=0, padx=5, pady=5)

        startAnimationBtn = ctk.CTkButton(editFrame, text='start', hover_color=("gray70", "gray30"), anchor="w",
                                         command=startGIF)
        startAnimationBtn.grid(row=0, column=1, padx=5, pady=5)

        cropLabel = ctk.CTkLabel(editFrame, text='Crop: ', font=ctk.CTkFont(size=15), compound="left")
        cropLabel.grid(row=1, column=0, padx=5, pady=5, sticky="nw")

        cropLeftButton = ctk.CTkButton(editFrame, text='left',
                                          hover_color=("gray70", "gray30"),
                                          anchor="w", command=cropLeft)

        cropLeftButton.grid(row=1, column=1, padx=5, pady=5, sticky="nw")

        cropRightButton = ctk.CTkButton(editFrame, text='right',
                                       hover_color=("gray70", "gray30"),
                                       anchor="w", command=cropRight)

        cropRightButton.grid(row=1, column=2, padx=5, pady=5, sticky="nw")

        cropTopButton = ctk.CTkButton(editFrame, text='top',
                                       hover_color=("gray70", "gray30"),
                                       anchor="w", command=cropTop)

        cropTopButton.grid(row=1, column=3, padx=5, pady=5, sticky="nw")

        cropBottomButton = ctk.CTkButton(editFrame, text='bottom',
                                       hover_color=("gray70", "gray30"),
                                       anchor="w", command=cropBottom)

        cropBottomButton.grid(row=1, column=4, padx=5, pady=5, sticky="nw")

        brightLabel = ctk.CTkLabel(editFrame, text="Brightness: ", compound="left",
                                        font=ctk.CTkFont(size=15))
        brightLabel.grid(row=2, column=0, padx=0, pady=5, sticky="nw")

        brightUp = ctk.CTkButton(editFrame, image=upImage, text="", fg_color="transparent",
                                      hover_color=("gray70", "gray30"), anchor="w", command=brightenUp)
        brightUp.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        brightDown = ctk.CTkButton(editFrame, image=downImage, text="", fg_color="transparent",
                                        hover_color=("gray70", "gray30"), anchor="w", command=brightenDown)
        brightDown.grid(row=2, column=2, padx=5, pady=5, sticky="w")

        contrastLabel = ctk.CTkLabel(editFrame, text="Contrast: ", compound="left",
                                          font=ctk.CTkFont(size=15))
        contrastLabel.grid(row=3, column=0, padx=0, pady=5, sticky="nw")

        contrastUp = ctk.CTkButton(editFrame, image=upImage, text="", fg_color="transparent",
                                        hover_color=("gray70", "gray30"), anchor="w", command=constUp)
        contrastUp.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        contrastDown = ctk.CTkButton(editFrame, image=downImage, text="",
                                          fg_color="transparent",
                                          hover_color=("gray70", "gray30"), anchor="w", command=constDown)
        contrastDown.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        indx = 0
        app.after(30, animateGIF, indx)
    app.mainloop()
    tempDir.cleanup()
