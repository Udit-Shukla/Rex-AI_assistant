import pyautogui
import random
name = random.randint(0, 100)
image = pyautogui.screenshot('image'+str(name)+'.png')
# image.save('D:\]python project\\)
