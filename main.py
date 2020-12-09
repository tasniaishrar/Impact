from PIL import ImageTk, Image
import random
from tkinter import Tk, Button, Label, Menu, Frame, Radiobutton, StringVar, PhotoImage, Canvas

root = Tk()
root.title("Let's make an imPACT!")
root.geometry("1000x1000")

#Setting window icon
icon = PhotoImage(file='logo/imPACT icon.png')
root.iconphoto(False, icon)


#Setting BG
filename = ImageTk.PhotoImage(Image.open("logo/main bg.png"))
background_label = Label(root, image=filename)
background_label.image = filename
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Empty arrays to prevent repetition of cards in each session
racism_shown = []
gen_ineq_shown = []
homophobia_shown = []
classism_shown = []

#Creating racism functions
def racism():
    hide_frames()
    racism_frame.pack(fill="both", expand=1)
    my_label = Label(racism_frame, text="Racism").pack()
    filename = ImageTk.PhotoImage(Image.open("logo/default bg.png"))
    background_label = Label(racism_frame, image=filename)
    background_label.image = filename
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #To prevent repetition of cards
    global rando
    rando = random.randint(1,7)
    while (rando in racism_shown):
        rando = random.randint(1, 7)
    racism_shown.append(rando)
    #dislay image
    global racism_pic
    racism_pic = ImageTk.PhotoImage(Image.open('racism/'+str(rando)+'.png'))
    show_pic = Label(racism_frame, image=racism_pic)
    show_pic.pack(pady=30)


    #Create radio answer buttons
    global racism_radio
    racism_radio = StringVar()
    racism_radio.set('Yes')
    racism_radio_butto1 = Radiobutton(racism_frame,text='Yes',variable=racism_radio,value='Yes').pack()
    racism_radio_butto2 = Radiobutton(racism_frame,text='No',variable=racism_radio,value='No').pack()

    #Create answer button
    racism.answer_button_pic = PhotoImage(file='buttons/button_answer.png')
    answer_button = Button(racism_frame, image = racism.answer_button_pic, command = racism_answer,borderwidth=0).pack(pady=20)

def racism_answer():
    if (racism_radio.get() =='Yes'):
        hide_frames()
        racism_frame.pack(fill="both", expand=1)

        filename = ImageTk.PhotoImage(Image.open("logo/default bg.png"))
        background_label = Label(racism_frame, image=filename)
        background_label.image = filename
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        my_label = Label(racism_frame, text="Let's see why it's wrong!").pack()
        # dislay image
        global racism_pic
        racism_pic = ImageTk.PhotoImage(Image.open('racism/ans'+str(rando)+'.png'))
        show_pic = Label(racism_frame, image=racism_pic)
        show_pic.pack(pady=15)

    elif (racism_radio.get() == 'No'):
        hide_frames()
        racism_frame.pack(fill="both", expand=1)

        filename = ImageTk.PhotoImage(Image.open("logo/default bg.png"))
        background_label = Label(racism_frame, image=filename)
        background_label.image = filename
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        my_label = Label(racism_frame, text="Since none of you faced this, let's move on to the next card!").pack()
        # display image
        racism_pic = ImageTk.PhotoImage(Image.open('racism/'+str(rando)+'.png'))
        show_pic = Label(racism_frame, image=racism_pic)
        show_pic.pack(pady=15)

    # Create buttons to generate randomized cards
    racism_answer.button_pic = PhotoImage(file='buttons/button_next-card.png')
    answer_button = Button(racism_frame, image=racism_answer.button_pic, command=racism, borderwidth=0).pack()
    #Display logo
    #racism_answer.logo_pic = ImageTk.PhotoImage(Image.open('logo/imPACT logo.png'))
    #show_logo = Label(racism_frame, image=racism_answer.logo_pic).pack(pady=10)

    racism_answer.end_button_pic = PhotoImage(file='buttons/button_end.png')
    end_button = Button(racism_frame, image = racism_answer.end_button_pic, command= end, borderwidth=0).pack(pady=10)


