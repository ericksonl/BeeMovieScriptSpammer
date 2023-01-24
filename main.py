import pyautogui
import time

file1 = open("Script.txt")

time.sleep(5)

with open("Script.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    pyautogui.write(stripped_line)
    pyautogui.press('enter')
    time.sleep(1.5)

    

