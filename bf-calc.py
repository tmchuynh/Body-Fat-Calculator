from tkinter import *
from tkinter import messagebox

def calculate_us_BMI():
    lb = int(weight_tf.get())
    feet = float(height_tf.get())
    inch = feet * 12
    bmi = (lb / (inch * inch)) * 703
    bmi = round(bmi, 1)
    indexBMI(bmi)
    
def calculate_metric_BMI():
    kg = int(weight_tf.get())
    m = float(height_tf.get())
    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    indexBMI(bmi)

def indexBMI(bmi):
    if bmi < 16.0:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is severely underweight')
    elif (bmi > 16.0) and (bmi < 18.4):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is underweight')
    elif (bmi > 18.4) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is overweight')
    elif (bmi > 29.9) and (bmi < 34.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is moderately obese')
    elif (bmi > 34.9) and (bmi < 39.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is severly obese')
    elif (bmi > 40.0):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is morbidly obese') 
    else:
        messagebox.showerror('bmi-pythonguides', 'something went wrong!') 
        
def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

ws = Tk()
ws.title('PythonGuides')
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
    text='Select Mode'
)

us_rb = Checkbutton(
    frame2,
    text = 'US',
    variable = var,
    onvalue = 1,
    offvalue = 0,
    command = calculate_us_BMI
)

metric_rb = Checkbutton(
    frame2,
    text = 'Metric',
    variable = var,
    onvalue = 2,
    offvalue = 0,
    command = calculate_metric_BMI
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
    text="Enter Height (ft or m)  "
)

weight_lb = Label(
    frame4,
    text="Enter Weight (lbs or kg)  "
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
    text="Enter neck measurements (ft or m)  "
)

waist_tf = Entry(
    frame6,
)

waist_lb = Label(
    frame6,
    text="Enter waist measurements (ft or m)  "
)

frame2.grid(row=0, column=2, pady=5)
select_lb.grid(row=1, column=0)
us_rb.grid(row=1, column=1)
metric_rb.grid(row=1, column=2)

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

frame6.grid(row=4, column=2, pady=5)
neck_lb.grid(row=1, column=1)
neck_tf.grid(row=1, column=2)



frame2.grid(row=5, columnspan=3, pady=10)

ws.mainloop()