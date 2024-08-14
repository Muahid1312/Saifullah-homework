from tkinter import *
root=Tk()
root.geometry("1800x1000")
root.colormapwindows()
root.title("Muahid homework")
root.geometry("1700x1000")

root["background"]="lightcyan"

labell1=Label(root,text="Email")
labell1.place(x=540,y=190)

e=Entry(root,width=34,borderwidth=2)
e.place(x=540,y=210)
e.insert(90,"")

def show_hide():
    if show_hide_button["text"]=="Show":
        e1.config(show="")
        show_hide_button.config(text="Hide")

    else:
        e1.config(show="*")
        show_hide_button.config(text="Show")

labell2=Label(root,text="Password")
labell2.place(x=540,y=240)

e1=Entry(root,width=34,borderwidth=2,show="*")
e1.place(x=540,y=260)
e1.insert(90,"")

def Exit():
    if e1.get()=="44546521" and e.get()=="saifullahmuahid@gmail.com":
        return root.quit()
    elif e1.get()=="44546521" and e.get()!="saifullahmuahid@gmail.com":
        return my_labell1.place(x=540,y=190)
    elif e1.get()!= "44546521"  and e.get() == "saifullahmuahid@gmail.com":
        return my_labell2.place(x=540,y=240)
    else:
        return my_labell3.place(x=540,y=160)


show_hide_button=Button(root,text="Show",font=("SimSum",10),command=show_hide,padx=5,pady=5)
show_hide_button.place(x=755,y=264)

my_labell1=Label(root,text="Email is incorrect Please inter a valid email address")
my_labell2=Label(root,text="Password is incorrect Please inter a valid Password")
my_labell3=Label(root,text="Please inter correct Password and Email address")

button_Exit=Button(root,text="Login",fg="white",bg="black",width=20,borderwidth=3,command=Exit)
button_Exit.place(x=540,y=290)

root.mainloop()



                                         # This is the code of main Page(windows)

from tkinter import *
windows=Tk()
windows.geometry("1800x1000")
windows.colormapwindows()
windows.title("saifullah muahid homework")
windows.geometry("1700x1000")

windows["background"]="lightcyan"

labell_g=(Label(windows,text="Welcome to the muahid homework TCA program",
             fg="white",bg="red",font=16)).place(x=1,y=1)
#labell_g.grid(row=0,column=0)

windows.iconbitmap('C:\\Users\\MRC\\Pictures\\pictures')
e=Entry(windows,width=35,borderwidth=6)
e.place(x=1,y=28)
e.insert(90,"Hey! you can search programs here")
def online():
    #labell=Label(windows,text="Place check internet")
    e.insert(90,{Label(windows,text="Place check internet")})

button_entry=Button(windows,text="Search",bg="white",fg="blue",width=5,command=online)
button_entry.place(x=227,y=29)

def button_clear():
    e.delete(0,END)
button_exit=Button(windows,text="Clean",bg="white",fg="red",command=button_clear,width=5)
button_exit.place(x=273,y=29)

option_frame=Frame(windows,bg="#c3c3c3")
option_frame.pack(side=RIGHT)
option_frame.pack_propagate(False)
option_frame.configure(width=150,height=800)

main_frame=Frame(windows,highlightbackground="black",
                 highlightthickness=2)
main_frame.pack(side=RIGHT)
main_frame.pack_propagate(False)
main_frame.configure(width=900,height=800)

first_button=Button(option_frame,text="1.PY Homework",bg="#c3c3c3",
                    fg="black",borderwidth=0,command=lambda:indicate(first_indicate,first_page))
first_button.place(x=10,y=50)
first_indicate=Label(option_frame,text="",bg="#c3c3c3",fg="black")
first_indicate.place(x=3,y=50)

second_button=Button(option_frame,text="2.PY Homework",bg="#c3c3c3",
                     fg="black",borderwidth=0,command=lambda:indicate(second_indicate,second_page))
second_button.place(x=10,y=150)
second_indicate=Label(option_frame,text="",bg="#c3c3c3",fg="black")
second_indicate.place(x=3,y=150)

third_button=Button(option_frame,text="3.PY Homework",bg="#c3c3c3",
                     fg="black",borderwidth=0,command=lambda:indicate(third_indicate,third_page))
