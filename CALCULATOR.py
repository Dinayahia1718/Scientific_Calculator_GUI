from tkinter import*
import tkinter.messagebox
import math
window= Tk()
window.title(" OUR FIRST CALCULATOR ")
window.resizable(width= False, height= False)   
window.geometry("480x658+50+50")
window.iconbitmap(r"C:\Users\lenovo\Desktop\Python Assignments\sheet 8\001_calculator_JxE_icon.ico")

calculator= Frame(window)
calculator.grid()

#FUNCTIONS#

#when this function is called, the number on the calculator's screen will be evaluated and then be divided by 100 to calculate its percentage and then the answer appears on the screen after what inside it was deleted#

def percent():
   x= eval(num_input.get())
   ans= x/100
   num_input.delete(0, END)
   num_input.insert(0, ans)
   
# this function is used so when it's invoked it evaluates, deletes and calculates the simple operations written on the calculator's screen including summation, subtraction,etc.#

def EQUAL():
   content= eval(num_input.get())
   num_input.delete(0, END)
   num_input.insert(0, str(content))
      
#when this function is called, a message box will appear to the user in order to make sure that he wants to close the calculator, so if he clicks the button "yes" the calculator will disappear, otherwise it will remain.#

def Exit_btn():
   Exit_btn= tkinter.messagebox.askquestion("WARNING!","Are You Sure You Want To Exit?!")
   if Exit_btn == "yes":
      window.destroy()
      
#when this function is called, it's going to evaluate the number written on calculator's screen then delete it and calculate its square root to appear on the screen, and in case the user entered an invalid number including negative numbers, a messagebox will appear to him warning him to check out the used operators and numbers.#         
              
def sqrt_clicked():
   try:
      ans= eval(num_input.get())
      ans=math.sqrt(ans)
      num_input.delete(0, END)
      num_input.insert (0, (ans))  
   except:
      tkinter.messagebox.showerror('ERROR!','Check your values and operators')
         
#when this function is called, the Scientific calculator will appear to the user to be able to use options that aren't found in the standard one including sin, cos, log10, etc.#
                         
def Scientific():
   window.resizable(width= False, height= False)   
   window.geometry("738x638+50+50")
   num_input= Entry(calculator, font=("Times New Roman",20, "bold"), bg="dark gray",fg="white",bd=30, width=48, justify= LEFT)    
   num_input.grid(column=0 ,row=0,columnspan=6)
   num_input.insert(0, "0")
   
   def percent():
      x= eval(num_input.get())
      ans= x/100
      num_input.delete(0, END)
      num_input.insert(0, ans)
      
   def EQUAL():
      content= eval(num_input.get())
      num_input.delete(0, END)
      num_input.insert(0, (content))
         
   def Exit_btn():
      Exit_btn= tkinter.messagebox.askquestion("WARNING!","Are You Sure You Want To Exit?!")
      if Exit_btn == "yes":
         window.destroy()   
       
   def BUTTONS(clicked_num): 
      if num_input.get() == "0":
         num_input.delete(0, END)
         num_input.insert(0, str(clicked_num))
      else:               
         indx= len(num_input.get())
         num_input.insert(indx, str(clicked_num))  
         
   def CLEAR():
      num_input.delete(0, END)
      num_input.insert(0,"0")
              
   def DELETE():
      len_of_nums= len(num_input.get())
      num_input.delete((len_of_nums -1), END)
      if len_of_nums ==0:
         num_input.insert(0,"0")
   
   def OPERATORS(operator):
      if num_input.get() != "0":
         len_of_nums= len(num_input.get())
         num_input.insert( len_of_nums, operator)     
      elif operator == "-":
         num_input.delete(0, END)
         num_input.insert(0, "-")
      elif operator=="(":
         num_input.delete(0, END)
         num_input.insert(0, "(")  
      elif operator==")":
         num_input.delete(0, END)
         num_input.insert(0, ")")

# this function is used to calculate the sin of the number on the screen after evaluating it, where it clears what on the screen and shows the final answer after that, and in case the user entered an invalid number, a messagebox will appear to him warning him to check out the used operators and numbers.#
         
   def sin_clicked():
      try:
         ans= eval(num_input.get())
         ans= math.sin(math.radians(ans))
         num_input.delete(0, END)
         num_input.insert(0, (ans))
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators')    
         
