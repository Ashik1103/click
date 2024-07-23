import pyautogui as pg
import keyboard
import time

print("move the mouse pointer to the circle and click enter")

while True:
    if keyboard.read_key() == "enter":
        mousePos = pg.position()
        break
print("starting the clicker")
time.sleep(5)
print("started the clicker")

while True:
    print(mousePos.x, mousePos.y)
    pg.click(mousePos.x, mousePos.y)
    print("clicked")
    # time.sleep(5)

    if keyboard.is_pressed("q"):
        break
