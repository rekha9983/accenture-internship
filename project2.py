from tkinter import *
root=Tk()
Label (root, text = "Employee Form", bg="blue", fg="white",font="Verdana 14 bold italic").grid(row=0, column=0)

lab= Label( root, text= "First name", height=2, width=10,fg='blue',font="BOLD")
lab.grid(row=1,column=0,sticky=W)
w=Entry(root)
w.grid(row=1,column=1)

lab= Label( root, text= "Last name", height=2, width=10,fg='blue',font="BOLD")
lab.grid(row=2,column=0,sticky=W)
w=Entry(root)
w.grid(row=2,column=1)

lab= Label( root, text= "Email id", height=2, width=10,fg='blue',font="BOLD")
lab.grid(row=3,column=0,sticky=W)
w=Entry(root)
w.grid(row=3,column=1)

lab= Label( root, text= "Enterprise id", height=2, width=10,fg='blue',font="BOLD")
lab.grid(row=4,column=0,sticky=W)
w=Entry(root)
w.grid(row=4,column=1)

lab= Label( root, text= "Project name", height=2, width=10,fg='blue',font="BOLD")
lab.grid(row=5,column=0,sticky=W)
w=Entry(root)
w.grid(row=5,column=1)

lab= Label( root, text= "Technology", height=2, width=10,fg='blue',font="BOLD")
lab.grid(row=6,column=0,sticky=W)
w=Entry(root)
w.grid(row=6,column=1)

lab= Label( root, text= "Manager", height=2, width=10,fg='blue',font="BOLD")
lab.grid(row=7,column=0,sticky=W)
w=Entry(root)
w.grid(row=7,column=1)

lab= Label( root, text= "Location", height=2, width=10,fg='blue',font="BOLD")
lab.grid(row=8,column=0,sticky=W)
w=Entry(root)
w.grid(row=8,column=1)

B=Button(root,text="submit", height=1, width=10, bg="green", fg="White",font="Verdana 14 bold")
B.grid(row=10,column=0)

