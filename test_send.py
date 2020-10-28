from z9c import *

device = setup("COM11")

while True:
    data = input(">>")
    send_progress(device, data)
    print("packet sent")
