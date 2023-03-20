from distutils.cmd import Command
import os
import shutil 
from time import strftime
from tkinter import *
from tkinter import filedialog   # This has all the code for GUIs.
import tkinter.font as font      # This lets us use different fonts.
from PIL import  ImageTk, Image
import datetime as dt

#Setting up the date and time
date = dt.datetime.now()
time = strftime('%H-%M')

#Global Variables
global load1;
global Name;

#Functions used in the UI and button functions
def center_window_on_screen():
    width = root.winfo_screenwidth()
    hieght = root.winfo_screenheight()
    root.geometry("%dx%d" % (width,hieght))

#Function used for file browser
def browseFiles ():
    path= filedialog.askopenfilename(title="Select an Image", filetype=(('image    files','*.jpg'),('all files','*.*')))
    img= Image.open(path)
    img = img.resize((200,150))
    img=ImageTk.PhotoImage(img)
    label= Label(Frame7, image= img)
    label.image= img
    label.grid(row = 1, column = 1)
    filename = os.path.splitext(path)[0]
    lbl_name = Label(Frame7, text=filename)
    lbl_name.grid(row = 0, column = 1)

def SelectDir ():
    global Path1;
    Path1 = filedialog.askdirectory(initialdir = r'C:\users', title = "Save location")
    loc_lbl = Label(Frame8, text = Path1)
    loc_lbl.grid(row = 1, column = 2)


def return_to_menu():
    Frame6.forget()
    Frame7.forget()
    Frame1.pack(fill='both', expand =1)
    center_window_on_screen()
    #root.geometry('500x400')

def change_to_Frame2():
    Frame1.forget()
    Frame6.forget()
    Frame2.pack(fill='both', expand=1)
    center_window_on_screen()
    #root.geometry('500x400')


def view_data():
    Frame1.forget()
    Frame7.pack(fill='both', expand = 1)
    center_window_on_screen()
    #root.geometry('700x600')

def change_to_capture():
    Frame2.forget()
    Frame3.pack(fill='both', expand=1)
    center_window_on_screen()
    #root.geometry('700x600')

def processing():
    Frame3.forget()
    Frame4.pack(fill='both', expand=1)
    center_window_on_screen()
    #root.geometry('500x400')


def save_file():
    Frame5.forget()
    Frame6.pack(fill='both', expand=1)
    center_window_on_screen()
    #root.geometry('500x400')
    #img = open("Placeholder.jpg")
    #save_path = "C:/Users/Berserk/Pictures/Test"
    img_name = Name.get()
    shutil.copy("Placeholder.jpg","C:/Users/Berserk/Pictures/Test/")
    os.rename("C:/Users/Berserk/Pictures/Test/Placeholder.jpg","C:/Users/Berserk/Pictures/Test/"+img_name+".jpg")
   

def recapture():
    Frame5.forget()
    Frame3.pack(fill='both', expand=1)
    center_window_on_screen()
    #root.geometry('700x600')

def settings():
    Frame1.forget()
    Frame2.forget()
    Frame3.forget()
    Frame4.forget()
    Frame5.forget()
    Frame6.forget()
    Frame7.forget()
    Frame8.pack(fill='both', expand = 1)
    center_window_on_screen()
    
def skip():
    Frame3.forget()
    Frame4.forget()
    Frame5.pack(fill='both', expand=1)
    center_window_on_screen()
    #root.geometry('500x400')

def TypeA():
    btn_A.configure(bg = "#A3CFE9")
    btn_B.configure(bg= '#D9D9D9')
    btn_C.configure(bg= '#D9D9D9')
    Name.delete(0, 'end')
    Name.insert(0,f'A_{date:%d_%b_%y}_{time}_xxx')
    center_window_on_screen()
    Frame2.pack()
    
def TypeB():
    btn_A.configure(bg = "#D9D9D9")
    btn_B.configure(bg= '#A3CFE9')
    btn_C.configure(bg= '#D9D9D9')
    Name.delete(0, 'end')
    Name.insert(0,f'B_{date:%d_%b_%y}_{time}_xxx')
    center_window_on_screen()
    Frame2.pack()
    
