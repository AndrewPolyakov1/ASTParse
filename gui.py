from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
file_sel = filedialog.askopenfilename()
print(file_sel)