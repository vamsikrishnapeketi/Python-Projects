import tkinter.filedialog
import tkinter as tk
from PIL import ImageTk, Image

FONT_NAME = "Courier"
WATERMARK = "By Vamsi Krishna"
image_file = ""

root = tk.Tk()
root.title("Image Watermark Adder")

def upload_image():
    global image_file
    image_file = tk.filedialog.askopenfilename(title="Select an image", filetypes=[("Image Files", "*.jpg *.png *.gif")])

button = tk.Button(root, text="Upload Image", command=upload_image)
button.pack()


canvas = tk.Canvas(width=200, height=224, highlightthickness=0)
uploaded_img = tk.PhotoImage(file=image_file)
canvas.create_image(100,112,image= uploaded_img)
watermark = canvas.create_text(100,130, text="00:00",fill="white", font=(FONT_NAME, 35, "bold"))
canvas.itemconfig(watermark, text=WATERMARK)

canvas.pack()

root.mainloop()