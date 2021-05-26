import random
from tkinter import *
from PIL import Image, ImageTk


def RPS():
    global root
    global P1_label, P2_label, label_list
    global P1_pts, P2_pts, Status_label, Score
    global button_paper, button_rock, button_scissor
    global img_rock, img_paper, img_scissor
    root = Tk()
    root.title('Stone Paper Scissor')
    root.configure(bg='#ffff99')
    root.geometry('800x600')
    root.resizable(0, 0)

    exit_button = Button(root, text='Exit', font=("Times", "10", "bold italic"), command=root.quit)
    exit_button.place(x=750, y=10)

    global sps
    sps = ['rock', 'paper', 'scissor']
    P1_pts = 0
    P2_pts = 0

    P1_label = Label(root, bg='#ffff99')
    P2_label = Label(root, bg='#ffff99')

    P1_label.place(x=200, y=200)
    P2_label.place(x=500, y=200)

    Status_label = Label(root, bg='#ffff99')
    Status_label.place(x=0, y=0)

    Heading= Label(root, text='***Rock Paper Scissor***', font=('Algerian',26), bg='#ffff99')
    Heading.place(x=200, y=10)

    Score = Label(root, text=str(P1_pts) + ' : ' + str(P2_pts), bg='#ffff99', font=("Times", "36", "bold italic"))
    Score.place(x=360, y=70)

    Start_label=Label(root, text='Click on any button to start!', bg='#ffff99', font=('ariel', 30, 'bold'))
    Start_label.place(x=150, y=250)

    def play(P1):
        if Start_label.winfo_exists():
            Start_label.destroy()

        global sps
        global P1_label, P2_label, label_list
        global P1_pts, P2_pts, Status_label, Score
        global button_paper, button_rock, button_scissor
        global img_rock, img_paper, img_scissor
        P1_label.destroy()
        Status_label.destroy()
        Score.destroy()

        P2 = random.choice(sps)
        P1_index = sps.index(P1)

        label_rock = Label(root, image=img_rock, borderwidth=4, relief='solid')
        label_paper = Label(root, image=img_paper, borderwidth=4, relief='solid')
        label_scissor = Label(root, image=img_scissor, borderwidth=4, relief='solid')

        label_list = [label_rock, label_paper, label_scissor]

        P1_label = label_list[P1_index]
        P1_label.place(x=200, y=200)

        res = Calc(P1, P2)
        if res == 0:  # Draw
            Status_label = Label(root, text='Draw', font=('times', 25, 'bold italic'), bg='#ffff99', fg='blue')
            Status_label.place(x=370, y=230)
        elif res == 1:  # Player
            Status_label = Label(root, text='Win', font=('times', 25, 'bold italic'), bg='#ffff99', fg='Red')
            Status_label.place(x=220, y=330)
            P1_pts += 1
        elif res == 2:  # Computer
            Status_label = Label(root, text='Win', font=('times', 25, 'bold italic'), bg='#ffff99', fg='Red')
            Status_label.place(x=520, y=330)
            P2_pts += 1

        # Score Update
        Score = Label(root, text=str(P1_pts) + ' : ' + str(P2_pts), bg='#ffff99', font=("Times", "37", "bold italic"))
        Score.place(x=360, y=70)

        if P1_pts == 10 or P2_pts == 10:
            button_paper['state'] = DISABLED
            button_rock['state'] = DISABLED
            button_scissor['state'] = DISABLED
            Status_label.destroy()
            Final_label = Label(root, text='Win', font=('times', 35, 'bold italic underline'), bg='#ffff99', fg='Red')
            if P1_pts == 10:
                Final_label.place(x=215, y=330)
            else:
                Final_label.place(x=515, y=330)

            restart_button = Button(root, text='Restart', font=('calibri', 25, 'bold'), command=restart)
            restart_button.place(x=0, y=0)

    def Calc(P1, P2):
        global sps, P2_label

        label_rock2 = Label(root, image=img_rock, borderwidth=4, relief='solid')
        label_paper2 = Label(root, image=img_paper, borderwidth=4, relief='solid')
        label_scissor2 = Label(root, image=img_scissor, borderwidth=4, relief='solid')

        label_list2 = [label_rock2, label_paper2, label_scissor2]

        P2_index = sps.index(P2)
        P2_label.destroy()
        P2_label = label_list2[P2_index]
        P2_label.place(x=500, y=200)

        if P1 == sps[0]:  # stone
            if P2 == sps[0]:
                return 0  # draw
            elif P2 == sps[1]:
                return 2  # P2 win
            elif P2 == sps[2]:
                return 1  # P1 win

        elif P1 == sps[1]:  # paper
            if P2 == sps[0]:
                return 1  # p1 win
            elif P2 == sps[1]:
                return 0  # draw
            elif P2 == sps[2]:
                return 2  # P2 win

        elif P1 == sps[2]:  # scissor
            if P2 == sps[0]:
                return 2  # p2 win
            elif P2 == sps[1]:
                return 1  # p1 win
            elif P2 == sps[2]:
                return 0  # draw

    img_paper = ImageTk.PhotoImage(Image.open('image/Paper.png'))
    img_rock = ImageTk.PhotoImage(Image.open('image/Rock.png'))
    img_scissor = ImageTk.PhotoImage(Image.open('image/Scissor.png'))

    label_rock = Label(root, text='Rock', font=('Algerian', 20), bg='#ffff99', fg='black')
    label_rock.place(x=365, y=410)
    label_paper = Label(root, text='paper', font=('Algerian', 20), bg='#ffff99', fg='black')
    label_paper.place(x=135, y=410)
    label_scissor = Label(root, text='scissor', font=('Algerian', 20), bg='#ffff99', fg='black')
    label_scissor.place(x=555, y=410)

    button_paper = Button(root, image=img_paper, command=lambda: play('paper'))
    button_paper.place(x=120, y=450)
    button_rock = Button(root, image=img_rock, command=lambda: play('rock'))
    button_rock.place(x=350, y=450)
    button_scissor = Button(root, image=img_scissor, command=lambda: play('scissor'))
    button_scissor.place(x=550, y=450)

    label_Player = Label(root, text=player.capitalize(), font=('times', 30, 'bold italic'), bg='#ffff99', fg='black', justify=CENTER, width=10)
    label_Player.place(x=140, y=150)
    label_Player = Label(root, text='Computer', font=('times', 30, 'bold italic'), bg='#ffff99', fg='black')
    label_Player.place(x=470, y=150)

    root.mainloop()

def start():
    global root1
    root1 = Tk()
    root1.title('Stone Paper Scissor')
    root1.configure(bg='#ffff99')
    root1.geometry('400x400')
    root1.resizable(0, 0)
    player=''

    def cont():
        global player
        player=e.get()
        root1.destroy()

    Name_label=Label(root1, text='::Enter Your Name::', font=("Times", "26", "bold"), bg='#ffff99')
    Name_label.place(x=40, y=90)

    exit_button = Button(root1, text='Exit', font=("Times", "10", "bold italic"), command=root1.quit)
    exit_button.place(x=350, y=10)

    e=Entry(root1, bd=3, font=('Roman', 20, 'bold'), bg='white', justify='center', relief='groove')
    e.place(x=70,y=140)

    cont_button=Button(root1, text='Continue >>', bg='light blue', fg='black', bd=3, relief='raised', font=('Helvatica', 12), command=cont)
    cont_button.place(x=160, y=190)

    root1.mainloop()


if __name__ == '__main__':
    def restart():
        root.destroy()
        RPS()


    try:
        start()
        RPS()
    except:
        pass