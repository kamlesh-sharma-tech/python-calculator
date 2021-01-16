from tkinter import *
from tkinter import messagebox,ttk

font=("Verdana",22,"bold")


def inputField(event):
    which_button = event.widget
    text = which_button['text']
    if text == "x":
        textField.insert(END, "*")
        return 
    if text == "=":
        try:
            get_value = textField.get()
            answer = eval(get_value)
            textField.delete(0,END)
            textField.insert(0,answer)
        except Exception as e:
            messagebox.showerror("Error",e)
        return
    textField.insert(END, text)

def single_clear():
    get_value = textField.get()
    signle = get_value[0:len(get_value)-1]
    textField.delete(0,END)
    textField.insert(0,signle)


def all_clear():
    textField.delete(0,END)


def destroy():
    ex = messagebox.askyesno("Exit","Are you sure you want to exit the app ?")
    if(ex == True):
        win.destroy()

win = Tk()
win.title("My Calculator")
win.geometry("440x600+600+100")
win.resizable(0,0)
win.wm_iconbitmap("calculator.ico")
win.configure(bg="lightblue")

calculatorPhoto = PhotoImage(file="calculator.png")
calculatorLabel = Label(win,image=calculatorPhoto)
calculatorLabel.pack(side=TOP,pady=10)


calculatortitle = Label(win,text="Calculator",font=font,underline=0)
calculatortitle.pack(side=TOP,pady=5)


textField = Entry(win,font=("Helvetica",20,"bold"),justify=LEFT,width=27)
textField.pack(side=TOP,pady=5)
textField.focus()

buttonsFrame = Frame(win)
buttonsFrame.pack()

temp = 1
for i in range(0,3):
    for j in range(0,3):
        btns1to9 = Button(buttonsFrame,text=str(temp),font=font,relief="ridge",width=4,padx=7,pady=5)
        btns1to9.grid(row=i,column=j)
        btns1to9.bind('<Button-1>', inputField)
        temp = temp + 1

zeroBtn = Button(buttonsFrame,text="0",font=font,relief="ridge",width=4,padx=7,pady=5)
zeroBtn.grid(row=3,column=0)

dotBtn = Button(buttonsFrame,text=".",font=font,relief="ridge",width=4,padx=7,pady=5)
dotBtn.grid(row=3,column=1)

equalBtn = Button(buttonsFrame,text="=",font=font,relief="ridge",width=4,padx=7,pady=5)
equalBtn.grid(row=3,column=2)


plusBtn = Button(buttonsFrame,text="+",font=font,relief="ridge",width=4,padx=7,pady=5)
plusBtn.grid(row=0,column=3)

minusBtn = Button(buttonsFrame,text="-",font=font,relief="ridge",width=4,padx=7,pady=5)
minusBtn.grid(row=1,column=3)

multBtn = Button(buttonsFrame,text="x",font=font,relief="ridge",width=4,padx=7,pady=5)
multBtn.grid(row=2,column=3)

divideBtn = Button(buttonsFrame,text="/",font=font,relief="ridge",width=4,padx=7,pady=5)
divideBtn.grid(row=3,column=3)


singleclearBtn = Button(buttonsFrame,text="Back",font=font,relief="ridge",width=9,padx=7,pady=5,command=lambda : single_clear())
singleclearBtn.grid(row=4,column=0,columnspan=2)

allclearBtn = Button(buttonsFrame,text="AC",font=font,relief="ridge",width=9,padx=7,pady=5,command=lambda : all_clear())
allclearBtn.grid(row=4,column=2,columnspan=2)

exitBtn = Button(win,text="Exit App",font=("Arial",10),relief="ridge",command=lambda : destroy())
exitBtn.pack(side=BOTTOM,pady=15)


zeroBtn.bind('<Button-1>', inputField)
dotBtn.bind('<Button-1>', inputField)
equalBtn.bind('<Button-1>', inputField)
plusBtn.bind('<Button-1>', inputField)
minusBtn.bind('<Button-1>', inputField)
multBtn.bind('<Button-1>', inputField)
divideBtn.bind('<Button-1>', inputField)


win.mainloop()
