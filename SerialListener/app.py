import serial
from datetime import datetime
file_name = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')[:-3]
file_name = file_name + '.txt'

ser = serial.Serial("COM4", baudrate=115200, parity=serial.PARITY_NONE, stopbits=1)



with open(file_name, 'w') as output_file: # w = writing data, r = reading data, a = appending
    output_file.write('')

print("/// 31.08.2023 ///")
print("\n")

while True:
    
    raw_data = ser.read()
    received_str_bin_data = []
    for each_data in raw_data:
        if each_data >= ord(' ') or each_data == ord('\n') or each_data == ord('\r') or each_data == ord('\t') :
            received_str_bin_data.append(each_data)
    data = bytes(received_str_bin_data).decode('utf-8')
    print(data, end='', flush=True)
    with open(file_name, 'a') as output_file:
        data = data.replace('\r', '')
        output_file.write(data)
        output_file.flush()