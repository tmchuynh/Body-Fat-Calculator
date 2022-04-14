from tkinter import *
from tkinter import messagebox
import math


def calculate_male():
    age = int(age_tf.get())
    height = float(height_tf.get())

    lb = float(weight_tf.get())

    hip = float(hip_tf.get())
    neck = float(neck_tf.get())
    waist = float(waist_tf.get())

    m1 = waist - neck;
    first_half = 86.010 * (math.log10(m1))

    second_half = 70.041 * (math.log10(height))

    BFP = first_half - second_half + 36.76

    indexBF_M(BFP)
    
def calculate_female():
    age = int(age_tf.get())
    height = float(height_tf.get())

    lb = float(weight_tf.get())

    hip = float(hip_tf.get())
    neck = float(neck_tf.get())
    waist = float(waist_tf.get())

    m1 = waist + hip - neck;
    first_half = 163.205 * (math.log10(m1))

    second_half = 97.684 * (math.log10(height))

    BFP = first_half - second_half - 78.387

    indexBF_F(BFP)

def indexBF_F(BFP):
    if (BFP > 10) and (BFP < 13):
        messagebox.showinfo('Body Fat Estimate', f'BFP = {BFP} is called essential fat')
    elif (BFP > 14) and (BFP < 20):
        messagebox.showinfo('Body Fat Estimate', f'BFP = {BFP} is within the athletes range')
    elif (BFP > 21) and (BFP < 24):
        messagebox.showinfo('Body Fat Estimate', f'BFP = {BFP} is considered in the fitness level')
    elif (BFP > 25) and (BFP < 31):
        messagebox.showinfo('Body Fat Estimate', f'BFP = {BFP} is average')
    elif (BFP > 32):
        messagebox.showinfo('Body Fat Estimate', f'BFP = {BFP} is  obese') 
    else:
        messagebox.showerror('Body Fat Estimate', 'something went wrong!')

def indexBF_M(BFP):
    if (BFP > 2) and (BFP < 5):
        messagebox.showinfo('Body Fat Estimate', f'BFP = {BFP} is called essential fat')
    elif (BFP > 6) and (BFP < 13):
        messagebox.showinfo('Body Fat Estimate', f'BFP = {BFP} is within the athletes range')
    elif (BFP > 14) and (BFP < 17):
        messagebox.showinfo('Body Fat Estimate', f'BFP = {BFP} is considered in the fitness level')
    elif (BFP > 18) and (BFP < 24):
        messagebox.showinfo('Body Fat Estimate', f'BFP = {BFP} is average')
    elif (BFP > 25):
        messagebox.showinfo('Body Fat Estimate', f'BFP = {BFP} is  obese') 
    else:
        messagebox.showerror('Body Fat Estimate', 'something went wrong!') 
        
def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

ws = Tk()
ws.title('Body Fat Calculator')
ws.geometry('400x300')
ws.config(bg='#686e70')

var = IntVar()

frame = Frame(
    ws,
    padx=10, 
    pady=10
)
frame.pack(expand=True)

frame2 = Frame(
    frame
)

select_lb = Label(
    frame2,
    text='Select Gender'
)

male_rb = Checkbutton(
    frame2,
    text = 'Male',
    variable = var,
    onvalue = 1,
    offvalue = 0,
    command = calculate_male
)

female_rb = Checkbutton(
    frame2,
    text = 'Female',
    variable = var,
    onvalue = 2,
    offvalue = 0,
    command = calculate_female
)

frame3 = Frame(
    frame
)

age_lb = Label(
    frame3,
    text="Enter Age (2 - 120)     "
)

age_tf = Entry(
    frame3, 
)

frame4 = Frame(
    frame
)

height_lb = Label(
    frame4,
    text="Enter Height (inches)  "
)

weight_lb = Label(
    frame4,
    text="Enter Weight (lbs)  "
)

height_tf = Entry(
    frame4,
)

weight_tf = Entry(
    frame4,
)

frame5 = Frame(
    frame
)

frame6 = Frame(
    frame
)

neck_tf = Entry(
    frame5,
)

neck_lb = Label(
    frame5,
    text="Enter neck measurements (inches)  "
)

waist_tf = Entry(
    frame6,
)

waist_lb = Label(
    frame6,
    text="Enter waist measurements (inches)  "
)

frame7 = Frame(
    frame
)

hip_lb = Label(
    frame7,
    text="Enter hip measurements (inches)  "
)

hip_tf = Entry(
    frame7,
)

frame2.grid(row=0, column=2, pady=5)
select_lb.grid(row=1, column=0)
male_rb.grid(row=1, column=1)
female_rb.grid(row=1, column=2)

frame3.grid(row=1, column=2, pady=3)
age_lb.grid(row=1, column=0)
age_tf.grid(row=1, column=2, pady=5)

frame4.grid(row=2, column=2)
height_lb.grid(row=1, column=1)
weight_lb.grid(row=2, column=1)
height_tf.grid(row=1, column=2, pady=5)
weight_tf.grid(row=2, column=2, pady=5)

frame5.grid(row=3, column=2, pady=5)
waist_lb.grid(row=1, column=1)
waist_tf.grid(row=1, column=2)

frame7.grid(row=4, column=2, pady=5)
hip_lb.grid(row=1, column=1)
hip_tf.grid(row=1, column=2)

frame6.grid(row=5, column=2, pady=5)
neck_lb.grid(row=1, column=1)
neck_tf.grid(row=1, column=2)



frame2.grid(row=6, columnspan=3, pady=10)

ws.mainloop()