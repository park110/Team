from tkinter import*
import tkinter.messagebox

win = tkinter.Tk()

def click_button():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "나를 죽이지 못하는 고통은 나를 더 강하게 만든다")

def click_button2():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "인연은 만들어 가는 것이다")

def click_button3():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "여전할 것인가, 역전할 것인가")

def click_button4():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "이 책의 앞표지와 뒤표지는 너무 멀리 떨어져있다")

def click_button5():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "단순히 읽기 시작했다는 이유만으로 결코 책을 끝까지 읽지마라")

def click_button6():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "책 없는 방은 영혼 없는 몸과도 같다")

def click_button7():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "강인한 신체에 강인한 정신이 깃든다")

def click_button8():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "목표를 이루고 싶다면 체력부터 길러라")

def click_button9():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "긴 하루 끝에 좋은 책이 기다리고 있다는 생각만으로 그날은 더욱 행복해진다")

def click_button10():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "내가 우울한 생각의 공격을 받을 때 내 책에 달려가는 일처럼 도움이 되는 것은 없다")

def click_button11():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "좋은 책을 읽는다는 것은 과거 몇 세기의 가장 훌륭한 사람들과 이야기를 나누는 것과 같다")

def click_button12():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "R=VD")

def click_button13():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "나만이 내 행복을 지킬 수 있다")

def click_button14():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "누군가의 의견은 당신의 현실이 되지 않는다")

def click_button15():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "우리는 여러가지의 '나'가 될 수 있는 가능성이 있는 사람이다. 그걸 인지하고 있으면 하나 실패하더라도 괜찮다")

def click_button16():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "사람이 작게 태어날진 몰라도, 하는 일은 크게 해야지")

def click_button17():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "새로운 사람을 내 사람으로 만들 게 아니고, 내 주변에 있는 사람들을 더 내 사람으로 만들어야겠다는 생각이 들었어요")

def click_button18():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "읽는 것 만큼 쓰는 것을 통해서도 많이 배운다")

def click_button19():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "한계를 설정하지 마라")

def click_button20():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "의지는 용기를 만든다")

def click_button21():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "좋은 성과를 얻으려면 한 걸음 한 걸음이 힘차고 충실하지 않으면 안 된다")

def click_button22():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "성공의 비결은 단 한 가지, 잘할 수 있는 일에 광적으로 집중하는 것이다")

def click_button23():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "사막이 아름다운 것은 어딘가에 샘이 숨겨져 있기 때문이다")

def click_button24():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "성공해서 만족하는 것이 아니다. 만족하고 있었기 때문에 성공한 것이다")

def click_button25():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "하루 하루를 마지막 날이라고 생각하라")

def click_button26():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "'할 수 없다'고 생각하면 이룰 수 없다")

def click_button27():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "변화의 첫 걸음은 행동에 옮기는 것이다")

def click_button28():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "시련을 당하면 가능한 한 웃어 넘겨라")

def click_button29():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "가장 훌륭한 일은 모험과 도전정신으로 이루어진다")

def click_button30():
    msg = tkinter.messagebox.showinfo("포춘쿠키", "내 비장의 무기는 아직 손 안에 있다. 그것은 바로 희망이다")

rightFrame = Frame(win)
rightFrame.pack(side = RIGHT)

leftFrame = Frame(win)
leftFrame.pack(side = LEFT)

topFrame = Frame(win)
topFrame.pack(side = TOP)

bottomFrame = Frame(win)
bottomFrame.pack(side = BOTTOM)

win.title("포춘 쿠키")
win.geometry("320x350")

# 버튼 붙이기
button = tkinter.Button(leftFrame, text="1", font=("System", 20), bg="yellow", relief='ridge', width=7, command=click_button)
button.pack()

button2 = tkinter.Button(leftFrame, text="2", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button2)
button2.pack()

button3 = tkinter.Button(leftFrame, text="3", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button3)
button3.pack()

