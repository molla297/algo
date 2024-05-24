from tkinter import *
import time

rt = Tk()

f=0 ; k=0; L=0

def movearrow():
    global L
    if L == 0:
        i=0
        while(i<10):
            time.sleep(0.05)
            can.move(arrow,2,0)
            i+=1
            rt.update()
            if i == 10:
                while(i>0):
                    time.sleep(0.05)
                    can.move(arrow,-2,0)
                    i-=1
                    rt.update() 
def stopL():
    global L
    L=1
    
def show_first():
    global arrow
    can.create_text(200,50,text="# Example of LomutoPartition",font=50,fill="Green")
    can.create_text(200,115,text="arr = [4, 5, 3, 7]",font=50)
    can.create_text(100,160,text="left = 0",font=50)
    can.create_text(140,210,text="right = len(arr) - 1",font=50)
    can.create_text(250,260,text="pivot_index = Lomutopartition(arr, left, right)",font=50)
    can.create_text(500,350,text="Move Right ",font=50,fill="red")
    can.create_text(600,365,text="==>> ",font=50,fill="red")
    can.create_text(495,380,text="By Right arrow",font=50,fill="blue",
                    anchor="center",justify="center",activefill="red")
    arrow= can.create_text(500,165,text=">>    >>",font=('time roman',25),fill="red")
    middle()
    
def middle():
    can.create_text(700, 90,text="Notice:",font=50)
    can.create_text(815, 130,text="Right click ",font=50,fill="red")
    can.create_text(1000, 130,text="to show algorithm step by step",font=50)
    can.create_text(815, 170,text="Left click ",font=50,fill="red")
    can.create_text(930, 170,text="to back step one",font=50)
    can.create_text(980, 210,text="if right click not work in moment after left click continue press it",font=50,fill="blue")
    can.create_text(950, 260,text="Now: click Right click",font=50,fill="purple")


def do(event):
    global k
    if k == 0:
        for i in range(10,17):
            can.delete(i)
        k=1
    global f
    if f == 0:
        can.create_text(800, 40,text="def LomutoPartition (A,low,high)",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 1:
        can.create_text(770, 90,text="pivot = A[low]",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 2:
        can.create_text(750, 130,text="s = low",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 3:
        can.create_text(845, 170,text=" for i in range(           ,             ):",font=50)
        can.create_text(937, 170,text="high + 1",font=50,fill="blue")
        can.create_text(860, 170,text="low + 1",font=50,fill="purple")
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 4:
        can.create_text(820, 210,text=" if A[i] < pivot:",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 5:
        can.create_text(850, 250,text="s += 1",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 6:
        can.create_text(900, 290,text="A[s], A[i] = A[i], A[s]",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 7:
        can.create_text(820, 350,text="A[low], A[s] = A[s], A[low]",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 8:
        can.create_text(740, 390,text="return s",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 9:
        can.create_text(1100, 100,text="Let low = 0",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 10:
        can.create_text(1230, 100,text=",Let high = n",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 11:
        can.create_text(1100, 160,text="T(n)=",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 12:
        can.create_text(1150, 140,text="n+1",font=('Time roman',12),fill="blue")
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 13:
        can.create_text(1150, 160,text="∑",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 14:
        can.create_text(1150, 182,text="i=1",font=('Time roman',12),fill="purple")
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 15:
        can.create_text(1160, 162,text="1",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 16:
        can.create_text(1270, 160,text=",∑",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 17:
        can.create_text(1270, 140,text="u",font=('Time roman',12))
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 18:
        can.create_text(1270, 182,text="i=l",font=('Time roman',12))
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 19:
        can.create_text(1282, 162,text="1",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 20:
        can.create_text(1270, 207,text=",u-l+1",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 21:
        can.create_text(1160, 207,text="=n+1-1+1",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 22:
        can.create_text(1140, 237,text="=n+1",font=50)
        print("f=",f)
        f+=1
        print("fnew=",f)
    elif f == 23:
        can.create_text(1148, 270,text="€ Ꝋ(n)",font=50)
        can.create_text(1150, 355,text=" the pivot elemnt: 7",font=50,fill="Green")
        can.create_text(1150, 380,text=" the pivot index: 3",font=50,fill="Green")
        print("f=",f)
        f+=1
        print("fnew=",f)
        
        
def delete_last_circle(event):
    global f,k
    
    if f > 0:
        items = can.find_all()
        if items:
            last_item_id = items[-1]
            can.delete(last_item_id)
            f-=1
            print("F=",f)
            print("Deleted circle with ID:", last_item_id)
        else:
            print("No circles to delete.") 
    
##################################################################3

def on_left_arrow(event):
    if can.canvasx(0) > 0:
        can.xview_scroll(-1, "units")


def on_right_arrow(event):
    stopL()
    if can.canvasx(0) < 600:
        can.xview_scroll(1, "units")
        
#########################################################

text = Text(rt, font=('Arial', 15, 'bold'),width=700)
text.place(x=0,y=450)

################################################################

can = Canvas(rt, width=700, height=450,bg="#f0f8ff")
can.pack(expand=False, fill="both")


rt.bind_all("<Left>", on_left_arrow)
rt.bind_all("<Right>", on_right_arrow)

can.bind("<Button-3>", do)# Change from "<Right>" to "<Button-3>"
can.bind("<Button-1>", delete_last_circle)# Change from "<Right>" to "<Button-3>"


show_first()
movearrow()

#rt.resizable(False, False)
rt.mainloop()