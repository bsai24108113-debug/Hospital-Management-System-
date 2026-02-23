import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random
import itertools

# ---------------- Window ----------------
root = tk.Tk()
root.title("Happy New Year My Love ❤️")
root.geometry("720x720")
root.resizable(False, False)

# ---------------- Canvas ----------------
canvas = tk.Canvas(root, width=720, height=720, bg="#1a001a", highlightthickness=0)
canvas.place(x=0, y=0)

# ---------------- Snow + Hearts ----------------
hearts = []
snowflakes = []

def create_heart():
    x = random.randint(20, 700)
    y = 720
    size = random.randint(14, 26)
    heart = canvas.create_text(x, y, text="❤️", font=("Arial", size))
    hearts.append(heart)

def create_snow():
    x = random.randint(0, 720)
    y = 0
    size = random.randint(8, 14)
    snow = canvas.create_text(x, y, text="❄️", font=("Arial", size))
    snowflakes.append(snow)

def animate_elements():
    if random.random() < 0.25:
        create_heart()
    if random.random() < 0.4:
        create_snow()

    for heart in hearts[:]:
        canvas.move(heart, 0, -2)
        if canvas.coords(heart)[1] < 0:
            canvas.delete(heart)
            hearts.remove(heart)

    for snow in snowflakes[:]:
        canvas.move(snow, 0, 2)
        if canvas.coords(snow)[1] > 720:
            canvas.delete(snow)
            snowflakes.remove(snow)

    root.after(40, animate_elements)

# ---------------- Click Heart Explosion ----------------
def heart_explosion(event):
    for _ in range(12):
        size = random.randint(10, 18)
        h = canvas.create_text(
            event.x + random.randint(-30, 30),
            event.y + random.randint(-30, 30),
            text="❤️",
            font=("Arial", size)
        )
        explode(h, random.randint(-6, 6), random.randint(-6, 6))

def explode(item, dx, dy, steps=15):
    if steps > 0:
        canvas.move(item, dx, dy)
        root.after(40, explode, item, dx, dy, steps - 1)
    else:
        canvas.delete(item)

canvas.bind("<Button-1>", heart_explosion)

# ---------------- Animated Text ----------------
colors = itertools.cycle(["#ff4d6d", "#ff99c8", "#ffd6ff", "white", "#ffc8dd"])

wish_label = tk.Label(
    root,
    text="🎉 Happy New Year My Saiyara 🌹❄️❤️",
    font=("Comic Sans MS", 24, "bold"),
    bg="#1a001a"
)
wish_label.pack(pady=15)

def animate_text():
    wish_label.config(fg=next(colors))
    root.after(400, animate_text)

# ---------------- Image Slideshow ----------------
images = []
image_cycle = None
current_img = None

image_label = tk.Label(root, bg="#1a001a")
image_label.pack(pady=10)

def upload_images():
    global image_cycle
    files = filedialog.askopenfilenames(
        filetypes=[("Images", "*.jpg *.png *.jpeg")]
    )
    images.clear()
    for file in files:
        img = Image.open(file)
        img = img.resize((420, 300))
        images.append(ImageTk.PhotoImage(img))

    if images:
        image_cycle = itertools.cycle(images)
        show_images()

def show_images():
    global current_img
    current_img = next(image_cycle)
    image_label.config(image=current_img)
    root.after(2500, show_images)

upload_btn = tk.Button(
    root,
    text="Upload Our Memories 💑",
    font=("Arial", 14),
    command=upload_images,
    bg="#ffb3c6",
    relief="flat"
)
upload_btn.pack(pady=15)

# ---------------- Love Letter ----------------
frame = tk.Frame(root, bg="#1a001a")
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

love_text = tk.Text(
    frame,
    width=65,
    height=10,
    wrap="word",
    font=("Arial", 12, "italic"),
    bg="#2a002a",
    fg="white",
    yscrollcommand=scrollbar.set,
    relief="flat"
)
love_text.pack()
scrollbar.config(command=love_text.yview)

love_text.insert("1.0", """Lines for you my babes 💖

My Saiyara ❄️ 🌹
Mare sahiba 🌹

Usama hamesha ap ky sath ha
kbhi akela nahi choray ga
har condition my mare jan ♥️💖

You are my everything ❤️
My princess 🩷
My queen 👑

Mara bacha ♥️
Mara piyara baby 🐥
""")
love_text.config(state="disabled")

# ---------------- Footer ----------------
footer = tk.Label(
    root,
    text="Click anywhere for heart explosion 💥❤️",
    font=("Arial", 12, "italic"),
    bg="#1a001a",
    fg="#ffc8dd"
)
footer.pack(pady=8)

# ---------------- Start ----------------
animate_text()
animate_elements()

root.mainloop()
