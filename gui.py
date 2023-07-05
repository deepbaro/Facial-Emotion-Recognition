import customtkinter as ctk
from tkinter import filedialog


#buttons
def add_todo():
    img_name = filedialog.askopenfilename()
    print(img_name)
#setting up tkinter
ctk.set_appearance_mode("Dark")
root = ctk.CTk()
root.geometry("750x450")
root.title("Todo App")

#setting up resources
comic_font = ("Eras Light ITC", 20, "bold")

title = ctk.CTkLabel(root, text="Facial Emotion Detector", font=comic_font)
title.pack(padx=10, pady=(40, 20))


scrollable_frame = ctk.CTkFrame(root, width=500, height=200)
scrollable_frame.pack()

add_button = ctk.CTkButton(root, text="Upload Your Image", width=500, command=add_todo)
add_button.pack(pady=20)

root.mainloop()
