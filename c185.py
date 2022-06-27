from tkinter import *
from tkinter import filedialog as fd
import hashlib
from simplecrypt import encrypt,decrypt

root=Tk()
root.geometry("250x190")


    
def MD5():
    text_file=fd.askopenfilename(title="open text file",filetypes=(("Text Files","*.txt"),))
    print(text_file)
    read_file=open(text_file,"r")
    paragraph=read_file.read()
    result=hashlib.md5(paragraph.encode())
    file_hexd=result.hexdigest()
    md5_file=open("md5.txt","w")
    md5_file.write(file_hexd)
    md5_file.close()

    

 
btn=Button(root,text="apply md5",command=MD5)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()   
    

