import tkinter as GUI
from tkinter import *
import math
Cards={}
with open("cards.csv","r")as file:
   current_card=None
   for line in file:
      line=line.strip()
      if line.startswith("card:"):
         current_card=int(line.split(":")[1])
         Cards[current_card]={}
      elif current_card:
         key,value=line.split(":")
         if line.startswith("balance"):
            Cards[current_card][key.strip()]=int(value.strip())
         else :
            Cards[current_card][key.strip()]=(value.strip())
main_window=GUI.Tk()

homePage=Frame(main_window)
secPage=Frame(main_window)
cashPage=Frame(main_window)
fawryPage=Frame(main_window)

homePage.grid(column=0,row=0,sticky="nsew")
secPage.grid(column=0,row=0,stick="nsew")
cashPage.grid(column=0,row=0,stick="nsew")
fawryPage.grid(column=0,row=0,sticky="nsew")
#################################################################

label_1=GUI.Label(homePage,text="PAN")
label_1.pack(side=LEFT,pady=150,padx=60)
 ## 
pan=GUI.Entry(homePage) 
pan.pack(side=LEFT,padx=10)
 ## 
 

def check():
     k=0
     for i in Cards.keys() :
         if pan.get()==f'{i}' :
                  print(pan.get())
                  k+=1
                  label_2=GUI.Label(homePage,text="Password")
                  label_2.place(x=60,y=180) 
                  my_entry_2=GUI.Entry(homePage,show="*")  
                  my_entry_2.place(x=160,y=180) 
                  print(Cards[i]['password'])
                  def checkpass() :
                     p=int(pan.get())
                     if Cards[p]['password']==my_entry_2.get() :
                      bt=GUI.Button(homePage,text="Second page",command=lambda:[secPage.tkraise(),my_entry_2.delete(0,END)])
                      bt.place(x=190,y=220)
                     else :
                       Wrong=GUI.Label(text="Wrong password")
                       Wrong.place(x=160,y=240) 
                       tAbtn=GUI.Button(homePage,text="try again?",command=lambda :[homePage.tkraise(),my_entry_2.delete(0,END)])
                       tAbtn.place(x=190,y=260)
                  btn1=GUI.Button(homePage,text="Enter",command=checkpass)
                  btn1.place(x=190,y=200)
                  
         else:
                  continue
         
     if k==0:         
      Wrong=GUI.Label(text="Cant Find this account")
      Wrong.place(x=160,y=240) 
      tAbtn=GUI.Button(homePage,text="try again?",command=lambda :[homePage.tkraise(),pan.delete(0,END)])
      tAbtn.place(x=190,y=260)


              
 
 ##    
