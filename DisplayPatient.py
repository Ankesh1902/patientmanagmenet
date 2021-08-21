import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

import Patient
from database import DatabaseConnection

class DisplayPatient(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        fontStyle = tkFont.Font(family="Lucida Grande", size=36)
        self.radio_ = tk.StringVar()
        self.geometry("600x500")

        self.patientIdLabel=tk.Label(self, text="Patient Id :", font=36)
        self.patientId = tk.Entry(self)
        self.nameLabel=tk.Label(self, font=36)
        self.name = tk.Label(self, font=36)

        self.age = tk.Label(self)
        self.ageLabel=tk.Label(self)
        self.mobileLabel = tk.Label(self)
        self.mobile = tk.Label(self)
        self.diseaseLabel = tk.Label(self)
        self.disease = tk.Label(self)
        self.genderLabel = tk.Label(self)
        self.gender = tk.Label(self)
        self.admissionLabel = tk.Label(self)
        self.admission = tk.Label(self)

        self.billLabel = tk.Label(self,)
        self.bill = tk.Label(self)
        self.bloodGroupLabel = tk.Label(self)
        self.blood = tk.Label(self)



        self.button = tk.Button(self, text="View Patient", command=self.viewPatient)
        self.reset = tk.Button(self,  command=self.on_reset)
        self.patientIdLabel.grid(row=1,column=10)
        self.patientId.grid(row=1,column=15)
        self.nameLabel.grid(row=5,column=10)
        self.name.grid(row=5,column=15)
        self.genderLabel.grid(row=20, column=10)
        self.gender.grid(row=20,column=15)
        self.mobileLabel.grid(row=35, column=10)
        self.mobile.grid(row=35, column=15)
        self.diseaseLabel.grid(row=50, column=10)
        self.disease.grid(row=50, column=15)
        self.ageLabel.grid(row=75, column=10)
        self.age.grid(row=75,column=15)
        self.bloodGroupLabel.grid(row=100, column=10)
        self.blood.grid(row=100, column=15)
        self.billLabel.grid(row=115, column=10)
        self.bill.grid(row=115, column=15)
        self.admissionLabel.grid(row=130,column=10)
        self.admission.grid(row=130,column=15)

        self.button.grid(row=1, column=50)
        self.reset.grid(row=145)
    def selection(self):
        selection = "You selected the option " + str(self.radio_.get())
        print(selection)
    def on_reset(self):
        self.nameLabel.config(text="")
        self.name.config(text='')
        self.ageLabel.config(text="")
        self.age.config(text="")
        self.mobileLabel.config(text="")
        self.mobile.config(text="")
        self.diseaseLabel.config(text="")
        self.disease.config(text="")
        self.admissionLabel.config(text="")
        self.admission.config(text="")
        self.genderLabel.config(text="")
        self.gender.config(text="")
        self.bloodGroupLabel.config(text="")
        self.blood.config(text="")
        self.billLabel.config(text="")
        self.bill.config(text="")

    def viewPatient(self):
        print(self.patientId.get())
        flag=DatabaseConnection()
        patient=flag.getPatientDetail(self.patientId.get())
        if patient==0:
            messagebox.showerror("patient","no record found")
        else:

            self.nameLabel.config(text="name :")
            self.name.config(text=patient.getName())
            self.ageLabel.config(text="gender :")
            self.age.config(text=int(patient.getAge()))
            self.mobileLabel.config(text="Mobile No :")
            self.mobile.config(text=patient.getMobile())
            self.diseaseLabel.config(text="Disease :")
            self.disease.config(text=patient.getDisease())
            self.admissionLabel.config(text="admission :")
            self.admission.config(text=patient.getAdmission())
            self.genderLabel.config(text="Gender :")
            self.gender.config(text=patient.getGender())
            self.bloodGroupLabel.config(text="BloodGroup :")
            self.blood.config(text=patient.getBlood())
            self.billLabel.config(text="bill")
            self.bill.config(text=patient.getBill())
            self.reset.config(text="reset")
    def call(self):
        app = DisplayPatient()

        app.mainloop()

