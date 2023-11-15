from PIL import Image, ImageTk
import shutil
from tkinter import Tk, Button, Label, Listbox, Frame, Text, PhotoImage, filedialog, ttk, Menu, Toplevel, colorchooser
import ASTlib
from tkinter.constants import CENTER

class TokenPreviewer:
    def __init__(self, root : Tk):
        self.root = root
        self.root.title("Token Previewer")
        self.root.geometry('1350x800') 
        self.selected_token = None
        self.text_content = None

        self.style_frame = ttk.Style()
        self.style_frame.configure('Custom.TFrame', background='#F5FBEF', borderwidth=5, relief='sunken')

        self.style_label = ttk.Style()
        self.style_label.configure("My.TLabel", background="#F5FBEF", borderwidth=2, padding=10, foreground="#503D42", font=("Helvetica", 16))


        self.button_frame = ttk.Frame(root)
        self.button_frame.grid(row=0, column=0, padx=50, sticky='n', pady= 50)
        #Кнопка открыть файл
        self.open_file_button = ttk.Button(self.button_frame,
                                           text="Открыть файл", 
                                           command=self.open_file,
                                           style='TButton')
        self.open_file_button.grid(row=0, pady=10)
        # self.open_file_button.place(x=45, y=50)
        # self.open_file_button.pack(side='left')

        #Кнопка закрыть файл
        self.save_file_button = ttk.Button(self.button_frame, 
                                           text="Сохранить файл", 
                                           command=self.save_file,
                                           style='TButton')
        self.save_file_button.grid(row=1, pady=10)
        # self.save_file_button.place(x=45, y=100)
        # self.save_file_button.pack(side='left')

        self.tokens = [("Token 1", "PREVIEW", Image.open('token1.png'))]
        # Создаем выпадающий список для отображения токенов
        self.token_combobox = ttk.Combobox(self.button_frame, 
                                   values=self.tokens, 
                                   state="readonly", 
                                   width=15)
        
        for token in self.tokens:
            self.token_combobox.insert("end", token[0])

        self.token_combobox.grid(row=2, pady=10)
        self.token_combobox.bind("<<ComboboxSelected>>", self.show_preview)

        # self.token_listbox = Listbox(self.button_frame, 
        #                             selectmode="single", 
        #                             width=16, 
        #                             height=len(self.tokens),
        #                             background='#1b4332', 
        #                             foreground='#d8f3dc',
        #                             font=('Helvetica', 12),
        #                             highlightcolor='#40916c',
        #                             highlightbackground='#1b4332')
        
        # for token in self.tokens:
        #     self.token_listbox.insert("end", token[0])

        # self.token_listbox.grid(row=2, pady=10)
        # self.token_listbox.bind("<<ListboxSelect>>", self.show_preview)

        # Создаем фрейм для предпросмотра txt
        self.preview_frame_txt = ttk.Frame(root, style='TFrame')
        # self.preview_frame_txt.pack()
        # self.preview_frame_txt.place(anchor="ne", )
        self.preview_frame_txt.grid(row=0, column=1, padx=50, pady=50)

        # Создаем метку для отображения txt
        self.text_label = ttk.Label(self.preview_frame_txt, text="Text Preview", style='My.TLabel')
        self.text_label.grid(row=0, column=0, sticky="n", padx=50, pady=20)

        self.text_preview = Text(self.preview_frame_txt, height=49, width=60, state="disabled")
        self.text_preview.grid(row=1, column=0, padx=5, pady=5)

        # Создаем фрейм для предпросмотра изображения
        self.preview_frame_im = ttk.Frame(root)
        
        self.preview_frame_im.configure(style='Custom.TFrame')
        # self.preview_frame_im.configure(background='#F5FBEF', borderwidth=5, relief='sunken')
        self.preview_frame_im.grid(row=0, column=2, pady=50)
        self.preview_frame_im.place(x=800,
                                    y=50, 
                                    width=600, 
                                    height=800)

       # Создаем метку для отображения изображения
        self.image_label = ttk.Label(self.preview_frame_im, text="Image Preview", style='My.TLabel')
        self.image_label.place(anchor=CENTER, rely=10)
        self.image_label.grid(row=0, column=0, padx=50, pady=5)
        
        
        self.image_preview = ttk.Label(self.preview_frame_im)
        self.image_preview.grid(row=1, column=0)

        # Создание меню
        self.mainmenu = Menu(self.root)
        self.root.config(menu=self.mainmenu)
        self.mainmenu.add_command(label="Кастомизация", command=self.customization)
 

    def show_preview(self, event):
        selected_index = self.token_combobox.current()
        if selected_index >= 0:
            self.selected_token = self.tokens[selected_index]
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
            self.style_frame.configure('Custom.TFrame', background='#F5FBEF', borderwidth=0, relief='sunken')

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_content = file.read()
                self.tokens = ASTlib.wrapper(file_path)
                self.text_preview.config(state="normal")
                self.text_preview.delete(1.0, "end")
                self.text_preview.insert("end", self.text_content)
                self.text_preview.config(state="disabled")

            self.token_combobox.destroy()
            self.token_combobox = ttk.Combobox(self.button_frame, 
                                   values=self.tokens, 
                                   state="readonly", 
                                   width=16)
        
            for token in self.tokens:
                self.token_combobox.insert("end", token[0])

            self.token_combobox.grid(row=2, pady=10)
            self.token_combobox.bind("<<ComboboxSelected>>", self.show_preview)


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

    customizationExists = False


    def customization(self):
        if not self.customizationExists:
            self.customizationExists = True
                
            self.color_customization_window = Toplevel(self.root) 
            def on_closing():
                self.customizationExists = False
                self.color_customization_window.destroy()
            
            def choose_color(element : str, key):
                color_code = colorchooser.askcolor(title ="Choose color for" ) 
            self.color_customization_window.protocol('WM_DELETE_WINDOW', on_closing)
            self.color_customization_window.geometry('600x400')
            self.color_customization_window.title("Кастомизация") 
            # Добавляем виджеты в новое окно
            label = Label(self.color_customization_window, text="новое окно!")
            label.pack(padx=10, pady=10)

            # Пример кнопки в новом окне
            button = Button(self.color_customization_window, text="Нажми меня")
            button.pack(padx=10, pady=10)

            self.color_customization_window.mainloop()
        else:
            self.color_customization_window.wm_state('normal')
            self.color_customization_window.deiconify()
            self.color_customization_window.lift()
            self.color_customization_window.focus()


if __name__ == "__main__":
    root = Tk()
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")
    # root.configure(bg='#F5FBEF')

    # style = ttk.Style()
    # style.theme_use('clam')

    # style.configure('TButton', 
    #                 background = '#D3F39C', 
    #                 foreground = '#503D42', 
    #                 width = 15, 
    #                 borderwidth=1, 
    #                 focusthickness=3,
    #                 relief="raised",
    #                 font =('Helvetica', 12), 
    #                 borderradius=10, 
    #                 focuscolor='none')
    # style.map('TButton', background=[('active','#84c318')])

    # style.configure('TFrame', background='#F5FBEF', borderwidth=5, relief='sunken')

    app = TokenPreviewer(root)
    root.mainloop()