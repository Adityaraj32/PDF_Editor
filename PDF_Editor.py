from pypdf import PdfWriter
from tkinter import filedialog
from PIL import Image
import ttkbootstrap as ttk


# Merge the PDF files into a single PDF file
def merge_pdf():
    merger = PdfWriter()   
    selected_pdf = filedialog.askopenfilenames(filetypes=[("PDF Files","*.pdf")])
    if selected_pdf:
        for pdf in selected_pdf:
            merger.append(pdf)
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf")
        if output_path:
            merger.write(output_path)


# Converting Image to PDF
def image_to_pdf():
    image_select = filedialog.askopenfilenames(filetypes=[("Image Types","*.jpg *.png *.jpeg")])
    if image_select:
        images = []
        for image in image_select:
            image = Image.open(image)
            image = image.convert("RGB")
            images.append(image)
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf")
        if output_path:
            images[0].save(output_path,save_all = True,append_images =images[1:])
        
# creating a GUI window
root = ttk.Window(themename="superhero")
root.title("PDF Editor")
root.geometry("620x420")
lab1 = ttk.Label(root,text="PDF Editor",font=("Segoe UI",32,"bold"), bootstyle="light", padding=10)
lab1.pack(pady=40)
btn1 = ttk.Button(root, text="📄 Merge PDFs", command=merge_pdf, bootstyle="success-outline", width="30")
btn2 = ttk.Button(root, text="🖼️ Image to PDF", command=image_to_pdf, bootstyle="info-outline", width="30")
btn1.pack(pady=15)
btn2.pack(pady=10)

root.mainloop()