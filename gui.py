import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk

#buttons
def add_todo():
    img_path = filedialog.askopenfilename()
    image_toview =  ctk.CTkImage(Image.open(img_path), size=(250, 250)) 
    print(img_path)

    view_box.configure(image=image_toview)


def button_event():
     pass
#setting up tkinter
ctk.set_appearance_mode("Dark")
root = ctk.CTk()
root.geometry("750x450")
root.title("Todo App")

#setting up resources
comic_font = ("Eras Light ITC", 20, "bold")

title = ctk.CTkLabel(root, text="Facial Emotion Detector", font=comic_font)
title.pack(padx=10, pady=(40, 20))



frame_a = ctk.CTkFrame(root)
frame_a.pack()

frame_b = ctk.CTkFrame(root)
frame_b.pack()

view_box = ctk.CTkLabel(master=frame_a, text="")
view_box.pack()
add_button = ctk.CTkButton(frame_b, text="Upload Your Image", width=500, command=add_todo)
add_button.pack(pady=20)




root.mainloop()
