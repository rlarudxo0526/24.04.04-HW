## Self Study 10-5 ##
from tkinter import *
from tkinter.filedialog import*

def func_open():
    filename = askopenfilename(parent=window, filetypes=(("GIF파일", "*.gif"),("모든 파일","*.*")))
    photo = PhotoImage(file = filename)
    width = photo.width()
    height = photo.height()

    for i in range(height):
        for k in range(width):
            r,g,b = photo.get(k,i)
            grey = int((r+g+b)/3)
            photo.put("#%02x%02x%02x" %(grey,grey,grey), (k,i))
            
    pLabel.configure(image=photo)
    pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy()

window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel=Label(window, image = photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.mainloop()
