from tkinter import *
from tkinter import messagebox
from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


# Screen
root = Tk()
root.geometry("500x335")
root.title("PDF to MP3 File Converter")
root.configure(bg="")


# Function takes the path to the file and the language of audio track.
def pdf_to_mp3(file_path='Xiamen_eng.pdf', language='en'):
    
    if Path(file_path).is_file and Path(file_path).suffix == '.pdf':  # Check if there is a file on a selected path (is_file method) and the file has .pdf extension ('suffix' method).

        # MessageBox to show that a file is processing.
        messagebox.showinfo('Processing', f'Original file: {Path(file_path).name} \nProcessing...')

        # Read the PDF file as a regular string (context manager 'with').
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:  # PDF class of pdfplumber module.
            pages = [page.extract_text() for page in pdf.pages]  # List comprehension construction.
        
        # Join the pages together.
        text = ''.join(pages)
        # Remove line breaks so the audio file won't have long pauses.
        text = text.replace('\n', '')

        # Compile an audio file.
        my_audio = gTTS(text=text, lang=language, slow=False)
        # Get the file's name using 'stem' method.
        file_name = Path(file_path).stem
        # Save audio file with 'save' method, in its parameters pass the file's name.
        my_audio.save(f"{file_name}.mp3")

        return ResultLabel.config(text=f'{file_name}.mp3 saved successfully!\nHave a good day!', fg="Green")


    else:
        return ResultLabel.config(text='File not exists, check the file path!', fg='Red')
        

def main():
    # Get the values for file_path and language from entry boxes
    file_path = AnswerEntry1.get()
    language = AnswerEntry2.get()
    pdf_to_mp3(file_path=file_path, language=language)

    AnswerEntry1.delete(0, "end")
    AnswerEntry2.delete(0, "end")


# Title
Title = Label(root, text="PDF to MP3 File Converter", font=("Arial",30))
Title.pack()


# Main Frame
MainFrame = Frame(root)
MainFrame.pack(pady=40)
MainFrame.configure(bg="")


# File Path Label
GuessNumLabel1 = Label(MainFrame, text="Enter a file's path:", font=("Arial",18))
GuessNumLabel1.pack()


# Answer Entry 1
AnswerEntry1 = Entry(MainFrame, font=("Arial",16), width=50)
AnswerEntry1.pack(pady=10)


# Language Label
GuessNumLabel2 = Label(MainFrame, text="Choose language, for example 'en' or 'ru':", font=("Arial",16))
GuessNumLabel2.pack()


# Answer Entry 2
AnswerEntry2 = Entry(MainFrame, font=("Arial",16))
AnswerEntry2.pack(pady=10)


# Convert File Button
GenerateNumberBtn = Button(MainFrame, text="Convert File", width=16, font=("Arial",16), bg='orange', fg='#15e650', command=main)
GenerateNumberBtn.pack()


# Result Label
ResultLabel = Label(MainFrame, text="", font=("Arial", 16))
ResultLabel.pack()


# Mainloop
root.mainloop()
