import tkinter as tk
import tkinter.font as font
from find_motion import *
from threading import Thread
import smtplib
from email.message import EmailMessage
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
import time
from PIL import Image, ImageTk


def email_send(fileNameInput):
    print(fileNameInput)
    inputFile = 'C:\\Users\\adith\\OneDrive\\Documents\\PES\\Hackathons\\Tri-NIT\\stolen\\stoleVideo.mp4'

    print(inputFile)
    msg = EmailMessage()
    msg['Subject'] = 'Check out Bronx as a puppy'
    msg['From'] = 'testboss699@gmail.com'
    msg['To'] = 'adithyaskolavi@gmail.com'
    msg.set_content("Video attachment-----")

    with open(inputFile, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    
    msg.add_attachment(file_data,maintype = "application", subtype="octet-stream",filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login('testboss699@gmail.com','Aaryan$2003')
        smtp.send_message(msg)

def mainFunction():
    find_motion()
    time.sleep(2)
    email_send('stolenVideo.mp4')

# window =  tk.Tk()
# window.title = "find stolen"
# window.geometry("500x300")


# #label
# label = tk.Label(window, text="Welcome")
# label.grid(row=0, column=1)
# label['font'] = font.Font(size=35, weight='bold',family='Helvetica')

# #button font
# btn_font = font.Font(size=15, weight='bold',family='Helvetica')

# #button main
# button1 = tk.Button(window, text="spot diff",fg="green", height=3, width=10, command=mainFunction)
# button1['font'] = btn_font
# button1.grid(row=1, pady=(25,10),padx=(10,0), column = 0)




# #footer
# label2 = tk.Label(window, text="thanks for using")
# label2.grid(row=2, columnspan = 3)
# label2['font'] = font.Font(size=20, weight='bold',family='Helvetica')
root = tk.Tk(className='Main MENU')
root.geometry("620x1000")
root.minsize(620,1000)
root.maxsize(620,1000)

introFrame = tk.Frame(root, bg= "#F5F7FD" )
introFrame.place(height=1000, width=630, x=0, y=0)

# window.mainloop()
landingImage = (Image.open("Assets\image 2.png"))
landingImage = landingImage.resize((630,660), Image.ANTIALIAS)
landingImage = ImageTk.PhotoImage(landingImage)
label = Label(introFrame, image = landingImage)
label.place(x=int(-10), y=(0))

signupImage = Image.open("Assets\image 3.png")
signupImage = signupImage.resize((339,114), Image.ANTIALIAS)
signupImage = ImageTk.PhotoImage(signupImage)
startButton = Button(introFrame,image = signupImage ,bg='#F5F7FD',command = mainFunction ,borderwidth = 0)
startButton.place(x=141.15, y=707)

startimage = Image.open("Assets\image 4.png")
startimage = startimage.resize((339,114), Image.ANTIALIAS)
startimage = ImageTk.PhotoImage(startimage)
startButton = Button(introFrame,image = startimage ,bg='#F5F7FD',command = mainFunction ,borderwidth = 0)
startButton.place(x=140 ,y=827)

root.mainloop()