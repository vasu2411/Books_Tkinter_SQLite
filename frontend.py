from tkinter import *
import backend

#main window
window = Tk()

#label Title
l1 = Label(window, text="Title")
l1.grid(row=0,column=0)

#label Author
l2 = Label(window, text="Author")
l2.grid(row=0,column=2)

#label Year
l3 = Label(window, text="Year")
l3.grid(row=1,column=0)

#label ISBN
l4 = Label(window, text="ISBN")
l4.grid(row=1,column=2)

#entry Title
t1 = Entry(window)
t1.grid(row=0,column=1)

#entry Author
t2 = Entry(window)
t2.grid(row=0,column=3)

#entry Year
t3 = Entry(window)
t3.grid(row=1,column=1)

#entry ISBN
t4 = Entry(window)
t4.grid(row=1,column=3)

#listbox
li1 = Listbox(window,height=8,width=35)
li1.grid(row=2,column=0,rowspan=6,columnspan=2)

#scrollbar
sc1 = Scrollbar(window)
sc1.grid(row=2,column=2,rowspan=6)

#configure scrollbar for list
li1.configure(yscrollcommand=sc1.set)
sc1.configure(command=li1.yview)

#View all button
b1 = Button(window,text="View All",width=13)
b1.grid(row=2,column=3)

#search entry button
b2 = Button(window,text="Search entry",width=13)
b2.grid(row=3,column=3)

#add entry button
b3 = Button(window,text="Add entry",width=13)
b3.grid(row=4,column=3)

#update button
b4 = Button(window,text="Update selected",width=13)
b4.grid(row=5,column=3)

#delete button
b5 = Button(window,text="Delete selected",width=13)
b5.grid(row=6,column=3)

#close button
b6 = Button(window,text="Close",width=13)
b6.grid(row=7,column=3)

window.mainloop()