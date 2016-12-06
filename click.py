import pyautogui

running = True
ticks = 0

while running:
    #ticks += 1
    positions = open("command.txt", "r")

    for line in positions:
        xy = line

        coordinates = xy.split(":")
        x = coordinates[0]
        y = coordinates[1]
        time_between = coordinates[2]

        time_between = time_between[:-1]
        # int(round(time_between, 0))

        pyautogui.moveTo(int(x), int(y), float(time_between))
        pyautogui.click()

    #if ticks == 10:
     #   running = False

    positions.close()