#Creating gender inequality function
def gen_ineq():
    hide_frames()
    gen_ineq_frame.pack(fill="both",expand=1)
    my_label = Label(gen_ineq_frame, text="Gender Inequality").pack()

    filename = ImageTk.PhotoImage(Image.open("logo/default bg.png"))
    background_label = Label(gen_ineq_frame, image=filename)
    background_label.image = filename
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #To prevent repetition of cards
    global rando1
    rando1 = random.randint(1,9)
    while (rando1 in gen_ineq_shown):
        rando1 = random.randint(1, 9)
    gen_ineq_shown.append(rando1)
    #display image
    global gen_ineq_pic
    gen_ineq_pic = ImageTk.PhotoImage(Image.open('gender/'+str(rando1)+'.png'))
    show_pic = Label(gen_ineq_frame, image=gen_ineq_pic)
    show_pic.pack(pady=30)


    #Create radio answer buttons
    global gen_radio
    gen_radio = StringVar()
    gen_radio.set('Yes')
    gen_butto1 = Radiobutton(gen_ineq_frame,text='Yes',variable=gen_radio,value='Yes').pack()
    gen_butto2 = Radiobutton(gen_ineq_frame,text='No',variable=gen_radio,value='No').pack()

    #Create answer button
    gen_ineq.answer_button_pic = PhotoImage(file='buttons/button_answer.png')
    answer_button = Button(gen_ineq_frame, image = gen_ineq.answer_button_pic, command = gen_answer,borderwidth=0).pack(pady=20)

def gen_answer():
    if (gen_radio.get() =='Yes'):
        hide_frames()
        gen_ineq_frame.pack(fill="both", expand=1)
        my_label = Label(gen_ineq_frame, text="Let's see why it's wrong!").pack()

        filename = ImageTk.PhotoImage(Image.open("logo/default bg.png"))
        background_label = Label(gen_ineq_frame, image=filename)
        background_label.image = filename
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # display image
        global gen_ineq_pic
        gen_ineq_pic = ImageTk.PhotoImage(Image.open('gender/ans'+str(rando1)+'.png'))
        show_pic = Label(gen_ineq_frame, image=gen_ineq_pic)
        show_pic.pack(pady=30)
    elif (gen_radio.get() == 'No'):
        hide_frames()
        gen_ineq_frame.pack(fill="both", expand=1)
        my_label = Label(racism_frame, text="Since none of you faced this, let's move on to the next card!").pack()

        filename = ImageTk.PhotoImage(Image.open("logo/default bg.png"))
        background_label = Label(gen_ineq_frame, image=filename)
        background_label.image = filename
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # dislay image
        gen_ineq_pic = ImageTk.PhotoImage(Image.open('gender/'+str(rando1)+'.png'))
        show_pic = Label(gen_ineq_frame, image=gen_ineq_pic)
        show_pic.pack(pady=30)

    # Create buttons to generate randomized cards
    gen_answer.button_pic = PhotoImage(file='buttons/button_next-card.png')
    answer_button = Button(gen_ineq_frame, image=gen_answer.button_pic, command=gen_ineq, borderwidth=0).pack()

    gen_answer.end_button_pic = PhotoImage(file='buttons/button_end.png')
    end_button = Button(gen_ineq_frame, image = gen_answer.end_button_pic, command= end, borderwidth=0).pack(pady=10)


