from tkinter import *
from tkinter import messagebox
import nltk
from nltk.corpus import words
from time import gmtime, strftime
import time
from collections import Counter
nltk.download('words')
word_list = words.words()
Matrix_list = ['a', 'r', 'b', 'z', 't', 'n', 'd', 'h', 'm', 'v', 's', 'x', 'l', 'u', 'g', 'y', 'p', 'k', 'c', 'o']
score = 0

window = Tk()
window.title("Scrambling Words")
window.geometry("600x500")


def checkspells():
    global score
    word = word_check.get()
    if word in word_list:
        dict = Counter(word)
        flag = 1
        for key in dict.keys():
            if key not in Matrix_list:
                flag = 0
        if flag == 1 and len(word) > 3:
            score = score+len(word)
            total = "score = "+str(score)
            label.configure(text=total)
            print(word)
        else:
            messagebox.showinfo("check", "No matching with above character OR word length should be greater than 3")
    else:
        print("No word")
    word_check.delete(0, 'end')


def tick(time1=''):
    time2 = time.strftime("%M:%S")
    if time2 != time1:
        time1 = time2
        timer.config(text="After 1 minute it will close automatically "+time2)
    timer.after(200, tick)


def quit_pro():
    messagebox.showinfo("OOPS!!!!!!!", "Time UP!!! Your Score "+str(score))
    window.destroy()


btn1 = Button(window, text="A", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=1)
btn2 = Button(window, text="R", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=1)
btn3 = Button(window, text="B", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=1)
btn4 = Button(window, text="Z", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=1)
btn5 = Button(window, text="T", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=1)

btn1 = Button(window, text="N", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=2)
btn2 = Button(window, text="D", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=2)
btn3 = Button(window, text="H", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=2)
btn4 = Button(window, text="M", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=2)
btn5 = Button(window, text="V", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=2)

btn1 = Button(window, text="S", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=3)
btn2 = Button(window, text="X", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=3)
btn3 = Button(window, text="L", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=3)
btn4 = Button(window, text="U", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=3)
btn5 = Button(window, text="G", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=3)

btn1 = Button(window, text="Y", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=4)
btn2 = Button(window, text="P", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=4)
btn3 = Button(window, text="K", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=4)
btn4 = Button(window, text="C", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=4)
btn5 = Button(window, text="O",bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=4)

word_check = Entry(window, width=50)
word_check.configure(highlightbackground="red", highlightcolor="red")
word_check.grid(row=5, column=0, columnspan=6)
btncheck = Button(window, text="Submit", bg="Green", fg="White", width=5, height=2, font=('Helvetica', '10'), command=checkspells)
btncheck.grid(column=10, row=5)
label = Label(window, text="Score = 0")
label.grid(column=11, row=5)
timer = Label(window, text="you have 1 minute")
timer.grid(column=0, row=6, columnspan=6)
tick()
window.after(60000, quit_pro)

window.mainloop()
