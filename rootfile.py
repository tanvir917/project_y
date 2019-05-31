from tkinter import*
import datetime
import time;

root = Tk()

root.geometry("1600x800")
root.title("Human Resource Management System")

text_Input = StringVar()

Tops = Frame(root, width = 1600, height=50, bg = "powder blue", relief = SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 700, height=600, bg = "powder blue", relief = SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 700, height=600, bg = "powder blue", relief = SUNKEN)
f2.pack(side=RIGHT)

lblInfo = Label(Tops, font = ('arial',50,'bold'), text="Human Resource Management Systems",fg="blue")
lblInfo.grid(row=0,column=0)

LeftInsideLF=Frame(f1, width=700, height=200, bg="red")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(f1, width=325, height=400, bg="yellow")
LeftInsideLFLF.pack(side=LEFT)
LeftInsideLFRF=Frame(f1, width=325, height=400, bg="black")
LeftInsideLFRF.pack(side=RIGHT)

RightInsideLF=Frame(f2, width=700, height=200, bg="red")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(f2, width=300, height=400, bg="yellow")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(f2, width=300, height=400, bg="black")
RightInsideRFRF.pack(side=RIGHT)

#=============== Left Side
lblEmployeeN = Label(LeftInsideLF, font = ('arial',12,'bold'), text="Employee Name",fg="blue")
lblEmployeeN.grid(row=0,column=0)
txtEmployeeN = Entry(LeftInsideLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtEmployeeN.grid(row=0,column=1)

lblAddress = Label(LeftInsideLF, font = ('arial',12,'bold'), text="Address",fg="blue")
lblAddress.grid(row=1,column=0)
txtAddress = Entry(LeftInsideLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtAddress.grid(row=1,column=1)

lblEmployeeN = Label(LeftInsideLF, font = ('arial',12,'bold'), text="Reference",fg="blue")
lblEmployeeN.grid(row=2,column=0)
txtEmployeeN = Entry(LeftInsideLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtEmployeeN.grid(row=2,column=1)

lblAddress = Label(LeftInsideLF, font = ('arial',12,'bold'), text="Employer Name",fg="blue")
lblAddress.grid(row=3,column=0)
txtAddress = Entry(LeftInsideLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtAddress.grid(row=3,column=1)
#=== LEFT LEFT
lblEmployeeN = Label(LeftInsideLFLF, font = ('arial',12,'bold'), text="City Weighting",fg="blue")
lblEmployeeN.grid(row=0,column=0)
txtEmployeeN = Entry(LeftInsideLFLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtEmployeeN.grid(row=0,column=1)

lblAddress = Label(LeftInsideLFLF, font = ('arial',12,'bold'), text="Basic Salary",fg="blue")
lblAddress.grid(row=1,column=0)
txtAddress = Entry(LeftInsideLFLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtAddress.grid(row=1,column=1)

lblEmployeeN = Label(LeftInsideLFLF, font = ('arial',12,'bold'), text="Over Time",fg="blue")
lblEmployeeN.grid(row=2,column=0)
txtEmployeeN = Entry(LeftInsideLFLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtEmployeeN.grid(row=2,column=1)

lblAddress = Label(LeftInsideLFLF, font = ('arial',12,'bold'), text="Gross Pay",fg="blue")
lblAddress.grid(row=3,column=0)
txtAddress = Entry(LeftInsideLFLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtAddress.grid(row=3,column=1)

lblAddress = Label(LeftInsideLFLF, font = ('arial',12,'bold'), text="Net Pay",fg="blue")
lblAddress.grid(row=4,column=0)
txtAddress = Entry(LeftInsideLFLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtAddress.grid(row=4,column=1)

#=== LEFT RIGHT
lblEmployeeN = Label(LeftInsideLFRF, font = ('arial',12,'bold'), text="Tax",fg="blue")
lblEmployeeN.grid(row=0,column=0)
txtEmployeeN = Entry(LeftInsideLFRF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtEmployeeN.grid(row=0,column=1)

lblAddress = Label(LeftInsideLFRF, font = ('arial',12,'bold'), text="pension",fg="blue")
lblAddress.grid(row=1,column=0)
txtAddress = Entry(LeftInsideLFRF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtAddress.grid(row=1,column=1)

lblEmployeeN = Label(LeftInsideLFRF, font = ('arial',12,'bold'), text="Student Loan",fg="blue")
lblEmployeeN.grid(row=2,column=0)
txtEmployeeN = Entry(LeftInsideLFRF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtEmployeeN.grid(row=2,column=1)

lblAddress = Label(LeftInsideLFRF, font = ('arial',12,'bold'), text="NI Payment",fg="blue")
lblAddress.grid(row=3,column=0)
txtAddress = Entry(LeftInsideLFRF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtAddress.grid(row=3,column=1)

lblAddress = Label(LeftInsideLFRF, font = ('arial',12,'bold'), text="Deductions",fg="blue")
lblAddress.grid(row=4,column=0)
txtAddress = Entry(LeftInsideLFRF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtAddress.grid(row=4,column=1)



#=============== Right Side
lblPostCode= Label(RightInsideLF, font = ('arial',12,'bold'), text="Post Code",fg="blue")
lblPostCode.grid(row=0,column=0)
txtPostCode = Entry(RightInsideLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtPostCode.grid(row=0,column=1)

lblGender = Label(RightInsideLF, font = ('arial',12,'bold'), text="Gender",fg="blue")
lblGender.grid(row=1,column=0)
txtGender = Entry(RightInsideLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtGender.grid(row=1,column=1)

#==== Right Left Side
#=== LEFT RIGHT
lblEmployeeN = Label(RightInsideLFLF, font = ('arial',12,'bold'), text="Pay Date",fg="blue")
lblEmployeeN.grid(row=0,column=0)
txtEmployeeN = Entry(RightInsideLFLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtEmployeeN.grid(row=0,column=1)

lblAddress = Label(RightInsideLFLF, font = ('arial',12,'bold'), text="Tax Period",fg="blue")
lblAddress.grid(row=1,column=0)
txtAddress = Entry(RightInsideLFLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtAddress.grid(row=1,column=1)

lblEmployeeN = Label(RightInsideLFLF, font = ('arial',12,'bold'), text="Nl Number",fg="blue")
lblEmployeeN.grid(row=2,column=0)
txtEmployeeN = Entry(RightInsideLFLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtEmployeeN.grid(row=2,column=1)

lblAddress = Label(RightInsideLFLF, font = ('arial',12,'bold'), text="Taxable Pay",fg="blue")
lblAddress.grid(row=3,column=0)
txtAddress = Entry(RightInsideLFLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtAddress.grid(row=3,column=1)

lblAddress = Label(RightInsideLFLF, font = ('arial',12,'bold'), text="Pensionable Pay",fg="blue")
lblAddress.grid(row=4,column=0)
txtAddress = Entry(RightInsideLFLF, font = ('arial',16,'bold'), bd=10, insertwidth = 8, bg = "white", justify ='right')
txtAddress.grid(row=4,column=1)


addEmpl = Button(RightInsideRFRF, padx=8, bd=8, fg="black", font = ('arial',12,'bold'), width=12, text = "Add Employee  ")
addEmpl.grid(row = 0, column=0)
wagePayment = Button(RightInsideRFRF, padx=8, bd=8, fg="black", font = ('arial',12,'bold'), width=12, text = "Wage Payment  ")
wagePayment.grid(row = 1, column=0)
payReference = Button(RightInsideRFRF, padx=8, bd=8, fg="black", font = ('arial',12,'bold'), width=12, text = "Pay Reference  ")
payReference.grid(row = 2, column=0)
exit = Button(RightInsideRFRF, padx=8, bd=8, fg="black", font = ('arial',12,'bold'), width=12, text = "Exit  ")
exit.grid(row = 3, column=0)

root.mainloop()