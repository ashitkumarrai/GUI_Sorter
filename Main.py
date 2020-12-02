from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
from time import sleep

main = Tk()
main.title("Sorter")
main.geometry("800x570")
main.resizable(False,False)
main.configure(bg='black')
ic=ImageTk.PhotoImage(Image.open('img\\books.png'))
main.iconphoto(FALSE,ic)

#functions
def exc():
    reset()
    x=t.get(1.0,'end-1c')
    l=[i.strip() for i in x.split(',')]
    try:
        l=list(map(int,l))
    except:
        pass
    animator(len(l),l,combo.get())

def animator(length,lst,choice):
    if choice=="Selection Sort":
        srt=selection(length,lst)
    elif choice=="Bubble Sort":
        srt = bubble(length,lst)
    elif choice=="Merge Sort":
        srt=merge(length,lst)
    elif choice=="Quick Sort":
        srt=quick(length,lst)
    elif choice=="Insertion Sort":
        srt=insertion(length,lst)
    outp(srt)
    
def selection(length,lst):
    n=1
    mod=0
    for i in range(length):
        for j in range(i+1,length):
            if ordr.get()=='Ascending':
                if lst[i]>lst[j]:
                    mod=1
            else:
                if lst[i]<lst[j]:
                    mod=1
            Label(labelframe, text='step'+str(n),fg='white',bg='black').grid(row=n,column=0,padx=5 ,pady=10)
            for k in range(length):
                if k==i or k==j:
                    if mod:
                        Label(labelframe, text=lst[k],bg='red').grid(row=n,column=k+1,padx=5 ,pady=10)
                    else:
                        Label(labelframe, text=lst[k],bg='green').grid(row=n,column=k+1,padx=5 ,pady=10)
                else:
                    Label(labelframe, text=lst[k]).grid(row=n,column=k+1,padx=5 ,pady=10)
            if mod:
                lst[i],lst[j]=lst[j],lst[i]
            mod=0
            n=n+1
    while(n<9):
        Label(labelframe,bg='black').grid(row=n,column=0,padx=5 ,pady=10)
        n+=1
    return(lst)

def bubble(length,lst):
    n=0
    mod=0
    s=1
    for i in range(length):
        for j in range(length-1-i):
            if ordr.get()=='Ascending':
                if lst[j]>lst[j+1]:
                    mod=1
                    s=0
            else:
                if lst[j]<lst[j+1]:
                    mod=1
                    s=0
            Label(labelframe, text='step'+str(n+1),fg='white',bg='black').grid(row=n,column=0,padx=5 ,pady=10)
            for k in range(length):
                if k==j or k==j+1:
                    if mod:
                        Label(labelframe, text=lst[k],bg='red').grid(row=n,column=k+1,padx=5 ,pady=10)
                    else:
                        Label(labelframe, text=lst[k],bg='green').grid(row=n,column=k+1,padx=5 ,pady=10)
                else:
                    Label(labelframe, text=lst[k]).grid(row=n,column=k+1,padx=5 ,pady=10)
            if mod:
                lst[j+1],lst[j]=lst[j],lst[j+1]
            mod=0
            n=n+1
        if s:
            while(n<8):
                Label(labelframe,bg='black').grid(row=n,column=0,padx=5 ,pady=10)
                n+=1
            return(lst)
    while(n<8):
        Label(labelframe,bg='black').grid(row=n,column=0,padx=5 ,pady=10)
        n+=1    
    return(lst)

def insertion(length,lst):
    n=1
    s=[]
    p=2
    #list denotion
    Label(labelframe, text='Step1',fg='white',bg='black').grid(row=0,column=0,padx=5 ,pady=10)
    Label(labelframe, text=lst[0],bg='green').grid(row=0,column=1,padx=5 ,pady=10)
    for j in range(len(lst)-1):
        Label(labelframe, text=lst[j+1]).grid(row=0,column=j+2,padx=5 ,pady=10)

    #working
    for i in range(length):
        # utha patak
        
        v=lst.pop(0)
        s.insert(0,v)
        #setting sort list
        for j in range(len(s)-1):
            if ordr.get()=='Ascending':
                if s[j]>s[j+1]:
                    Label(labelframe, text='Step'+str(p),fg='white',bg='black').grid(row=n,column=0,padx=5 ,pady=10)

                    for q in range(len(s)):
                        if q==j:
                            Label(labelframe, text=s[q],bg='red').grid(row=n,column=q+1,padx=5 ,pady=10)
                        else:
                            Label(labelframe, text=s[q]).grid(row=n,column=q+1,padx=5 ,pady=10)
                    Label(labelframe,bg='royalblue4',font="lucida 15").grid(row=n,column=q+2,padx=5 ,pady=10)
                    for k in range(len(lst)):
                        Label(labelframe, text=lst[k]).grid(row=n,column=q+3+k,padx=5 ,pady=10)
                    p+=1
                    n+=1
                    s[j+1],s[j]=s[j],s[j+1]
            else:
                if s[j]<s[j+1]:
                    Label(labelframe, text='Step'+str(p),fg='white',bg='black').grid(row=n,column=0,padx=5 ,pady=10)

                    for q in range(len(s)):
                        if q==j:
                            Label(labelframe, text=s[q],bg='red').grid(row=n,column=q+1,padx=5 ,pady=10)
                        else:
                            Label(labelframe, text=s[q]).grid(row=n,column=q+1,padx=5 ,pady=10)
                    Label(labelframe,bg='royalblue4',font="lucida 15").grid(row=n,column=q+2,padx=5 ,pady=10)
                    for k in range(len(lst)):
                        Label(labelframe, text=lst[k]).grid(row=n,column=q+3+k,padx=5 ,pady=10)
                    p+=1
                    n+=1
                    s[j+1],s[j]=s[j],s[j+1]
            
        Label(labelframe, text='Step'+str(p),fg='white',bg='black').grid(row=n,column=0,padx=5 ,pady=10)
        for a in range(len(s)):
            Label(labelframe, text=s[a]).grid(row=n,column=a+1,padx=5 ,pady=10)
            if a==len(s)-1:
                Label(labelframe,bg='royalblue4',font="lucida 15").grid(row=n,column=a+2,padx=5 ,pady=10)
        if len(lst):
            Label(labelframe, text=lst[0],bg='green').grid(row=n,column=a+3,padx=5 ,pady=10)
        for k in range(len(lst)-1):
            Label(labelframe, text=lst[k+1]).grid(row=n,column=a+4+k,padx=5 ,pady=10)
        p+=1
        n+=1
    while(p<8):
        Label(labelframe,bg='black').grid(row=p,column=0,padx=5 ,pady=10)
        p+=1
    return(s)

