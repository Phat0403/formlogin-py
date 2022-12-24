
import tkinter
import ast
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#95a5a6")
root.resizable(False,False)
#hình nền của đăng nhập
path='D:\python\python dang nhap\Main login\login.png'
img = Image.open(path)
img = img.resize((450, 500), 	Image.Resampling.LANCZOS)
test = ImageTk.PhotoImage(img)
Label(root, image=test, bg='#95a5a6').place(x=0, y=0)
#@@@@@@@@@@@@@@@@@@@
frame=Frame(root,width=350, height=350, bg='white')
frame.place(x=480, y=70)
heading=Label(frame,text='LOGIN',fg='#57a18f',bg='white',font=('Comic Sans MS',23, 'bold'))
heading.place(x=120,y=5)



#######################################____________________________
def signin():
    username=user.get()
    password=code.get()

    file =open('datasheet.txt', 'r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
    # print(r.keys())
    # print(r.values()) 
    if username in r.keys() and password==r[username]:
        print('Phat dep trai')
    else:
        messagebox.showerror('Invalid','Invalid username or password')
def signup_command():
                  #Dang ki
    window=Toplevel(root)
    window.title('Sign Up')
    window.geometry('925x500+300+200')
    window.configure(bg="#95a5a6")
    window.resizable(False,False)

    def signup():
        username=user.get()
        password=code.get()
        conform=conform_code.get()

        if password==conform:
            try:

                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt','w')
                w=file.write(str(r))
                messagebox.showinfo('Signup','Sucessfully sign up')
                window.destroy()
            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'Password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid','Both Password should match')
    def sign():
        window.destroy()

    #hiÌ€nh nÃªÌ€n cuÌ‰a Ä‘Äƒng nhÃ¢Ì£p
    path='D:\python\python dang nhap\Main login\signup.png'
    img1 = Image.open(path)
    img1 = img1.resize((450, 500), 	Image.Resampling.LANCZOS)
    test1 = ImageTk.PhotoImage(img1)
    Label(window, image=test1, bg='#95a5a6').place(x=0, y=0)

    frame=Frame(window, width=350, height=350, bg='white')
    frame.place(x=480,y=50)

    heading=Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Comic Sans MS',23, 'bold'))
    heading.place(x=120,y=5)
    ################------------------------1
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')
    user=Entry(frame, width=25, fg='black',border=0,bg='white', font=('Comic Sans MS',11))
    user.place(x=30,y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    ################------------------------2
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')
    code=Entry(frame, width=25, fg='black',border=0,bg='white' ,font=('Comic Sans MS',11))
    code.place(x=30,y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    ################------------------------3
    def on_enter(e):
        conform_code.delete(0,'end')
    def on_leave(e):
        if conform_code.get()=='':
            conform_code.insert(0,'Conform password')
    conform_code=Entry(frame, width=25, fg='black',border=0,bg='white', font=('Comic Sans MS',11))
    conform_code.place(x=30,y=220)
    conform_code.insert(0, 'Conform password')
    conform_code.bind('<FocusIn>',on_enter)
    conform_code.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    ################------------------------
    Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',command=signup,border=0).place(x=35,y=280)
    label=Label(frame,text='I have an account ? ', fg='black',bg='white', font=('Comic Sans MS',9))
    label.place(x=90,y=320)

    signin=Button(frame,width=6,text='Sign in', border=0,bg='white',cursor='hand2',command=sign,fg='#57a1f8')
    signin.place(x=200,y=320)
    ################------------------------

    window.mainloop()


#het phan dang ki
##########--------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user=Entry(frame, width=25, fg='black',border=0,bg='white',font=('Comic Sans MS',11))
user.place(x=30,y=80)
user.insert(0,'User name')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2, bg='black').place(x=25,y=107)

###########---------------------------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
code=Entry(frame, width=25, fg='black',border=0,bg='white',font=('Comic Sans MS',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2, bg='black').place(x=25,y=177)

###########-----------------------------------------

Button(frame,width=39,pady=7, text='Sign in',bg='#57a1f8',fg='black',command=signin,border=0).place(x=35, y=204)
label1=Label(frame,text="Don't have account ?",fg='black',bg='white',font=('cambria',9))
label1.place(x=75,y=270)

sign_up=Button(frame,width=6, text='Sign Up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)
root.mainloop()