from tkinter import *

def user_register():
    user_info = username.get()
    password_info = password.get()

    file = open(user_info + '.txt', 'w')
    file.write(user_info + '\n')
    file.write(password_info)
    file.close()


    Label(screen1, text='Registration Succesfully', height='2', width='30').pack()

def register():
    global username
    global password
    global screen1

    screen1 = Toplevel(screen)
    screen1.title('Register Form')
    screen1.geometry('300x250')
    
    username = StringVar()
    password = StringVar()
    Label(screen1, text='Register Form', height='2', width='300', bg='green', font=('calibri', 15)).pack()
    Label(screen1, text='').pack()
    Label(screen1, text='Username').pack()
    user_entry = Entry(screen1, textvariable=username)
    user_entry.pack()
    Label(screen1, text='').pack()
    Label(screen1, text='Password').pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text='').pack()
    Button(screen1, text="Register", height='2', width='30',bg='gray', command=user_register).pack()



def login():
    print('login')
def main_screen():
    global screen

    screen = Tk()
    screen.title('Form')
    screen.geometry('300x250')

    Label(text="Form", height='2', width='300', bg='green', font=('calibri', 15)).pack()
    Label(text='').pack()
    Button(text="Login", height='2', width='30',bg='gray', command = login).pack()
    Label(text='').pack()
    Button(text="Register", height='2', width='30', bg='gray', command=register).pack()

    screen.mainloop()
main_screen()