import evdev
from time import sleep 

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

for event in dev.read_loop():
#	print(evdev.categorize(event))
	if hex(event.value) == KEY_MENU:
		print("\npress MENU")
	elif hex(event.value) == "0x0":
		continue
	print("\nCode:",hex(event.value))
	print("---------------")
#	sleep(1)
#	print("ready...")
#	print(event.type)
