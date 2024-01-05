import tkinter as tk
import tkinter.scrolledtext as tksc


def exit_button():
    root.destroy()


def test_my_button():
    # TODO: Use get method of ent_password when the button is pressed,
    # and store the result
    user_pass = ent_password.get()
    # TODO: Configure the label in frame_auth to display the password
    lbl_display.config(text=user_pass)
    frame_auth.tkraise()


# main window
root = tk.Tk()
root.wm_geometry("400x200")
root.title("Authorization")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky='news')

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky='news')

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack(pady=5)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:', font='Arial')
lbl_password.pack(padx=5)

ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(pady=5)

bt_image = tk.PhotoImage(file="button.gif")
bt_image = bt_image.subsample(10, 10)

btn_login = tk.Button(frame_login, text='Login',
                      command=test_my_button, image=bt_image)
btn_login.pack(padx=175, pady=20)

# TODO: Add a label to frame_auth
lbl_display = tk.Label(frame_auth, text='Password:', font='Arial')
lbl_display.pack(padx=5)

frame_login.tkraise()
test_textbox = tksc.ScrolledText(frame_auth)
test_textbox.pack(pady=20)
test_textbox.configure(height=10, width=50)

exit_img = tk.PhotoImage(file="exit.gif")
exit_img = exit_img.subsample(10, 10)

end_button = tk.Button(frame_auth, text="Exit",
                       command=exit_button, image=exit_img)
end_button.pack(pady=40)

root.mainloop()
