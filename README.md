<a id="anchor"></a>
# Конвертер файлов из PDF в mp3 

Данная программа принимает путь до PDF файла и язык для воспроизведения. В результате, формируется mp3 файл с надиктованным текстом :cd:. Используется графический Tkinter интерфейс для взаимодействия с пользователем.


### Полный код программы с комментариями
```
from tkinter import *
from tkinter import messagebox
from gtts import gTTS
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
```

### Скриншоты 
* Главное окно программы. Поле для ввода 'Enter a file's path' принимает полный путь до файла, поле 'Choose language' язык для воспроизведения.
<img width="517" alt="screen1" src="https://user-images.githubusercontent.com/97599612/169635247-c34e5fb0-1dd4-4673-a6f9-32c14fa63ad6.png">


* При заполнении полей ввода 'Enter a file's path'  и 'Choose language' и нажатии на кнопку 'Convert File', появится всплывающее окно с названием конвертируемого файла и сообщением о запуске процесса конвертации.
<img width="770" alt="screen2" src="https://user-images.githubusercontent.com/97599612/169635254-932cdd14-bced-43c4-95bc-a49c194d3eaf.png">

* При завершении процесса преобразования файла в mp3 формат, будет выведено соответствующее сообщение с названием файла и его расширением.
<img width="526" alt="screen3" src="https://user-images.githubusercontent.com/97599612/169639581-eedee8f3-1011-4e95-8db1-05cc722e30e9.png">

* Если путь до файла введен с ошибкой, появится 
соответсвующее предупреждение.
<img width="515" alt="screen4" src="https://user-images.githubusercontent.com/97599612/169635257-e642354e-b6e7-4d3b-8734-f171fdaedb05.png">

* Готовый результат. Оригинальный .pdf файл доступен для прослушивания в mp3 формате.
<img width="681" alt="screen5" src="https://user-images.githubusercontent.com/97599612/169635260-08d3a777-4817-45ae-8601-20b720322bcf.png">

[Вверх](#anchor)