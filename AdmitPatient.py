import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import ttk

from database import DatabaseConnection

LARGEFONT = ("Verdana", 35)


class AdmitPatient(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Patient Management System", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        label2 = ttk.Label(self, text="implemented by: Ankesh Raj,Vikram Saini,Lal ahmed,Praneet", foreground="red",
                           font=20).grid(row=1, column=4)
        button1 = ttk.Button(self, text="Patient Entry",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=3, column=4, padx=8, pady=8)

        # button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Patient Record",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=4, column=4, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Patient Record Entry", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Display Patient",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    # take the data

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        mydb = DatabaseConnection()

        patients = mydb.getPatientDetail()
        if len(patients) > 0:

            tree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"), show='headings',
                                height=len(patients))

            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Name")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Age")
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Phone No")
            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Diesease")
            tree.column("# 5", anchor=CENTER)
            tree.heading("# 5", text="ADMISSION_DATE")
            tree.column("# 6", anchor=CENTER)
            tree.heading("# 6", text="GENDER")
            tree.column("# 7", anchor=CENTER)
            tree.heading("# 7", text="Blood Group")
            tree.column("# 8", anchor=CENTER)
            tree.heading("# 8", text="bill")

            # Insert the data in Treeview widget
            for x in patients:
                tree.insert('', 'end', text="1", values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))

            tree.grid(row=5)

        else:
            # screens.A()
            label = ttk.Label(self, text="Sorry no Patient Detail found", font=LARGEFONT)
            label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2



def demo() :
    root = tk.Tk()
    root.title('Treeview demo')
    root.geometry('620x200')

    # columns
    columns = ('#1', '#2', '#3')

    # tree = ttk.Treeview( column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"), show='headings')
    # tree.column("# 1", anchor=CENTER)
    # tree.heading("# 1", text="Name")
    # tree.column("# 2", anchor=CENTER)
    #
    # tree.heading("# 2", text="Age")
    # tree.column("# 3", anchor=CENTER)
    # tree.heading("# 3", text="Phone No")
    # tree.column("# 4", anchor=CENTER)
    # tree.heading("# 4", text="Diesease")
    # tree.column("# 5", anchor=CENTER)
    # tree.heading("# 5", text="ADMISSION_DATE")
    # tree.column("# 6", anchor=CENTER)
    # tree.heading("# 6", text="GENDER")
    # tree.column("# 7", anchor=CENTER)
    # tree.heading("# 7", text="Blood Group")
    # tree.column("# 8", anchor=CENTER)
    # tree.heading("# 8", text="bill")
    #
    # # define headings
    # tree.heading('#1', text='First Name')
    # tree.heading('#2', text='Last Name')
    # tree.heading('#3', text='Email')
    #
    # # generate sample data
    # contacts = []
    # for n in range(1, 100):
    #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
    #
    # # adding data to the treeview
    # for contact in contacts:
    #     tree.insert('', tk.END, values=contact)
    #
    # # bind the select event
    # def item_selected(event):
    #     for selected_item in tree.selection():
    #         # dictionary
    #         item = tree.item(selected_item)
    #         # list
    #         record = item['values']
    #         #
    #         showinfo(title='Information',
    #                  message=','.join(record))
    #
    # tree.bind('<<TreeviewSelect>>', item_selected)
    #
    # tree.grid(row=0, column=0, sticky='nsew')
    #
    # # add a scrollbar
    # scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    # tree.configure(yscroll=scrollbar.set)
    # scrollbar.grid(row=0, column=1, sticky='ns')

    # run the app
    root.mainloop()
