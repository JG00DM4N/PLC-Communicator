# PLC-Communicator
App to communicate and control our PLCs

We have Unitronics PLCs running automation in our lab. Previous we only had the Unitronics interface to communicate with the PLC. It was slow and could only communicate one at a time. But utilized the Modbus protocol on the PLCs and the modbus_tk library on Python to directly communicate with each PLC. The connection is instantaneous, and speeds up access to the important functions of the PLCs, without having to go to the PLCs.

command_plc.py -> The main apparatus for Modbus communication for the program. All communication is through this program. Uses the modbus_tk library

plctalk.py -> A small command line program I used to test the various registers and coils on the PLC. I needed to find the correct modbus memory actions to program into the main application.

keypad.py -> The "keypad" emulator to use the automated keypad on the test equipment. Uses tkinter library for the GUI.

PLC_Communicator.py -> The main application, showing the status of all PLCs. Uses tkinter library for the GUI.

plclist.txt -> External file to store IDs and IPs of each PLC. That way if an ID or IP changes, only this file needed changed.

