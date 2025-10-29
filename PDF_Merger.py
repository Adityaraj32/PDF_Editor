from tkinter import filedialog,messagebox
from pypdf import PdfWriter,PdfReader
from docx import Document
from PIL import Image
import customtkinter as ctk

app = ctk.CTk()
app.title("PDF Editor")
app.geometry("700x400")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app.configure(fg_color="#0F2027")

selected_files = []

# For compressing PDF files
def compress_pdf():
    # Selecting Files
    file = filedialog.askopenfilenames(
        title="Select Files",
        filetypes=[("PDF Files","*.pdf")])
    
    if not file:
        return
    
    for file_path in file:
        file_read = PdfReader(file_path)
        file_write = PdfWriter()
        for page in file_read.pages:
            file_write.add_page(page)
        for page in file_write.pages():
            page.compress_content_streams()
        with open("compressed_pdf.pdf","wb") as f:
            file_write.write(f)
    messagebox.showinfo("Title","Fully compressed!")


# For converting the PDF to word file
def pdf_word():
    # for selecting the PDF files
    file = filedialog.askopenfilenames(
        title = "Select Files",
        filetypes= [("PDF Files","*.pdf")])
    # If no file is selected
    if not file:
        return
    # Extracting text and making the word file
    for file_path in file:
        Reader = PdfReader(file_path)
        doc = Document()
        for page in Reader.pages:
            text = page.extract_text()
            if text:
                doc.add_paragraph(text)
                doc.add_page_break()
        doc.save("PDF_Word.docx")  
        messagebox.showinfo("Title","PDF to Word Completed!!!")  

def pdf_ppt():
    pass

def pdf_excel():
    pass


# For Converting Image to PDF file
def select_image():
    file = filedialog.askopenfilenames(
        title = "Select Files",
        filetypes = [("Image","*.jpg *.jpeg *.png")])
    
    # If no file is selected
    if not file:
        return
    elif file:
        selected_files.clear()
        selected_files.extend(file)
    
    Images = []
    for image_path in selected_files:
        image = Image.open(image_path)
        Images.append(image)

    pdf_name = "Image_merged_pdf.pdf"
    Images[0].save(pdf_name, save_all = True ,append_images = Images[1:], resolution = 100.0)
    print("PDF created!!!")


# For Merging PDF files
def merge_pdf():
    # Selecting PDF files
    file = filedialog.askopenfilenames(
    title="Select Files",
    filetypes=[("PDF files", "*.pdf")])

    # If no file is selected
    if not file:
        return
    elif file:
        merger = PdfWriter()
        selected_files.clear()
        selected_files.extend(file)

        for pdf_path in selected_files:
            merger.append(pdf_path)
        merger.write("Mergred_pdf.pdf")
        merger.close()
        print("Merging completed...")


frame = ctk.CTkFrame(app,width=200,height=200,fg_color="#161B22",corner_radius=10)
frame.pack(side="left",padx= 30,pady=30)

button_1 = ctk.CTkButton(frame,text='Make PDF',corner_radius=100, fg_color="#0078FF",hover_color="#005FCC",command=select_image)
button_1.pack(side="left")

button_2 = ctk.CTkButton(frame,text = "Merge PDF",corner_radius=100, fg_color="#0078FF",hover_color="#005FCC",command=merge_pdf)
button_2.pack(side="left")

button_3 = ctk.CTkButton(frame, text = "Compress PDF",corner_radius=100, fg_color="#0078FF",hover_color="#005FCC",command=compress_pdf)
button_3.pack(side="left")

button_4 = ctk.CTkButton(frame, text = "PDF to Word",corner_radius=100, fg_color="#0078FF",hover_color="#005FCC",command=pdf_word)
button_4.pack(side="left")

button_5 = ctk.CTkButton(frame, text = "PDF to PPT",corner_radius=100, fg_color="#0078FF",hover_color="#005FCC",command=pdf_ppt)
button_5.pack(side="left")

button_6 = ctk.CTkButton(frame, text = "PDF to Excel",corner_radius=100, fg_color="#0078FF",hover_color="#005FCC",command=pdf_excel)
button_6.pack(side="left")

app.mainloop()