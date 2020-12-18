from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size = 0
"""""
def progress_Check(stream=0, chunk=0, remaining=None):
    file_downloaded=(file_size - remaining)
    percent = (file_downloaded/file_size)*100
    dBtn.config(text ="{} % Downloaded".format(percent))
"""""

#Video Download
def startDownload():
    global file_size
    try:
        url =urlField.get()
        # changing button text
        dBtn.config(text="Please wait...")
        dBtn.config(state=DISABLED)

        path_to_save_video = askdirectory()

        if path_to_save_video is None:
            return

        else:
            # Creating youtube object with url
            obj = YouTube(url)



            strm = obj.streams.first()

            file_size=strm.filesize

            strm.download(path_to_save_video)
            print("done")
            dBtn.config(text="Start Download")
            dBtn.config(state=NORMAL)
            showinfo("Download finished", "Download successfully")
            urlField.delete(0,END)



    except Exception as e:
        print(e)
        print("error !")


#Audio Download
def startAudioDownload():
    global file_size
    try:
        url =urlField.get()
        # changing button text
        adBtn.config(text="Please wait...")
        adBtn.config(state=DISABLED)

        path_to_save_video = askdirectory()

        if path_to_save_video is None:
            return

        else:
            # Creating youtube object with url
            obj = YouTube(url)

            audioStream = obj.streams.filter(type = "audio")

            audioStream.first().download(path_to_save_video)
            print("done")
            adBtn.config(text="Start Download")
            adBtn.config(state=NORMAL)
            showinfo("Download finished", "Download successfully")
            urlField.delete(0,END)



    except Exception as e:
        print(e)
        print("error !")




def startDownloadThread():
    thread=Thread(target=startDownload)
    thread.start()


def startAudioDownloadThread():
    thread=Thread(target=startAudioDownload)
    thread.start()




# GUI development
main = Tk()

main.title("Youtube Downloader")

main.iconbitmap('res/icon.ico')
main.geometry("500x600")

# heading icon
file = PhotoImage(file='res/download.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)

# Url Input
urlField =Entry(main, font=("verdana", 18), justify="center")
urlField.pack(side=TOP, fill=X, padx=10)

# Download Button
dBtn = Button(main, text="Download Video", font=("verdana", 18),relief='ridge',command=startDownloadThread)
dBtn.pack(side=TOP, pady=10)

#Audio Download Button
adBtn = Button(main, text="Download Audio", font=("verdana", 18),relief='ridge',command=startAudioDownloadThread)
adBtn.pack(side=TOP, pady=10)


main.mainloop()