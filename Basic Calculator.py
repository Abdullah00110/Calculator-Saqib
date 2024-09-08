from tkinter import *

class CALCULATOR(Tk):
    eq = ''
    result = ''

    def __init__(self, w=484, h=543, bg='grey'):
        self.w = w
        self.h = h
        self.bg = bg
        super().__init__()

        self.geometry(f"{self.w}x{self.h}")
        self.config(background=self.bg)
        self.title("CALCULATOR BY SAQIB SHAIKH")

        # Bindings for key presses
        self.bind_keys()

    def bind_keys(self):
        for i in [str(x) for x in range(10)] + ['.', '+', '-', '*', '/', 'x', '÷']:
            self.bind(i, self.enter)

        self.bind('<Delete>', self.clear_all)
        self.bind("<Return>", self.calculate)
        self.bind("<BackSpace>", self.backspace)

    def create_display(self, color1='grey16', color2='grey15', fg='white'):
        self.lb1 = Label(self, bg=color1, fg=fg, font='verdana 16', anchor=E)
        self.lb1.place(x=3, y=6, width=self.w-6, height=30)

        self.lb2 = Label(self, bg=color2, fg=fg, font='comicsans 35 bold', anchor=W)
        self.lb2.place(x=3, y=38, width=self.w-6, height=65)

    def create_buttons(self, color='orange1'):
        buttons = [
            ['C', 'CE / ←', '∛', '√'],
            ['X³', 'X²', '÷', '%'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '+'],
            ['1', '2', '3', 'x'],
            ['.', '0', 'ANS', '=']
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                b = Button(self, text=text, font='Vardana 22 bold', activebackground='grey27',
                           bg=color, relief=RIDGE)
                b.place(x=c*120+3, y=r*72+110, width=118, height=70)

                # Bind appropriate functions
                if text not in ['=', 'ANS', 'CE / ←', 'C', '√', '∛', 'X³', 'X²']:
                    b.bind('<Button-1>', self.enter)
                elif text == '=':
                    b.bind('<Button-1>', self.calculate)
                elif text == 'ANS':
                    b.bind('<Button-1>', self.use_answer)
                elif text == 'C':
                    b.bind("<Button-1>", self.clear_all)
                elif text == 'CE / ←':
                    b.bind("<Button-1>", self.backspace)
                elif text == '√':
                    b.bind("<Button-1>", self.square_root)
                elif text == '∛':
                    b.bind("<Button-1>", self.cube_root)
                elif text == 'X²':
                    b.bind("<Button-1>", self.square)
                elif text == 'X³':
                    b.bind("<Button-1>", self.cube)

    def enter(self, event):
        char = event.widget['text'] if event.widget else event.char
        if char in ['x', '÷']:
            char = char.replace('x', '*').replace('÷', '/')
        self.eq += char
        self.lb2.config(text=self.eq)

    def backspace(self, event):
        self.eq = self.eq[:-1]
        self.lb2.config(text=self.eq)

    def clear_all(self, event):
        self.eq = ''
        self.result = ''
        self.lb1.config(text=self.eq)
        self.lb2.config(text=self.result)

    def use_answer(self, event):
        self.eq = self.result
        self.lb2.config(text=self.eq)

    def square_root(self, event):
        try:
            eq_val = eval(self.eq)
            self.result = str(round(eq_val ** 0.5, 2))
            self.update_result(f"√{eq_val} = {self.result}")
        except:
            self.show_error()

    def cube_root(self, event):
        try:
            eq_val = eval(self.eq)
            self.result = str(round(eq_val ** (1 / 3), 2))
            self.update_result(f"³√{eq_val} = {self.result}")
        except:
            self.show_error()

    def square(self, event):
        try:
            eq_val = eval(self.eq)
            self.result = str(round(eq_val ** 2, 2))
            self.update_result(f"({eq_val})² = {self.result}")
        except:
            self.show_error()

    def cube(self, event):
        try:
            eq_val = eval(self.eq)
            self.result = str(round(eq_val ** 3, 2))
            self.update_result(f"{eq_val}³ = {self.result}")
        except:
            self.show_error()

    
    def calculate(self, event):
        try:
            eq_val = eval(self.eq)
            self.result = str(eq_val)
            self.update_result(f"{self.eq} = {self.result}")
        except ZeroDivisionError:
            self.show_error("Cannot divide by zero!")
        except:
            self.show_error()

    def update_result(self, result_text):
        self.lb1.config(text=f"Ans : {result_text}")
        self.lb2.config(text=self.result)
        self.eq = self.result

    def show_error(self, message="Error!"):
        truncated_message = self.truncate_message(message)
        self.lb2.config(text=truncated_message)
        self.lb1.config(text="")

    def truncate_message(self, message, max_chars=20):
        """Truncate the message if it exceeds max characters."""
        if len(message) > max_chars:
            return message[:max_chars] + "..."
        return message

if __name__ == '__main__':
    Calculator = CALCULATOR()
    Calculator.create_display()
    Calculator.create_buttons()
    Calculator.mainloop()