button4 = tkinter.Button(leftFrame, text="4", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button4)
button4.pack()

button5 = tkinter.Button(leftFrame, text="5", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button5)
button5.pack()

button6 = tkinter.Button(leftFrame, text="6", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button6)
button6.pack()

button7 = tkinter.Button(leftFrame, text="7", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button7)
button7.pack()

button8 = tkinter.Button(leftFrame, text="8", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button8)
button8.pack()

button9 = tkinter.Button(leftFrame, text="9", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button9)
button9.pack()

button10 = tkinter.Button(leftFrame, text="10", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button10)
button10.pack()

button11 = tkinter.Button(topFrame, text="11", font=("System", 20), bg="aliceblue", width=7, relief='ridge', command=click_button11)
button11.pack()

button12 = tkinter.Button(topFrame, text="12", font=("System", 20), width=7, bg="aliceblue", relief='ridge',  command=click_button12)
button12.pack()

button13 = tkinter.Button(topFrame, text="13", font=("System", 20), width=7, bg="aliceblue", relief='ridge', command=click_button13)
button13.pack()

button14 = tkinter.Button(topFrame, text="14", font=("System", 20), width=7, bg="aliceblue", relief='ridge', command=click_button14)
button14.pack()

button15 = tkinter.Button(topFrame, text="15", font=("System", 20), width=7, bg="aliceblue", relief='ridge', command=click_button15)
button15.pack()

button16 = tkinter.Button(topFrame, text="16", font=("System", 20), width=7, bg="aliceblue", relief='ridge', command=click_button16)
button16.pack()

button17 = tkinter.Button(topFrame, text="17", font=("System", 20), width=7, bg="aliceblue", relief='ridge', command=click_button17)
button17.pack()

button18 = tkinter.Button(topFrame, text="18", font=("System", 20), width=7, bg="aliceblue", relief='ridge', command=click_button18)
button18.pack()

button19 = tkinter.Button(topFrame, text="19", font=("System", 20), width=7, bg="aliceblue", relief='ridge', command=click_button19)
button19.pack()

button20 = tkinter.Button(topFrame, text="20", font=("System", 20), width=7, bg="aliceblue", relief='ridge', command=click_button20)
button20.pack()

button21 = tkinter.Button(rightFrame, text="운동", font=("System", 20), bg="lavenderblush", relief='ridge', width=7, command=click_button21)
button21.pack()

button22 = tkinter.Button(rightFrame, text="22", font=("System", 20), bg="lavenderblush", relief='ridge', width=7, command=click_button22)
button22.pack()

button23 = tkinter.Button(rightFrame, text="23", font=("System", 20), bg="lavenderblush", relief='ridge', width=7, command=click_button23)
button23.pack()

button24 = tkinter.Button(rightFrame, text="24", font=("System", 20), bg="lavenderblush", relief='ridge', width=7, command=click_button24)
button24.pack()

button25 = tkinter.Button(rightFrame, text="25", font=("System", 20), bg="lavenderblush", relief='ridge', width=7, command=click_button25)
button25.pack()

button26 = tkinter.Button(rightFrame, text="26", font=("System", 20), bg="lavenderblush", relief='ridge', width=7, command=click_button26)
button26.pack()

button27 = tkinter.Button(rightFrame, text="27", font=("System", 20), bg="lavenderblush", relief='ridge', width=7, command=click_button27)
button27.pack()

button28 = tkinter.Button(rightFrame, text="28", font=("System", 20), bg="lavenderblush", relief='ridge', width=7, command=click_button28)
button28.pack()

button29 = tkinter.Button(rightFrame, text="29", font=("System", 20), bg="lavenderblush", relief='ridge', width=7, command=click_button29)
button29.pack()

button30 = tkinter.Button(rightFrame, text="30", font=("System", 20), bg="lavenderblush", relief='ridge', width=7, command=click_button30)
button30.pack()

win.mainloop()