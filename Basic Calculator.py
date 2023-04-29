from tkinter import *

class CALCULATOR(Tk) :
    eq =''
    result = ''

    def __init__(self , w = 484 , h = 543 ,bg = 'grey'):
        
        self.w = w 
        self.h = h
        self.bg= bg
        super().__init__()

        for i in [0,1,2,3,4,5,6,7,8,9,'.',"+",'-','*','/','x','÷','X'] :
            self.bind(str(i) , self.Enter)

        self.bind('<Delete>',self.DEL)
        self.bind("<Return>",self.ANS)
        self.bind("<=>",self.calc)
        self.bind("<BackSpace>",self.clear)

        self.geometry(f"{self.w}x{self.h}")
        self.config(background = self.bg)
        self.title("CALCULATOR BY SAQIB SHAIKH")
        #self.resizable(False,False)
    
    def getDisplay(self , color2= 'grey19' , color1 = 'grey16' , fg = 'white') :   
        self.lb1 = Label(self , bg = color1 , fg = fg , font = 'verdana 16')
        self.lb1.place(x = 3 , y = 6  , width = self.w-6 , height = 30) 

        self.lb2 = Label(self , bg = color2 , fg = fg , font = 'comicsans 35 bold' )
        self.lb2.place(x = 3 , y = 38 , width = self.w-6 , height = 65)

    def getButtons(self , color = 'orange1') :

        A = 'ANS'
        C = 'CE / ←'
        l = 110

        bt = [['C','CE / ←','∛','√'],['X³','X²','÷','%'],['7','8','9','-'],['4','5','6','+'],['1','2','3','x'],['.','0',A,'=']]    
        
        for i in bt :
            k = 3
            for j in i :
                b = Button(self , text = j  , font = 'Vardana 22 bold' , activebackground = 'grey27' , bg = color , relief = RIDGE)
                b.place(x = k   , width = 118 , height = 70 , y = l)

                if j not in ['=' , A , C , 'C' , '√' , '∛' , 'X³','X²'] :
                    b.bind('<Button-1>' , self.show)
                elif j == '=' : 
                    b.bind('<Button-1>' , self.calc)
                elif j == A :
                    b.bind('<Button-1>' , self.ANS)
                elif j == 'C' :
                    b.bind("<Button-1>" , self.DEL)
                elif j == C : 
                    b.bind("<Button-1>" , self.clear)
                elif j == '√' :
                    b.bind("<Button-1>" , self.square_root)
                elif j == '∛' :
                    b.bind("<Button-1>" , self.cube_root)
                elif j == 'X²' :
                    b.bind("<Button-1>" , self.square)
                elif j == 'X³' :
                    b.bind("<Button-1>" , self.cube)
                k += 120
            l += 72
        
# ALL FUNCTIONS

    def show (self , event) :
        b =  event.widget 
        self.eq += b['text']
        self.lb1.config(text = self.eq , anchor = E)
        self.lb2.config(text = self.eq , anchor = W)
            
    def clear(self , event) :
        self.eq = self.eq[:-1]
        self.lb2.config(text = self.eq)

    def DEL  (self , event) :
        self.result = ''
        self.eq = ''
        
        self.lb1.config(text=self.eq)
        self.lb2.config(text=self.result)
    
    def ANS  (self , event) :
        self.calc(event)
        self.eq = self.result
        self.lb1.config(text=self.eq)
        self.lb2.config(text=self.eq)

    def square_root(self, event):
        try:
            eq1  = eval(self.eq.translate(str.maketrans('x÷' , '*/')))
            self.result = str(round(eq1 ** 0.5,2))
            self.lb2.config(text=self.result)
            self.lb1.config(text=f"√{eq1} = {self.result}")
            self.eq = self.result
        except:
            self.lb2.config(text="Error!")
            
    def cube_root(self, event):
        try:
            eq1  = eval(self.eq.translate(str.maketrans('x÷' , '*/')))
            self.result = str(round(eq1 ** (1/3),2))
            self.lb2.config(text=self.result)
            self.lb1.config(text=f"³√{eq1} = {self.result}")
            self.eq = self.result
        except:
            self.lb2.config(text="Error!")
            
    def square(self, event):
        try:
            eq1  = eval(self.eq.translate(str.maketrans('x÷' , '*/')))
            self.result = str(round(eq1 ** 2,2))
            self.lb2.config(text=self.result)
            self.lb1.config(text=f"({eq1}² = {self.result}")
            self.eq = self.result
        except:
            self.lb2.config(text="Error!")
            
    def cube(self, event):
        try:
            eq1  = eval(self.eq.translate(str.maketrans('x÷' , '*/')))
            self.result = str(round(eq1 ** 3,2))
            self.lb2.config(text=self.result)
            self.lb1.config(text=f"{eq1}³ = {self.result}")
            self.eq = self.result
        except:
            self.lb2.config(text="Error!")


    def calc (self , event) :

        eq1 = self.eq.translate(str.maketrans('x÷' , '*/'))
        if '%' in eq1 :
            eq1 = eq1.replace('%' , '*(0.01)*')

        if self.eq != ''  :
            try : 
                self.result = f'{eval(eq1)}' 
                
                if ( '.' in self.result ) and ( int(self.result[self.result.index('.') + 1 : ]) == 0 ):
                    self.result = f'{int(eval(self.result))}' 
                
                self.lb2.config(text=self.result , anchor = W)
                self.lb1.config(text = f'Ans  : {self.eq} = '+self.result , anchor = E)
            except  :
                self.lb2.config(text='ERROR !')

    def Enter(self , event) :
        self.eq += event.char
        self.eq  = self.eq.translate(str.maketrans('/X' , '÷x'))
        self.lb2.config(text = self.eq)
        
if __name__ == '__main__' :
    Calculator = CALCULATOR()
    Calculator.getDisplay()
    Calculator.getButtons()
    Calculator.mainloop()

