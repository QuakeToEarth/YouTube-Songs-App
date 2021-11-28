from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pywhatkit


def listenToSong():
    song = song_text.get()
    pywhatkit.playonyt(song)


root = Tk()
root.title('YouTube')
root.geometry('500x300')

bg = ImageTk.PhotoImage(file='Aesthetic Moon - 2.jpg')
bgI = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

song_label = Label(root, text='Enter song name :', font=('Times 20 Bold', 20))
song_label.place(x=200, y=5)

song_text = StringVar()
song_entry = Entry(root, textvariable=song_text, bg='lightGrey')
song_entry.place(x=200, y=50)

button = Button(root, text='Listen to Song', width=12, command=listenToSong)
button.place(x=200, y=80)

root.mainloop()
