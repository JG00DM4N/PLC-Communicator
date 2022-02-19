import modbus_tk.defines as cst
import modbus_tk.modbus as modbus
import modbus_tk.modbus_tcp as modbus_tcp

while True:
    connection = modbus_tcp.TcpMaster(host="10.28.48.121", port=502, timeout_in_sec=5.0)
    user_input = input("Type a bit to read: ")
    if user_input == "x":
        break
    if user_input == "w":
        while True:
            command_input = input("Type bit to write: ")
            if command_input == "x":
                break
            value = input("0 or 1: ")
            output = int(command_input)
            connection.open
            connection.execute(slave=4, function_code=cst.WRITE_MULTIPLE_COILS, starting_address=output, output_value=[int(value)])
            connection.close
        continue
    if user_input == "i":
        while True:
            slave = input("Enter to continue ")
            if slave == "x":
                break
            connection.open
            #print(connection.execute(slave=6, function_code=1, starting_address=3, quantity_of_x=1))
            #print(connection.execute(slave=6, function_code=2, starting_address=3, quantity_of_x=1))
            fromplc = connection.execute(slave=1, function_code=3, starting_address=28696, quantity_of_x=2)
            hex1 = hex(fromplc[0])
            hex2 = hex(fromplc[1])
            hex1 = hex1.replace("0x","")
            hex2 = hex2.replace("0x","")

            totalhex = hex2 + hex1
            real = int(totalhex,16)
            print(real)
            print(hex1,hex2)



            #print(connection.execute(slave=6, function_code=4, starting_address=1, quantity_of_x=4))
            connection.close
        continue
    connection.open
    command = int(user_input)
    connection = modbus_tcp.TcpMaster(host="10.28.48.124", port=502, timeout_in_sec=5.0)
    connection.open
    mb = connection.execute(slave=4, function_code=cst.READ_COILS, starting_address=command, quantity_of_x=1)
    print(mb)
    connection.close