btn=GUI.Button(homePage,text="Enter",command=check)
btn.place(x=190,y=200)
#################### end of page one ###################################


   
class Services :
    def __init__(self,Pan):
        self.Pan=Pan
 
    @classmethod
    def cash_withdraw(self):
        n=GUI.Label(cashPage,text='Enter the amount of money : ')
        n.place(x=50,y=80)
        y=GUI.Entry(cashPage)
        y.place(x=200,y=80)
        def checkentry():
           pr=int(y.get())
           pa=int(pan.get())
           if pr>5000 :
             lm=GUI.Label(cashPage,text='thats of the limits ')
             lm.place(x=50,y=100)
             tAbtn=GUI.Button(cashPage,text="home page",command=lambda :[homePage.tkraise(),pan.delete(0,END)])
             tAbtn.place(x=190,y=260)
           elif  pr>Cards[pa]['balance'] :
               lim=GUI.Label(cashPage,text='thats of the limits in your bank account ')
               lim.place(x=50,y=100)
               tAbtn=GUI.Button(cashPage,text="home page",command=lambda :[homePage.tkraise(),pan.delete(0,END)])
               tAbtn.place(x=190,y=260)
           else:
             Cards[pa]['balance']-=pr
             l=GUI.Label(cashPage,text='Done thank you.... ')
             l.place(x=50,y=100)
             tAbtn=GUI.Button(cashPage,text="home page",command=lambda :[homePage.tkraise(),pan.delete(0,END)])
             tAbtn.place(x=190,y=260)

        btnn=GUI.Button(cashPage,text='Enter',command=checkentry)
        btnn.place(x=220,y=110)
    def balance(self):
       pa=int(pan.get())
       b=GUI.Label(secPage,text=f"Your balance= {Cards[pa]['balance']}")
       b.place(x=100,y=250)
       tAbtn=GUI.Button(secPage,text="home page",command=lambda :[homePage.tkraise(),pan.delete(0,END)])
       tAbtn.place(x=190,y=280)
       name=GUI.Label(secPage,text=f"Welcome {Cards[pa]['Name']}")
       name.place(x=50,y=50) 
    def passChange(self):
        n=GUI.Label(secPage,text='Enter the new password ')
        n.place(x=40,y=230)
        y=GUI.Entry(secPage,width=150)
        y.place(x=190,y=230)
        rn=GUI.Label(secPage,text='Repeat the new password ')
        rn.place(x=40,y=260)
        ry=GUI.Entry(secPage,width=150)
        ry.place(x=210,y=260)
        
        def checkk():
          pa=int(y.get())
          p=int(pan.get())
          if y.get()!=ry.get():
             se=GUI.Label(secPage,text='the password dont matches')
             se.place(x=20,y=290) 
             tAbtn=GUI.Button(secPage,text="try again?",command=lambda :[y.delete(0,END),ry.delete(0,END)])
             tAbtn.place(x=180,y=300)
          elif pa>10000 or pa<999:
             se=GUI.Label(secPage,text='the password should be 4-digits')
             se.place(x=10,y=285) 
             tAbtn=GUI.Button(secPage,text="try again?",command=lambda :[y.delete(0,END),ry.delete(0,END)])
             tAbtn.place(x=180,y=300)
          else:
             Cards[p]['password']=pa  
             se=GUI.Label(secPage,text='                                    saved thank you...     ')
             se.place(x=10,y=285) 
             tAbtn=GUI.Button(secPage,text="home page",command=lambda :[homePage.tkraise(),pan.delete(0,END)])
             tAbtn.place(x=180,y=300) 
             
        chec=GUI.Button(secPage,text="save",background="gray",command=checkk)
        chec.place(x=250,y=290)
    def Fawry(self):
       def selecte():
          n=GUI.Label(fawryPage,text='Enter the number ')
          n.place(x=50,y=180)
          y=GUI.Entry(fawryPage)
          y.place(x=200,y=180)
          m=GUI.Label(fawryPage,text='Enter the amount of money : ')
          m.place(x=50,y=210)
          mm=GUI.Entry(fawryPage)
          mm.place(x=200,y=210)
          def chek() :
               pr=int(mm.get())
               pa=int(pan.get())
               x=len(y.get())
               if x<11 or x>11 :
                  labl=GUI.Label(fawryPage,text='should be 11 digit')
                  labl.place(x=30,y=240)
               elif y.get()[2]!='1':
                  labl=GUI.Label(fawryPage,text='its not an etisatat number')
                  labl.place(x=30,y=240)
               elif  pr>Cards[pa]['balance'] :
                   lim=GUI.Label(fawryPage,text='thats of the limits in your bank account ')
                   lim.place(x=30,y=240)
               else:
                  Cards[pa]['balance']-=pr
                  l=GUI.Label(fawryPage,text='Done thank you.... ')
                  l.place(x=50,y=300)
          btn1=GUI.Button(fawryPage,text="transform",command=chek)
          btn1.place(x=200,y=260)
       def selectw():
          n=GUI.Label(fawryPage,text='Enter the number ')
          n.place(x=50,y=180)
          y=GUI.Entry(fawryPage)
          y.place(x=200,y=180)
          m=GUI.Label(fawryPage,text='Enter the amount of money : ')
          m.place(x=50,y=210)
          mm=GUI.Entry(fawryPage)
          mm.place(x=200,y=210)
         
          def chek() :
               pr=int(mm.get())
               pa=int(pan.get())
               x=len(y.get())
               if x<11 or x>11 :
                  labl=GUI.Label(fawryPage,text='should be 11 digit')
                  labl.place(x=30,y=240)
               elif y.get()[2]!='5':
                  labl=GUI.Label(fawryPage,text='its not an we number')
                  labl.place(x=30,y=240)
               elif  pr>Cards[pa]['balance'] :
                   lim=GUI.Label(fawryPage,text='thats of the limits in your bank account ')
                   lim.place(x=30,y=240)
               else:
                  Cards[pa]['balance']-=pr
                  l=GUI.Label(fawryPage,text='Done thank you.... ')
                  l.place(x=50,y=300)
          btn1=GUI.Button(fawryPage,text="transform",command=chek)
          btn1.place(x=200,y=260)
       def selectv():
          n=GUI.Label(fawryPage,text='Enter the number ')
          n.place(x=50,y=180)
          y=GUI.Entry(fawryPage)
          y.place(x=200,y=180)
          m=GUI.Label(fawryPage,text='Enter the amount of money : ')
          m.place(x=50,y=210)
          mm=GUI.Entry(fawryPage)
          mm.place(x=200,y=210)
         
          def chek() :
               pr=int(mm.get())
               pa=int(pan.get())
               x=len(y.get())
               if x<11 or x>11 :
                  labl=GUI.Label(fawryPage,text='should be 11 digit')
                  labl.place(x=30,y=240)
               elif y.get()[2]!='0':
                  labl=GUI.Label(fawryPage,text='its not an vodafone number')
                  labl.place(x=30,y=240)
               elif  pr>Cards[pa]['balance'] :
                   lim=GUI.Label(fawryPage,text='thats of the limits in your bank account ')
                   lim.place(x=30,y=240)
               else:
                  Cards[pa]['balance']-=pr
                  l=GUI.Label(fawryPage,text='Done thank you.... ')
                  l.place(x=50,y=300)
          btn1=GUI.Button(fawryPage,text="transform",command=chek)
          btn1.place(x=200,y=260)   
       def selecto():
          n=GUI.Label(fawryPage,text='Enter the number ')
          n.place(x=50,y=180)
          y=GUI.Entry(fawryPage)
          y.place(x=200,y=180)
          m=GUI.Label(fawryPage,text='Enter the amount of money : ')
          m.place(x=50,y=210)
          mm=GUI.Entry(fawryPage)
          mm.place(x=200,y=210)
         
          def chek() :
               pr=int(mm.get())
               pa=int(pan.get())
               x=len(y.get())
               if x<11 or x>11 :
                  labl=GUI.Label(fawryPage,text='should be 11 digit')
                  labl.place(x=30,y=240)
               elif y.get()[2]!='2':
                  labl=GUI.Label(fawryPage,text='its not an orange number')
                  labl.place(x=30,y=240)
               elif  pr>Cards[pa]['balance'] :
                   lim=GUI.Label(fawryPage,text='thats of the limits in your bank account ')
                   lim.place(x=30,y=240)
               else:
                  Cards[pa]['balance']-=pr
                  l=GUI.Label(fawryPage,text='Done thank you.... ')
                  l.place(x=50,y=300)
          btn1=GUI.Button(fawryPage,text="transform",command=chek)
          btn1.place(x=200,y=260)
       selectedBtn=GUI.IntVar()
       c=GUI.Label(fawryPage,text='Chosse ')
       c.place(x=50,y=80)
       orange=GUI.Radiobutton(fawryPage,text="Orange Recharge",value=1,variable=selectedBtn,command=selecto)
       orange.place(x=150,y=80)
       etisalat=GUI.Radiobutton(fawryPage,text="etisalat Recharge",value=2,variable=selectedBtn,command=selecte)
       etisalat.place(x=150,y=100)
       vodafone=GUI.Radiobutton(fawryPage,text="vodafone Recharge",value=3,variable=selectedBtn,command=selectv)
       vodafone.place(x=150,y=120)
       we=GUI.Radiobutton(fawryPage,text="we Recharge",value=4,variable=selectedBtn,command=selectw)
       we.place(x=150,y=140)
       tAbtn=GUI.Button(fawryPage,text="home page",command=lambda :[homePage.tkraise(),pan.delete(0,END)])
       tAbtn.place(x=180,y=290)
       
       
         
             
        
        
