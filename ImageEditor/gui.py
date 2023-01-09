import tkinter
import customtkinter as ctk
from PIL import Image, ImageEnhance, ImageFilter
from imageEditor import imageEditor
import os

class photoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Photo Enhancer")
        self.geometry("1024x700")

        #grid layout (2 rows x 1 column)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.fileFrame = ctk.CTkFrame(self, corner_radius=0)
        self.fileFrame.grid(row=0, column=0, sticky="nsew")
        self.fileFrame.grid_columnconfigure(4, weight=1)

        self.fileLabel = ctk.CTkLabel(self.fileFrame, text="File: ",compound="left",
                                                font=ctk.CTkFont(size=15, weight="bold"))

        self.fileLabel.grid(row=0, column=0, padx=5, pady=10)

        self.filePathLabel = ctk.CTkLabel(self.fileFrame, text="Select a picture...",compound="left",
                                                font=ctk.CTkFont(size=15))

        self.filePathLabel.grid(row=0, column=1, padx=5, pady=10)

        self.fileButton = ctk.CTkButton(self.fileFrame, corner_radius=10, height=40, border_spacing=10, text="Select...",
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.selectImageFile)

        self.fileButton.grid(row=0, column=2, sticky="nw", padx=5, pady=10)

        self.fileSaveButton = ctk.CTkButton(self.fileFrame, corner_radius=10, height=40, border_spacing=10,
                                        text="Save...",
                                        hover_color=("gray70", "gray30"),
                                        anchor="w", command=self.saveImageFile)

        self.fileSaveButton.grid(row=0, column=3, sticky="nw", padx=5, pady=10)

        #image frame
        self.imageFrame = ctk.CTkFrame(self, corner_radius=0)
        self.imageFrame.grid(row=1, column=0, sticky="nsew")
        self.imageFrame.grid_rowconfigure(1, weight=1)
        self.imageFrame.grid_columnconfigure(0, weight=1)

        self.editor = imageEditor()
        self.editor.setImageFile("./resources/matrix-4.jpg")
        picture = ctk.CTkImage(self.editor.getImage(), size=self.editor.getImageSize((800, 600)))
        self.imageLabel = ctk.CTkLabel(self.imageFrame, text="", image=picture)
        self.imageLabel.grid(row=0, column=0, sticky="nsew", padx=10, pady=20)

        self.controlsFrame = ctk.CTkFrame(self.imageFrame, corner_radius=0)
        self.controlsFrame.grid(row=0, column=1, sticky="nsew")
        self.controlsFrame.grid_rowconfigure(1, weight=1)
        self.controlsFrame.grid_columnconfigure(3, weight=1)

        self.controlsButtonFrame = ctk.CTkFrame(self.controlsFrame, corner_radius=0)
        self.controlsButtonFrame.grid(row=0, column=0, sticky="nsew")
        self.controlsButtonFrame.grid_rowconfigure(1, weight=1)
        self.controlsButtonFrame.grid_columnconfigure(2, weight=1)

        self.autoButton = ctk.CTkButton(self.controlsButtonFrame, corner_radius=10, height=40, border_spacing=10,
                                         text="Auto",
                                         hover_color=("gray70", "gray30"),
                                         anchor="w", command=self.autoEnhanceImage)

        self.autoButton.grid(row=0, column=0, sticky="nw", padx=5, pady=10)

        self.resetButton = ctk.CTkButton(self.controlsButtonFrame, corner_radius=10, height=40, border_spacing=10, text="Reset",
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.resetImage)

        self.resetButton.grid(row=0, column=1, sticky="nw",padx=5, pady=10)

        self.controlsInnerFrame = ctk.CTkFrame(self.controlsFrame, corner_radius=0)
        self.controlsInnerFrame.grid(row=1, column=0, sticky="nsew")
        self.controlsInnerFrame.grid_rowconfigure(4, weight=1)
        self.controlsInnerFrame.grid_columnconfigure(4, weight=1)

        self.sharpLabel = ctk.CTkLabel(self.controlsInnerFrame, text="Sharpen: ", compound="left",
                                                font=ctk.CTkFont(size=15))
        self.sharpLabel.grid(row=1, column=0, padx=0, pady=5, sticky="nw")

        imgUp = Image.open('up.png')
        imgDown = Image.open('down.png')
        self.upImage = ctk.CTkImage(imgUp, size=(24, 24))
        self.downImage = ctk.CTkImage(imgDown, size=(24, 24))
        self.sharpUp = ctk.CTkButton(self.controlsInnerFrame, image=self.upImage, text="", fg_color="transparent",
                                     hover_color=("gray70", "gray30"), anchor="w", command=self.sharpenUp)
        self.sharpUp.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.sharpDown = ctk.CTkButton(self.controlsInnerFrame, image=self.downImage, text="", fg_color="transparent",
                                     hover_color=("gray70", "gray30"), anchor="w", command=self.sharpenDown)
        self.sharpDown.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.brightLabel = ctk.CTkLabel(self.controlsInnerFrame, text="Brightness: ", compound="left",
                                          font=ctk.CTkFont(size=15))
        self.brightLabel.grid(row=2, column=0, padx=0, pady=5, sticky="nw")

        self.brightUp = ctk.CTkButton(self.controlsInnerFrame, image=self.upImage, text="", fg_color="transparent",
                                     hover_color=("gray70", "gray30"), anchor="w", command=self.brightenUp)
        self.brightUp.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.brightDown = ctk.CTkButton(self.controlsInnerFrame, image=self.downImage, text="", fg_color="transparent",
                                       hover_color=("gray70", "gray30"), anchor="w", command=self.brightenDown)
        self.brightDown.grid(row=2, column=2, padx=5, pady=5, sticky="w")

        self.contrastLabel = ctk.CTkLabel(self.controlsInnerFrame, text="Contrast: ", compound="left",
                                       font=ctk.CTkFont(size=15))
        self.contrastLabel.grid(row=3, column=0, padx=0, pady=5, sticky="nw")

        self.contrastUp = ctk.CTkButton(self.controlsInnerFrame, image=self.upImage, text="", fg_color="transparent",
                                      hover_color=("gray70", "gray30"), anchor="w", command=self.constUp)
        self.contrastUp.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.contrastDown = ctk.CTkButton(self.controlsInnerFrame, image=self.downImage, text="", fg_color="transparent",
                                        hover_color=("gray70", "gray30"), anchor="w", command=self.constDown)
        self.contrastDown.grid(row=3, column=2, padx=5, pady=5, sticky="w")



    def updateImage(self):
        picture = ctk.CTkImage(self.editor.getImage(), size=self.editor.getImageSize((800, 600)))
        self.imageLabel.configure(image=picture)

    def saveImageFile(self):
        dirPath = tkinter.filedialog.askdirectory()
        self.editor.saveImage(dirPath)

    def selectImageFile(self):
        print("open file selection...")
        filename = tkinter.filedialog.askopenfilename(title="Select a Picture",
                                              filetypes=(("JPG files", "*.jpg"),
                                                         ("PNG files", "*.png"),
                                                         ("JPEG files", "*.jpeg"),
                                                         ("WEBP files", "*.webp"),
                                                         ("all files", "*.*")))
        print(filename)
        self.editor.setImageFile(filename)
        self.updateImage()
        self.filePathLabel.configure(text=filename)

    def resetImage(self):
        self.editor.reset()
        self.updateImage()

    def autoEnhanceImage(self):
        self.editor.autoEnhance()
        self.updateImage()

    def sharpenUp(self):
        self.editor.editSharpness(1.1)
        self.updateImage()

    def sharpenDown(self):
        self.editor.editSharpness(0.9)
        self.updateImage()

    def constUp(self):
        self.editor.editContrast(1.1)
        self.updateImage()

    def constDown(self):
        self.editor.editContrast(0.9)
        self.updateImage()

    def brightenUp(self):
        self.editor.editBrightness(1.1)
        self.updateImage()

    def brightenDown(self):
        self.editor.editBrightness(0.9)
        self.updateImage()

if __name__ == "__main__":
    app = photoApp()
    app.mainloop()