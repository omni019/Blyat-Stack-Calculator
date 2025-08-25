import webbrowser
import tkinter as tk
from tkinter import PhotoImage
import os
root = tk.Tk()
root.title("Blyat Shulker Converter")
root.geometry("500x350")
root.resizable(False, False)
# Remove window border and title bar, but keep it in the taskbar (Windows only)
icon_ico_path = os.path.join(os.path.dirname(__file__), "shulker.ico")
if os.path.exists(icon_ico_path):
    try:
        root.iconbitmap(icon_ico_path)
    except Exception:
        pass
# Load background image
bg_path = os.path.join(os.path.dirname(__file__), "background.png")
bg_img = None
try:
    from PIL import Image, ImageTk
    if os.path.exists(bg_path):
        bg_img_raw = Image.open(bg_path)
        bg_img = ImageTk.PhotoImage(bg_img_raw)
except ImportError:
    if os.path.exists(bg_path):
        bg_img = PhotoImage(file=bg_path)
# Create canvas and tile background
canvas = tk.Canvas(root, width=500, height=350, highlightthickness=0)
canvas.place(x=0, y=0, relwidth=1, relheight=1)
if bg_img:
    img_w = bg_img.width()
    img_h = bg_img.height()
    for x in range(0, 500, img_w):
        for y in range(0, 350, img_h):
            canvas.create_image(x, y, image=bg_img, anchor='nw')

# Load and display gunslol.png icon
gunslol_icon_path = os.path.join(os.path.dirname(__file__), "gunslol.png")
gunslol_img = None
if os.path.exists(gunslol_icon_path):
    try:
        from PIL import Image, ImageTk
        img = Image.open(gunslol_icon_path)
        img = img.resize((32, 32), Image.LANCZOS)
        gunslol_img = ImageTk.PhotoImage(img)
    except Exception:
        gunslol_img = PhotoImage(file=gunslol_icon_path)

gunslol_icon_id = None
if gunslol_img:
    gunslol_icon_id = canvas.create_image(450, 310, image=gunslol_img, anchor='nw')
    def open_gunslol(event=None):
        webbrowser.open_new("https://guns.lol/omni019")
    canvas.tag_bind(gunslol_icon_id, '<Button-1>', open_gunslol)
title = tk.Label(root, text="Blyat Shulker Converter", font=("Arial", 24, "bold"))
title_text_id = canvas.create_text(250, 40, text="Blyat Shulker Converter", font=("Arial", 24, "bold"), fill="#D3D3D3")
by_label_id = canvas.create_text(250, 65, text="by omni019", font=("Arial", 10, "italic"), fill="#D3D3D3")
label_text_id = canvas.create_text(250, 90, text="Enter value:", font=("Arial", 12), fill="#D3D3D3")
user_input = ""
input_box_id = canvas.create_rectangle(150, 100, 350, 140, outline="#D3D3D3", width=2)
input_text_id = canvas.create_text(250, 120, text=user_input, font=("Arial", 18), fill="#D3D3D3", anchor="center")

def on_key(event):
    global user_input
    if event.keysym == "BackSpace":
        user_input = user_input[:-1]
    elif event.keysym == "Return":
        entry_value = user_input
        entry_callback(entry_value)
        user_input = ""
    elif len(event.char) == 1 and event.char.isprintable():
        user_input += event.char
    canvas.itemconfig(input_text_id, text=user_input)

def entry_callback(value):
    entry.delete(0, tk.END)
    entry.insert(0, value)
    convertitems()

canvas.focus_set()
canvas.bind("<Key>", on_key)
# Load and resize shulker icon
icon_path = os.path.join(os.path.dirname(__file__), "shulker.png")
shulker_img_small = None
try:
    from PIL import Image, ImageTk
    if os.path.exists(icon_path):
        img = Image.open(icon_path)
        img = img.resize((36, 36), Image.LANCZOS)
        shulker_img_small = ImageTk.PhotoImage(img)
except ImportError:
    if os.path.exists(icon_path):
        shulker_img_small = PhotoImage(file=icon_path)
shulker_text_id = None
shulker_icon_id = None
stack_text_id = None
item_text_id = None
error_text_id = None
def convertitems():
    global shulker_text_id, shulker_icon_id, stack_text_id, item_text_id, error_text_id, user_input
    # Clear previous canvas text/icons
    for item in [shulker_text_id, shulker_icon_id, stack_text_id, item_text_id, error_text_id]:
        if item:
            canvas.delete(item)
    shulker_text_id = shulker_icon_id = stack_text_id = item_text_id = error_text_id = None
    try:
        number = int(eval(user_input, {"__builtins__": None}, {}))
    except Exception:
        error_text_id = canvas.create_text(250, 155, text="Please enter a valid number or expression.", fill="red", font=("Arial", 18, "bold"), anchor="center")
        return
    s = 64
    sh = 27
    if number <= 0:
        error_text_id = canvas.create_text(250, 155, text="Error: number must be positive.", fill="red", font=("Arial", 18, "bold"), anchor="center")
        return
    shulker = number // (s * sh)
    remainder = number % (s * sh)
    stack = remainder // s
    item = remainder % s
    y_base = 180
    if shulker > 0:
        if shulker_img_small:
            shulker_icon_id = canvas.create_image(110, y_base, image=shulker_img_small, anchor='e')
        shulker_text_id = canvas.create_text(150, y_base, text=f"{shulker} shulker{'s' if shulker > 1 else ''}", fill="#D3D3D3", font=("Arial", 16, "bold"), anchor='w')
    if stack > 0:
        stack_text_id = canvas.create_text(150, y_base+30, text=f"{stack} stack{'s' if stack > 1 else ''}", fill="#D3D3D3", font=("Arial", 16, "bold"), anchor='w')
    if item > 0:
        item_text_id = canvas.create_text(150, y_base+60, text=f"{item} item{'s' if item > 1 else ''}", fill="#D3D3D3", font=("Arial", 16, "bold"), anchor='w')
    if shulker == 0 and stack == 0 and item == 0:
        error_text_id = canvas.create_text(250, y_base+90, text="0 items", fill="red", font=("Arial", 18, "bold"), anchor="center")
label = tk.Label(root, text="Enter value:")
# ...existing code...
button = tk.Button(root, text="Run", command=convertitems,
    bg="#222222", fg="#D3D3D3", activebackground="#222222", activeforeground="#D3D3D3",
    font=("Arial", 18), borderwidth=0, highlightthickness=0, relief='flat', padx=32, pady=8)
button_window = canvas.create_window(250, 300, window=button)
root.mainloop()