from tkinter import *
root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0) #extended : 여러개선택 single : 한개만 선택 height=0:전체가 보임
                                                         #height=3:3개만 보임
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermellon")
listbox.insert(END, "grape")
listbox.pack()


def btncmd():
#   listbox.delete(END) #맨 뒤에 항목을 삭제
#   listbox.delete(0)   #맨 앞에서 부터 삭제
    #갯수 확인
    #print("리스트에는", listbox.size(), "개가 있어요")
    #항목 확인
    #print("1번째부터 3번째까지의 항목 :", listbox.get(0, 2))
    #선택된 항목 확인(인덱스값으로 반환)
    print("선택된 항목 :", listbox.curselection())



btn = Button(root, text="Click", command=btncmd)
btn.pack()


root.mainloop()