def TypeC():
    Frame2.pack()
    btn_A.configure(bg = "#D9D9D9")
    btn_B.configure(bg= '#D9D9D9')
    btn_C.configure(bg= '#A3CFE9')
    Name.delete(0, 'end')
    Name.insert(0,f'C_{date:%d_%b_%y}_{time}_xxx')
    center_window_on_screen()
    Frame2.pack()

def RTM():
    Frame2.forget()
    Frame3.forget()
    Frame4.forget()
    Frame5.forget()
    Frame6.forget()
    Frame7.forget()
    Frame8.forget()
    Frame1.pack(fill='both', expand =1)
    center_window_on_screen()



#Setting up the UI
#Setting up the window
root = Tk()
root.title("Crystal Mate")
root.configure(bg='white')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_window_on_screen()

# Here, we create two frames of which only
# one will be visible at a time.
Frame1 = Frame(root)
Frame2 = Frame(root)
Frame3 = Frame(root)
Frame4 = Frame(root)
Frame5 = Frame(root)
Frame6 = Frame(root)
Frame7 = Frame(root)
Frame8 = Frame(root)

#Frame1 = The opening page to the program
#Frame2 = The Filename page
#Frame3 = The Capture page
#Frame4 = The saved successfully page
#Frame5 = The sample analysis page

#Starts the Program with Frame 1
Frame1.pack(fill='both', expand=1)



# Widgets for frame 1 (Opening Frame). (Blank labels are added for now to help with the psotionsing of widgets)
Frame1.configure(bg="#FFFFFF")
Welcome_Message = Label(Frame1, text="Welcome to Crystal Mate", bg="#FFFFFF", font=("Helvetica", 16))
Message2 = Label(Frame1, text="What would you like to do today?", bg="#FFFFFF", font=("Helvetica", 10))
# And finally, the button to swap between the frames.
btn_change = Button(Frame1,text='Take New sample', bg = '#D9D9D9',fg='#000000', height = 2, width = 22, command= change_to_Frame2)
btn_2 = Button(Frame1, text='check data of existing samples',bg = '#D9D9D9',fg='#000000', height = 2, width = 22, command = view_data)
set_btn = Button(Frame1, text = 'settings', command = settings)
# Gris command adds the widgets to the program in a specified Place
Welcome_Message.grid(row = 0, column = 1,padx = 90, pady = 10)
Message2.grid(row = 1, column = 1, pady = 15)
btn_change.grid(row = 2, column = 1, padx = 45, sticky = W)
btn_2.grid(row = 2, column = 1,padx = 45, sticky = E)
set_btn.grid(row = 0, column = 0)



#Widgets for Frame 2 (Filename Frame)
Frame2.configure(bg="#FFFFFF")
#Choosing Massecuite Type:
lbl_heading1 = Label (Frame2, text='Please choose a Massecuite type:',bg="#FFFFFF", font=('Helvetica', 16))
btn_A = Button(Frame2, text="A Mass",font=('Helvetica',10), bg= '#D9D9D9', fg='#000000', command = TypeA)
btn_B = Button(Frame2, text="B Mass",font=('Helvetica',10), bg= '#D9D9D9', fg='#000000', command = TypeB)
btn_C = Button(Frame2, text="C Mass",font=('Helvetica',10), bg= '#D9D9D9', fg='#000000', command = TypeC)
#Filename Labels
lbl_heading = Label(Frame2,text='Filename:',bg= '#FFFFFF', font=("Helvetica", 16))
Name = Entry(Frame2, bg= '#D9D9D9', width = 25 )
Name.insert(0,f'{date:%d_%b_%y}_{time}_xxx')
#Save location button
btn_S = Button(Frame2, text='...', bg='#D9D9D9', command = SelectDir)

#txt_filename = tk.Text(Frame2, height = 5, width = 10).pack()
btn_capture = Button(Frame2, text="Take Samples Images", font=("helvetica", 10), bg = '#D9D9D9',fg='#000000', height = 2, width = 18, command = change_to_capture)
lbl_heading1.grid(row = 0, column = 1, padx = 95, pady = 10)
btn_A.grid(row = 1, column = 1,padx = 180, pady = 15, sticky = W)
btn_B.grid(row = 1, column = 1,pady = 15)
btn_C.grid(row = 1, column = 1,padx = 180, pady = 15, sticky = E)
lbl_heading.grid(row = 2, column = 1, sticky = W, padx = 110, pady = 15)
Name.grid(row = 2, column = 1, sticky = E, padx = 145, pady = 15)
btn_S.grid(row = 2, column = 1, sticky = E, padx = 140, pady = 15)
btn_capture.grid(row = 3, column = 1,padx = 95, pady = 10)


