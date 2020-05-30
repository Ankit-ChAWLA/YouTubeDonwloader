import pafy
from tkinter import *

url = 'https://www.youtube.com/watch?v=tPEE9ZwTmy0'

root= Tk()
root.geometry('300x300')

def mycb(total, recvd, ratio, rate, eta):
  prcnt = ratio
  l = Label(root, text = ratio )
  l.place(x =10 , y=210 )
  

def audioonly(event):
  url = e.get()
  video = pafy.new(url) 
  best = video.getbestaudio()  
  best.download(quiet=True, callback=mycb) 
  print(video.author)

def AVBoth(event):
  url = e.get()
  video = pafy.new(url) 
  best = video.getbest()  
  best.download(quiet=True, callback=mycb) 
  print(video.author)



l = Label(root, text = "Welcome to YouTube Donwloader !! " , font = ('Helvetica', 13, 'bold'))
l.place(x =10 , y=30 )

entry1Var = StringVar(value='Delete & enter video link')
e = Entry(root, borderwidth = 3, textvariable=entry1Var , font=(5))
e.place(x = 35, y= 115)

b = Button(root,text='Download Video', bg = 'yellow' , command = AVBoth)
b.place(x =100 , y=150 )
b.bind('<Button-1>' , AVBoth)

b2 = Button(root,text='Download Audio Only', bg = 'SeaGreen1' ,command = audioonly )
b2.place(x =85 , y=180 )
b2.bind('<Button-1>' , audioonly)


root.mainloop()


