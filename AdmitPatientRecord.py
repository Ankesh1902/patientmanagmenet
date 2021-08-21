import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from datetime import date

import Patient
from database import DatabaseConnection

class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        fontStyle = tkFont.Font(family="Lucida Grande", size=36)
        self.radio_ = tk.StringVar()
        self.geometry("600x500")

        self.nameLabel=tk.Label(self, text="name",font=36)
        self.name = tk.Entry(self)
        self.ageLabel = tk.Label(self, text="age")
        self.age = tk.Entry(self)
        self.mobileLabel = tk.Label(self, text="mobileNo")
        self.mobile = tk.Entry(self)
        self.diseaseLabel = tk.Label(self, text="Disease")
        self.disease = tk.Entry(self)
        self.genderLabel = tk.Label(self, text="Gender")
        self.radio=tk.Radiobutton(self,text="Male",variable=self.radio_,value="male",command=self.selection)
        self.radio2 = tk.Radiobutton(self, text="Female", variable=self.radio_, value="female", command=self.selection)
        self.billLabel = tk.Label(self, text="Bill")
        self.bill = tk.Entry(self)
        self.bloodGroupLabel = tk.Label(self, text="Blood Group")
        self.blood = tk.Entry(self)
        self.button = tk.Button(self, text="Admit Patient", command=self.on_button)

        self.nameLabel.grid(row=5, column=10)
        self.name.grid(row=5,column=15)
        self.genderLabel.grid(row=20,column=10)
        self.radio.grid(row=20,column=15)
        self.radio2.grid(row=20, column=18)
        self.mobileLabel.grid(row=35,column=10)
        self.mobile.grid(row=35,column=15)
        self.diseaseLabel.grid(row=50,column=10)
        self.disease.grid(row=50,column=15)
        self.ageLabel.grid(row=75,column=10)
        self.age.grid(row=75,column=15)
        self.bloodGroupLabel.grid(row=100,column=10)
        self.blood.grid(row=100,column=15)
        self.billLabel.grid(row=115, column=10)
        self.bill.grid(row=115, column=15)

        self.button.grid(row=130, column=5)

    def selection(self):
        selection = "You selected the option " + str(self.radio_.get())
        print(selection)
    def on_button(self):
        name=self.name.get()
        age=self.age.get()
        mobile=self.mobile.get()
        gender=self.radio.getvar("PY_VAR0")
        disease=self.disease.get()
        bill=self.bill.get()
        blood=self.blood.get()
        p=Patient.PatientEntity(name,age,mobile,disease,date.today(),gender,blood,bill)
        flag=DatabaseConnection().insertPatientDetail(p)
        if flag>=0:

            messagebox.showinfo("correct","patient admitted successfully")
            self.destroy()
        else:
            messagebox.showerror("error","something went wrong")

    def call(self):
        app = SampleApp()

        app.mainloop()

