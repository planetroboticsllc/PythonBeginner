import tkinter
from tkinter import filedialog
import customtkinter as ctk
from pytube import YouTube

resolutions = []
ytSt = []

def loadVideo():
    print("load video...")
    link = urlEditor.get()
    nameLabel.configure(text='Video Name')
    viewsLabel.configure(text='(number of views)')
    authorLabel.configure(text='by author')
    if not link:
        print("Please enter link")
    else:
        try:
            print(link)
            yt = YouTube(link)
            nameLabel.configure(text=yt.title)
            viewsLabel.configure(text=f'views: {yt.views}')
            authorLabel.configure(text=f'by: {yt.author}')
            ytStreams = yt.streams.filter(type="video", mime_type="video/mp4").order_by("resolution")
            res = []
            for st in ytStreams:
                if st.resolution and ytStreams.get_by_resolution(st.resolution):
                    res.append(st.resolution)

            res = list(set(res))
            streams.configure(values=res)
            #print(yt.streams.filter(type="video", mime_type="video/mp4").get_highest_resolution())
        except:
            nameLabel.configure(text='Check if valid link')


def downloadVideo():
    filePath = filedialog.askdirectory()

    link = urlEditor.get()
    yt = YouTube(link)
    resolution = streams.get()
    yd = yt.streams.filter(type="video", mime_type="video/mp4").get_by_resolution(resolution)
    yd.download(output_path=filePath, filename_prefix=f'{resolution}_')

if __name__ == '__main__':
    app = ctk.CTk()

    app.geometry('800x300')
    app.title("Download Youtube videos")
    icon = tkinter.PhotoImage(file='./youtube.png')
    app.iconphoto(False, icon)

    #grid layout
    app.grid_rowconfigure(1, weight=1)
    app.grid_columnconfigure(0, weight=1)

    urlFrame = ctk.CTkFrame(app, corner_radius=5)
    urlFrame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    urlFrame.grid_rowconfigure(0, weight=1)
    urlFrame.grid_columnconfigure(4, weight=1)

    urlLabel = ctk.CTkLabel(urlFrame, text='Youtube link: ', compound="left",
                            font=ctk.CTkFont(size=20))
    urlLabel.grid(row=0, column=0, sticky="w", padx=5)

    urlEditor = ctk.CTkEntry(urlFrame, width=275, height=25, corner_radius=2,
                             placeholder_text="Enter YouTube link", font=ctk.CTkFont(size=20))
    urlEditor.grid(row=0, column=1, sticky="ew", padx=5)

    urlShow = ctk.CTkButton(urlFrame, text='Load', corner_radius=5, hover_color=("gray70", "gray30"),
                            command=loadVideo)

    urlShow.grid(row=0, column=2, sticky="ew", padx=5)

    tubeFrame = ctk.CTkFrame(app, corner_radius=5)
    tubeFrame.grid(row=1, column=0, sticky="ew")
    tubeFrame.grid_columnconfigure(0, weight=1)
    tubeFrame.grid_rowconfigure(2, weight=1)

    nameLabel = ctk.CTkLabel(tubeFrame, text='Video Name', font=ctk.CTkFont(size=30))
    nameLabel.grid(row=0, column=0, padx=20, pady=20)

    tubeInfoFrame = ctk.CTkFrame(tubeFrame)
    tubeInfoFrame.grid(row=1, column=0, sticky="ew")
    tubeInfoFrame.grid_rowconfigure(4, weight=0)
    tubeInfoFrame.grid_columnconfigure(0, weight=1)

    authorLabel = ctk.CTkLabel(tubeInfoFrame, text='by Author', font=ctk.CTkFont(size=15))
    authorLabel.grid(row=0, column=0, padx=10, pady=10)

    viewsLabel = ctk.CTkLabel(tubeInfoFrame, text='(number of views)', font=ctk.CTkFont(size=15))
    viewsLabel.grid(row=1, column=0, padx=10, pady=10)

    downloadFrame = ctk.CTkFrame(tubeInfoFrame, corner_radius=5)
    downloadFrame.grid(row=2, column=0, sticky="e", padx=20)
    downloadFrame.grid_rowconfigure(0, weight=1)
    downloadFrame.grid_columnconfigure(1, weight=1)

    streams = ctk.CTkOptionMenu(downloadFrame, width=200, height=25, corner_radius=5,
                                font=ctk.CTkFont(size=20), values=['360p', '720p', '1080p'])
    streams.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    videoDownload = ctk.CTkButton(downloadFrame, text='Download...', corner_radius=5, hover_color=("gray70", "gray30"),
                              command=downloadVideo)
    videoDownload.grid(row=0, column=1, padx=10, sticky="w")

    app.mainloop()