# this function is used to calculate the cos of the number on the screen after evaluating it, where it clears what on the screen and shows the final answer after that, and in case the user entered an invalid number, a messagebox will appear to him warning him to check out the used operators and numbers.#         
         
   def cos_clicked():
      try:
         ans=eval(num_input.get())
         math.sin(math.radians(ans))
         num_input.delete(0, END)
         num_input.insert(0, (ans))
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators')  
         
# this function is used to calculate the tan of the number on the screen after evaluating it, where it clears what on the screen and shows the final answer after that, and in case the user entered an invalid number, a messagebox will appear to him warning him to check out the used operators and numbers.#         
         
   def tan_clicked():
      try:
         ans=eval(num_input.get())
         ans=math.tan(math.radians(ans))
         num_input.delete(0, END)
         num_input.insert (0, (ans))
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators') 
         
   def sqrt_clicked():
      try:
         ans=eval(num_input.get())
         ans=math.sqrt(ans)
         num_input.delete(0, END)
         num_input.insert (0, (ans))  
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators')
         
# this function is used to calculate the log10 of the number on the screen after evaluating it, where it clears what on the screen and shows the final answer after that, and in case the user entered an invalid number "0", a messagebox will appear to him warning him to check out the used operators and numbers.#         
         
   def log10_clicked():
      try:
         ans=eval(num_input.get())
         ans=math.log10(ans)
         num_input.delete(0, END)
         num_input.insert (0, (ans))
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators')
         
# this function is used to calculate the natural log of the number on the screen after evaluating it, where it clears what on the screen and shows the final answer after that, and in case the user entered an invalid number "0", a messagebox will appear to him warning him to check out the used operators and numbers.#                   
         
   def ln_clicked():
      try:
         ans=eval(num_input.get())
         ans=math.log(ans)
         num_input.delete(0, END)
         num_input.insert (0,(ans))
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators')
      
   def sinh_clicked():
      try:
         ans=eval(num_input.get())
         ans=math.sinh(ans)
         num_input.delete(0, END)
         num_input.insert (0,(ans))
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators')
         
   def cosh_clicked():
      try:
         ans=eval(num_input.get())
         ans=math.cosh(ans)
         num_input.delete(0, END)
         num_input.insert (0,(ans))
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators')
         
   def tanh_clicked():
      try:
         ans=eval(num_input.get())
         ans=math.tanh(ans)
         num_input.delete(0, END)
         num_input.insert (0,(ans))
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators')
         
   def asinh_clicked():
      try:
         ans=eval(num_input.get())
         ans=math.asinh(ans)
         num_input.delete(0, END)
         num_input.insert (0,(ans))
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators')
         
   def acosh_clicked():
      try:
         ans=eval(num_input.get())
         ans=math.acosh(ans)
         num_input.delete(0, END)
         num_input.insert (0,(ans))
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators')
         
   def atanh_clicked():
      try:
         ans=eval(num_input.get())
         ans=math.atanh(ans)
         num_input.delete(0, END)
         num_input.insert (0,(ans))
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators')
   
   btn1= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="1",command= lambda: BUTTONS(1))
   btn2= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="2",command= lambda: BUTTONS(2))
   btn3= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="3",command= lambda: BUTTONS(3))
   btn4= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="4",command= lambda: BUTTONS(4))
   btn5= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="5",command= lambda: BUTTONS(5))
   btn6= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="6",command= lambda: BUTTONS(6))  
   btn7= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="7",command= lambda: BUTTONS(7))
   btn8= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="8",command= lambda: BUTTONS(8))
   btn9= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="9",command= lambda: BUTTONS(9))
   btn0= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="0",command= lambda: BUTTONS(0))
   btn_delete= Button(calculator, font=("Times New Roman",20, "bold"), bg="orange",fg="white",bd=5, width=7, height=2, text="Delete",command=DELETE)
   btn_clear= Button(calculator, font=("Times New Roman",20, "bold"), bg="orange",fg="white",bd=5, width=7, height=2, text="Clear",command= CLEAR)
   btn_sum= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=5, height=2, text="+",command=lambda:OPERATORS("+"))
   btn_minus= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=5, height=2, text="-",command= lambda:OPERATORS("-"))
   btn_divide= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=5, height=2, text="÷",command= lambda:OPERATORS("/"))
   btn_mult= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=5, height=2, text="×",command= lambda:OPERATORS("*"))
   btn_equal= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=13, height=2 , text="=",command= EQUAL)
   btn_dot= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=7, height=2, text=".",command= lambda: BUTTONS("."))
   btn_sqrt= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=7, height=2, text="√",command= sqrt_clicked)
   btn_sin= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="sin",command= sin_clicked)
   btn_cos= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="cos",command= cos_clicked)
   btn_tan= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="tan",command= tan_clicked)
   btn_ln= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="ln",command= ln_clicked)
   btn_log10= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="log10",command= log10_clicked)
   btn_brct1= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="(",command= lambda:OPERATORS("("))
   btn_brct2= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text=")",command= lambda:OPERATORS(")"))
   btn_percentage= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="%",command= percent)
   btn_sinh= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="sinh",command= sinh_clicked)
   btn_cosh= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="cosh",command= cosh_clicked)
   btn_tanh= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="tanh",command= tanh_clicked)
   btn_asinh= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="asinh",command= asinh_clicked)
   btn_acosh= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="acosh",command= acosh_clicked)
   btn_atanh= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="atanh",command= atanh_clicked)
   btn_power= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=13, height=2, text="Power",command= lambda:OPERATORS("**"))
   
   btn1.grid(column=0, row=4)
   btn2.grid(column=1, row=4)
   btn3.grid(column=2, row=4)
   btn4.grid(column=0, row=3)
   btn5.grid(column=1, row=3)
   btn6.grid(column=2, row=3)
   btn7.grid(column=0, row=2)
   btn8.grid(column=1, row=2)
   btn9.grid(column=2, row=2)
   btn0.grid(column=1, row=5)
   btn_clear.grid(column=0, row=1)
   btn_delete.grid(column=1, row=1)
   btn_sum.grid(column=3, row=2)
   btn_minus.grid(column=3, row=1)
   btn_divide.grid(column=3, row=3)
   btn_mult.grid(column=3, row=4)
   btn_equal.grid(column=2, row=5, columnspan=2)
   btn_dot.grid(column=0, row=5)
   btn_sqrt.grid(column=2, row=1)
   btn_sin.grid(column=4, row=1)
   btn_cos.grid(column=4, row=2)
   btn_tan.grid(column=4, row=3)
   btn_ln.grid(column=4, row=4)
   btn_log10.grid(column=4, row=5)
   btn_brct1.grid(column=0, row=6)
   btn_brct2.grid(column=1, row=6)
   btn_percentage.grid(column=2, row=6)
   btn_sinh.grid(column=5, row=1)
   btn_cosh.grid(column=5, row=2)
   btn_tanh.grid(column=5, row=3)
   btn_asinh.grid(column=5, row=4)
   btn_acosh.grid(column=5, row=5)
   btn_atanh.grid(column=5, row=6)
   btn_power.grid(column=3, row=6, columnspan=2)
   