p=pan.get()
s=Services(p)
s.cash_withdraw()
s.Fawry()
##########endd cash page##############





sec=GUI.Label(secPage,text='Choose your service')
sec.place(x=40,y=80) 
fawry=Button(secPage,text="Fawry service",background="gray",command=lambda:fawryPage.tkraise())
fawry.place(x=170,y=80)
withdraw=GUI.Button(secPage,text="Cash Withdraw",background="gray",command=lambda:cashPage.tkraise())
withdraw.place(x=170,y=120)
Balance_Inquiry=GUI.Button(secPage,text="Balance Inquiry",background="gray",command=s.balance)
Balance_Inquiry.place(x=170,y=160)
Password_Change=GUI.Button(secPage,text="Password Change",background="gray",command=s.passChange)
Password_Change.place(x=170,y=200)

## 

homePage.tkraise()
main_window.title("Bank")
main_window.resizable(False,False)
main_window.geometry("450x450+600+200")
main_window.mainloop()
with open("cards.csv","w") as file:
   for i in Cards.keys():
     file.write(f'card:{i}\n')
     n=Cards[i]['Name']
     file.write(f' Name:{n}\n')
     b=Cards[i]['balance']
     file.write(f' balance:{b}\n')
     p=Cards[i]['password']
     file.write(f' password:{p}\n')
     e=Cards[i]['expiry date']
     file.write(f' expiry date:{e}\n')
print(Cards)