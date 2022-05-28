        
import serial

serialPort = serial.Serial(port = "COM4", baudrate=9600)
         
serialString = ""

while(1):

    # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        print(serialString.decode('Ascii'))


       # serialPort.write(b"Thank you for sending data \r\n")
