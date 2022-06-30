from tkinter import *


root =Tk()
e=Entry(root,bg="blue",borderwidth=5)
e.pack()
e.insert(0,"enter your name")



def clicked():
	hellow= "hellow "+e.get()
	hi=Label(root,text=hellow )
	hi.pack()

#myLabel= Label(root,text='Hellow world!')


#myLabel1= Label(root,text='hi there')
#myLabel2= Label(root,text='saurav').grid( row = 1 , column=1)



#myButton=Button(root,text='click me!' ,padx=50 ,pady=30,command=clicked())   clicked() Doesnot work
myButton=Button(root,text='Enter your name', fg="blue",bg="red",command=clicked)




#myLabel.pack()

#myLabel1.grid( row = 0 , column=0)
#myLabel2.grid( row = 1 , column=1)

myButton.pack()

root.mainloop()
