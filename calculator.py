import tkinter as tk
import math


class Calculator(tk.Tk):
    FONTS = {
        'result_font': ('Arial', 30, 'bold'),
        'button_font': ('Arial', 25),
    }

    ERROR_MESSAGE = 'Error'

    def __init__(self):
        super().__init__()

        self.title('Calculator')
        self.config(bg='azure3')
        self.geometry('500x565')
        self.resizable(0, 0)

        self.grid_columnconfigure(0, weight=1)

        self.result = tk.Entry(self, bd=5, font=self.FONTS['result_font'], justify=tk.CENTER)
        self.result.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        self.result.bind('<Key>', lambda e: 'break')

        button_frame = tk.Frame(self, bg='azure3')
        button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.create_button('9', button_frame, 0, 2, lambda: self.add_number(9))
        self.create_button('8', button_frame, 0, 1, lambda: self.add_number(8))
        self.create_button('7', button_frame, 0, 0, lambda: self.add_number(7))
        self.create_button('6', button_frame, 1, 2, lambda: self.add_number(6))
        self.create_button('5', button_frame, 1, 1, lambda: self.add_number(5))
        self.create_button('4', button_frame, 1, 0, lambda: self.add_number(4))
        self.create_button('3', button_frame, 2, 2, lambda: self.add_number(3))
        self.create_button('2', button_frame, 2, 1, lambda: self.add_number(2))
        self.create_button('1', button_frame, 2, 0, lambda: self.add_number(1))
        self.create_button('0', button_frame, 3, 1, lambda: self.add_number(0))
        
        self.create_button('+', button_frame, 0, 3, lambda: self.add_operator('+'), bg='azure4', fg='white')
        self.create_button('-', button_frame, 1, 3, lambda: self.add_operator('-'), bg='azure4', fg='white')
        self.create_button('×', button_frame, 2, 3, lambda: self.add_operator('*'), bg='azure4', fg='white')
        self.create_button('÷', button_frame, 3, 3, lambda: self.add_operator('/'), bg='azure4', fg='white')
        self.create_button('.', button_frame, 4, 0, lambda: self.add_number('.'), bg='azure4', fg='white', columnspan=5)

        self.create_button('C', button_frame, 3, 0, lambda: self.clear(), bg='darkred', fg='white')
        self.create_button('=', button_frame, 3, 2, lambda: self.calculate(), bg='darkgreen', fg='white')

        self.create_button('sin', button_frame, 0, 4, lambda: self.add_trigonometry_function('sin'), bg='azure4', fg='white')
        self.create_button('cos', button_frame, 1, 4, lambda: self.add_trigonometry_function('cos'), bg='azure4', fg='white')
        self.create_button('tan', button_frame, 2, 4, lambda: self.add_trigonometry_function('tan'), bg='azure4', fg='white')
        self.create_button('π', button_frame, 3, 4, lambda: self.add_number(math.pi), bg='azure4', fg='white')

    def create_button(self, text, frame, row, column, command, bg='white', fg='black', columnspan=1):
        button = tk.Button(frame, text=text, fg=fg, bd=4, font=self.FONTS['button_font'], command=command, width=2, height=1)
        button.config(bg=bg)
        button.grid(row=row, column=column, columnspan=columnspan, sticky=tk.E + tk.W, padx=12, pady=10, ipadx=10)
    
    def add_number(self, number):
        if self.ERROR_MESSAGE in str(self.result.get()):
            self.result.delete(0, tk.END)

        current = self.result.get()
        current += str(number)
        self.result.delete(0, tk.END)
        self.result.insert(0, current)
    
    def add_operator(self, operator):
        if self.ERROR_MESSAGE in str(self.result.get()):
            self.result.delete(0, tk.END)
            
        current = self.result.get()
        current += f" {operator} "
        self.result.delete(0, tk.END)
        self.result.insert(0, current)
    
    def add_trigonometry_function(self, func_name):
        current = self.result.get()
        degree = float(current or 0)
        radian = math.radians(degree)

        # Python 3.10 and Newer
        # match func_name:
        #     case 'sin':
        #         result = str(math.sin(radian))
        #     case 'cos':
        #         result = str(math.cos(radian))
        #     case 'tan':
        #         result = str(math.tan(radian))

        if func_name == 'sin':
            result = str(math.sin(radian))
        elif func_name == 'cos':
            result = str(math.cos(radian))
        elif func_name == 'tan':
            result = str(math.tan(radian))
        
        self.result.delete(0, tk.END)
        self.result.insert(0, result)

    def calculate(self):
        try:
            if str(self.result.get()) != '':
                current = str(self.result.get())
                self.result.delete(0, tk.END)
                self.result.insert(0, eval(current))
        except:
            self.result.delete(0, tk.END)
            self.result.insert(0, self.ERROR_MESSAGE)

    def clear(self):
        self.result.delete(0, tk.END)


if __name__ == '__main__':
    calculator = Calculator()
    calculator.mainloop()
