import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def myClick():
    pass
frame = customtkinter.CTkFrame(master=root)

frame.grid(row=0, column=0, sticky='nsew')

root.title("Simple Calculator") 
entry = customtkinter.CTkEntry(master=frame)
entry.configure(font=("Calibri",75))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=12, sticky="ew")

button_1 = customtkinter.CTkButton(master=frame,text="1",command=myClick)
button_1.configure(width=10, height=4, font=("Calibri",75))
button_1.grid(row=1, column=0, sticky="we")

button_2 = customtkinter.CTkButton(master=frame,text="2",command=myClick)
button_2.configure(width=10, height=4, font=("Calibri",75))
button_2.grid(row=1, column=1,sticky="we")

button_3 = customtkinter.CTkButton(master=frame,text="3",command=myClick)
button_3.configure(width=10, height=4, font=("Calibri",75))
button_3.grid(row=1, column=2,sticky="we")


button_4 = customtkinter.CTkButton(master=frame,text="4",command=myClick)
button_4.configure(width=10, height=4, font=("Calibri",75))
button_4.grid(row=2, column=0,sticky="we")


button_5 = customtkinter.CTkButton(master=frame,text="5",command=myClick)
button_5.configure(width=10, height=4, font=("Calibri",75))
button_5.grid(row=2, column=1,sticky="we")


button_6 = customtkinter.CTkButton(master=frame,text="6",command=myClick)
button_6.configure(width=10, height=4, font=("Calibri",75))
button_6.grid(row=2, column=2,sticky="we")

button_7 = customtkinter.CTkButton(master=frame,text="7",command=myClick)
button_7.configure(width=10, height=4, font=("Calibri",75))
button_7.grid(row=3, column=0,sticky="we")

button_8 = customtkinter.CTkButton(master=frame,text="8",command=myClick)
button_8.configure(width=10, height=4, font=("Calibri",75))
button_8.grid(row=3, column=1,sticky="we")

button_9 = customtkinter.CTkButton(master=frame,text="9",command=myClick)
button_9.configure(width=10, height=4, font=("Calibri",75))
button_9.grid(row=3, column=2,sticky="we")

button_0 = customtkinter.CTkButton(master=frame,text="0",command=myClick)
button_0.configure(width=10, height=4, font=("Calibri",75))
button_0.grid(row=4, column=1,sticky="we")

button_clear = customtkinter.CTkButton(master=frame,text="C",command=myClick)
button_clear.configure(width=10, height=4, font=("Calibri",75))
button_clear.grid(row=4, column=0,sticky="we")

button_equal = customtkinter.CTkButton(master=frame,text="=",command=myClick)
button_equal.configure(width=10, height=4, font=("Calibri",75))
button_equal.grid(row=4, column=2,sticky="we")

button_multiply = customtkinter.CTkButton(master=frame,text="×",command=myClick)
button_multiply.configure(width=10, height=4, font=("Calibri",75))
button_multiply.grid(row=1, column=3,sticky="we")

button_divide = customtkinter.CTkButton(master=frame,text="÷",command=myClick)
button_divide.configure(width=10, height=4, font=("Calibri",75))
button_divide.grid(row=2, column=3,sticky="we")

button_add = customtkinter.CTkButton(master=frame,text="+",command=myClick)
button_add.configure(width=10, height=4, font=("Calibri",75))
button_add.grid(row=3, column=3,sticky="we")

button_subtract = customtkinter.CTkButton(master=frame,text="-",command=myClick)
button_subtract.configure(width=10, height=4, font=("Calibri",75))
button_subtract.grid(row=4, column=3,sticky="we")

root.mainloop()
