import pyautogui

password = "ayylmao"

pyautogui.keyDown("alt")
pyautogui.keyDown("tab")
pyautogui.keyUp("tab")
pyautogui.keyDown("tab")
pyautogui.keyUp("tab")
pyautogui.keyUp("alt")

pyautogui.typewrite(password)

pyautogui.keyDown("enter")
pyautogui.keyUp("enter")
