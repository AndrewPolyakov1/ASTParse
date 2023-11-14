from tkinter import Tk, Button, Label
from PIL import Image, ImageTk  # Убедитесь, что у вас установлена библиотека Pillow

class ImageDisplayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        # Создаем кнопку
        self.button_show_image = Button(root, text="Старт", command=self.show_image)
        self.button_show_image.pack()

        # Создаем метку для отображения изображения (пустая на начальном этапе)
        self.image_label = Label(root)
        self.image_label.pack()

    def show_image(self):
        # Загружаем изображение с использованием Pillow
        image_path = "token1.png"
        try:
            image = Image.open(image_path)
            image = image.resize((300, 300), Image.ANTIALIAS)  # Вы можете изменить размер изображения по вашему усмотрению
            tk_image = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
            return

        # Обновляем метку для отображения нового изображения
        self.image_label.configure(image=tk_image)
        self.image_label.image = tk_image  # Сохраняем ссылку на изображение, чтобы избежать его уничтожения

if __name__ == "__main__":
    root = Tk()
    app = ImageDisplayer(root)
    root.mainloop()
