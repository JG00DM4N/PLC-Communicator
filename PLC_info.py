from email.policy import default
from tkinter import *
from tkinter import font
from tkinter import messagebox
from command_plc import *
from functools import partial

class PLCInfo():
    """ Class for Displaying PLC information to the user. """
    def __init__(self, parent, plclist) -> None:
        self.pwindow = Toplevel(parent)
        self.pwindow.attributes('-topmost',True)
        self.pwindow.iconbitmap('coding.ico')
        self.pwindow.geometry("550x400+100+100")
        self.pwindow.resizable(0,0)

        self.plclist = plclist

        self.selected_PLC = StringVar()
        options = self.plclist.keys()
        self.selected_PLC.set('Select a PLC')
        PLC_dropdown = OptionMenu(self.pwindow, self.selected_PLC, *options, command=self.get_PLC_info)
        PLC_dropdown.pack(side=TOP)

        self.info_frame = LabelFrame(self.pwindow)
        self.info_frame.pack(side=BOTTOM)

    def convert_to_dec(self,hexvalue):
        """ Hexadecimal convertion (register response from PLC is sent in 2 part HEX values. """
        hex1 = hex(hexvalue[0])
        hex2 = hex(hexvalue[1])
        hex1 = hex1.replace("0x","") # Remove the "0x" if part of response from PLC.
        hex2 = hex2.replace("0x","") # Remove the "0x" if part of response from PLC.
        totalhex = hex2 + hex1
        return int(totalhex,16)

    def reset_value(self,reset_value):
        """ Processed reseting some of the PLC register values. """
        MsgBox = messagebox.askquestion('Reset Value','Are you sure you want to reset this value?',icon='warning',parent=self.pwindow)
        if MsgBox == 'yes':
            reset(self.plclist[self.selected_PLC.get()],reset_value)
            self.info_frame.destroy()
            self.get_PLC_info(None)
        return
       
    def get_PLC_info(self,event):
        """ Display the requested PLC information to the user. """
        font = ("Comic Sans MS", 20, "bold")
        selected_PLC = self.selected_PLC.get()
        plc = self.plclist[selected_PLC]
        PLC_info = get_info(plc)

        self.info_frame.destroy() # Destroy LabelFrame every time to make sure all info is cleared for next PLC.
        self.info_frame = LabelFrame(self.pwindow)
        self.info_frame.pack(side=BOTTOM)
        gradeA = Label(self.info_frame, text="Side A Current Grade: " + str(PLC_info[0]), font=font)
        gradeA.grid(row=1)

        trans_count_A = Label(self.info_frame, text="Side A Transaction Count: " + str(PLC_info[1]),font=font)
        trans_count_A.grid(row=2)
        reset_trans_count_A = Button(self.info_frame, text="Reset", command=partial(self.reset_value, "transA"))
        reset_trans_count_A.grid(row=2,column=1)

        card_count_A = Label(self.info_frame, text="Side A Total Card Insertions: " + str(self.convert_to_dec(PLC_info[4])),font=font)
        card_count_A.grid(row=3)
        reset_card_count_A = Button(self.info_frame, text="Reset", command=partial(self.reset_value, "cardA"))
        reset_card_count_A.grid(row=3,column=1)

        main_odometer_A = Label(self.info_frame, text="Main Odometer A Side: " + str(self.convert_to_dec(PLC_info[6])),font=font,fg="orange")
        main_odometer_A.grid(row=4)

        gradeB = Label(self.info_frame, text="Side B Current Grade: " + str(PLC_info[2]),font=font)
        gradeB.grid(row=5)

        trans_count_B = Label(self.info_frame, text="Side B Transaction Count: " + str(PLC_info[3]),font=font)
        trans_count_B.grid(row=6)
        reset_trans_count_B = Button(self.info_frame, text="Reset", command=partial(self.reset_value, "transB"))
        reset_trans_count_B.grid(row=6,column=1)
        
        card_count_B = Label(self.info_frame, text="Side B Total Card Insertions: " + str(self.convert_to_dec(PLC_info[5])), font=font)
        card_count_B.grid(row=7)
        reset_card_count_B = Button(self.info_frame, text="Reset", command=partial(self.reset_value, "cardB"))
        reset_card_count_B.grid(row=7,column=1)

        main_odometer_B = Label(self.info_frame, text="Main Odometer B Side: " + str(self.convert_to_dec(PLC_info[7])),font=font,fg="orange")
        main_odometer_B.grid(row=8)

        return