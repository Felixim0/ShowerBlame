import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

def send_start_time(minutes, seconds):
    ser.write(f"{minutes},{seconds}".encode())

if __name__ == "__main__":
    send_start_time(10, 20)  # Send start time of 10 minutes and 20 seconds
