from sre_constants import SRE_FLAG_ASCII
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import shutil
from tkinter import Tk, Button, Label, Listbox, Frame, Text, PhotoImage, filedialog, ttk, Menu, Toplevel, colorchooser, Scrollbar, scrolledtext, LabelFrame
import py2art
from tkinter.constants import CENTER

class CustomizationWindow():
        
        customizationExists = False
        formats = py2art.get_supported_formats()
        cur_format = formats[0]
        def __init__(self, parent : Tk) -> None:
             self.parent = parent
             pass

        def on_closing(self):
            self.customizationExists = False
            self.child.destroy()

        def change_color(self, element : str, key : str):
            color_code = colorchooser.askcolor(color=self.node_styles[key],title ="Choose " + element +  "'s color", parent=self.child)
            if color_code[1] is not None:
                self.node_styles[key] = color_code[1]
                py2art.change_keys_colors(self.node_styles)
                self.key_image = py2art.get_keys_image()
                self.key_image = ImageTk.PhotoImage(self.key_image)
                self.image.config(image=self.key_image)

        def change_format(self, event):
            self.cur_format = self.formats[self.combobox_format.current()]
        
        def show(self):
            if not self.customizationExists:
                self.node_styles = py2art.get_keys_colors()
                self.child = Toplevel(self.parent)
                self.customizationExists = True
                # 0 - Create general Frame for objects
                self.frame_general = ttk.Frame(self.child)
                self.frame_general.grid(row=0, column=0, sticky=N+W+E+S, pady=20)
                # 0 - 1 - Create Frames for buttons and formats
                self.frame_gr1 = ttk.Frame(self.frame_general)
                self.frame_gr1.grid(row=0, column=0, padx=20, pady=20, sticky='nw')
                # 1 - Create Frame for buttons
                self.frame_box_button = ttk.Frame(self.frame_gr1, style='Card.TFrame')
                self.frame_box_button.grid(row=0, column=0, padx=10, pady=20)
                # 1 - 0 Create label colors
                self.label_txt = ttk.Label(self.frame_box_button,
                                   text="Change Colors",
                                   font=(None, 16))
                self.label_txt.grid(row=0, columnspan=4, pady=10)
                # 1 - 1 Button change If color
                self.button_If_color = ttk.Button(self.frame_box_button,
                                      text='if',
                                      command= lambda: self.change_color('If', 'If'),
                                      width=10)
                self.button_If_color.grid(row=1, column=0, padx=10, pady=5)
                # 1 - 2 Button change For color
                self.button_For_color = ttk.Button(self.frame_box_button,
                                      text='for',
                                      command= lambda: self.change_color('For', 'For'),
                                      width=10)
                self.button_For_color.grid(row=1, column=1, padx=10, pady=5)
                # 1 - 3 Button change While color
                self.button_While_color = ttk.Button(self.frame_box_button,
                                      text='while',
                                      command= lambda: self.change_color('While', 'While'),
                                      width=10)
                self.button_While_color.grid(row=1, column=2, padx=10, pady=5)
                # 1 - 4 Button change Try color
                self.button_Try_color = ttk.Button(self.frame_box_button,
                                      text='try',
                                      command= lambda: self.change_color('Try', 'Try'),
                                      width=10)
                self.button_Try_color.grid(row=1, column=3, padx=10, pady=5)
                # 1 - 5 Button change input color
                self.button_input_color = ttk.Button(self.frame_box_button,
                                      text='input',
                                      command= lambda: self.change_color('input', 'input'),
                                      width=10)
                self.button_input_color.grid(row=2, column=0, padx=10, pady=5)
                # 1 - 6 Button change Return color
                self.button_Return_color = ttk.Button(self.frame_box_button,
                                      text='return',
                                      command= lambda: self.change_color('Return', 'Return'),
                                      width=10)
                self.button_Return_color.grid(row=2, column=1, padx=10, pady=5)
                # 1 - 7 Button change Raise color
                self.button_Raise_color = ttk.Button(self.frame_box_button,
                                      text='raise',
                                      command= lambda: self.change_color('Raise', 'Raise'),
                                      width=10)
                self.button_Raise_color.grid(row=2, column=3, padx=10, pady=5)
                # 1 - 8 Button change Call color
                self.button_Call_color = ttk.Button(self.frame_box_button,
                                      text='call',
                                      command= lambda: self.change_color('Call', 'Call'),
                                      width=10)
                self.button_Call_color.grid(row=3, column=0, padx=10, pady=5)
                # 1 - 9 Button change code background color
                self.button_default_color = ttk.Button(self.frame_box_button,
                                      text='default',
                                      command= lambda: self.change_color('code background', 'default'),
                                      width=10)
                self.button_default_color.grid(row=3, column=1, padx=10, pady=5)
                # 2 Create Frame for comboBox with format
                self.frame_box_format = ttk.Frame(self.frame_gr1, style='Card.TFrame')
                self.frame_box_format.grid(row=1, column=0, padx=20, pady=20, sticky='nw')
                # 1 - 0 Create label colors
                self.label_txt = ttk.Label(self.frame_box_format,
                                   text="Choose format",
                                   font=(None, 16))
                self.label_txt.grid(row=0, pady=10)
                
                # 2 - 1 Create comboBox with formats

                self.combobox_format = ttk.Combobox(self.frame_box_format,
                                    value=self.formats,
                                    state='readonly',
                                    width=30)
                self.combobox_format.current(self.formats.index(self.cur_format))
                self.combobox_format.bind("<<ComboboxSelected>>", self.change_format)
                self.combobox_format.grid(row=1, column=0, pady=10)

                # 3 Create Frame for keys Image
                self.frame_general_image = ttk.Frame(self.frame_general, style='Card.TFrame', padding={10, 10, 10 , 10})
                self.frame_general_image.grid(row=0, column=1, padx=10, pady=20, sticky='nw')
                # 3 - 1 Create Image
                self.image = ttk.Label(self.frame_general_image, compound=None)
                self.image.grid(row=1, column=0, sticky=W+E, padx=10)
                key_image = py2art.get_keys_image()
                key_image = ImageTk.PhotoImage(key_image)
                self.image.config(image=key_image)
                    
                
                
                self.child.protocol('WM_DELETE_WINDOW', self.on_closing)
                # self.color_customization_window.geometry('600x400')
                self.child.title("Кастомизация") 

                self.child.mainloop()
            else:
                self.child.wm_state('normal')
                self.child.deiconify()
                self.child.lift()
                self.child.focus()


