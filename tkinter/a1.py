from tkinter import *
from tkinter import Image,messagebox

win=Tk()
win.title("sinup/singin")
win.geometry("500x500")
win.resizable(0,0)
win.config(background="violet")
img=PhotoImage(file="logo.png")
win.iconphoto(False,img)
cb=IntVar()
name=StringVar()
email=StringVar()
password=StringVar()

def bs():
    if cb.get()==1:
      
      btn['state']=ACTIVE
      btn1['state']=ACTIVE
    else:
       btn['state']=DISABLED
       btn1['state']=DISABLED
def sigUp():
   import mysql.connector as sql
   mycon=sql.connect(host="localhost",user="root",password="1234567890@",database="gui")
   mycur=mycon.cursor()
   n=name.get()
   e=email.get()
   p=password.get()
   q="insert into users values('"+n+"','"+e+"','"+p+"')"
   mycur.execute(q)
   mycon.commit()
   messagebox.showinfo("SignUp","SignUp Successfully")
def sigIn():
   
   import mysql.connector as sql
   mycon=sql.connect(host="localhost",user="root",password="1234567890@",database="gui")
   mycur=mycon.cursor()
   n=name.get()
   e=email.get()
   p=password.get()
   q="select * from users where email='{}' and password='{}'".format(e,p)
   mycur.execute(q)
   rec=mycur.fetchone()
   if rec!=None:
      messagebox.showinfo("Login","Logged In Successfully")
   else:
      messagebox.showinfo("Login","Logged In Failure")


   

    
h1=Label(win,text="A1 Registration Form",font=("times new roman",22,"bold"),bg="violet",fg="white")
h1.pack(pady=10)
l1=Label(win,text="Enter Name",font=("times new roman",18,"bold"),bg="violet",fg="black")
l1.place(x=90,y=70)
e1=Entry(win,font=("times new roman",18,"bold"),bg="white",fg="black",bd=10,textvariable=name)
e1.place(x=90,y=100)

l2=Label(win,text="Enter Email",font=("times new roman",18,"bold"),bg="violet",fg="black")
l2.place(x=90,y=160)
e2=Entry(win,font=("times new roman",18,"bold"),bg="white",fg="black",bd=10,textvariable=email)
e2.place(x=90,y=190)

l3=Label(win,text="Enter Password",font=("times new roman",18,"bold"),bg="violet",fg="black")
l3.place(x=90,y=250)
e3=Entry(win,font=("times new roman",18,"bold"),bg="white",fg="black",bd=10,show="*",textvariable=password)
e3.place(x=90,y=280)
cb1=Checkbutton(win,text="I Have Read All Instructions & Agree Them",font=("monotype corsiva",14,"bold"),bg="violet",fg="black",offvalue=0,onvalue=1,variable=cb,command=bs)
cb1.place(x=50,y=340)
btn=Button(win,text="singIn",font=("monotype corsiva",20,"bold"),bg="pink",fg="black",bd=10,state="disabled",command=sigIn)
btn.place(x=140,y=400)
btn1=Button(win,text="singUp",font=("monotype corsiva",20,"bold"),bg="pink",fg="black",bd=10,state="disabled",command=sigUp)
btn1.place(x=290,y=400)


win.mainloop()
