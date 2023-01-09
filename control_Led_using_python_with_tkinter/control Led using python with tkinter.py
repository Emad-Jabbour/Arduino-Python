import tkinter as tk
import serial

# Set up the serial connection to the Arduino
ser = serial.Serial('COM6', 9600)

# Set up the tkinter GUI
root = tk.Tk()

# Create a button to turn the LED on and off
def toggle_led():
    if led_button["text"] == "Turn LED On":
        # Send the "on" command to the Arduino
        ser.write(b'on\n')
        led_button["text"] = "Turn LED Off"
    else:
        # Send the "off" command to the Arduino
        ser.write(b'off\n')
        led_button["text"] = "Turn LED On"
led_button = tk.Button(root, text="Turn LED On", command=toggle_led)
led_button.pack()

# Run the tkinter event loop
root.mainloop()