#Creating homophobia function
def homophobia():
    hide_frames()
    homophobia_frame.pack(fill="both", expand=1)
    my_label = Label(homophobia_frame, text="Homophobia").pack()

    filename = ImageTk.PhotoImage(Image.open("logo/default bg.png"))
    background_label = Label(homophobia_frame, image=filename)
    background_label.image = filename
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Prevents repetiton of cards
    global rando2
    rando2 = random.randint(1, 3)
    while (rando2 in homophobia_shown):
        rando2 = random.randint(1, 3)
    homophobia_shown.append(rando2)
    # display image
    global homophobia_pic
    homophobia_pic = ImageTk.PhotoImage(Image.open('homophobia/' + str(rando2) + '.png'))
    show_pic = Label(homophobia_frame, image=homophobia_pic)
    show_pic.pack(pady=30)

    # Create radio answer buttons
    global homophobia_radio
    homophobia_radio = StringVar()
    homophobia_radio.set('Yes')
    hom_butto1 = Radiobutton(homophobia_frame, text='Yes', variable=homophobia_radio, value='Yes').pack()
    hom_butto2 = Radiobutton(homophobia_frame, text='No', variable=homophobia_radio, value='No').pack()

    # Create answer button
    homophobia.answer_button_pic = PhotoImage(file='buttons/button_answer.png')
    answer_button = Button(homophobia_frame, image=homophobia.answer_button_pic, command=homophobia_answer, borderwidth=0).pack(pady=20)

def homophobia_answer():
    if (homophobia_radio.get() =='Yes'):
        hide_frames()
        homophobia_frame.pack(fill="both", expand=1)
        my_label = Label(homophobia_frame, text="Let's see why it's wrong!").pack()

        filename = ImageTk.PhotoImage(Image.open("logo/default bg.png"))
        background_label = Label(homophobia_frame, image=filename)
        background_label.image = filename
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # display image
        global homophobia_pic
        homophobia_pic = ImageTk.PhotoImage(Image.open('homophobia/ans'+str(rando2)+'.png'))
        show_pic = Label(homophobia_frame, image=homophobia_pic)
        show_pic.pack(pady=30)
    elif (homophobia_radio.get() == 'No'):
        hide_frames()
        homophobia_frame.pack(fill="both", expand=1)
        my_label = Label(homophobia_frame, text="Since none of you faced this, let's move on to the next card!").pack()

        filename = ImageTk.PhotoImage(Image.open("logo/default bg.png"))
        background_label = Label(homophobia_frame, image=filename)
        background_label.image = filename
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # display image
        homophobia_pic = ImageTk.PhotoImage(Image.open('homophobia/'+str(rando2)+'.png'))
        show_pic = Label(homophobia_frame, image=homophobia_pic)
        show_pic.pack(pady=30)

    # Create buttons to generate randomized cards
    homophobia_answer.button_pic = PhotoImage(file='buttons/button_next-card.png')
    answer_button = Button(homophobia_frame, image=homophobia_answer.button_pic, command=homophobia, borderwidth=0).pack()

    homophobia_answer.end_button_pic = PhotoImage(file='buttons/button_end.png')
    end_button = Button(homophobia_frame, image = homophobia_answer.end_button_pic, command= end, borderwidth=0).pack(pady=10)


#Creating classism functions
def classism():

    hide_frames()
    classism_frame.pack(fill="both", expand=1)
    my_label = Label(classism_frame, text="Classism").pack()

    filename = ImageTk.PhotoImage(Image.open("logo/default bg.png"))
    background_label = Label(classism_frame, image=filename)
    background_label.image = filename
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Prevents card repetiton
    global rando3
    rando3 = random.randint(1, 5)
    while (rando3 in classism_shown):
        rando3 = random.randint(1, 5)
    classism_shown.append(rando3)

    # display image
    global classism_pic
    classism_pic = ImageTk.PhotoImage(Image.open('classism/' + str(rando3) + '.png'))
    show_pic = Label(classism_frame, image=classism_pic)
    show_pic.pack(pady=30)

    # Create radio answer buttons
    global classism_radio
    classism_radio = StringVar()
    classism_radio.set('Yes')
    class_butto1 = Radiobutton(classism_frame, text='Yes', variable=classism_radio, value='Yes').pack()
    class_butto2 = Radiobutton(classism_frame, text='No', variable=classism_radio, value='No').pack()

    # Create answer button
    classism.answer_button_pic = PhotoImage(file='buttons/button_answer.png')
    answer_button = Button(classism_frame, image=classism.answer_button_pic, command=classism_answer, borderwidth=0).pack(pady=20)

