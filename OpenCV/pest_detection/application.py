from tkinter import *
from PIL import ImageTk,Image
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename


import cv2
from PIL import Image
import numpy as np
import imutils
#blur the image for further processing
def blur(image):
    blur = cv2.GaussianBlur(image,(11,11),0)
    
    return blur

#we use green as mask so that other than green on paddy are dected as bugs
def mask(image):
    greenLower = (27, 25, 25)
    greenUpper = (70, 255, 255)
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,greenLower,greenUpper)
    mask = cv2.erode(mask, None, iterations= 2)
    mask = cv2.dilate(mask, None, iterations= 2)
    mask = cv2.bitwise_not(mask)

    return mask

#after having bug on image we contour those images to count number of pests
def contour(mask):

    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    boxes = []

    for cnt in cnts:
        if cv2.contourArea(cnt) > 350:
            x,y,w,h = cv2.boundingRect(cnt)
            boxes.append([x,y,w,h])
    
    return boxes

#we create rectangular boxes which are shown on those bugs present on the position of orginal image
def bounding(image,boxes):
    img = image.copy()
    for box in boxes:
        x,y,w,h = box
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    return img

#finaly number of rectangular boxes are separetly show us the bugs present on image
def crops(image,boxes):
    crop_list = []
    for box in boxes:
        x,y,w,h = box
        crop = image[y:y+h,x:x+w]
        crop = cv2.resize(crop,(240,360))
        crop_list.append(crop)
    
    return crop_list

#process of creating an interface for this program is made using tkinter module
#firstly we create frames which are used as pages

def raise_frame(f):
    f.tkraise()
 
def finish():
    r.destroy()
def Fr1():
    raise_frame(f1)
def Fr2():
    raise_frame(f2) 
def Fr3():
    raise_frame(f3)
def Fr4():
    raise_frame(f4)
def Fr5():
    raise_frame(f5)
def Fr6():
    raise_frame(f6)
def Fr7():
    raise_frame(f7)
def Fr8():
    raise_frame(f8)
def Fr9():
    raise_frame(f9)
    
#-------------------------------------Page 1-------------------------------------------------------------
def fun1():

    global img
    global img_label

    path = askopenfilename(filetypes=[("Image File",'.jpg')])
    
    

    img_int = Image.open(path)
    img_int = img_int.resize((480,360),)
    img_pil = ImageTk.PhotoImage(img_int)
    img = np.asarray(img_int)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    try:
        if img_label is not None:
            img_label.destroy()
    except:
        p = 3
    img_label = Label(f4,width=480,height=360,image=img_pil, anchor=CENTER)
    img_label.place(x= 250,y=30)
    img_label.pack()
    img_label.configure(image=img_pil)
    img_label.image()
    

def fun2():
    global blurs
    global img_pil

    blurs = blur(img)
    img_pil = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(blurs,cv2.COLOR_RGB2BGR)))
    img_label.configure(image=img_pil)
    img_label.image(img_pil)

def fun3():
    global masks
    global img_pil
    masks = mask(blurs)
    img_pil = ImageTk.PhotoImage(Image.fromarray(masks))
    img_label.configure(image=img_pil)
    img_label.image(img_pil)
    

def fun4():
    global masks
    global final
    global img_pil
    global boxes

    boxes = contour(masks)
    final = bounding(img,boxes)
    img_pil = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(final,cv2.COLOR_RGB2BGR)))
    img_label.configure(image=img_pil)
    img_label.image(img_pil)


def fun5():
    
    global c_list
    c_list = crops(img,boxes)
    for c in c_list:
        cv2.imshow('bugs',c)
        cv2.waitKey(0)
    cv2.destroyAllWindows()

def fun6():

    c_list = crops(img,boxes)
    num = len(c_list)
    count_var.set(str(num))
    



#-------------------------------------Page 2-------------------------------------------------------------

def fun7():
    x7.set('')
def fun8():
    x8.set('')
def fun9():
    x9.set('')
def fun10():
    x10.set('')

    
r = Tk()
f0 = Frame(r)
f1 = Frame(r)
f2 = Frame(r)
f3 = Frame(r)
f4 = Frame(r)
f5 = Frame(r)
f6 = Frame(r)
f7 = Frame(r)
f8 = Frame(r)
f9 = Frame(r)

f0.place(x = 0,y = 0,height=800, width=1200)
f1.place(x = 100,y = 250,height=430, width=1000)
f2.place(x = 100,y = 250,height=430, width=1000)
f3.place(x = 100,y = 250,height=430, width=1000)
f4.place(x = 100,y = 250,height=430, width=1000)
f5.place(x = 100,y = 250,height=430, width=1000)
f6.place(x = 100,y = 250,height=430, width=1000)
f7.place(x = 100,y = 250,height=430, width=1000)
f8.place(x = 100,y = 250,height=430, width=1000)
f9.place(x = 100,y = 250,height=430, width=1000)