#when this function is called, the standard calculator will appear to the user that have options less than that of the scientific one including "+","-","×" signs.#            
        
def Standard():
   window.resizable(width= False, height= False)    
   window.geometry("480x638+50+50")
   num_input= Entry(calculator, font=("Times New Roman",20, "bold"), bg="dark gray",fg="white",bd=30, width=30, justify= LEFT)
   num_input.grid(column=0 ,row=0,columnspan=4) 
   num_input.insert(0, "0")
   
   def percent():
      x= eval(num_input.get())
      ans= x/100
      num_input.delete(0, END)
      num_input.insert(0, ans)
   
   def BUTTONS(clicked_num):
      if num_input.get() == "0":
         num_input.delete(0, END)
         num_input.insert(0, str(clicked_num))
      else:               
         indx= len(num_input.get())
         num_input.insert(indx, str(clicked_num))  
         
   def EQUAL():
      content= eval(num_input.get())
      num_input.delete(0, END)
      num_input.insert(0, str(content))
         
   def Exit_btn():
      Exit_btn= tkinter.messagebox.askquestion("WARNING!","Are You Sure You Want To Exit?!")
      if Exit_btn == "yes":
         window.destroy()         
         
   def CLEAR():
      num_input.delete(0, END)
      num_input.insert(0,"0")
              
   def DELETE():
      len_of_nums= len(num_input.get())
      num_input.delete((len_of_nums -1), END)
      if len_of_nums ==1:
         num_input.insert(0,"0")
   
   def OPERATORS(operator):
      if num_input.get() != "0":
         len_of_nums= len(num_input.get())
         num_input.insert( len_of_nums, operator)   
      elif operator == "-":
         num_input.delete(0, END)
         num_input.insert(0, "-")
      elif operator=="(":
         num_input.delete(0, END)
         num_input.insert(0, "(")  
      elif operator==")":
         num_input.delete(0, END)
         num_input.insert(0, ")")
         
   def sqrt_clicked():
      try:
         ans=eval(num_input.get())
         ans=math.sqrt(ans)
         num_input.delete(0, END)
         num_input.insert (0, (ans))  
      except:
         tkinter.messagebox.showerror('ERROR!','Check your values and operators')
   
   btn1= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="1",command= lambda: BUTTONS(1))
   btn2= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="2",command= lambda: BUTTONS(2))
   btn3= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="3",command= lambda: BUTTONS(3))
   btn4= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="4",command= lambda: BUTTONS(4))
   btn5= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="5",command= lambda: BUTTONS(5))
   btn6= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="6",command= lambda: BUTTONS(6))
   btn7= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="7",command= lambda: BUTTONS(7))
   btn8= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="8",command= lambda: BUTTONS(8))
   btn9= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="9",command= lambda: BUTTONS(9))
   btn0= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="0",command= lambda: BUTTONS(0))
   btn_delete= Button(calculator, font=("Times New Roman",20, "bold"), bg="orange",fg="white",bd=5, width=7, height=2, text="Delete",command=DELETE)
   btn_clear= Button(calculator, font=("Times New Roman",20, "bold"), bg="orange",fg="white",bd=5, width=7, height=2, text="Clear",command= CLEAR)
   btn_sum= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=5, height=2, text="+",command=lambda:OPERATORS("+"))
   btn_minus= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=5, height=2, text="-",command= lambda:OPERATORS("-"))
   btn_divide= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=5, height=2, text="÷",command= lambda:OPERATORS("/"))
   btn_mult= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=5, height=2, text="×",command= lambda:OPERATORS("*"))
   btn_equal= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=13, height=2 , text="=",command= EQUAL)
   btn_dot= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=7, height=2, text=".",command= lambda: BUTTONS("."))
   btn_sqrt= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=7, height=2, text="√",command= sqrt_clicked)
   btn_brct1= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="(",command= lambda:OPERATORS("("))
   btn_brct2= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text=")",command= lambda:OPERATORS(")"))
   btn_power= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="Power",command= lambda:OPERATORS("**"))
   btn_percentage= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=5, height=2, text="%",command= percent)
   
   btn1.grid(column=0, row=4)
   btn2.grid(column=1, row=4)
   btn3.grid(column=2, row=4)
   btn4.grid(column=0, row=3)
   btn5.grid(column=1, row=3)
   btn6.grid(column=2, row=3)
   btn7.grid(column=0, row=2)
   btn8.grid(column=1, row=2)
   btn9.grid(column=2, row=2)
   btn0.grid(column=1, row=5)
   btn_clear.grid(column=0, row=1)
   btn_delete.grid(column=1, row=1)
   btn_sum.grid(column=3, row=2)
   btn_minus.grid(column=3, row=1)
   btn_divide.grid(column=3, row=3)
   btn_mult.grid(column=3, row=4)
   btn_equal.grid(column=2, row=5, columnspan=2)
   btn_dot.grid(column=0, row=5)
   btn_sqrt.grid(column=2, row=1)
   btn_brct1.grid(column=0, row=6)
   btn_brct2.grid(column=1, row=6)
   btn_power.grid(column=2, row=6)
   btn_percentage.grid(column=3, row=6)
            
