

# Add your code here to run in your startup task
from tkinter import *
from tkinter import ttk




def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
root = Tk()
root.title("Feet to Meters")



mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

var = StringVar()
myCheck =ttk.Checkbutton(mainframe, text="Domestic", variable=var, onvalue="y", offvalue="n")


feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
myCheck.grid(column=1, row=3, sticky=E)

def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

ttk.Label(mainframe, text="Your sex:").grid(row=0, sticky=W)
var1 = IntVar()
ttk.Checkbutton(mainframe, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
ttk.Checkbutton(mainframe, text="female", variable=var2).grid(row=2, sticky=W)
#Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(mainframe, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)




for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()


def parcelType(parcel):
  if parcel == "y":
    return True # Domestic parcel
  else:
    return False # Internationl parcel

def postStandard(standard):
  if standard == "y":
    return True
  else: 
    return False
def ebayOrder(order):
  if order == "y":
    return True
  else:
    return False
postcodeList = list()
postcodeList=list(range(3000, 3221))
postcodeList.extend(list(range(3335, 3342)))
postcodeList.extend(list(range(3425, 3444)))
postcodeList.extend(list(range(3750, 3812)))
postcodeList.extend(list(range(3910, 3921)))
postcodeList.extend(list(range(3926, 3945)))
postcodeList.extend(list(range(3972, 3979)))
postcodeList.extend(list(range(3980, 3984)))
postcodeList.extend(list(range(8000, 9000)))
MSG_D=input("Domestic Parcel? y/n ")
pclDomestic = parcelType(MSG_D)

if pclDomestic == False:
  print("International parcel")
else: 
    MSG_S=input("Standard post? y/n ")
    postOutput = postStandard(MSG_S)

    if postOutput == False:
      print("Express Post")
    else:
      MSG_B=input("How many bars? ")
      barsOutput = int(MSG_B)
      if barsOutput <= 4:
        print("Auspost Prepaid Satchel Bag, Small up to 500 gram")
      else:
        MSG_O=input("eBay order? y/n ")
        orderOutput = ebayOrder(MSG_O)
        if orderOutput == False and barsOutput <= 8:
          print("Auspost Prepaid Satchel Bag up to 1kg")
        elif orderOutput == False and barsOutput > 8 and barsOutput <= 24:
          print("Auspost Prepaid Satchel Bag up to 3kg")
        elif orderOutput == False and barsOutput > 24 and barsOutput <= 40:
          print("Auspost Prepaid Satchel Bag up to 5kg")
        elif orderOutput == True and barsOutput <= 8:
          print("Auspost Flat Rate BX1 Small Box -- up to 1kg -- $7.55")
        elif orderOutput == True and barsOutput > 8:
          MSG_C = input("Postcode: ")
          postcodeOutput = int(MSG_C)
          if postcodeOutput in postcodeList:
            print("Auspost Business Account -- Up to 20kg -- $10.55") 
          else:
            if barsOutput <= 24:
              print("eBay Australia Post Flat Rate 3kg Satchel -- $12.20")
            elif barsOutput > 24 and barsOutput <= 40:
              print("Australia Post Flat Rate BX4 Large Box -- $15.90")
            elif barsOutput > 40:
              print("Multi Prepaid Satchels / Business Account")  
