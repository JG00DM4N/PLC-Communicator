import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp

def get_plc_status(plc, side):

    try:
        connection = modbus_tcp.TcpMaster(host=plc["IP"], port=502, timeout_in_sec=5.0)
        connection.open
        a_side_status = connection.execute(slave=plc["ID"], function_code=cst.READ_COILS, starting_address=0, quantity_of_x=1)
        b_side_status = connection.execute(slave=plc["ID"], function_code=cst.READ_COILS, starting_address=14, quantity_of_x=1)
        alarm = connection.execute(slave=plc["ID"], function_code=cst.READ_COILS, starting_address=52, quantity_of_x=2)
        connection.close

        if side == "a":
            if alarm[0] == 1: # Yes, in alarm
                return 2
            else:
                return a_side_status[0]
        else:
            if alarm[1] == 1: # Yes, in alarm
                return 2
            else:
                return b_side_status[0]

    except:
        return False


def start_plc(plc, side):
    a_or_b = 1 if side == "a" else 13 # 1 is start bit for A side, 13 for B side
    try:
        connection = modbus_tcp.TcpMaster(host=plc["IP"], port=502, timeout_in_sec=5.0)
        connection.open
        connection.execute(slave=plc["ID"], function_code=cst.WRITE_MULTIPLE_COILS, starting_address=a_or_b, output_value=[1])
        connection.close
        return
    except:
        return False

def stop_plc(plc, side):
    a_or_b = 79 if side == "a" else 80 # 79 is reset bit for A side, 80 for b side
    try:
        connection = modbus_tcp.TcpMaster(host=plc["IP"], port=502, timeout_in_sec=5.0)
        connection.open
        connection.execute(slave=plc["ID"], function_code=cst.WRITE_MULTIPLE_COILS, starting_address=a_or_b, output_value=[1])
        connection.close
        return
    except:
        return

def key_press(plc, side, key_pressed, button_state):
    keymap = {"a":
                {"SK1":109,
                 "SK2":110,
                 "SK3":111,
                 "SK4":112,
                 "SK5":113,
                 "SK6":114,
                 "SK7":115,
                 "SK8":116,
                 "1":125,
                 "2":126,
                 "3":127,
                 "4":129,
                 "5":130,
                 "6":131,
                 "7":133,
                 "8":134,
                 "9":135,
                 "0":138,
                 "YES":128,
                 "NO":132,
                 "CANCEL":136,
                 "CLEAR":137,
                 "ENTER":139,
                 "HELP":140},
              "b":
                {"SK1":141,
                 "SK2":142,
                 "SK3":143,
                 "SK4":144,
                 "SK5":145,
                 "SK6":146,
                 "SK7":147,
                 "SK8":148,
                 "1":157,
                 "2":158,
                 "3":159,
                 "4":161,
                 "5":162,
                 "6":163,
                 "7":165,
                 "8":166,
                 "9":167,
                 "0":170,
                 "YES":160,
                 "NO":164,
                 "CANCEL":168,
                 "CLEAR":169,
                 "ENTER":171,
                 "HELP":172}
             }

    if button_state == "pressed":
        try:
            connection = modbus_tcp.TcpMaster(host=plc["IP"], port=502, timeout_in_sec=5.0)
            connection.open
            connection.execute(slave=plc["ID"], function_code=cst.WRITE_MULTIPLE_COILS, starting_address=keymap[side][key_pressed], output_value=[1])
            connection.close
            return
        except:
            return
    else: # released
        try:
            connection = modbus_tcp.TcpMaster(host=plc["IP"], port=502, timeout_in_sec=5.0)
            connection.open
            connection.execute(slave=plc["ID"], function_code=cst.WRITE_MULTIPLE_COILS, starting_address=keymap[side][key_pressed], output_value=[0])
            connection.close
            return
        except:
            return

def get_info(plc):
    registers = [0,1,5,3]
    longs = [28705,28704,28696,28697]
    try:
        connection = modbus_tcp.TcpMaster(host=plc["IP"], port=502, timeout_in_sec=5.0)
        connection.open
        values = []
        for register in registers:
            values.append((connection.execute(slave=plc["ID"], function_code=cst.READ_HOLDING_REGISTERS, starting_address=register, quantity_of_x=1))[0])
        for long in longs:
            values.append((connection.execute(slave=plc["ID"], function_code=cst.READ_HOLDING_REGISTERS, starting_address=long, quantity_of_x=2)))
        connection.close
        return values
    except:
        return

def reset(plc,reset_item):
    try:
        connection = modbus_tcp.TcpMaster(host=plc["IP"], port=502, timeout_in_sec=5.0)
        connection.open
        if reset_item == "transA": 
            connection.execute(slave=plc["ID"], function_code=cst.WRITE_SINGLE_REGISTER, starting_address=1, output_value=0)
        elif reset_item == "cardA":
            connection.execute(slave=plc["ID"], function_code=cst.WRITE_SINGLE_REGISTER, starting_address=28705, output_value=0)
        elif reset_item == "transB":
            connection.execute(slave=plc["ID"], function_code=cst.WRITE_SINGLE_REGISTER, starting_address=3, output_value=0)
        elif reset_item == "cardB":
            connection.execute(slave=plc["ID"], function_code=cst.WRITE_SINGLE_REGISTER, starting_address=28704, output_value=0)
        return
    except:
        return