class TokenPreviewer:
    def __init__(self, root : Tk):
        self.root = root
        self.root.title("PyGraphViz")
        self.screen_width_max = self.root.winfo_screenwidth()
        self.screen_height_max = self.root.winfo_screenheight()
        self.root.maxsize(self.screen_width_max, self.screen_height_max)
        # self.root.geometry('1650x900')
        self.selected_token = None
        self.text_content = None

        # 0 - Create general Frame for objects
        self.frame_general = ttk.Frame(self.root)
        self.frame_general.grid(row=0, column=0, sticky=N+W+E+S, pady=20)

        # 0-1 - Create Frame for 2 Frame (Buttoms and ScrollTexts)

        self.frame_gr1 = ttk.Frame(self.frame_general)
        self.frame_gr1.grid(row=0, column=0, padx=20, pady=20, sticky='nw')

        # 1 - Create Frame for buttons and list of tokens

        self.frame_box_button = ttk.Frame(self.frame_gr1, style='Card.TFrame')
        self.frame_box_button.grid(row=0, column=0, padx=10, pady=20)

        # 1-1 - Button - open file 
        self.button_open = ttk.Button(self.frame_box_button,
                                      text='Open',
                                      command=self.open_file,
                                      width=25)
        self.button_open.grid(row=0, column=0, padx=10, pady=5)

        # 1-2 - Button - save file
        self.button_save = ttk.Button(self.frame_box_button,
                                      text="Save",
                                      command=self.save_file,
                                      width=25)
        self.button_save.grid(row=1, column=0, padx=10, pady=5)

        # 1-3 Frame - save_all
        self.frame_save_all = ttk.Frame(self.frame_box_button)
        self.frame_save_all.grid(row=2, column=0, padx=10, pady=5)

        # 1-3 - Flag - save all files
        self.button_save_all = ttk.Button(self.frame_save_all,
                                          text= "Save all",
                                          command=self.save_file_all,
                                          width=15)
        self.button_save_all.grid(row=0, column=0, padx=0, pady=5)

        # 1-3-1 CheckButton - save dot format

        self.checkbutton_save_dot = ttk.Checkbutton(self.frame_save_all,
                                                    text = '.dot',
                                                    variable=BooleanVar(),
                                                    onvalue=True,
                                                    offvalue=False)
        self.checkbutton_save_dot.grid(row=0, column=1, padx=3, pady=5)

        # 1-4 - Label for combobox
        self.label_tokens = ttk.Label(self.frame_box_button,
                                      text="Functions and classes")
        self.label_tokens.grid(row=3, column=0, pady=10)

        # 1-5 - Create tokens for preview
        self.tokens = [("Preview Function", "PREVIEW", Image.open('assets/token1.png'))]
        _tok = [i[0] for i in self.tokens]

        # 1-6 - Create combobox for tokens
        self.combobox_tokens = ttk.Combobox(self.frame_box_button,
                                            value=_tok,
                                            state='readonly',
                                            width=25)
        self.combobox_tokens.grid(row=4, column=0, pady=10)

        for token in self.tokens:
            self.combobox_tokens.insert("end", token[0])

        self.combobox_tokens.bind("<<ComboboxSelected>>", self.show_preview)

        # 1-7 - Create checkbutton for pseudocode format
        self.checkbutton_pseudo = ttk.Checkbutton(self.frame_box_button,
                                    text="Pseudocode in graph",
                                    variable=BooleanVar(), 
                                    onvalue=True,
                                    offvalue=False)
        self.checkbutton_pseudo.grid(row=5, column=0, pady=5)


        # 2 Create Frame for ScrolledTexts and Labels

        self.frame_box_txt = ttk.Frame(self.frame_gr1, style='Card.TFrame', padding={10, 10, 10, 10})
        self.frame_box_txt.grid(row=0, column=1, padx=20, pady=0, sticky='wn')

        # 2-1 Create Label for first ScrollText

        self.label_txt_1 = ttk.Label(self.frame_box_txt,
                                   text="Pseudocode",
                                   font=(None, 16))
        self.label_txt_1.grid(row=0, column=0, pady=10)

        # 2-2 Create first ScrolledText

        self.text = scrolledtext.ScrolledText(self.frame_box_txt, 
                                              font=(None, 10),
                                              height=15,
                                              width=35)
        self.text.grid(row=1, column=0)

        # 2-3 Create Label for second ScrollText

        self.label_txt = ttk.Label(self.frame_box_txt,
                                   text="Python Code",
                                   font=(None, 16))
        self.label_txt.grid(row=2, column=0, pady=10)

        # 2-4 Create second ScrolledText

        self.text_ini = scrolledtext.ScrolledText(self.frame_box_txt, 
                                              font=(None, 10),
                                              height=15,
                                              width=35)
        self.text_ini.grid(row=3, column=0, pady=10)

        # 3 - Create Frame for Image

        self.frame_general_image = ttk.Frame(self.frame_general, 
                                             style='Card.TFrame', 
                                             padding={10, 10, 10 , 10})
        self.frame_general_image.grid(row=0, column=1, padx=10, pady=20, sticky='n')

        # 3-1 Create Label for Image

        self.label_image = ttk.Label(self.frame_general_image,
                                           text="CFG",
                                           font=(None, 16)
                                           )
        self.label_image.place(anchor=CENTER, rely=10)
        self.label_image.grid(row=0, column=0, padx=0, pady=10)

        # 3-2 Create Image

        self.image = ttk.Label(self.frame_general_image, 
                               compound=None)
        self.image.grid(row=1, column=0, sticky=W+E, padx=10)

        # 4 - Create Menu
        self.customizationWindow = CustomizationWindow(self.root)
        self.mainmenu = Menu(self.root)
        self.root.config(menu=self.mainmenu)
        # self.mainmenu.add_command(label="Customize", command=self.customizationWindow.show)

        open_image = ImageTk.PhotoImage(Image.open("assets/menu.png").resize((30,30)))
        self.mainmenu.open_image = open_image
        
        self.mainmenu.add_command(image=open_image,label="Customize",compound = LEFT, command=self.customizationWindow.show)

        # self.root.columnconfigure(0, weight=1)
        # self.root.rowconfigure(0, weight=1)
        
        # self.frame_general_image.columnconfigure(0, weight=1)
        # self.frame_general_image.rowconfigure(0, weight=1)


    def show_preview(self, event):
        selected_index = self.combobox_tokens.current()

        if selected_index >= 0:
            self.selected_token = self.tokens[selected_index]
            text_content = str(self.selected_token[1]) 
            image_file = self.selected_token[2]

            # Отображаем псевокод
            self.text.config(state="normal")
            self.text.delete(1.0, "end")
            self.text.insert("end",text_content)
            self.text.config(state="disabled")

            # Отображаем изображение с фиксированным размером
            try:
                fixed_size = (
                    self.screen_width_max - self.frame_box_txt.winfo_width(),
                    self.screen_height_max - self.frame_box_txt.winfo_height()
                )
                image = image_file.copy()
                # print (self.root.winfo_screenheight())
                # print(self.screen_width_max)
                # print(self.root.winfo_width())
                # print(self.frame_box_button.winfo_width())
                # print(self.frame_box_txt.winfo_width())
                # print(fixed_size[0])
                image.thumbnail(fixed_size, Image.BICUBIC)
                
                self.photo_image = ImageTk.PhotoImage(image)

                self.image.config(image=self.photo_image)
            except Exception as e:
                print(f"Ошибка загрузки изображения: {e}")
            # self.style_frame.configure('Custom.TFrame', background='#F5FBEF', borderwidth=0, relief='sunken')

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_content = file.read()
                if self.checkbutton_pseudo.instate(['selected']):
                    self.tokens = py2art.code_to_image_and_pseudocode(file_path, pseudocode = True)
                else:
                    self.tokens = py2art.code_to_image_and_pseudocode(file_path, pseudocode = False)
                self.text_ini.config(state="normal")
                self.text_ini.delete(1.0, "end")
                self.text_ini.insert("end", self.text_content)
                self.text_ini.config(state="disabled")
            _tok = [i[0] for i in self.tokens]
            self.combobox_tokens = ttk.Combobox(self.frame_box_button,
                                            value=_tok,
                                            state='readonly',
                                            width=25)
            self.combobox_tokens.grid(row=4, column=0, pady=10)

            for token in self.tokens:
                self.combobox_tokens.insert("end", token[0])

            self.combobox_tokens.bind("<<ComboboxSelected>>", self.show_preview)


            # Сброс выбранного токена
            self.selected_token = None

    def save_file(self):
        if self.selected_token:
            save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text, pseudo, and dot files", ".txt")])
            if save_path:
                # Сохранение текстового файла
                with open(save_path, "w", encoding="utf8") as file:
                    # Получаем содержимое виджета ScrolledText
                    text_content = self.text.get("1.0", "end-1c")
                    file.write(text_content)

                # Получение пути к изображению
                image_file = self.selected_token[2]
                # Сохранение изображения 

                if self.customizationWindow.cur_format == "png":
                    image_file.save(save_path.replace(".txt", ".png"))
                else:
                    py2art.save_image(save_path.replace(".txt", ""), self.selected_token[3], self.customizationWindow.cur_format)


                # Проверяем состояние чекбокса и сохраняем файл в формате .dot, если чекбокс отмечен
                if self.checkbutton_save_dot.instate(['selected']):
                    with open(save_path.replace(".txt", ".dot"), "w") as dot_file:
                        dot_content = self.selected_token[3]
                        dot_file.write(dot_content)

                # Проверяем состояние чекбокса и сохраняем файл в формате .dot, если чекбокс отмечен
                if self.checkbutton_save_dot.instate(['selected']):
                    with open(save_path.replace(".txt", ".dot"), "w") as dot_file:
                        dot_content = self.selected_token[3]
                        dot_file.write(dot_content)

    def save_file_all(self):
        folder_path = filedialog.askdirectory()

        if folder_path:
            for index, token in enumerate(self.tokens):
                save_path = f"{token[0]}_{index}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

                with open(f"{folder_path}/{save_path}.txt", "w", encoding="utf8") as file:
                    file.write(str(token[1]))
                
                if self.customizationWindow.cur_format == "png":
                    token[2].save(f"{folder_path}/{save_path}.png")
                else:
                    py2art.save_image(f"{folder_path}/{save_path}", token[3], self.customizationWindow.cur_format)


                if self.checkbutton_save_dot.instate(['selected']):
                    with open(f"{folder_path}/{save_path}.dot", "w") as dot_file:
                        dot_file.write(token[3])
   

if __name__ == "__main__":
    root = Tk()
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")
    root.resizable(True, True)

    app = TokenPreviewer(root)
    root.mainloop()


from tkinter import( 
    Toplevel,
    Button,
    colorchooser,
    Tk,
)

