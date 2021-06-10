from tkinter import *
def click(key) :
    if key == '자동선택' :
        try :
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except :
            entry.insert(END, "오류!!!!!!")
    elif key == '초기화' :
        entry.delete(0, END)
    else :
        entry.insert(END, key)

buttons = ['1', '2', '3', '4', '5', '6', '7',
           '8', '9', '10', '11', '12', '13', '14',
           '15', '16', '17', '18', '19', '20', '21',
           '22', '23', '24', '25', '26', '27', '28',
           '29', '30', '31', '32', '33', '34', '35',
           '36', '37', '38', '39', '40', '41', '42',
           '43', '44', '45', ' ', ' ', ' ', ' ',
           ' ', '초기화', ' ', ' ', '자동선택', ' ', ' ']
        
window = Tk()
window.title("로또 시뮬레이션")

i = 0
for b in buttons :
    cmd = lambda x=b : click(x)
    but = Button(window, text=b, width=7,
                 relief='ridge', command=cmd)
    but.grid(row=i//7+1, column=i%7)
    i += 1
    
    entry = Entry(window, width=30, bg='yellow')
    entry.grid(row=0, column=0, columnspan=10)

window.mainloop()