'''
import tkinter

#command for button
def click():
    name = entry.get()
    mylabel.config(text="Hello "+name)

#def window
window = tkinter.Tk()

window.title("test")
window.geometry("300x200")

#def label
mylabel = tkinter.Label(
    window,
    text = "Hello",
    bg="gold",fg="teal",
    font=("Arial",20),
    width=20,height=1)
mylabel.pack()

#def frame
frame = tkinter.Frame(
    window,
    width=400,
    height=30)
frame.pack()

#def entry
entry = tkinter.Entry(
    window,
    width=27)
entry.pack()

frame = tkinter.Frame(
    window,
    width=400,
    height=30)
frame.pack()

#def button
button = tkinter.Button(
    window,
    text="Click to start",
    bg="teal",fg="snow",
    font=("Arial",20),
    width=10,height=1,
    command=click)
button.pack()

window.mainloop()

'''
import customtkinter

def username():
    name=entry1.get()
    label.configure(text="Welcome "+name)

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("400x400")
window.title("Login")

frame = customtkinter.CTkFrame(master=window)
frame.pack(pady=30,padx=50,fill = "both",expand=True)

label = customtkinter.CTkLabel(master=frame,
                              text="Welcome",
                              font=("Roboto",24))
label.pack(pady=40,padx=10)

entry1 = customtkinter.CTkEntry(master=frame,placeholder_text="username",border_width=0)
entry1.pack(pady=5,padx=10)

entry2 = customtkinter.CTkEntry(master=frame,placeholder_text="password",border_width=0,show="*")
entry2.pack(pady=5,padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame,
                                     text="Remember me",
                                     border_width=0.5,
                                     checkbox_width=13,
                                     checkbox_height=13,
                                     corner_radius=4)
checkbox.pack(pady=5,padx=10)

button = customtkinter.CTkButton(master = frame, 
                                 text = "LOGIN",
                                 width=140,
                                 height=30,
                                 corner_radius=6,
                                 command=username)

button.pack(pady=10,padx=10)

window.mainloop()