from tkinter import *
from PIL import Image, ImageTk


def main():
    root = Tk()
    root.title('Password Generator')
    root.iconbitmap('padlock.ico')

    img = ImageTk.PhotoImage(Image.open('bg.jpg'))

    canvas = Canvas(root, width=899, height=513)
    canvas.create_image(0, 0, anchor=NW, image=img)

    canvas.create_text(50, 30, anchor=NW, text='Password Generator', font=('times', 30), fill='yellow',
                       activefill='white', justify=CENTER)

    canvas.create_text(50, 110, text='Your First Name:', fill='papaya whip', font=('ariel', 20), anchor=NW)
    e1 = Entry(bd=3, fg='black', justify=LEFT, relief=RIDGE, font=('algerian', 20))
    canvas.create_window(50, 150, window=e1, anchor=NW)

    canvas.create_text(50, 240, text='Your Email-ID:', fill='papaya whip', font=('ariel', 20), anchor=NW)
    e2 = Entry(bd=3, fg='black', justify=LEFT, relief=RIDGE, font=('footlight mt light', 20))
    canvas.create_window(50, 280, window=e2, anchor=NW)

    canvas.create_text(50, 370, text='Site Name:', fill='papaya whip', font=('ariel', 20), anchor=NW)
    e3 = Entry(bd=3, fg='black', justify=LEFT, relief=RIDGE, font=('algerian', 20))
    canvas.create_window(50, 410, window=e3, anchor=NW)

    canvas.create_text(600, 110, text='Password length:', fill='papaya whip', font=('ariel', 18), anchor=NW)
    e4 = Entry(bd=3, fg='black', justify=CENTER, relief=RAISED, font=('algerian', 14), width=16)
    e4.insert(0, '10')
    canvas.create_window(600, 150, window=e4, anchor=NW)

    def click():
        fname = e1.get()
        email = e2.get()
        sname = e3.get()
        l = int(e4.get())
        txt = fname.upper() + '_' + '12345' + sname + '67890' + ';?' + email
        enc_txt = encode(txt)
        password = ''
        skip=1
        if len(enc_txt)<=20:
            skip=1
        elif len(enc_txt)>20 and len(enc_txt)<=30:
            skip=2
        elif len(enc_txt)>30:
            skip=3

        for x in range(0, len(enc_txt), skip):
            password += enc_txt[x]
            if len(password) == l:
                password=password.swapcase()
                break

        print_pass(password)

    def print_pass(password):
        canvas.pack_forget()
        newCanvas=Canvas(root, width=899, height=513)
        newCanvas.create_image(0, 0, anchor=NW, image=img)

        newCanvas.create_text(50, 30, anchor=NW, text='Password Generator', font=('times', 30), fill='yellow',
                       activefill='white', justify=CENTER)

        newCanvas.create_text(50, 230, text= 'Generated password:',fill='#6699ff', font=('castellar', 18), anchor=NW, activefill='#ccddff')

        show=Entry(bd=5, fg='red', justify=CENTER, relief=GROOVE, font=('goudy old style', 20, 'bold'), show='*')
        show.insert(0, password)
        newCanvas.create_window(50, 280, anchor=NW, window=show)

        def change():
            show['show']=''
            show_button['state']=DISABLED

            Exit=Button(text='Exit', font=('pristina', 14, 'bold'), bg='light yellow', command=root.quit)
            newCanvas.create_window(845, 15, anchor=NW, window=Exit)

        show_button=Button(text='Show', bg='deep sky blue', font=('prussian', 16), bd=5, activebackground='light blue', padx=4, command=change)
        newCanvas.create_window(380, 280, anchor=NW, window=show_button)

        newCanvas.create_text(50, 450, text='**Enter the same details next time to retrieve this password**', font=('gabriola', 22, 'underline'), fill='white', anchor=NW, activefill='grey')

        newCanvas.pack()

    def encode(str):
        txt = 'abcdefghijklmnopqrstuvwxyz@$.?;_!1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        enc = 'qwertyuiopasdfghjklzxcvbnm.!_;@$?0789456123QWERTYUIOPASDFGHJKLZXCVBNM'
        x = ''

        enc_tbl = x.maketrans(txt, enc)
        enc_txt = str.translate(enc_tbl)
        return enc_txt

    button = Button(text='Continue >>', width=10, bg='deep sky blue', font=('prussian', 19), bd=7,
                    activebackground='light green', padx=9, command=click)
    canvas.create_window(600, 250, anchor=NW, window=button)

    canvas.pack(expand=True)
    root.mainloop()


if __name__ == '__main__':
    main()
