from tkinter import *
from tkinter import ttk
from tkinter import messagebox

global root

def calculate():
    total_grades = 0
    total_credits = int(n1.get()) + int(n2.get()) + int(n3.get()) + int(n4.get()) + int(n5.get()) + int(n6.get()) + int(n7.get())
    if g1.get() == 'O':
        total_grades += 10*int(n1.get())
    if g1.get() == 'A+':
        total_grades += 9*int(n1.get())
    if g1.get() == 'A':
        total_grades += 8*int(n1.get())
    if g1.get() == 'B+':
        total_grades += 7*int(n1.get())
    if g2.get() == 'O':
        total_grades += 10*int(n2.get())
    if g2.get() == 'A+':
        total_grades += 9*int(n2.get())
    if g2.get() == 'A':
        total_grades += 8*int(n2.get())
    if g2.get() == 'B+':
        total_grades += 7*int(n2.get())
    if g3.get() == 'O':
        total_grades += 10*int(n3.get())
    if g3.get() == 'A+':
        total_grades += 9*int(n3.get())
    if g3.get() == 'A':
        total_grades += 8*int(n3.get())
    if g3.get() == 'B+':
        total_grades += 7*int(n3.get())
    if g4.get() == 'O':
        total_grades += 10*int(n4.get())
    if g4.get() == 'A+':
        total_grades += 9*int(n4.get())
    if g4.get() == 'A':
        total_grades += 8*int(n4.get())
    if g4.get() == 'B+':
        total_grades += 7*int(n4.get())
    if g5.get() == 'O':
        total_grades += 10*int(n5.get())
    if g5.get() == 'A+':
        total_grades += 9*int(n5.get())
    if g5.get() == 'A':
        total_grades += 8*int(n5.get())
    if g5.get() == 'B+':
        total_grades += 7*int(n5.get())
    if g6.get() == 'O':
        total_grades += 10*int(n6.get())
    if g6.get() == 'A+':
        total_grades += 9*int(n6.get())
    if g6.get() == 'A':
        total_grades += 8*int(n6.get())
    if g6.get() == 'B+':
        total_grades += 7*int(n6.get())
    if g7.get() == 'O':
        total_grades += 10*int(n7.get())
    if g7.get() == 'A+':
        total_grades += 9*int(n7.get())
    if g7.get() == 'A':
        total_grades += 8*int(n7.get())
    if g7.get() == 'B+':
        total_grades += 7*int(n7.get())
    
    
    try:
        scored = total_grades/int(total_credits)
        message = f'You Scored: {scored}'
        cgpa = Label(root, text = (message))
        cgpa.place(x=200, y=650)
    except:
        messagebox.showwarning("showwarning", "Entered value is wrong!")

    
    pass

if __name__ == '__main__':
    root = Tk()
    root.geometry('500x700')
    root.title('SRM SGPA Calculator')
    root.resizable(False, False)

    srm_GPA_CALCULATOR = Label(root, text = "SRM GPA CALCULATOR", font = ('Sans Serif', 18, 'bold'))
    srm_GPA_CALCULATOR.place(x=150, y=50)

    sub = Label(root, text = 'Subjects', font = ('Sans Serif', 14))
    sub.place(x=30, y=100)

    credits = Label(root, text = 'Credits', font = ('Sans Serif', 14))
    credits.place(x=220, y=100)

    grade_obt = Label(root, text = 'Grades Obtained', font = ('Sans Serif', 14))
    grade_obt.place(x=350, y=100)

    global n1, n2, n3, n4, n5, n6, n7
    n1, n2, n3, n4, n5, n6, n7 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
    global g1, g2, g3, g4, g5, g6, g7
    g1, g2, g3, g4, g5, g6, g7 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar() 
#Number 1
    numbering1 = Label(root, text='1.')
    numbering1.place(x=40, y=150)

    credits_score1 = Spinbox(root, from_=0, to = 5, width=3, textvariable = n1)
    credits_score1.place(x=220, y=150)

    grade_score1 = ttk.Combobox(root, width=5, textvariable = g1)
    grade_score1.place(x=380, y=150)
    grade_score1['values'] = ('O', 'A+', 'A', 'B+')

#Number 2
    numbering2 = Label(root, text='2.')
    numbering2.place(x=40, y=200)

    credits_score2 = Spinbox(root, from_=0, to = 5, width=3, textvariable = n2)
    credits_score2.place(x=220, y=200)

    grade_score2 = ttk.Combobox(root, width=5, textvariable = g2)
    grade_score2.place(x=380, y=200)
    grade_score2['values'] = ('O', 'A+', 'A', 'B+')

#Number 3
    numbering3 = Label(root, text='3.')
    numbering3.place(x=40, y=250)

    credits_score3 = Spinbox(root, from_=0, to = 5, width=3, textvariable = n3)
    credits_score3.place(x=220, y=250)

    grade_score3 = ttk.Combobox(root, width=5, textvariable = g3)
    grade_score3.place(x=380, y=250)
    grade_score3['values'] = ('O', 'A+', 'A', 'B+')

#Number 4
    numbering4 = Label(root, text='4.')
    numbering4.place(x=40, y=300)

    credits_score4 = Spinbox(root, from_=0, to = 5, width=3, textvariable = n4)
    credits_score4.place(x=220, y=300)

    grade_score4 = ttk.Combobox(root, width=5, textvariable = g4)
    grade_score4.place(x=380, y=300)
    grade_score4['values'] = ('O', 'A+', 'A', 'B+')

#Number 5
    numbering5 = Label(root, text='5.')
    numbering5.place(x=40, y=350)

    credits_score5 = Spinbox(root, from_=0, to = 5, width=3, textvariable = n5)
    credits_score5.place(x=220, y=350)

    grade_score5 = ttk.Combobox(root, width=5, textvariable = g5)
    grade_score5.place(x=380, y=350)
    grade_score5['values'] = ('O', 'A+', 'A', 'B+')
#Number 6
    numbering6 = Label(root, text='6.')
    numbering6.place(x=40, y=400)

    credits_score6 = Spinbox(root, from_=0, to = 5, width=3, textvariable = n6)
    credits_score6.place(x=220, y=400)

    grade_score6 = ttk.Combobox(root, width=5, textvariable = g6)
    grade_score6.place(x=380, y=400)
    grade_score6['values'] = ('O', 'A+', 'A', 'B+')
#Number 7
    numbering7 = Label(root, text='7.')
    numbering7.place(x=40, y=450)

    credits_score7 = Spinbox(root, from_=0, to = 5, width=3, textvariable = n7)
    credits_score7.place(x=220, y=450)

    grade_score7 = ttk.Combobox(root, width=5, textvariable = g7)
    grade_score7.place(x=380, y=450)
    grade_score7['values'] = ('O', 'A+', 'A', 'B+')

    cal = Button(root, text='CALCULATE', command = calculate)
    cal.place(x=200, y=600)

    root.mainloop()
