import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

def send_start_time(minutes, seconds):
    ser.write(f"{minutes},{seconds}".encode())

def reset_timer():
    ser.write(b"reset")

if __name__ == "__main__":
    # Initialise by immediately resetting the timer
    reset_timer()  # Reset the timer
    time.sleep(10)
    send_start_time(1, 20)  # Send start time of 10 minutes and 20 seconds
    time.sleep(5)  # Wait for 5 seconds
    reset_timer()  # Reset the timer
    time.sleep(10)
    send_start_time(1, 20)  # Send start time of 10 minutes and 20 seconds
