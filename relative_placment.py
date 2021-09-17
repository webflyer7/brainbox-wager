from tkinter import *
import random
window = Tk()
divyansh = IntVar()
#this is the rolle the dice function where user can select any number between 1 to 6 
def game():
    x = random.randrange(1, 7)
    #get takes value from the object #divyansh is the object of IntVar class
    y = divyansh.get()
    if x == y:
        #relx stands for relative horizontal position of the object with respect to window size
        #rely stands for relative vertical position of the object with respect to window size

        label = Label (window,text = "Congratulations the number you have selected is " + str(y) + " and the number generated is " +str(x) , bg = 'light blue', font = (14)).place( relx = 0.5 , y = 200 , anchor = 'center')
    else:
        label = Label (window,text = "Oops try again the number you have selected is " + str(y) + " and the number generated is " +str(x) , bg = 'light blue', font = (14)).place( relx = 0.5 , y = 200 , anchor = 'center')    
window.configure(bg = 'light blue')
btn = Button(window, text = "This is a button widget",bg = "dark blue" , fg = 'white' ,command = game)
btn.place(relx = 0.5, y = 100, anchor = 'center')
lbl = Label(window, text = "This is a number game", fg = 'red', bg ='light blue',font = ("Lucida Calligraphy",16))
lbl.place(relx = 0.5  , y = 50, anchor ="center")
txtfld = Entry(window , textvariable = divyansh, bd = 5)
txtfld.place(relx = 0.5, y =150 ,anchor = 'center') 
window.title("Memory Guess")
window.geometry("300x300")
window.mainloop()