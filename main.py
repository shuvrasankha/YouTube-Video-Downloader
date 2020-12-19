from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
from tkinter import ttk
import tkinter as tk



file_size = 0
"""""
def progress_Check(chunk, file_handle, bytes_remaining):
    file_downloaded=(file_size - bytes_remaining)
    percent = (file_downloaded/file_size)*100
    dBtn.config(text ="{:00.0f} % Downloaded".format(percent))
"""""

#Video Download function
def startDownload():
    global file_size
    try:
        url =urlField.get()
        res = vQualityChoosen.get()
        print(res)
        # changing button text and State
        dBtn.config(text="Please wait...")
        dBtn.config(state=DISABLED)
        adBtn.config(state=DISABLED)

        #Get the location to save the file
        path_to_save_video = askdirectory()

        if path_to_save_video is None:
            return

        else:
            # Creating youtube object with url
            obj = YouTube(url)

            strm = obj.streams.get_by_resolution(res)
            #strm = obj.streams.first()
            # strm.on_progress=progress_Check
            file_size = strm.filesize

            #get video name and file size
            fSize.config(text="File Size : {:00.0f} MB".format(file_size/1000000))
            fSize.pack(side=TOP,pady=10)
            vTitle.config(text=strm.title)
            vTitle.pack(side=TOP, pady=20)

            #change button state
            dBtn.config(text="Downloading....")

            #Downloading the file
            strm.download(path_to_save_video)
            print("Video downloaded Successfully")

            #change button state again
            dBtn.config(text="Start Download")
            dBtn.config(state=NORMAL)
            adBtn.config(state=NORMAL)
            showinfo("Download finished", "Download successfully")
            urlField.delete(0,END)
            vTitle.pack_forget()
            fSize.pack_forget()

    except Exception as e:
        print(e)
        print("error !")
        showinfo("ERROR", "Can't Download This type")
        dBtn.config(text="Start Download")
        dBtn.config(state=NORMAL)


#Audio Download function
def startAudioDownload():

    try:
        url =urlField.get()

        # changing button text And State
        adBtn.config(text="Please wait...")
        adBtn.config(state=DISABLED)
        dBtn.config(state=DISABLED)

        #geting the location to save the file
        path_to_save_video = askdirectory()

        if path_to_save_video is None:
            return

        else:
            # Creating youtube object with url
            obj = YouTube(url)
            strm = obj.streams.first()
            audioStream = obj.streams.filter(type = "audio")

            #changeing button text and printing the title of the video
            #fSize.config(text="File Size : {:00.0f} MB".format(audio_file_size / 1000000))
            #fSize.pack(side=TOP, pady=10)
            vTitle.config(text=strm.title)
            vTitle.pack(side=TOP, pady=20)
            adBtn.config(text="Downloading....")

            #Start downloading the file
            audioStream.first().download(path_to_save_video)
            print("Audio downloaded successfully ...........")

            #Changing the button state and text
            adBtn.config(text="Start Download")
            adBtn.config(state=NORMAL)
            showinfo("Download finished", "Download successfully")
            urlField.delete(0,END)

    except Exception as e:
        print(e)
        print("error !")
        #Chenging button state and showing error
        showinfo("ERROR", "Can't Download This type")
        adBtn.config(text="Start Download")
        adBtn.config(state=NORMAL)
        dBtn.config(state=NORMAL)



#Video downloading thread
def startDownloadThread():
    thread=Thread(target=startDownload)
    thread.start()


#Audio downloading thread
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
urlLabel = Label(main,text="Pest your URL", font=("montserrat", 15))
urlLabel.pack(side=TOP,pady=10)
urlField =Entry(main, font=("verdana", 18), justify="center")
urlField.pack(side=TOP, fill=X, padx=10)

# Drop Down
vQuality=Label(main,text="Select Video Quality", font=("montserrat", 12))
vQuality.pack(side=TOP,pady=10)
n = tk.StringVar()
vQualityChoosen = ttk.Combobox(main, width = 27,  textvariable = n)
vQualityChoosen['values'] = ("360p","720p")
vQualityChoosen.pack(side=TOP, pady=10 )



#Video Download Button
dBtn = Button(main, text="Download Video", font=("verdana", 18),relief='ridge',command=startDownloadThread)
dBtn.pack(side=TOP, pady=10)

#Audio Download Button
adBtn = Button(main, text="Download Audio", font=("verdana", 18),relief='ridge',command=startAudioDownloadThread)
adBtn.pack(side=TOP, pady=10)


#video title
vTitle=Label(main,text='"Title"', font=("montserrat", 10))
#File Size
fSize=Label(main,text='"File Size"', font=("montserrat", 15))

main.mainloop()