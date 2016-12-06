import pyautogui

running = True
clicks = 0

while running:
    positions = open("command.txt", "r")

    for line in positions:
        xy = line
        clicks += 1

        coordinates = xy.split(":")
        x = coordinates[0]
        y = coordinates[1]
        time_between = coordinates[2]

        time_between = time_between[:-1]
        # int(round(time_between, 0))

        if clicks == 10:
            clean_inv = open("clear.txt", "r")
            counter = 0
            for commands in clean_inv:
                command = commands

                point = command.split(":")

                x = point[0]
                y = point[1]
                time_between = point[2]
                time_between = time_between[:-1]

                if (counter % 2) == 0:
                    pyautogui.click(int(x), int(y), int(time_between), button="right")
                else:
                    pyautogui.click(int(x), int(y), int(time_between))

                counter += 1

            clean_inv.close()
        else:
            pyautogui.moveTo(int(x), int(y), float(time_between))
            pyautogui.click()

    positions.close()