#when this function is called, the default zero on calculator's screen will be deleted in order to insert the required numbers instead of it to be calculated.#                
            
def BUTTONS(clicked_num):
   if num_input.get() == "0":
      num_input.delete(0, END)
      num_input.insert(0, str(clicked_num))
   else:               
      indx= len(num_input.get())
      num_input.insert(indx, str(clicked_num))
          
#when this function is called, everything on calculator's screen will be deleted in order to calculate new operations, and when everything is cleared, default zero will appear one more time.#               
            
def CLEAR():
   num_input.delete(0, END)
   num_input.insert(0,"0")
           
#this function is used to delete only one number in case we wanted to edit the numbers we entered on the screen.#           
           
def DELETE():
   len_of_nums= len(num_input.get())
   num_input.delete((len_of_nums -1), END)
   if len_of_nums ==1:
      num_input.insert(0,"0")

#this function allows the appearance of the operators on the screen with the numbers to be calculated, and in case there was a default zero on the screen and we needed to insert a "-" sign, this zero will be deleted and will be replaced by "-" sign.#

def OPERATORS(operator):
   if num_input.get() != "0":
      len_of_nums= len(num_input.get())
      num_input.insert( len_of_nums, operator)
   elif operator == "-":
      num_input.delete(0, END)
      num_input.insert(0, "-")
   elif operator=="(":
      num_input.delete(0, END)
      num_input.insert(0, "(")  
   elif operator==")":
      num_input.delete(0, END)
      num_input.insert(0, ")") 
      
