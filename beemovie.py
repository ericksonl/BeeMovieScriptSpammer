import pyautogui
import time

file1 = open("MovieScript.txt")

time.sleep(5)

with open("MovieScript.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    pyautogui.write(stripped_line)
    pyautogui.press('enter')
    time.sleep(1.5)

    

