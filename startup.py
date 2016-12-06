import pyHook
import pythoncom
import time

start_timer = time.time()


def onclick(event):
    global start_timer

    ### file = open("clear.txt", "a")
    end_timer = time.time()

    mouse_position = event.Position
    x = mouse_position[0]
    y = mouse_position[1]

    time_taken = end_timer - start_timer

    coordinates = str(x)
    coordinates += ":"
    coordinates += str(y)
    coordinates += ":"
    coordinates += str(time_taken)

    file.write(coordinates + "\n")

    start_timer = time.time()

    file.close()
    return True

hm = pyHook.HookManager()
hm.SubscribeMouseAllButtonsDown(onclick)
hm.HookMouse()
pythoncom.PumpMessages()
hm.UnhookMouse()

# Use pyAutoGui to move mouse