def classism_answer():
    if (classism_radio.get() =='Yes'):
        hide_frames()
        classism_frame.pack(fill="both", expand=1)
        my_label = Label(classism_frame, text="Let's see why it's wrong!").pack()

        filename = ImageTk.PhotoImage(Image.open("logo/default bg.png"))
        background_label = Label(classism_frame, image=filename)
        background_label.image = filename
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # display image
        global classism_pic
        classism_pic = ImageTk.PhotoImage(Image.open('classism/ans'+str(rando3)+'.png'))
        show_pic = Label(classism_frame, image=classism_pic)
        show_pic.pack(pady=30)
    elif (classism_radio.get() == 'No'):
        hide_frames()
        classism_frame.pack(fill="both", expand=1)
        my_label = Label(classism_frame, text="Since none of you faced this, let's move on to the next card!").pack()

        filename = ImageTk.PhotoImage(Image.open("logo/default bg.png"))
        background_label = Label(classism_frame, image=filename)
        background_label.image = filename
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # display image
        classism_pic = ImageTk.PhotoImage(Image.open('classism/'+str(rando3)+'.png'))
        show_pic = Label(classism_frame, image=classism_pic)
        show_pic.pack(pady=30)

    # Create buttons to generate randomized cards
    classism_answer.button_pic = PhotoImage(file='buttons/button_next-card.png')
    answer_button = Button(classism_frame, image=classism_answer.button_pic, command=classism, borderwidth=0).pack()

    classism_answer.end_button_pic = PhotoImage(file='buttons/button_end.png')
    end_button = Button(classism_frame, image = classism_answer.end_button_pic, command= end, borderwidth=0).pack(pady=10)

def end():
    hide_frames()
    end_frame.pack(fill="both",expand=1)
    my_label = Label(end_frame, text="End Session").pack()

    filename = ImageTk.PhotoImage(Image.open("logo/end.png"))
    background_label = Label(end_frame, image=filename)
    background_label.image = filename
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    end.answer_button_pic = PhotoImage(file='buttons/button_exit.png')
    answer_button = Button(end_frame, image = end.answer_button_pic, command = off,borderwidth=0).pack(pady=(505,0))

def off():
    root.quit()

#Creating app menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Menu items
topic_menu = Menu(my_menu)
my_menu.add_cascade(label="Topic",menu=topic_menu)
topic_menu.add_command(label="Racism",command=racism)
topic_menu.add_command(label="Gender Inequality", command=gen_ineq)
topic_menu.add_command(label="Homophobia", command=homophobia)
topic_menu.add_command(label="Classism", command=classism)
topic_menu.add_separator()

#Creating frames
racism_frame = Frame(root, width=1000,height=1000)
gen_ineq_frame = Frame(root, width=1000,height=1000)
homophobia_frame = Frame(root, width=1000,height=1000)
classism_frame = Frame(root, width=1000, height=1000)
end_frame = Frame(root, width=1000, height=1000)

#Hide previous frames
def hide_frames():
    for widget in racism_frame.winfo_children():
        widget.destroy()
    for widget in gen_ineq_frame.winfo_children():
        widget.destroy()
    for widget in homophobia_frame.winfo_children():
        widget.destroy()
    for widget in classism_frame.winfo_children():
        widget.destroy()
    for widget in end_frame.winfo_children():
        widget.destroy()
    racism_frame.pack_forget()
    gen_ineq_frame.pack_forget()
    homophobia_frame.pack_forget()
    classism_frame.pack_forget()
    end_frame.pack_forget()


root.mainloop()