third_button.place(x=10,y=250)
third_indicate=Label(option_frame,text="",bg="#c3c3c3",fg="black")
third_indicate.place(x=3,y=250)

delete_all_button=Button(option_frame,text="Clean the Board",bg="#c3c3c3",
                     fg="black",borderwidth=0,command=lambda:indicate(delete_indicate,delete_all))
delete_all_button.place(x=10,y=400)
delete_indicate=Label(option_frame,text="",bg="#c3c3c3",fg="black")
delete_indicate.place(x=3,y=400)

def hide_indicate():
    first_indicate.config(bg="#c3c3c3")
    second_indicate.config(bg="#c3c3c3")
    third_indicate.config(bg="#c3c3c3")
    delete_all_button.config(bg="#c3c3c3")

def indicate(lb,page):
    hide_indicate()
    lb.config(bg="#158aff")
    delete_page()
    page()


def first_page():
    first_frame=Frame(main_frame)
    lb=Label(first_frame,text=""" def factorial(n):
    if n==0:
        return 1
    elif n ==1:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter a number to find the factorial of it: "))
print(factorial(n)) """)
    lb.pack()
    first_frame.pack()

def second_page():
    second_frame=Frame(main_frame)
    lb=Label(second_frame,text=""" def fibonancy(m):
    if m==0:
        return 0
    elif m==1:
        return 1
    else:
        return fibonancy(m) + fibonancy(m-1)
m=int(input("Enter the number to find the fibonancy of it: "))
print(fibonancy(m))""")
    lb.pack()
    second_frame.pack()

def third_page():
    third_frame=Frame(main_frame)
    lb=Label(third_frame,text="dlhsdhkshhsafhdhflasdhflkasd"
                              "fjsdlflsdhsdhglhsdalghsdhgshdgsd"
                              "dlgas;ldg;lsdhg;lshdg;ldshg;lshdg;l"
                              "###################################")
    lb.pack()
    third_frame.pack()


def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()

def delete_all():
    for frame in main_frame.winfo_children():
        frame.destroy()

def myClick1():
    from tkinter import Tk
    root=Tk()
    root.title("First homework of python")
    root.geometry("1700x1000")
    root.iconbitmap('C:\\Users\\MRC\\Pictures\\pictures')
    my_labell1= Label(root, text=""" #create a class called person with attributes name and age. Create an object of the class and print its attributes.abs
class person:
    def __init__(self,name,age,l_name,f_name):
        self.name=name
        self.age=age
        self.L_name=l_name
        self.f_name=f_name
        self.jap="Teacher"  #defult value
 """)


    my_labell1.place(x=350, y=90)

    root.mainloop()
button = (Button(windows, text="First homework of python",
                         command=myClick1,borderwidth=4,
                         fg="black", bg="white", font=17,
                         padx=39, pady=5))  # .place(x=10,y=39))
button.place(x=1, y=63)  # grid(row=1,column=0)


def myClick2():
    from tkinter import Tk
    root2=Tk()
    root2.title("Second homework of python ")
    root2.geometry("1700x1000")
    root2.iconbitmap('C:\\Users\\MRC\\Pictures\\pictures')
    my_labell =Label(root2, text="This is the second home work detal")
    my_labell.place(x=350, y=98)

    root2.mainloop()
button = Button(windows,text="Second homework of python",
                            fg="black", bg="white", font=17,
                            command=myClick2,borderwidth=4,
                            padx=28, pady=5)

button.place(x=1, y=107)

def myClick3():
    from tkinter import Tk
    root3=Tk()
    root3.title("Second homework of python ")
    root3.geometry("1700x1000")
    root3.iconbitmap('C:\\Users\\MRC\\Pictures\\pictures')
    my_labell=Label(root3,text="I am here to help you are")
    my_labell.place(x=350,y=150)
    root3.mainloop()

button=Button(windows,text="Third homework of python",
                  fg="black",bg="white",font=17,
                  command=myClick3,borderwidth=4,
                  padx=37,pady=5)
button.place(x=1,y=150)


def myClick4():
    from tkinter import Tk
    root4=Tk()
    root4.geometry("1700x1000")
    root4.title("The fourth homework of python")
    root4.iconbitmap('C:\\Users\\MRC\\Pictures\\pictures')
    root4.geometry("1700x1000")
    my_labell=Label(root4,text="This place is for write those methods that teacher take us homework")
    my_labell.place(x=350,y=200)
    root4.mainloop()
