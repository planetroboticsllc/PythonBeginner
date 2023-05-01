import customtkinter as ctk

app = ctk.CTk()
app.geometry("350x500")
app.title("Calculator")
app.configure(bg_color="white", fg_color="white")

num = 0  # current/previous number
currentText = "0"  # text to display
op = ""  # for operation


def addText(str):
    global currentText
    if float(currentText) == 0 and str != "." and "." not in currentText:
        currentText = ""
    currentText = currentText + str
    updateText()


def plus_minus():
    global currentText
    if "-" in currentText:
        currentText = currentText.replace('-', '')
    else:
        currentText = '-' + currentText
    updateText()


def operationStr(str):
    global op
    global currentText
    global num
    if op != '' or str == '%':  # perform the operation
        performOperation(str)
        op = ""  # reset the operation
    else:
        num = float(currentText)  # store the number

    op = str  # store the new operation
    currentText = "0"  # empty current text


def CE():
    global currentText
    global op
    global num
    currentText = "0"
    num = 0
    op = ""
    updateText()


def C():
    global currentText
    currentText = "0"
    updateText()


def Back():
    global currentText
    currentText = currentText[:len(currentText) - 1]
    updateText()


def performOperation(operation):
    global num
    global currentText
    global op

    if operation == '%':
        n = float(currentText) / 100.0
        currentText = str(n)
        updateText()
        return

    if op == '':
        return  # no operation to perform

    if num == 0:
        num = float(currentText)  # store previous number
        currentText = "0"  # empty the text so user can insert new number
        return

    # get current number
    currentNum = float(currentText)

    # perform actual opertaion
    if op == '+':  # addition
        currentText = str(num + currentNum)
    elif op == '-':  # substraction
        currentText = str(num - currentNum)
    elif op == 'X':  # multiplication
        currentText = str(num * currentNum)
    elif op == '/':  # division
        if currentNum == 0:
            currentText = "0"
        else:
            currentText = str(num / currentNum)
    elif op == '=':
        if currentNum == 0:
            currentText = str(num)
        else:
            num = currentNum

    num = float(currentText)  # reset stored number
    updateText()  # display the result


def updateText():
    global currentText
    if len(currentText) < 1:
        currentText = "0"
    elif len(currentText) > 12:
        currentText = currentText[:12]
    calcLabel.configure(text=currentText)


calcFrame = ctk.CTkFrame(app, width=340, height=90,
                         bg_color="white", fg_color="white")
calcFrame.grid(row=0, column=0, padx=5, pady=5)

calcLabel = ctk.CTkLabel(calcFrame, text="0", width=340, height=70,
                         anchor="e", bg_color="white",
                         font=ctk.CTkFont(size=50))
calcLabel.grid(row=0, column=0, padx=2, pady=2)

btnFrame = ctk.CTkFrame(app, width=340, height=400,
                        bg_color="white", fg_color="white")
btnFrame.grid(row=1, column=0, padx=5, pady=5)

# row = 0
btnCE = ctk.CTkButton(btnFrame, width=75, height=65, text="CE",
                      bg_color="white", fg_color="gray", anchor="center",
                      font=ctk.CTkFont(size=30), command=CE)
btnCE.grid(row=0, column=0, padx=2, pady=2)

btnC = ctk.CTkButton(btnFrame, width=75, height=65, text="C",
                     bg_color="white", fg_color="gray", anchor="center",
                     font=ctk.CTkFont(size=30), command=C)
btnC.grid(row=0, column=1, padx=2, pady=2)

btnBack = ctk.CTkButton(btnFrame, width=75, height=65, text="<--",
                        bg_color="white", fg_color="gray", anchor="center",
                        font=ctk.CTkFont(size=30), command=Back)
btnBack.grid(row=0, column=2, padx=2, pady=2)

btnDivide = ctk.CTkButton(btnFrame, width=75, height=65, text="/",
                          bg_color="white", fg_color="gray", anchor="center",
                          font=ctk.CTkFont(size=30), command=lambda: operationStr('/'))
btnDivide.grid(row=0, column=3, padx=2, pady=2)

# row = 1
btn7 = ctk.CTkButton(btnFrame, width=75, height=65, text="7", text_color="black",
                     bg_color="white", fg_color="gray75", anchor="center",
                     font=ctk.CTkFont(size=30), command=lambda: addText("7"))
btn7.grid(row=1, column=0, padx=2, pady=2)

btn8 = ctk.CTkButton(btnFrame, width=75, height=65, text="8", text_color="black",
                     bg_color="white", fg_color="gray75", anchor="center",
                     font=ctk.CTkFont(size=30), command=lambda: addText("8"))
