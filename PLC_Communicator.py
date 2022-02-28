from tkinter import *
from tkinter import messagebox, tix
from tkinter.tix import Balloon
from command_plc import *
from functools import partial
import json
from keypad import Keypad
from PLC_info import PLCInfo

class PLCInterface:

    def __init__(self, plc_list) -> None:
        """ SETTING UP THE GUI FOR THE PROGRAM """

        self.plclist = plc_list

        # Get the window setup
        self.window=tix.Tk()
        self.window.title("PLC Interface")
        self.window.resizable(0,0)
        self.window.geometry("+0+0")
        self.window.config(cursor="")
        self.window.iconbitmap('coding.ico')

        # Set up some fonts
        position_font = ("Arial",15,"italic")
        button_font = ("Arial", 15, "bold")
        status_font = ("Arial", 15)

        ##### PLC #1 CONTROLS #####
        lf1=LabelFrame(self.window,text="POSITION 1", font=position_font)
        lf1.grid(row=0,column=0,padx=2,pady=5)

        self.b1a=Button(lf1,text="Start/Stop A",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC1"], side="a"))
        self.b1a.grid(row=1,column=0)
        self.b1b=Button(lf1,text="Start/Stop B",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC1"], side="b"))
        self.b1b.grid(row=2,column=0)

        lPLC1Status=Label(lf1, text="Status", font=status_font)
        lPLC1Status.grid(row=0,column=1)
        PLC1_A_Side_Status_label=Label(lf1, text="A Status",font=status_font)
        PLC1_A_Side_Status_label.grid(row=1, column=1)
        PLC1_B_Side_Status_label=Label(lf1, text="B Status",font=status_font)
        PLC1_B_Side_Status_label.grid(row=2, column=1)

        ##### PLC #2 CONTROLS #####
        lf2=LabelFrame(self.window,text="POSITION 2", font=position_font)
        lf2.grid(row=1,column=0,padx=2,pady=5)

        self.b2a=Button(lf2,text="Start/Stop A",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC2"], side="a"))
        self.b2a.grid(row=1,column=0)
        self.b2b=Button(lf2,text="Start/Stop B",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC2"], side="b"))
        self.b2b.grid(row=2,column=0)

        lPLC2Status=Label(lf2, text="Status", font=status_font)
        lPLC2Status.grid(row=0,column=1)
        PLC2_A_Side_Status_label=Label(lf2, text="A Status", font=status_font)
        PLC2_A_Side_Status_label.grid(row=1, column=1)
        PLC2_B_Side_Status_label=Label(lf2, text="B Status", font=status_font)
        PLC2_B_Side_Status_label.grid(row=2, column=1)

        ##### PLC #3 CONTROLS #####
        lf3=LabelFrame(self.window,text="POSITION 3", font=position_font)
        lf3.grid(row=2,column=0, padx=2,pady=5)

        self.b3a=Button(lf3,text="Start/Stop A",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC3"], side="a"))
        self.b3a.grid(row=1,column=0)
        self.b3b=Button(lf3,text="Start/Stop B",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC3"], side="b"))
        self.b3b.grid(row=2,column=0)

        lPLC3Status=Label(lf3, text="Status", font=status_font)
        lPLC3Status.grid(row=0,column=1)
        PLC3_A_Side_Status_label=Label(lf3, text="A Status", font=status_font)
        PLC3_A_Side_Status_label.grid(row=1, column=1)
        PLC3_B_Side_Status_label=Label(lf3, text="B Status", font=status_font)
        PLC3_B_Side_Status_label.grid(row=2, column=1)

        ##### PLC #4 CONTROLS #####
        lf4=LabelFrame(self.window,text="POSITION 4", font=position_font)
        lf4.grid(row=3,column=0,padx=2,pady=5)

        self.b4a=Button(lf4,text="Start/Stop A",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC4"], side="a"))
        self.b4a.grid(row=1,column=0)
        self.b4b=Button(lf4,text="Start/Stop B",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC4"], side="b"))
        self.b4b.grid(row=2,column=0)

        lPLC4Status=Label(lf4, text="Status", font=status_font)
        lPLC4Status.grid(row=0,column=1)
        PLC4_A_Side_Status_label=Label(lf4, text="A Status", font=status_font)
        PLC4_A_Side_Status_label.grid(row=1, column=1)
        PLC4_B_Side_Status_label=Label(lf4, text="B Status", font=status_font)
        PLC4_B_Side_Status_label.grid(row=2, column=1)

        ##### PLC #5 CONTROLS #####
        lf5=LabelFrame(self.window,text="POSITION 5", font=position_font)
        lf5.grid(row=0,column=1,padx=2,pady=5)

        self.b5a=Button(lf5,text="Start/Stop A",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC5"], side="a"))
        self.b5a.grid(row=1,column=0)
        self.b5b=Button(lf5,text="Start/Stop B",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC5"], side="b"))
        self.b5b.grid(row=2,column=0)

        lPLC5Status=Label(lf5, text="Status", font=status_font)
        lPLC5Status.grid(row=0,column=1)
        PLC5_A_Side_Status_label=Label(lf5, text="A Status", font=status_font)
        PLC5_A_Side_Status_label.grid(row=1, column=1)
        PLC5_B_Side_Status_label=Label(lf5, text="B Status", font=status_font)
        PLC5_B_Side_Status_label.grid(row=2, column=1)

        ##### PLC #6 CONTROLS #####
        lf6=LabelFrame(self.window,text="POSITION 6", font=position_font)
        lf6.grid(row=1,column=1)

        self.b6a=Button(lf6,text="Start/Stop A",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC6"], side="a"))
        self.b6a.grid(row=1,column=0)
        self.b6b=Button(lf6,text="Start/Stop B",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC6"], side="b"))
        self.b6b.grid(row=2,column=0)

        lPLC6Status=Label(lf6, text="Status", font=status_font)
        lPLC6Status.grid(row=0,column=1)
        PLC6_A_Side_Status_label=Label(lf6, text="A Status", font=status_font)
        PLC6_A_Side_Status_label.grid(row=1, column=1)
        PLC6_B_Side_Status_label=Label(lf6, text="B Status", font=status_font)
        PLC6_B_Side_Status_label.grid(row=2, column=1)

        ##### PLC #7 CONTROLS #####
        ##### NO PLC #7 RIGHT NOW. THIS IS A PLACEHOLDER #####
        # l7=Label(self.window,text="Status #7", font=position_font)
        # l7.grid(row=6,column=1)

        # button6 = partial(self.start_stop, self.plclist["PLC6"])
        # self.b7=Button(self.window,text="Start/Stop",height=2,width=12,font=button_font,command=button6)
        # self.b7.grid(row=7,column=1)

        ##### PLC #8 CONTROLS #####
        lf8=LabelFrame(self.window,text="POSITION 8", font=position_font)
        lf8.grid(row=2,column=1,padx=2,pady=5)

        self.b8b=Button(lf8,text="Start/Stop A",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC8"], side="a"))
        self.b8b.grid(row=1,column=0)
        self.b8b=Button(lf8,text="Start/Stop B",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC8"], side="b"))
        self.b8b.grid(row=2,column=0)

        lPLC8Status=Label(lf8, text="Status", font=status_font)
        lPLC8Status.grid(row=0,column=1)
        PLC8_A_Side_Status_label=Label(lf8, text="A Status", font=status_font)
        PLC8_A_Side_Status_label.grid(row=1, column=1)
        PLC8_B_Side_Status_label=Label(lf8, text="B Status", font=status_font)
        PLC8_B_Side_Status_label.grid(row=2, column=1)

        ##### PLC #9 CONTROLS #####
        lf9=LabelFrame(self.window,text="POSITION 9", font=position_font)
        lf9.grid(row=3,column=1,padx=2,pady=5)

        self.b9b=Button(lf9,text="Start/Stop A",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC9"], side="a"))
        self.b9b.grid(row=1,column=0)
        self.b9b=Button(lf9,text="Start/Stop B",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC9"], side="b"))
        self.b9b.grid(row=2,column=0)

        lPLC9Status=Label(lf9, text="Status", font=status_font)
        lPLC9Status.grid(row=0,column=1)
        PLC9_A_Side_Status_label=Label(lf9, text="A Status", font=status_font)
        PLC9_A_Side_Status_label.grid(row=1, column=1)
        PLC9_B_Side_Status_label=Label(lf9, text="B Status", font=status_font)
        PLC9_B_Side_Status_label.grid(row=2, column=1)

        ##### PLC #10 CONTROLS #####
        ##### NO PLC #10. THIS IS A PLACEHOLDER. #####
        # l10=Label(self.window,text="Status #10", font=position_font)
        # l10.grid(row=3,column=2)

        # self.b10=Button(self.window,text="Start/Stop",height=2,width=12,font=button_font,command=self.view_command)
        # self.b10.grid(row=4,column=2)

        ##### PLC #11 CONTROLS #####
        lf11=LabelFrame(self.window,text="POSITION 11", font=position_font)
        lf11.grid(row=0,column=2,padx=2,pady=5)

        self.b11a=Button(lf11,text="Start/Stop A",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC11"], side="a"))
        self.b11a.grid(row=1,column=0)
        self.b11b=Button(lf11,text="Start/Stop B",height=2,width=12,font=button_font,command=partial(self.start_stop, self.plclist["PLC11"], side="b"))
        self.b11b.grid(row=2,column=0)

        lPLC11Status=Label(lf11, text="Status", font=status_font)
        lPLC11Status.grid(row=0,column=1)
        PLC11_A_Side_Status_label=Label(lf11, text="A Status", font=status_font)
        PLC11_A_Side_Status_label.grid(row=1, column=1)
        PLC11_B_Side_Status_label=Label(lf11, text="B Status", font=status_font)
        PLC11_B_Side_Status_label.grid(row=2, column=1)

        ##### ALL STATUS LABELS IN A DICTIONARY TO BE ABLE TO EDIT THEM #####
        ##### PLACEHOLDERS SO DICTIONARY ITEMS MATCH PLC #s #####
        self.status_list = {"a":
                            ["PLACEHOLDER0",
                             PLC1_A_Side_Status_label,
                             PLC2_A_Side_Status_label,
                             PLC3_A_Side_Status_label,
                             PLC4_A_Side_Status_label,
                             PLC5_A_Side_Status_label,
                             PLC6_A_Side_Status_label,
                             "PLACEHOLDER7",
                             PLC8_A_Side_Status_label,
                             PLC9_A_Side_Status_label,
                             "PLACEHOLDER10",
                             PLC11_A_Side_Status_label],
                            "b":
                            ["PLACEHOLDER0",
                             PLC1_B_Side_Status_label,
                             PLC2_B_Side_Status_label,
                             PLC3_B_Side_Status_label,
                             PLC4_B_Side_Status_label,
                             PLC5_B_Side_Status_label,
                             PLC6_B_Side_Status_label,
                             "PLACEHOLDER7",
                             PLC8_B_Side_Status_label,
                             PLC9_B_Side_Status_label,
                             "PLACEHOLDER10",
                             PLC11_B_Side_Status_label]
                           }

        ##### ALL STOP BUTTON #####
        self.b12=Button(self.window,text="ALL STOP",height=6,width=12,font=button_font,bg='red', command=self.stop_all)
        self.b12.grid(row=3,column=2, rowspan=6, columnspan=2)

        ##### UPDATE STATUS BUTTON #####
        self.b13=Button(self.window,text="Check Status", height=2,width=12,font=button_font,bg='green',command=self.update_status)
        self.b13.grid(row=2,column=2,columnspan=2)
        statustip = Balloon(self.window)
        statustip.message.config(font=("haveltica 15 bold"))
        statustip.bind_widget(self.b13,balloonmsg="Click here to refresh status of the PLCs.\nThis is done automatically every 30 seconds.")

        ##### LABELFRAME FOR KEYPAD AND INFO BUTTONS #####
        lfcontrols = LabelFrame(self.window,text="PLC Controls", font=position_font)
        lfcontrols.grid(row=1,column=2)

        ##### OPEN KEYPAD WINDOW BUTTON #####
        self.b14=Button(lfcontrols, text="Keypad", height=2,width=6,font=button_font,bg='yellow',command=self.keypad_window)
        self.b14.grid(row=0,column=0,columnspan=1)
        kptip = Balloon(self.window)
        kptip.message.config(font=("haveltica 15 bold"))
        kptip.bind_widget(self.b14,balloonmsg="Click here to access the keypad window.")

        ##### OPEN PLC INFO WINDOW BUTTON #####
        self.b15=Button(lfcontrols, text="INFO", height=2,width=6,font=button_font,bg="blue",command=self.info_window)
        self.b15.grid(row=0,column=1,columnspan=1)
        infotip = Balloon(self.window)
        infotip.message.config(font=("haveltica 15 bold"))
        infotip.bind_widget(self.b15,balloonmsg="Click here to access information about the PLC.")

        ##### CHECK STATUS ON STARTUP #####
        self.update_status()

    def start_stop(self, plc, side):
        """ Function to start or stop a side of a PLC, and also set its status. """
        plc_status = get_plc_status(plc, side)
        if plc_status == 0:
            start_plc(plc,side)
            self.status_list[side][plc["ID"]].configure(text="RUNNING", fg="green", bg=self.window.cget('bg'))
            self.status_list[side][plc["ID"]].update()
        elif plc_status == 1 or plc_status == 2:
            stop_plc(plc, side)
            self.status_list[side][plc["ID"]].configure(text="STOPPED", fg="red", bg=self.window.cget('bg'))
            self.status_list[side][plc["ID"]].update()
        else:
            self.status_list[side][plc["ID"]].configure(text="NOT CONNECTED", fg="blue", bg=self.window.cget('bg'))
            self.status_list[side][plc["ID"]].update()
            messagebox.showerror('PLC Error', "Connection Refused on PLC #" + plc["ID"])

    def stop_all(self):
        """ Function to stop all PLCs. """
        self.window.config(cursor="wait")
        self.window.update()
        for plcname in self.plclist.keys():
            stop_plc(self.plclist[plcname], "a")
            stop_plc(self.plclist[plcname], "b")
        self.window.config(cursor="")

    def update_status(self):
        """ Function to check status of all PLCs. Runs every 30 seconds. """
        for plc in self.plclist.keys():

            self.b13.configure(text="CHECKING\nSTATUS",bg="light gray",relief=FLAT)
            self.b13.update()
            self.b13["state"]="disabled"

            plc_status_a = get_plc_status(self.plclist[plc], "a")
            plc_status_b = get_plc_status(self.plclist[plc], "b")

            if plc_status_a == 1:
                self.status_list["a"][self.plclist[plc]["ID"]].configure(text="RUNNING", fg="green", bg=self.window.cget('bg'))
                self.status_list["a"][self.plclist[plc]["ID"]].update()
            elif plc_status_a == 0:
                self.status_list["a"][self.plclist[plc]["ID"]].configure(text="STOPPED", fg="red", bg=self.window.cget('bg'))
                self.status_list["a"][self.plclist[plc]["ID"]].update()
            elif plc_status_a == 2:
                self.status_list["a"][self.plclist[plc]["ID"]].configure(text="ALARM", fg="white", bg="red")
                self.status_list["a"][self.plclist[plc]["ID"]].update()                
            else:
                self.status_list["a"][self.plclist[plc]["ID"]].configure(text="OFFLINE", fg="blue", bg=self.window.cget('bg'))
                self.status_list["a"][self.plclist[plc]["ID"]].update()

            if plc_status_b == 1:
                self.status_list["b"][self.plclist[plc]["ID"]].configure(text="RUNNING", fg="green", bg=self.window.cget('bg'))
                self.status_list["b"][self.plclist[plc]["ID"]].update()
            elif plc_status_b == 0:
                self.status_list["b"][self.plclist[plc]["ID"]].configure(text="STOPPED", fg="red", bg=self.window.cget('bg'))
                self.status_list["b"][self.plclist[plc]["ID"]].update()
            elif plc_status_a == 2:
                self.status_list["b"][self.plclist[plc]["ID"]].configure(text="ALARM", fg="white", bg="red")
                self.status_list["b"][self.plclist[plc]["ID"]].update() 
            else:
                self.status_list["b"][self.plclist[plc]["ID"]].configure(text="OFFLINE", fg="blue", bg=self.window.cget('bg'))
                self.status_list["b"][self.plclist[plc]["ID"]].update()

            self.b13.configure(text="Check Status",bg="green",relief=RAISED)
            self.b13.update()
            self.b13["state"]="normal"

        self.window.after(30000, self.update_status)

    def keypad_window(self):
        """ Open the Keypad Window. """
        Keypad(self.window, self.plclist)
    
    def info_window(self):
        """ Open the PLC Info Window. """
        PLCInfo(self.window, self.plclist)

    def on_closing(self):
        self.window.destroy()

##### Load the PLC IP information from .txt file to send to Tkinter window. #####
f = open('plclist.txt', 'r')
plc_list = json.loads(f.read())
f.close()

if __name__ == "__main__":
    PLC = PLCInterface(plc_list)
    PLC.window.protocol("WM_DELETE_WINDOW", PLC.on_closing)
    PLC.window.mainloop()
