#a password generater with high safety
import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.geometry("270x210")
window.title("PASSWORD GENERATER")

def generater():
    import random

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "#&@/\!?*$"

    Use_for = lower_case + upper_case + numbers + symbols
    length_for_pass = 10

    password = "".join(random.sample(Use_for,length_for_pass))
    label.configure(text = password)

frame = customtkinter.CTkFrame(master = window)
frame.pack(pady=23,padx=20,fill = "both",expand=True)

label = customtkinter.CTkLabel(master = frame , text = "CLICK TO START",font=("Roboto",20))
label.pack(pady=30,padx=10)

button = customtkinter.CTkButton(master = frame, 
                                 text = "GENERATE A PASSWORD",
                                 command = generater,
                                 height=37,
                                 corner_radius=6)

button.pack(pady=12,padx=10)

window.mainloop()