x0=StringVar()
x1=StringVar()
x2=StringVar()
x3=StringVar()
x4=StringVar()
x5=StringVar()
x6=StringVar()
x7=StringVar()
x8=StringVar()
x9=StringVar()
x10=StringVar()
x11=StringVar()
x12=StringVar()
x13=StringVar()
x14=StringVar()
x15=StringVar()
x16=StringVar()
sc=StringVar()
sk=StringVar()
oc=StringVar()
ok=StringVar()

f0.configure(bg="black")
f1.configure(bg="black")
f2.configure(bg="black")
f3.configure(bg="black")
f4.configure(bg="black")
f5.configure(bg="black")
f6.configure(bg="black")
f7.configure(bg="black")
f8.configure(bg="black")
f9.configure(bg="black")

#HeadingPage


Label(f0, text = "",bg='gray',height=9,width=165).place(x = 20, y = 20)

Label(f0, justify='center',bg='gray',text = """GAYATRI VIDYA PARISHAD COLLEGE FOR DEGREE AND P.G. COURSES(A)
RUSHIKONDA, VISAKHAPATNAM-45
DEPARTMENT OF COMPUTER APPLICATION""",fg='white',height=4,font = "Helvetica 18 bold").place(x = 200, y = 30)

ph2=ImageTk.PhotoImage(Image.open("logo1.jpg"))
Label(f0, text = "",image=ph2,height=0).place(x = 50, y = 30)



b2 = Button(f0, text = "Home",fg="white",bg="black", font = "Helvetica 13 bold",height=2,width=10,command = Fr1).place(x = 227, y =180)
b3 = Button(f0, text = "Abstract",fg="white",bg="black", font = "Helvetica 13 bold",height=2,width=10,command = Fr2).place(x = 354, y =180)
b4 = Button(f0, text = "Proposed",fg="white",bg="black", font = "Helvetica 13 bold",height=2,width=10,command = Fr3).place(x = 481, y =180)
b5 = Button(f0, text = "Methodology",fg="white",bg="black", font = "Helvetica 13 bold",height=2,width=10,command = Fr4).place(x = 608, y =180)
b6 = Button(f0, text = "Conclusion",fg="white",bg="black", font = "Helvetica 13 bold",height=2,width=10,command = Fr8).place(x = 735, y =180)
b7 = Button(f0, text = "ThanQ",fg="white",bg="black", font = "Helvetica 13 bold",height=2,width=10,command = Fr9).place(x = 862, y =180)


#------------------StartPage---Frame 1--------------------------------------------------------------------------

Label(f1, text = """Pest Detection and Extraction
using Image Processing Techniques""",fg="white",bg='black',font = "Georgia 40 bold",height=2).place(x = 20, y = 50)

Label(f1, text = """Project by 
   
Aasim Ali shaik  (2018-1902055)
      
      BCA  VI SEMESTER
""",fg="purple",bg="black",font = "Georgia 14 bold",height=6).place(x = 20, y = 250)

Label(f1, text = """Project Guide
Mrs. ch Suneetha
Assistant Professor
""",fg="white",bg='black',font = "Georgia 14 bold",height=6,width=20).place(x = 600, y = 250)


#-----------------------------Frame-2----------------------------------------------------------------------------------------


Label(f2, text = "Abstract ",fg="white",bg="black", font = "Latin 18 bold").place(x = 50,y=30)


Label(f2,justify="left", text="""
Detection of pests in the fields is a major challenge in the field of agriculture, therefore effective measures should

be developed to fight the infestation while minimizing the use of pesticides. The techniques of image analysis are

extensively applied to agricultural science and it provides maximum protection to crops which can ultimately lead

to better crop management and production. Monitoring of pests infestation requires a huge amount of manpower,

however automatic monitoring has been advancing in order to minimize human efforts and errors. This project extends

the implementation of different image processing techniques to detect and extract insect pests by establishing an

automated detection and extraction system for estimating pest densities in paddy fields.""",fg="white",bg="black", font = "Latin 13 bold").place(x = 50, y =80)

b7 = Button(f2, text = "Prev",fg="white",bg="black", font = "Helvetica 14 bold",height=1,width=6,command=Fr1).place(x = 10, y = 385)
b8 = Button(f2, text = "Next",fg="white",bg="black", font = "Helvetica 14 bold",height=1,width=6,command = Fr3).place(x = 920, y = 385)

#-----------------------------Frame 3---------------------------------------------------------------------------------

l1 = Label(f3, text = "Proposed  System",fg="white",bg="black", font = "Latin 18 bold").place(x = 50,y=30)
l1 = Label(f3, text = """
Image processing : Image processing is the analysis and manipulation of graphical images from sources such as photographs and videos

There are three main steps in image processing :

 considering a captured image, converting the captured images into binary values that a computer can process. 

 Image enhancement and data compression. 

 This is an output step that consists of display and printing of processed image."""
,fg="white",bg="black",justify="left", font = "Latin 13 bold").place(x = 50,y=80)


