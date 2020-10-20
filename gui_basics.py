# This is the basics of Gui Tkinter

import tkinter as tk


# # Everything goes between these two
# root = tk.Tk()
# root.mainloop()
# # HOORAY WE DID IT TEAM!!!

# Button Test
root = tk.Tk()
button = tk.Button(root,text="Test button", bg='yellow', fg='blue')
button.pack()
# button.grid()
# button.place()
root.mainloop()

