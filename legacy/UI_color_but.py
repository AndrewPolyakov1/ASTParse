import shutil
from tkinter import Entry, Tk, Button, Label, Listbox, Frame, Text, PhotoImage, filedialog, Toplevel
from PIL import Image, ImageTk
import py2art

class TokenPreviewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Token Previewer")
        self.root.geometry('1350x800') 
        self.selected_token = None
        self.text_content = None

        # Кнопку для открытия нового окна !!!
        self.custom_button = Button(root, text="Открыть новое окно", command=self.open_new_window, width=12, height=1)
        self.custom_button.place(x=45, y=350)

        # Кнопка "Открыть файл"
        self.open_file_button = Button(root, text="Открыть файл", command=self.open_file, width=12, height=1)
        self.open_file_button.place(x=45, y=50)

        # Кнопка "Сохранить файл"
        self.save_file_button = Button(root, text="Сохранить файл", command=self.save_file, width=12, height=1)
        self.save_file_button.place(x=45, y=100)

        # Создаем список токенов
        self.tokens = [("Token 1", "tвыаплаывплоаывплвыальпьлаывпль ываьпываьлпьлыва выаьпл ыалв", Image.open('token1.png'))]

        # Создаем выпадающий список для отображения токенов
        self.token_listbox = Listbox(root, selectmode="single", width=16, height=len(self.tokens))
        for token in self.tokens:
            self.token_listbox.insert("end", token[0])
        self.token_listbox.place(x=45, y=150)
        self.token_listbox.bind("<<ListboxSelect>>", self.show_preview)

        # Создаем фрейм для предпросмотра txt
        self.preview_frame_txt = Frame(root, bd=2, relief="solid")
        self.preview_frame_txt.place(x=245, y=50)

        # Создаем метку для отображения текста
        self.text_preview = Text(self.preview_frame_txt, height=49, width=65, state="disabled")
        self.text_preview.pack()
        self.text_label = Label(self.preview_frame_txt, text="Text Preview:")
        self.text_label.pack()

        # Создаем фрейм для предпросмотра im
        self.preview_frame_im = Frame(root, bd=2, relief="solid")
        self.preview_frame_im.place(x=800, y=50, width=600, height=800)

        # Создаем метку для отображения изображения
        self.image_preview = Label(self.preview_frame_im)
        self.image_preview.pack()
        self.image_label = Label(self.preview_frame_im, text="Image Preview:")
        self.image_label.pack()

    def show_preview(self, event):
        selected_index = self.token_listbox.curselection()
        if selected_index:
            self.selected_token = self.tokens[selected_index[0]]
            text_content = str(self.selected_token[1]) 
            image_file = self.selected_token[2]

            # Отображаем псевокод
            self.text_preview.config(state="normal")
            self.text_preview.delete(1.0, "end")
            self.text_preview.insert("end",text_content)
            self.text_preview.config(state="disabled")

            # Отображаем изображение с фиксированным размером
            try:
                fixed_size = (
                    self.preview_frame_im.winfo_width(),
                    self.preview_frame_im.winfo_height()
                )
                image = image_file
                image.thumbnail(fixed_size, Image.BICUBIC)
                self.photo_image = ImageTk.PhotoImage(image)

                self.image_preview.config(image=self.photo_image)
            except Exception as e:
                print(f"Ошибка загрузки изображения: {e}")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_content = file.read()
                self.tokens = py2art.wrapper(file_path)
                self.text_preview.config(state="normal")
                self.text_preview.delete(1.0, "end")
                self.text_preview.insert("end", self.text_content)
                self.text_preview.config(state="disabled")

            self.token_listbox.destroy()
            self.token_listbox = Listbox(root, selectmode="single", width=16, height=len(self.tokens))
            for token in self.tokens:
                self.token_listbox.insert("end", token[0])
            self.token_listbox.place(x=45, y=150)
            self.token_listbox.bind("<<ListboxSelect>>", self.show_preview)    

            # Сброс выбранного токена
            self.selected_token = None

    def save_file(self):
        if self.selected_token:
            save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if save_path:
                # Сохранение текстового файла
                with open(save_path, "w") as file:
                    # Get the content from the Text widget
                    text_content = self.text_preview.get("1.0", "end-1c")
                    file.write(text_content)

                # Получение пути к изображению
                image_file = self.selected_token[2]
                # Сохранение изображения 
                image_file.save(save_path.replace(".txt", ".png"))

    #НОВОЕ ОКНО
    def open_new_window(self):
        new_window = Toplevel(self.root) 
        new_window.geometry('600x400')
        new_window.title("Кастомизация") 

        # Добавляем виджеты в новое окно
        label = Label(new_window, text="новое окно!")
        label.pack(padx=10, pady=10)

        # Пример кнопки в новом окне
        button = Button(new_window, text="Нажми меня")
        button.pack(padx=10, pady=10)

        new_window.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = TokenPreviewer(root)
    root.mainloop()