Menu_Bar= Menu(calculator)

Options_Menu= Menu(Menu_Bar, tearoff=0)
Menu_Bar.add_cascade( label= "Options", menu= Options_Menu) 
Options_Menu.add_command( label= "Standard Calculator", command= Standard)
Options_Menu.add_separator()
Options_Menu.add_command( label= "Scientific Calculator", command= Scientific)

Exit= Menu(Menu_Bar, tearoff=0)
Menu_Bar.add_cascade( label= "Exit", menu= Exit)
Exit.add_command( label="Want To Exit?", command= Exit_btn)
window.configure( menu=Menu_Bar)

num_input= Entry(calculator, font=("Times New Roman",20, "bold"), bg="dark gray",fg="white",bd=30, width=30)
num_input.grid(column=0 ,row=0,columnspan=4)
num_input.insert(0, "0")
    
btn1= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="1",command= lambda: BUTTONS(1))
btn2= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="2",command= lambda: BUTTONS(2))
btn3= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="3",command= lambda: BUTTONS(3))
btn4= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="4",command= lambda: BUTTONS(4))
btn5= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="5",command= lambda: BUTTONS(5))
btn6= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="6",command= lambda: BUTTONS(6))
btn7= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="7",command= lambda: BUTTONS(7))
btn8= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="8",command= lambda: BUTTONS(8))
btn9= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="9",command= lambda: BUTTONS(9))
btn0= Button(calculator, font=("Times New Roman",20, "bold"), bg="black",fg="white",bd=5, width=7, height=2, text="0",command= lambda: BUTTONS(0))
btn_delete= Button(calculator, font=("Times New Roman",20, "bold"), bg="orange",fg="white",bd=5, width=7, height=2, text="Delete",command=DELETE)
btn_clear= Button(calculator, font=("Times New Roman",20, "bold"), bg="orange",fg="white",bd=5, width=7, height=2, text="Clear",command= CLEAR)
btn_sum= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=5, height=2, text="+",command= lambda:OPERATORS("+"))
btn_minus= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=5, height=2, text="-",command= lambda:OPERATORS("-"))
btn_divide= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=5, height=2, text="÷",command= lambda:OPERATORS("/"))
btn_mult= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=5, height=2, text="×",command= lambda:OPERATORS("*"))
btn_equal= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=13, height=2 , text="=",command= EQUAL)
btn_dot= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=7, height=2, text=".",command= lambda: BUTTONS("."))
btn_sqrt= Button(calculator, font=("Times New Roman",20, "bold"), bg="blue",fg="white",bd=5, width=7, height=2, text="√",command= sqrt_clicked)
btn_brct1= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="(",command= lambda:OPERATORS("("))
btn_brct2= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text=")",command= lambda:OPERATORS(")"))
btn_power= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=7, height=2, text="Power",command= lambda:OPERATORS("**"))
btn_percentage= Button(calculator, font=("Times New Roman",20, "bold"), bg="gray",fg="white",bd=5, width=5, height=2, text="%",command= percent)

btn1.grid(column=0, row=4)
btn2.grid(column=1, row=4)
btn3.grid(column=2, row=4)
btn4.grid(column=0, row=3)
btn5.grid(column=1, row=3)
btn6.grid(column=2, row=3)
btn7.grid(column=0, row=2)
btn8.grid(column=1, row=2)
btn9.grid(column=2, row=2)
btn0.grid(column=1, row=5)
btn_clear.grid(column=0, row=1)
btn_delete.grid(column=1, row=1)
btn_sum.grid(column=3, row=2)
btn_minus.grid(column=3, row=1)
btn_divide.grid(column=3, row=3)
btn_mult.grid(column=3, row=4)
btn_equal.grid(column=2, row=5, columnspan=2)
btn_dot.grid(column=0, row=5)
btn_sqrt.grid(column=2, row=1)
btn_brct1.grid(column=0, row=6)
btn_brct2.grid(column=1, row=6)
btn_power.grid(column=2, row=6)
btn_percentage.grid(column=3, row=6)

window.mainloop()