btn8.grid(row=1, column=1, padx=2, pady=2)

btn9 = ctk.CTkButton(btnFrame, width=75, height=65, text="9", text_color="black",
                     bg_color="white", fg_color="gray75", anchor="center",
                     font=ctk.CTkFont(size=30), command=lambda: addText("9"))
btn9.grid(row=1, column=2, padx=2, pady=2)

btnMultiply = ctk.CTkButton(btnFrame, width=75, height=65, text="X",
                            bg_color="white", fg_color="gray", anchor="center",
                            font=ctk.CTkFont(size=30), command=lambda: operationStr('X'))
btnMultiply.grid(row=1, column=3, padx=2, pady=2)

# row = 2
btn4 = ctk.CTkButton(btnFrame, width=75, height=65, text="4", text_color="black",
                     bg_color="white", fg_color="gray75", anchor="center",
                     font=ctk.CTkFont(size=30), command=lambda: addText("4"))
btn4.grid(row=2, column=0, padx=2, pady=2)

btn5 = ctk.CTkButton(btnFrame, width=75, height=65, text="5", text_color="black",
                     bg_color="white", fg_color="gray75", anchor="center",
                     font=ctk.CTkFont(size=30), command=lambda: addText("5"))
btn5.grid(row=2, column=1, padx=2, pady=2)

btn6 = ctk.CTkButton(btnFrame, width=75, height=65, text="6", text_color="black",
                     bg_color="white", fg_color="gray75", anchor="center",
                     font=ctk.CTkFont(size=30), command=lambda: addText("6"))
btn6.grid(row=2, column=2, padx=2, pady=2)

btnSubstract = ctk.CTkButton(btnFrame, width=75, height=65, text="-",
                             bg_color="white", fg_color="gray", anchor="center",
                             font=ctk.CTkFont(size=30), command=lambda: operationStr('-'))
btnSubstract.grid(row=2, column=3, padx=2, pady=2)

# row = 3
btn1 = ctk.CTkButton(btnFrame, width=75, height=65, text="1", text_color="black",
                     bg_color="white", fg_color="gray75", anchor="center",
                     font=ctk.CTkFont(size=30), command=lambda: addText("1"))
btn1.grid(row=3, column=0, padx=2, pady=2)

btn2 = ctk.CTkButton(btnFrame, width=75, height=65, text="2", text_color="black",
                     bg_color="white", fg_color="gray75", anchor="center",
                     font=ctk.CTkFont(size=30), command=lambda: addText("2"))
btn2.grid(row=3, column=1, padx=2, pady=2)

btn3 = ctk.CTkButton(btnFrame, width=75, height=65, text="3", text_color="black",
                     bg_color="white", fg_color="gray75", anchor="center",
                     font=ctk.CTkFont(size=30), command=lambda: addText("3"))
btn3.grid(row=3, column=2, padx=2, pady=2)

btnAddition = ctk.CTkButton(btnFrame, width=75, height=65, text="+",
                            bg_color="white", fg_color="gray", anchor="center",
                            font=ctk.CTkFont(size=30), command=lambda: operationStr('+'))
btnAddition.grid(row=3, column=3, padx=2, pady=2)

# row = 4
btnPlus_minus = ctk.CTkButton(btnFrame, width=75, height=65, text="+/-", text_color="black",
                              bg_color="white", fg_color="gray75", anchor="center",
                              font=ctk.CTkFont(size=30), command=plus_minus)
btnPlus_minus.grid(row=4, column=0, padx=2, pady=2)

btn0 = ctk.CTkButton(btnFrame, width=75, height=65, text="0", text_color="black",
                     bg_color="white", fg_color="gray75", anchor="center",
                     font=ctk.CTkFont(size=30), command=lambda: addText("0"))
btn0.grid(row=4, column=1, padx=2, pady=2)

btnDot = ctk.CTkButton(btnFrame, width=75, height=65, text=".", text_color="black",
                       bg_color="white", fg_color="gray75", anchor="center",
                       font=ctk.CTkFont(size=30), command=lambda: addText("."))
btnDot.grid(row=4, column=2, padx=2, pady=2)

btnEqual = ctk.CTkButton(btnFrame, width=75, height=65, text="=",
                         bg_color="white", fg_color="gray", anchor="center",
                         font=ctk.CTkFont(size=30), command=lambda: operationStr('='))
btnEqual.grid(row=4, column=3, padx=2, pady=2)

app.mainloop()
