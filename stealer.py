import requests
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Stealer")
window.geometry("400x350")
window.maxsize(400, 350)
window.minsize(400, 350)
window.iconbitmap("assets/logo.ico")
window.config(background='#222222')
bg = PhotoImage(file="assets/background.png")
buttonsteal = PhotoImage(file="assets/img0.png")
buttonupload = PhotoImage(file="assets/img1.png")
class Stealer:
    def __init__(self):
        bgg = Label(window, image=bg, borderwidth=0)
        bgg.place(x=0, y=0)
        self.clothe = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#020059',width=44,borderwidth=0)
        self.clothe.place(x=51, y=203)
        steal = Button(window, image=buttonsteal,bg='#01001B',borderwidth=0, activebackground="#01001B",command=self.stealing)
        steal.place(x=80,y=252)
    def stealing(self):
        clothe = self.clothe.get()
        try:
            r=requests.get(f"https://assetdelivery.roblox.com/v1/assetId/{clothe}")
            if 'errors' in r.json():
                messagebox.showerror("Invalid ID")
            else:
                XML = r.json()['location']
                r2=requests.get(XML)
                JUIC = str(r2.content)
                IDD = str(JUIC.split("<url>http://www.roblox.com/asset/?id=")[1].split("</url>")[0])
                SOP = str(JUIC.split('<string name="Name">')[1].split("</string>")[0])
                if SOP == "Shirt":aaa = "s"
                else:aaa="p"
                r3=requests.get(f"https://www.roblox.com/library/{IDD}").text
                URLL = r3.split("""<span class="thumbnail-span" ><img  class='' src='""")[1].split("'")[0]
                TITLE = str(r3.split("<title>")[1].split("</title>")[0]);TITLE = TITLE.replace(" ","_")
                rurl = requests.get(URLL).content
                print(rurl)
                if aaa == "s":
                    with open(f"steal/shirts/{TITLE}.jpg","wb") as f:
                        f.write(rurl)
                    messagebox.showinfo("Successfully Saved Shirt in steal/shirts/");self.__init__()
                else:
                    with open(f"steal/pants/{TITLE}.jpg","wb") as f:
                        f.write(rurl)
                    messagebox.showinfo("Successfully Saved Pant in steal/pants/");self.__init__()
        except:messagebox.showerror("Invalid ID or Something went wrong")
Stealer()
window.mainloop()
