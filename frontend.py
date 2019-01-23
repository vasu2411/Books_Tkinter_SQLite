from tkinter import *
import backend

#main window
window = Tk()

#connection to the database
backend.connect()

#clear all text boxes
def clearAllTextBox():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)

#get data from text boxes
def getData():
    title = t1.get()
    author = t2.get()
    year = t3.get()
    isbn = t4.get()
    return (title,author,year,isbn)

#get selected row data to the text inputs
def get_selected_row(event):
    clearAllTextBox()
    index = li1.curselection()[0]
    seleted_tuple = li1.get(index)
    t1.insert(0,seleted_tuple[1])
    t2.insert(0, seleted_tuple[2])
    t3.insert(0, seleted_tuple[3])
    t4.insert(0, seleted_tuple[4])

#function to add book to the database
def addBook():
    (title, author, year, isbn) = getData()
    backend.insert(title,author,year,isbn)
    clearAllTextBox()
    viewBook()
    t1.focus()

#function to view all books from the database
def viewBook():
    li1.delete(0,END)
    row = backend.view()
    i=1
    for item in row:
        li1.insert(i,item)
        i=i+1

#function to search particular book from the database
def searchBook():
    li1.delete(0,END)
    (title, author, year, isbn) = getData()
    row = backend.search(title,author,year,isbn)
    i=1
    for item in row:
        li1.insert(i,item)
        i=i+1

#function to update data of selected book in to the database
def updateBook():
    activeTuple = li1.get(ACTIVE)
    (title, author, year, isbn) = getData()
    backend.update(activeTuple[0],title,author,year,isbn)
    clearAllTextBox()
    t1.focus()
    viewBook()

#function to delete selected book from the database
def deleteBook():
    activeTuple = li1.get(ACTIVE)
    backend.delete(activeTuple[0])
    clearAllTextBox()
    t1.focus()
    viewBook()

#function to close window
def close():
    window.destroy()

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

#text Title
t1 = Entry(window)
t1.grid(row=0,column=1)

#text Author
t2 = Entry(window)
t2.grid(row=0,column=3)

#text Year
t3 = Entry(window)
t3.grid(row=1,column=1)

#text ISBN
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

li1.bind('<<ListboxSelect>>',get_selected_row)

#View all button
b1 = Button(window,text="View All",width=13,command=viewBook)
b1.grid(row=2,column=3)

#search entry button
b2 = Button(window,text="Search entry",width=13,command=searchBook)
b2.grid(row=3,column=3)

#add entry button
b3 = Button(window,text="Add entry",width=13,command=addBook)
b3.grid(row=4,column=3)

#update button
b4 = Button(window,text="Update selected",width=13,command=updateBook)
b4.grid(row=5,column=3)

#delete button
b5 = Button(window,text="Delete selected",width=13,command=deleteBook)
b5.grid(row=6,column=3)

#close button
b6 = Button(window,text="Close",width=13,command=close)
b6.grid(row=7,column=3)

window.mainloop()