button=Button(windows,text="Fourth homework of python",
                  fg="black",bg="white",font=17,
                  command=myClick4,borderwidth=4,
                  padx=32,pady=5)
button.place(x=1,y=195)

def myClick5():
    from tkinter import Tk
    root5=Tk()
    root5.geometry("1700x1000")
    root5.title("The fourth homework of python")
    root5.iconbitmap('C:\\Users\\MRC\\Pictures\\pictures')
    root5.geometry("1700x1000")
    my_labell=Label(root5,text="this is the place"
                                     " that you can put homework of yourself.")
    my_labell.place(x=350,y=200)
    root5.mainloop()
button=Button(windows,text="Fifth homework of python",
                  fg="black",bg="white",font=17,
                  command=myClick5,borderwidth=4,
                  padx=39,pady=5)
button.place(x=1,y=240)

def myClick6():
    from tkinter import Tk
    root6=Tk()
    root6.geometry("1700x1000")
    root6.title("The fourth homework of python")
    root6.iconbitmap('C:\\Users\\MRC\\Pictures\\pictures')
    root6.geometry("1700x1000")
    my_labell=Label(root6,text="this is the place"
                                     " that you can put homework of yourself.")
    my_labell.place(x=350,y=200)
    root6.mainloop()
button=Button(windows,text="Six homework of python",
                  fg="black",bg="white",font=17,
                  command=myClick6,borderwidth=4,
                  padx=43,pady=5)
button.place(x=1,y=284)

def myClick7():
    from tkinter import Tk
    root7=Tk()
    root7.geometry("1700x1000")
    root7.title("The fourth homework of python")
    root7.iconbitmap('C:\\Users\\MRC\\Pictures\\pictures')
    root7.geometry("1700x1000")
    my_labell=Label(root7,text="this is the place"
                                     " that you can put homework of yourself.")
    my_labell.place(x=350,y=200)
    root7.mainloop()
button=Button(windows,text="Sevent homework of python",
                  fg="black",bg="white",font=17,
                  command=myClick7,borderwidth=4,
                  padx=30,pady=5)
button.place(x=1,y=329)

def myClick8():
    from tkinter import Tk
    root8=Tk()
    root8.geometry("1700x1000")
    root8.title("The fourth homework of python")
    root8.iconbitmap('C:\\Users\\MRC\\Pictures\\pictures')
    root8.geometry("1700x1000")
    my_labell=Label(root8,text="this is the place"
                                     " that you can put homework of yourself.")
    my_labell.place(x=350,y=200)
    root8.mainloop()
button=Button(windows,text="Eight homework of python",
                  fg="black",bg="white",font=17,
                  command=myClick8,borderwidth=4,
                  padx=36,pady=5)
button.place(x=1,y=373)

def myClick9():
    from tkinter import Tk
    root9=Tk()
    root9.geometry("1700x1000")
    root9.title("The fourth homework of python")
    root9.iconbitmap('C:\\Users\\MRC\\Pictures\\pictures')
    root9.geometry("1700x1000")
    my_labell=Label(root9,text="this is the place"
                                     " that you can put homework of yourself.")
    my_labell.place(x=350,y=200)
    root9.mainloop()
button=Button(windows,text="Ninet homework of python",
                  fg="black",bg="white",font=17,
                  command=myClick9,borderwidth=4,
                  padx=36,pady=5)
button.place(x=1,y=417)

def myClick10():
    from tkinter import Tk
    root10=Tk()
    root10.geometry("1700x1000")
    root10.title("The fourth homework of python")
    root10.iconbitmap('C:\\Users\\MRC\\Pictures\\pictures')
    root10.geometry("1700x1000")
    my_labell=Label(root10,text="this is the place"
                                     " that you can put homework of yourself.")
    my_labell.place(x=350,y=200)
    root10.mainloop()
button=Button(windows,text="Ten homework of python",
                  fg="black",bg="white",font=17,
                  command=myClick10,borderwidth=4,
                  padx=41,pady=5)
button.place(x=1,y=460)

def quit_button():
    return windows.quit()

button_quit=Button(windows,text="Exit",bg="white",fg="blue",borderwidth=4,command=quit_button,
                   padx=117,pady=5)
button_quit.place(x=1,y=505)

windows.mainloop()