#The widgets needed for Frame3 (The Capture page)
Frame3.configure(bg="#FFFFFF")
load1 = Image.open("Placeholder.jpg")
load = load1.resize((500,400))
render = ImageTk.PhotoImage(load)
img1 = Label(Frame3, image = render)
img1.image = render
Capture_btn = Button(Frame3, text="Capture", font=("Helvetica", 10), bg='#D9D9D9',fg='#000000', height = 2, width = 10, command = skip)
img1.grid(row = 0, column = 1, padx = 100, pady = 15)
Capture_btn.grid(row = 1, column = 1, padx = 120, pady = 10)


#Frame4 The processing Frame
Frame4.configure(bg="#FFFFFF")
Label(Frame4, text ='Processing Image',font=("Helvetica", 10),bg = "#FFFFFF",fg='#000000', height = 2, width = 22).pack()
temp_btn = Button(Frame4, text = 'Skip',font=("Helvetica", 10), bg='#D9D9D9',fg='#000000', height = 2, width = 22, command = skip).pack()



#Frame 5 Data captured page
Frame5.configure(bg="#FFFFFF")
load = Image.open("Placeholder2.png")
load = load.resize((300,200))
render = ImageTk.PhotoImage(load)
Img = Label(Frame5, image = render)
btn_recap = Button(Frame5, text = "Recapture sample",font=("Helvetica", 10), bg='#D9D9D9',fg='#000000', height = 2, width = 15, command = recapture)
btn_Save = Button(Frame5, text = "Save sample",font=("Helvetica", 10), bg='#D9D9D9',fg='#000000', height = 2, width = 15, command = save_file )
lbl = Label(Frame5, text = "Data Captured:",font=("Helvetica", 10),bg = "#FFFFFF",fg='#000000', height = 2, width = 22)
Img.grid(row = 0, column = 0, padx = 15)
btn_recap.grid(row = 1, column = 0, pady = 20)
btn_Save.grid(row = 1, column = 1, pady = 20)
lbl.grid(row = 0, column = 1, sticky = N)



#Widgets for Frame6 (The saved page)
Frame6.configure(bg="#FFFFFF")
Heading = Label(Frame6, text="File Saved!", font=("Helvetica", 16),bg = "#FFFFFF",fg='#000000')
btn1 = Button(Frame6, text="Return to main menu", font=("helvetica", 10), bg = '#D9D9D9',fg='#000000',height = 2, width = 20, command = return_to_menu)
btn2 = Button(Frame6, text="Capture new sample", font=("helvetica", 10), bg='#D9D9D9',fg='#000000',height = 2, width = 20, command = change_to_Frame2)
Err_lbl = Label()
Heading.grid(row = 0, column = 1, pady = 20)
btn1.grid(row = 1, column = 0, pady = 30, padx = 10)
btn2.grid(row = 1, column = 2, pady = 30, padx = 15)

#widgets for Frame7 (The sample analysis page)
Frame7.configure(bg="#FFFFFF")
#Heading = Label(Frame7, text= "Filename",font=("Helvetica", 16)).pack()
btn1 = Button(Frame7, text = 'Open sample',font=("Helvetica", 10),bg = '#D9D9D9',fg='#000000',height = 2, width = 22, command= browseFiles)
btn2 = Button(Frame7, text= 'Go back to main menu', font=("Helvetica", 10), bg = '#D9D9D9',fg='#000000',height = 2, width = 22, command = return_to_menu)

btn1.grid(row = 2, column = 0)
btn2.grid(row = 2, column = 2)

#widegts for Frame 8 (settings page)
Frame8.configure(bg='#FFFFFF')
ImgSze= Label(Frame8, text="Image size:", font=("Helvetica", 16),bg = "#FFFFFF",fg='#000000')
RTM = Button(Frame8, text = 'Return',font=("helvetica", 10), bg='#D9D9D9',fg='#000000', command = RTM)

# Widegts for Frame 8
ImgSze.grid(row = 0, column = 1, pady = 15)
RTM.grid(row = 2, column = 1)



root.mainloop()

