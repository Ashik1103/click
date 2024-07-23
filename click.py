import pyautogui as pg
import keyboard
import time

# print("move the mouse pointer to the circle and click enter")

# while True:
#     if keyboard.read_key() == "enter":
#         mousePos = pg.position()
#         break
# print("starting the clicker")
# time.sleep(5)
# print("started the clicker")

# while True:
#     print(mousePos.x, mousePos.y)
#     pg.click(mousePos.x, mousePos.y)
#     print("clicked")
#     # time.sleep(5)

#     if keyboard.is_pressed("q"):
#         break


# print(pg.position())  # Prints current mouse position
# pg.moveTo(100, 100)
# print("sleep")
# time.sleep(3)
# print(pg.position())  # Prints current mouse position

# pg.click()
from pynput.mouse import Button, Controller

mouse = Controller()

# Move the mouse to (100, 100)
mouse.position = (100, 100)
# Click at (100, 100)
mouse.click(Button.left, 1)