b7 = Button(f3, text = "Prev",fg="white",bg="black", font = "Helvetica 14 bold",height=1,width=6,command=Fr2).place(x = 10, y = 385)
b8 = Button(f3, text = "Next",fg="white",bg="black", font = "Helvetica 14 bold",height=1,width=6,command = Fr4).place(x = 920, y = 385)

#------------------------Frame-4-----------------------------------------------------------------------------------------

L0= Label(f4,text="Methodology",fg="black",bg="white",font="Latin 18 bold").place(x=10,y=10)

#img_label = Label(f4,fg="black",bg="light gray", font = "Latin 12 bold",width=50,height=15).place(x = 250,y=60)

B1= Button(f4,text="Input Image",fg="white",bg="black",font="Latin 12 bold",width=16,height=2,command=fun1).place(x=20,y=60)



B1= Button(f4,text="""Gaussian 
  Blur""",fg="white",bg="black",font="Latin 12 bold",width=16,height=3,command=fun2).place(x=20,y=120)
#l3= Label(f4,textvariable=x2,fg="black",bg="light gray", font = "Latin 12 bold",width=50,height=2).place(x = 250,y=120)

B2= Button(f4,text="""HSV Image
using Green
masking
""",fg="white",bg="black",font="Latin 12 bold",width=16,height=4,command=fun3).place(x=20,y=200)


B3= Button(f4,text="""Pest 
Detection
""",fg="white",bg="black",font="Latin 12 bold",width=16,height=3,command=fun4).place(x=20,y=300)
#L6= Label(f4,textvariable=x4,fg="black",bg="light gray",font="Latin 12 bold",width=50,height=2).place(x=250,y=240)



b1 = Button(f4, text = """Cropped bug
Images""",fg="white",bg="black", font = "Latin 12 bold",height=2,width=16,command = fun5).place(x =830, y =60)
#l2 = Label(f4, textvariable=x6,fg="black",bg="light gray", font = "Latin 12 bold",width=50,height=15).place(x = 250, y =60)

count_var = StringVar()
count_var.set('0')
l5 = Label(f4,textvariable=count_var,fg="black",bg="white",font="Latin 18 bold")
l5.place(x=830,y=180)

b2 = Button(f4, text = "Bug Count",fg="white",bg="black", font = "Latin 12 bold",height=2,width=16,command = fun6).place(x = 830, y =120)

b7 = Button(f4, text = "Prev",fg="white",bg="black", font = "Helvetica 14 bold",height=1,width=6,command=Fr3).place(x = 10, y = 385)
b8 = Button(f4, text = "Next",fg="white",bg="black", font = "Helvetica 14 bold",height=1,width=6,command = Fr8).place(x = 920, y = 385)


#-----------------------------Frame-5-------------------------------------------------------------------------------

l1 = Label(f8, text = "CONCLUSION ",fg="white",bg="black", font = "Latin 16 bold").place(x = 30,y=10)

l1 = Label(f8,
text = """
       In this system, the automatic detection and extraction system was presented, different image processing

techniques were used to detect and extract the pests in the captured image. The presented problem statement is

simple and yet efficient. We used background modelling to detect the presence of insect pests in the captured

image and a median filter was used to remove the noise produced by different light conditions. The mechanism

used to extract the detected objects from the image is simple, the image was scanned both horizontally and

vertically to determine each coordinates and save the object image. The problem statement is promising, efficient

and simple in providing better results which in turn results in the improvement of quality and quantity of crop in

the rice fields. """,fg="white",bg="black",justify='left', font = "Latin 13 bold").place(x = 30,y=50)



b7 = Button(f8, text = "Prev",fg="white",bg="black", font = "Helvetica 14 bold",height=1,width=6,command=Fr4).place(x = 10, y = 385)
b8 = Button(f8, text = "Next",fg="white",bg="black", font = "Helvetica 14 bold",height=1,width=6,command = Fr9).place(x = 920, y = 385)

#-----------------------------Frame-6-------------------------------------------------------------------------------

ph22=ImageTk.PhotoImage(Image.open("t.jpg"))
lab1 = Label(f9, text = "",image=ph22,height=0).place(x = -20, y = 0)


b7 = Button(f9, text = "Prev",fg="white",bg="black", font = "Helvetica 14 bold",height=1,width=6,command=Fr8).place(x = 10, y = 385)
b8 = Button(f9, text = "Next",fg="white",bg="black", font = "Helvetica 14 bold",height=1,width=6,command = Fr1).place(x = 920, y = 385)

#-----------------------------End-------------------------------------------------------------------

raise_frame(f1)
r.geometry("1200x700+70+0")
r.title("Pest Detection and Extraction using Image Processing Techniques")
r.mainloop()

