from sklearn.feature_extraction.text import TfidfVectorizer
import os
from sklearn.metrics.pairwise import cosine_similarity
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from time import time, sleep
from PIL import Image, ImageTk
import tkinter.messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


def convert_array(text):
    return TfidfVectorizer(strip_accents='unicode').fit_transform(text).toarray()



def similar(doc1,doc2):
    return cosine_similarity([doc1,doc2])

def plagiarism(s_vector1,s_vector2,files):
    ans_dict={}
    plagiarism_res=set()
    print(s_vector1)
    print(s_vector2)
    text_vector_a=s_vector2
    i=0
    for text_vector_b in s_vector1:
        sim_score=similar(text_vector_a,text_vector_b)[0][1]
        score=sim_score
        plagiarism_res.add(score)
    for k in plagiarism_res:
        if i<len(files):
            ans_dict[files[i]]=(k*100)
            i+=1
    print(plagiarism_res)
    plt.rcParams["axes.prop_cycle"]=plt.cycler(color=['g','r','b','y'])
    fig1,ax1=plt.subplots()
    ax1.bar(ans_dict.keys(),ans_dict.values())
    ax1.set_title("Plagiarism Level")
    ax1.set_xlabel("Files")
    ax1.set_ylabel("Plagiarism")
    fig2,ax2=plt.subplots()
    ax2.barh(list(ans_dict.keys()),ans_dict.values())
    ax2.set_title("Plagiarism Level")
    ax2.set_xlabel("Files")
    ax2.set_ylabel("Plagiarism")
    fig3,ax3=plt.subplots()
    ax3.pie(ans_dict.values(),labels=ans_dict.keys(),autopct='%1.1f%%')
    ax3.set_title("Plagiarism Breakdown")
    fig4,ax4=plt.subplots()
    ax4.plot(list(ans_dict.keys()),list(ans_dict.values()))
    ax4.set_title("Plagiarism Level")
    ax4.set_xlabel("Files")
    ax4.set_ylabel("Plagiarism")
    fig5,ax5=plt.subplots()
    ax5.fill_between(ans_dict.keys(),ans_dict.values())
    ax5.set_title("Plagiarism Level")
    ax5.set_xlabel("Files")
    ax5.set_ylabel("Plagiarism")
    root3=Tk()
    root3.title("Dashboard")
    root3.iconbitmap('A:/Plagiarism Project/icon.ico')
    root3.state('zoomed')
    upper_frame=Frame(root3)
    upper_frame.pack(fill="both",expand=True)
    canvas1=FigureCanvasTkAgg(fig1,upper_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side="left",fill="both",expand=True)
    canvas2=FigureCanvasTkAgg(fig2,upper_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side="left",fill="both",expand=True)
    canvas3=FigureCanvasTkAgg(fig3,upper_frame)
    canvas3.draw()
    canvas3.get_tk_widget().pack(side="left",fill="both",expand=True)
    lower_frame=Frame(root3)
    lower_frame.pack(fill="both",expand=True)
    canvas4=FigureCanvasTkAgg(fig4,lower_frame)
    canvas4.draw()
    canvas4.get_tk_widget().pack(side="left",fill="both",expand=True)
    canvas5=FigureCanvasTkAgg(fig5,lower_frame)
    canvas5.draw()
    canvas5.get_tk_widget().pack(side="left",fill="both",expand=True)
    
def check_plagiarism(Val_from_file,Lan):
        tkinter.messagebox.showinfo("Processing","Wait for while")
        sleep(5)
        os.chdir('C:\Plagiarism\English')
        files=[i for i in os.listdir() if i.endswith('.txt')]
        notes=[open(_file,encoding='utf-8').read() for _file in files]
        notes.append(Val_from_file)
        vectors1=convert_array(notes)
        vectors2=vectors1[(len(vectors1)-1)]
        plagiarism(vectors1,vectors2,files)
        
        
        
    
def file_insert():
    filetypes = (('text files', '*.txt'),
                 ('All files', '*.*'))
    f = fd.askopenfile(filetypes=filetypes,
                       initialdir="C:\\")
    if f is None:
        tkinter.messagebox.showerror("ERROR","NO FILE PATH")
    else:
        st=""
        for i in f.readlines():
            if i !='{' or i!='}':
                st+=i
        print(st)
        new_root = Tk()
        new_root.title("Plagiarism Checker")
        new_root.iconbitmap('A:/Plagiarism Project/icon.ico')
        new_root.geometry("1350x800") 
        Tab1 = Frame(new_root, bd=10,bg="pale green",width=1350, height=700,relief=RIDGE)
        Tab1.grid()
        topframe1=Frame(Tab1, bd=10,bg="dark green",width=1340, height=100, relief=RIDGE)
        topframe1.grid()
        center_frame=Frame(Tab1,bd=10,bg="dark green",width=800,height=600,relief=RIDGE)
        center_frame.grid()
        centre_mid=Frame(center_frame,bd=5,width=1330,bg="dark sea green",height=550,relief=RIDGE)
        centre_mid.grid()
        centre_mid1=Frame(centre_mid,bd=5,width=1320,bg="dark sea green",height=80)
        centre_mid1.grid(sticky=W)
        centre_mid2=Frame(centre_mid,bd=5,width=1310,bg="dark sea green",height=80)
        centre_mid2.grid(sticky=W)
        centre_mid4=Frame(centre_mid,bd=5,width=1300,bg="dark sea green",height=80)
        centre_mid4.grid()
        title=Label(topframe1,font=('Georgia',45,'bold'),bg="dark sea green",text="   PLAGIRISM CHECKER  ",bd=10)
        title.grid(row=0,column=0,sticky=W)
        title=Label(centre_mid1,font=('Georgia',25,'bold'),bg="dark sea green",text="TEXT",bd=10)
        title.grid(row=0,column=0,sticky=W)
        text_box=Text(centre_mid2,height=15)
        text_box.grid(row=0,column=0,sticky=W)
        text_box.insert('15.0',st)
        but1=Button(centre_mid4,bd=5,font=('Georgia',16,'bold'),width=20,bg="white",text="CHECK PLAGIARISM",command=lambda:check_plagiarism(st,radiobut.get()))
        but1.grid(row=0,column=0)
        
    
        
# root window
root = tk.Tk()
radiobut=StringVar()
root.title('plagiarism')
root.iconbitmap('A:/Plagiarism Project/icon.ico')
root.geometry('500x300')
label = Label(root,text="Click the Button to browse the Files", font=('Georgia 20'))
label.pack(pady=10)
photo = PhotoImage(file = r"A:\Plagiarism Project\buttons.png")
# Create a Button
ttk.Button(root, text="Browse",image=photo,command=file_insert).pack(pady=12)
root.mainloop()
