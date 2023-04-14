import evdev

KEY_MENU = "0x800b"

#def get_ir_device():
#    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
#    for device in devices:
#        if (device.name == "gpio_ir_recv"):
#            print("Using device", device.path, "\n")
#            return device
#    print("No device found!")

#dev = get_ir_device()

#while(True):
#    event = dev.read_one()
#    if (event):
#        print("Received commands", event.value)
#        break

print("Starting...")

dev = evdev.InputDevice('/dev/input/event3')
print("Device: ",dev)

print(dev.capabilities(verbose=True))

while True:
    print(".")
    event = dev.read_one()
    if event:
        print("code:",hex(event.value))
