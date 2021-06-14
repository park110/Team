from tkinter import *
import tkinter.messagebox
import random

win = tkinter.Tk()

win.title("포춘 쿠키")
win.geometry("320x350")

def click_button():
    msg = tkinter.messagebox.showinfo("명언", getList)
    
def click_button2():
    msg = tkinter.messagebox.showinfo("조언", getList2)

textList = ["유일한 선은 앎이요, 유일한 악은 무지이다.", 
            "살기 위해서 먹어야지 먹기 위해서 살아서는 안된다.", 
            "죽음은 인간이 받을 수 있는 축복 중 최고의 축복이다.", 
            "이 세상에서 영예롭게 사는 가장 위대한 길은 우리가 표방하는 모습이 되는 것이다.", 
            "바르게, 아름답게, 정의롭게 사는 것은 결국 모두 똑같은 것이다.", 
            "사탕발린 칭찬이 아닌 분별있는 애정의 증표로 친구를 사귀어라.",  
            "토론이 끝나면 패자는 중상모략을 하기 마련이다.", 
            "모든 언행을 칭찬하는 자보다 결점을 친절하게 말해주는 친구를 가까이하라.",
            "가장 적은 것으로도 만족하는 사람이 가장 부유한 사람이다.", 
            "무지를 아는 것이 곧 앎의 시작이다."  ]

getList = random.choice(textList)

textList2 = ["할까말까 고민되는 일이 있다면 이것을 했을 때 후회할 것인가 생각해보세요.",
             "삶이 피폐하다고 느낀다면 자신만을 위한 시간을 만드는 게 어떨까요?", 
             "제일 어려운 것은 시작입니다. 걱정하지 말고 시작을 먼저 해보는 게 어떨까요?", 
             "남과 비교하지 마세요. 자신의 생활에 만족하는 삶이 즐거운 삶입니다.", 
             "기회는 사소하게 찾아옵니다 미리 준비해야 그 기회를 잡을 수 있습니다.", 
             "과거를 후회하지 마세요 그 과거가 현재의 멋진 당신을 만든 것입니다.", 
             "자제력을 가지는 것이 중요합니다. 얻고 싶은 것이 있다면 자신을 누르고 한 발 물러나세요.", 
             "사랑하는 사람을 마음대로 하려고 하지 마세요. 사랑한다고 전부 가질 수는 없습니다.", 
             "사랑하는 사람에게 사랑한다고 말해주세요. 표현하면 사랑은 배가 됩니다.", 
             "사람을 움직이는 힘은 입이 아니라 귀에서 나옵니다. 잘 들어보세요." ]

getList2 = random.choice(textList2)


rightFrame = Frame(win)
rightFrame.pack(side = RIGHT)

leftFrame = Frame(win)
leftFrame.pack(side = LEFT)

topFrame = Frame(win)
topFrame.pack(side = TOP)

bottomFrame = Frame(win)
bottomFrame.pack(side = BOTTOM)

button = tkinter.Button(win, text="명언", font=("System", 20), bg="yellow", relief='ridge', width=7, command=click_button)
button2 = tkinter.Button(win, text="조언", font=("System", 20), bg="aliceblue", relief='ridge', width=7, command=click_button2)

button.pack()
button2.pack()

win.mainloop()