def quick(length,lst):
    def partition(a,s,e):
        pindex,pivot=s,lst[e]
        for i in range(s,e):
            if a[i]<=pivot:
                a[i],a[pindex]=a[pindex],a[i]
                pindex+=1
        a[pindex],a[e]=a[e],a[pindex]
        return pindex
    def quickSort(a,s,e):
        if s<e:
            p=partition(a,s,e)
            quickSort(a,s,p-1)
            quickSort(a,p+1,e)

    s=0
    e=length-1
    quickSort(lst,s,e)
    #lst is sorteeddd
    return(lst)

def merge(length,lst):
    pass

def use():
    pass

def abo():
    pass
    
def outp(ls):
    for k in range(len(ls)):
        Label(labelframe2, text=ls[k],font="lucida 22").grid(row=0,column=k,padx=5 ,pady=3)
    if len(ls)==1:
        Label(labelframe2, text="Don't make fool it's already sorted",font="lucida 22").grid(row=0,column=k+1,padx=5 ,pady=3)

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def reset():
    widget_list = all_children(labelframe)
    for item in widget_list:
        item.grid_forget()
    widget_list = all_children(labelframe2)
    for item in widget_list:
        item.grid_forget()

#menu bar
mmenu=Menu(main)
main.config(menu=mmenu)

file=Menu(mmenu,tearoff=False)
about=Menu(mmenu,tearoff=False)

mmenu.add_cascade(label='File',menu=file)
mmenu.add_cascade(label='Help',menu=about)

#file option
rt=ImageTk.PhotoImage(Image.open("img\\1.png"))
file.add_cascade(label="Reset",image = rt,compound = 'left',command=reset)
et=ImageTk.PhotoImage(Image.open("img\\ex.png"))
file.add_cascade(label="Exit",image = et,compound = 'left',command=main.quit)

#about option
hp=ImageTk.PhotoImage(Image.open('img\\about.png'))
about.add_cascade(label="How to Use",image = hp,compound = 'left',command=use)
at=ImageTk.PhotoImage(Image.open('img\\info.png'))
about.add_cascade(label="About",image = at,compound = 'left',command=abo)



container = ttk.Frame(main)
canvas = Canvas(container,bg='black')
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar2 = ttk.Scrollbar(container, orient="vertical", command=canvas.xview)
root = Frame(canvas,width=800,height=350,bg='black')
root.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((0, 0), window=root, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar2.set)

container.pack(fill="both", expand="yes")
canvas.pack( fill="both", expand=True,side='left')
Label(container, text=" X  Y ",bg='black',fg='white').pack(anchor=NE)
scrollbar.pack(side="right", fill="y")
scrollbar2.pack(side="right", fill="y")


Label(root, text="######################################  Enter the list values seprated by comma(,)  ######################################",bg='black',fg='white').pack(pady=2)

#textbox
t = Text(root, height = 2, width = 70,bg='aquamarine',fg='grey36')
t.pack(pady=2)

#choicebox
combo = ttk.Combobox(root,state='readonly',values=[
                                    "Selection Sort",
                                    "Bubble Sort",
                                    "Merge Sort",
                                    "Quick Sort",
                                    "Insertion Sort",],width=35)
ordr = ttk.Combobox(root,state='readonly',values=[
                                    "Ascending","Descending"],width=35)
combo.pack(pady=2)
ordr.pack(pady=2)
ordr.current(0)
combo.current(0)

#execute
btn = Button(root, text = "Execute", 
            command = lambda: exc())
btn.pack(pady=2)


labelframe = LabelFrame(root,text='ANIME SORTER RUNNER',bg='black',fg='white',height=340)
labelframe.pack_propagate(False)
labelframe.pack(fill="x", expand='yes')

lo=Image.open('img\\Capture.png')
ren=ImageTk.PhotoImage(lo)
Label(labelframe,image=ren,bg='grey').place(x=-5,y=-5)

labelframe2 = LabelFrame(root,text='OUTPUT',fg='white',bg='black',height=100)
labelframe2.pack_propagate(False)
labelframe2.pack(fill="x", expand="yes")

main.mainloop()
