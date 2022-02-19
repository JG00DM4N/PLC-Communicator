from tkinter import *
from tkinter import messagebox
from command_plc import *
from functools import partial

class Keypad():
    def __init__(self, parent, plclist) -> None:
        self.kwindow = Toplevel(parent)
        self.kwindow.attributes('-topmost',True)
        self.kwindow.resizable(0,0)
        self.kwindow.iconbitmap('coding.ico')

        self.plclist = plclist

        text_font = ("System", 20, "bold")

        self.selected_PLC = StringVar()
        options = self.plclist.keys()
        self.selected_PLC.set('Choose a PLC')
        PLC_dropdown = OptionMenu(self.kwindow, self.selected_PLC, *options)
        PLC_dropdown.grid(row=0,column=0, columnspan=4)

        self.side = StringVar()
        r_a_side = Radiobutton(self.kwindow, text="A side", variable=self.side, value="a")
        r_a_side.grid(row=0, column=4)
        r_b_side = Radiobutton(self.kwindow, text="B side", variable=self.side, value="b")
        r_b_side.grid(row=0, column=5)
        self.side.set("a")

        self.sk1 = Button(self.kwindow, text="SK1", height=2,width=7, font=text_font)
        self.sk1.grid(row=2,column=1,padx=5,pady=5)
        self.sk1.bind("<ButtonPress>", partial(self.k_press, "SK1"))
        self.sk1.bind("<ButtonRelease>", partial(self.k_press, "SK1"))

        self.upm1 = Button(self.kwindow, text="1", height=2,width=7, font=text_font)
        self.upm1.grid(row=2,column=2,padx=5,pady=5)
        self.upm1.bind("<ButtonPress>", partial(self.k_press, "1"))
        self.upm1.bind("<ButtonRelease>", partial(self.k_press, "1"))

        self.upm2 = Button(self.kwindow, text="2", height=2,width=7, font=text_font)
        self.upm2.grid(row=2,column=3,padx=5,pady=5)
        self.upm2.bind("<ButtonPress>", partial(self.k_press, "2"))
        self.upm2.bind("<ButtonRelease>", partial(self.k_press, "2"))

        self.upm3 = Button(self.kwindow, text="3", height=2,width=7, font=text_font)
        self.upm3.grid(row=2,column=4,padx=5,pady=5)
        self.upm3.bind("<ButtonPress>", partial(self.k_press, "3"))
        self.upm3.bind("<ButtonRelease>", partial(self.k_press, "3"))

        self.upmyes = Button(self.kwindow, text="YES", height=2,width=7, font=text_font)
        self.upmyes.grid(row=2,column=5,padx=5,pady=5)
        self.upmyes.bind("<ButtonPress>", partial(self.k_press, "YES"))
        self.upmyes.bind("<ButtonRelease>", partial(self.k_press, "YES"))

        self.sk5 = Button(self.kwindow, text="SK5", height=2,width=7, font=text_font)
        self.sk5.grid(row=2,column=6,padx=5,pady=5)
        self.sk5.bind("<ButtonPress>", partial(self.k_press, "SK5"))
        self.sk5.bind("<ButtonRelease>", partial(self.k_press, "SK5"))

        self.sk2 = Button(self.kwindow, text="SK2", height=2,width=7, font=text_font)
        self.sk2.grid(row=3,column=1,padx=5,pady=5)
        self.sk2.bind("<ButtonPress>", partial(self.k_press, "SK2"))
        self.sk2.bind("<ButtonRelease>", partial(self.k_press, "SK2"))

        self.upm4 = Button(self.kwindow, text="4", height=2,width=7, font=text_font)
        self.upm4.grid(row=3,column=2,padx=5,pady=5)
        self.upm4.bind("<ButtonPress>", partial(self.k_press, "4"))
        self.upm4.bind("<ButtonRelease>", partial(self.k_press, "4"))

        self.upm5 = Button(self.kwindow, text="5", height=2,width=7, font=text_font)
        self.upm5.grid(row=3,column=3,padx=5,pady=5)
        self.upm5.bind("<ButtonPress>", partial(self.k_press, "5"))
        self.upm5.bind("<ButtonRelease>", partial(self.k_press, "5"))

        self.upm6 = Button(self.kwindow, text="6", height=2,width=7, font=text_font)
        self.upm6.grid(row=3,column=4,padx=5,pady=5)
        self.upm6.bind("<ButtonPress>", partial(self.k_press, "6"))
        self.upm6.bind("<ButtonRelease>", partial(self.k_press, "6"))

        self.ppno = Button(self.kwindow, text="NO", height=2,width=7, font=text_font)
        self.ppno.grid(row=3,column=5,padx=5,pady=5)
        self.ppno.bind("<ButtonPress>", partial(self.k_press, "NO"))
        self.ppno.bind("<ButtonRelease>", partial(self.k_press, "NO"))

        self.sk6 = Button(self.kwindow, text="SK6", height=2,width=7, font=text_font)
        self.sk6.grid(row=3,column=6,padx=5,pady=5)
        self.sk6.bind("<ButtonPress>", partial(self.k_press, "SK6"))
        self.sk6.bind("<ButtonRelease>", partial(self.k_press, "SK6"))

        self.sk3 = Button(self.kwindow, text="SK3", height=2,width=7, font=text_font)
        self.sk3.grid(row=4,column=1,padx=5,pady=5)
        self.sk3.bind("<ButtonPress>", partial(self.k_press, "SK3"))
        self.sk3.bind("<ButtonRelease>", partial(self.k_press, "SK3"))

        self.pp7 = Button(self.kwindow, text="7", height=2,width=7, font=text_font)
        self.pp7.grid(row=4,column=2,padx=5,pady=5)
        self.pp7.bind("<ButtonPress>", partial(self.k_press, "7"))
        self.pp7.bind("<ButtonRelease>", partial(self.k_press, "7"))

        self.pp8 = Button(self.kwindow, text="8", height=2,width=7, font=text_font)
        self.pp8.grid(row=4,column=3,padx=5,pady=5)
        self.pp8.bind("<ButtonPress>", partial(self.k_press, "8"))
        self.pp8.bind("<ButtonRelease>", partial(self.k_press, "8"))

        self.pp9 = Button(self.kwindow, text="9", height=2,width=7, font=text_font)
        self.pp9.grid(row=4,column=4,padx=5,pady=5)
        self.pp9.bind("<ButtonPress>", partial(self.k_press, "9"))
        self.pp9.bind("<ButtonRelease>", partial(self.k_press, "9"))

        self.ppcancel = Button(self.kwindow, text="CANCEL", height=2,width=7, font=text_font)
        self.ppcancel.grid(row=4,column=5,padx=5,pady=5)
        self.ppcancel.bind("<ButtonPress>", partial(self.k_press, "CANCEL"))
        self.ppcancel.bind("<ButtonRelease>", partial(self.k_press, "CANCEL"))

        self.sk7 = Button(self.kwindow, text="SK7", height=2,width=7, font=text_font)
        self.sk7.grid(row=4,column=6,padx=5,pady=5)
        self.sk7.bind("<ButtonPress>", partial(self.k_press, "SK7"))
        self.sk7.bind("<ButtonRelease>", partial(self.k_press, "SK7"))

        self.sk4 = Button(self.kwindow, text="SK4", height=2,width=7, font=text_font)
        self.sk4.grid(row=5,column=1,padx=5,pady=5)
        self.sk4.bind("<ButtonPress>", partial(self.k_press, "SK4"))
        self.sk4.bind("<ButtonRelease>", partial(self.k_press, "SK4"))

        self.ppclear = Button(self.kwindow, text="CLEAR", height=2,width=7, font=text_font)
        self.ppclear.grid(row=5,column=2,padx=5,pady=5)
        self.ppclear.bind("<ButtonPress>", partial(self.k_press, "CLEAR"))
        self.ppclear.bind("<ButtonRelease>", partial(self.k_press, "CLEAR"))

        self.pp0 = Button(self.kwindow, text="0", height=2,width=7, font=text_font)
        self.pp0.grid(row=5,column=3,padx=5,pady=5)
        self.pp0.bind("<ButtonPress>", partial(self.k_press, "0"))
        self.pp0.bind("<ButtonRelease>", partial(self.k_press, "0"))

        self.ppenter = Button(self.kwindow, text="ENTER", height=2,width=7, font=text_font)
        self.ppenter.grid(row=5,column=4,padx=5,pady=5)
        self.ppenter.bind("<ButtonPress>", partial(self.k_press, "ENTER"))
        self.ppenter.bind("<ButtonRelease>", partial(self.k_press, "ENTER"))

        self.pphelp = Button(self.kwindow, text="HELP", height=2,width=7, font=text_font)
        self.pphelp.grid(row=5,column=5,padx=5,pady=5)
        self.pphelp.bind("<ButtonPress>", partial(self.k_press, "HELP"))
        self.pphelp.bind("<ButtonRelease>", partial(self.k_press, "HELP"))

        self.sk8 = Button(self.kwindow, text="SK8", height=2,width=7, font=text_font)
        self.sk8.grid(row=5,column=6,padx=5,pady=5)
        self.sk8.bind("<ButtonPress>", partial(self.k_press, "SK8"))
        self.sk8.bind("<ButtonRelease>", partial(self.k_press, "SK8"))

    def k_press(self,key_pressed,event):
        if self.selected_PLC.get() == 'Choose a PLC':
            if "ButtonPress" in str(event):
                # messagebox.showwarning('PLC Error', 'You need to choose a PLC.',parent=self.kwindow)
                return
            else: # Don't show the error box twice
                return
        else: # A PLC was chosen in the drop down
            if "ButtonRelease" in str(event):
                button_state = "released"
            elif "ButtonPress" in str(event):
                button_state = "pressed"
            key_press(self.plclist[self.selected_PLC.get()],self.side.get(),key_pressed,button_state)
    