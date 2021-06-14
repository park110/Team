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


win.title("포춘 쿠키")
win.geometry("350x350")

# 버튼 붙이기
button = tkinter.Button(win, text="1", font=("System", 20), bg="yellow", relief='ridge', width=7, command=click_button)
button.grid(column = 0, row = 0)

button2 = tkinter.Button(win, text="2", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button2)
button2.grid(column = 1, row = 0)

button3 = tkinter.Button(win, text="3", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button3)
button3.grid(column = 2, row = 0)

button4 = tkinter.Button(win, text="4", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button4)
button4.grid(column = 3, row = 0)

button5 = tkinter.Button(win, text="5", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button5)
button5.grid(column = 4, row = 0)

button6 = tkinter.Button(win, text="6", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button6)
button6.grid(column = 5, row = 0)

button7 = tkinter.Button(win, text="7", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button7)
button7.grid(column = 6, row = 0)

button8 = tkinter.Button(win, text="8", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button8)
button8.grid(column = 7, row = 0)

button9 = tkinter.Button(win, text="9", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button9)
button9.grid(column = 8, row = 0)

button10 = tkinter.Button(win, text="10", font=("System", 20), bg="yellow", width=7, relief='ridge', command=click_button10)
button10.grid(column = 9, row = 0)


win.mainloop()